"""Shared host-acquisition clock and derived forensic time coordinates."""

from __future__ import annotations

import time
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping


ACQUISITION_TIME_SCHEMA = "solardt-acquisition-time-v1"
MONOTONIC_CLOCK = "linux:CLOCK_MONOTONIC"
BOOT_ID_PATH = Path("/proc/sys/kernel/random/boot_id")
ACQUISITION_FIELDS = (
    "received_at_utc",
    "received_monotonic_ns",
    "monotonic_clock",
    "host_boot_id",
    "collector_run_id",
    "ingest_sequence",
)
ACQUISITION_EXTENSION_FIELDS = ACQUISITION_FIELDS[1:]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace(
        "+00:00", "Z"
    )


def read_host_boot_id(path: Path = BOOT_ID_PATH) -> str:
    """Return the Linux boot UUID used to qualify monotonic comparability."""
    value = path.read_text(encoding="ascii").strip()
    try:
        parsed = uuid.UUID(value)
    except (ValueError, AttributeError) as exc:
        raise RuntimeError("host boot identity is unavailable") from exc
    return str(parsed)


def new_collector_run_id() -> str:
    return str(uuid.uuid4())


@dataclass(frozen=True)
class AcquisitionStamp:
    received_at_utc: str
    received_monotonic_ns: int
    monotonic_clock: str
    host_boot_id: str
    collector_run_id: str
    ingest_sequence: int

    def as_mapping(self) -> dict[str, Any]:
        return {
            "acquisition_time_schema": ACQUISITION_TIME_SCHEMA,
            "received_at_utc": self.received_at_utc,
            "received_monotonic_ns": self.received_monotonic_ns,
            "monotonic_clock": self.monotonic_clock,
            "host_boot_id": self.host_boot_id,
            "collector_run_id": self.collector_run_id,
            "ingest_sequence": self.ingest_sequence,
        }


class AcquisitionClock:
    """Sample synchronized UTC and host monotonic time at one boundary."""

    def __init__(
        self,
        *,
        collector_run_id: str | None = None,
        host_boot_id: str | None = None,
        utc_reader: Callable[[], str] = utc_now,
        monotonic_ns_reader: Callable[[], int] | None = None,
    ) -> None:
        self.collector_run_id = collector_run_id or new_collector_run_id()
        self.host_boot_id = host_boot_id or read_host_boot_id()
        self._utc_reader = utc_reader
        self._monotonic_ns_reader = monotonic_ns_reader or (
            lambda: time.clock_gettime_ns(time.CLOCK_MONOTONIC)
        )

    def stamp(self, ingest_sequence: int) -> AcquisitionStamp:
        if (
            isinstance(ingest_sequence, bool)
            or not isinstance(ingest_sequence, int)
            or ingest_sequence < 1
        ):
            raise ValueError("ingest_sequence must be a positive integer")
        # Keep the two reads adjacent. They are a correlated acquisition stamp,
        # not an assertion that the clocks were sampled simultaneously.
        monotonic_ns = self._monotonic_ns_reader()
        received_at_utc = self._utc_reader()
        return AcquisitionStamp(
            received_at_utc=received_at_utc,
            received_monotonic_ns=monotonic_ns,
            monotonic_clock=MONOTONIC_CLOCK,
            host_boot_id=self.host_boot_id,
            collector_run_id=self.collector_run_id,
            ingest_sequence=ingest_sequence,
        )


def inherited_acquisition_time(record: Mapping[str, Any]) -> dict[str, Any]:
    """Return optional acquisition fields without sampling a new clock."""
    present = [field for field in ACQUISITION_EXTENSION_FIELDS if field in record]
    if not present:
        return {}
    if len(present) != len(ACQUISITION_EXTENSION_FIELDS):
        raise ValueError("incomplete_acquisition_time")
    if record.get("monotonic_clock") != MONOTONIC_CLOCK:
        raise ValueError("unsupported_monotonic_clock")
    monotonic_ns = record.get("received_monotonic_ns")
    sequence = record.get("ingest_sequence")
    if (
        isinstance(monotonic_ns, bool)
        or not isinstance(monotonic_ns, int)
        or monotonic_ns < 0
        or isinstance(sequence, bool)
        or not isinstance(sequence, int)
        or sequence < 1
    ):
        raise ValueError("invalid_acquisition_time")
    for field in ("received_at_utc", "host_boot_id", "collector_run_id"):
        if not isinstance(record.get(field), str) or not record[field]:
            raise ValueError("invalid_acquisition_time")
    return {
        "acquisition_time_schema": record.get("acquisition_time_schema"),
        "received_monotonic_ns": monotonic_ns,
        "monotonic_clock": record["monotonic_clock"],
        "host_boot_id": record["host_boot_id"],
        "collector_run_id": record["collector_run_id"],
        "source_ingest_sequence": sequence,
    }


def _parse_utc(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None or parsed.utcoffset() != timezone.utc.utcoffset(parsed):
        raise ValueError("timestamp must be UTC")
    return parsed


def daily_coordinate(received_at_utc: str) -> dict[str, Any]:
    """Derive the POSIX-UTC day coordinate; leap seconds are not represented."""
    observed = _parse_utc(received_at_utc)
    midnight = observed.replace(hour=0, minute=0, second=0, microsecond=0)
    return {
        "utc_day_id": observed.date().isoformat(),
        "daily_offset_ms": round((observed - midnight).total_seconds() * 1000, 3),
    }


def event_relative_coordinate(
    anchor: Mapping[str, Any],
    observation: Mapping[str, Any],
    *,
    anchor_observation_id: str,
) -> dict[str, Any]:
    """Derive event T+ without subtracting incompatible clock domains."""
    anchor_utc = _parse_utc(str(anchor["received_at_utc"]))
    observation_utc = _parse_utc(str(observation["received_at_utc"]))
    utc_offset_ms = (observation_utc - anchor_utc).total_seconds() * 1000
    same_monotonic_domain = (
        anchor.get("acquisition_time_schema") == ACQUISITION_TIME_SCHEMA
        and observation.get("acquisition_time_schema")
        == ACQUISITION_TIME_SCHEMA
        and anchor.get("monotonic_clock") == MONOTONIC_CLOCK
        and observation.get("monotonic_clock") == MONOTONIC_CLOCK
        and anchor.get("host_boot_id")
        and anchor.get("host_boot_id") == observation.get("host_boot_id")
        and isinstance(anchor.get("received_monotonic_ns"), int)
        and not isinstance(anchor.get("received_monotonic_ns"), bool)
        and isinstance(observation.get("received_monotonic_ns"), int)
        and not isinstance(observation.get("received_monotonic_ns"), bool)
    )
    if same_monotonic_domain:
        offset_ms = (
            observation["received_monotonic_ns"]
            - anchor["received_monotonic_ns"]
        ) / 1_000_000
        basis = "host_monotonic_same_boot"
        anchor_basis = "host_acquisition_monotonic"
        qualification = "acquisition_order_same_host_boot"
    else:
        offset_ms = utc_offset_ms
        basis = "solardt_utc_fallback"
        anchor_basis = "host_acquisition_utc"
        qualification = "acquisition_order_utc_clock_uncertainty_applies"
    result = {
        "anchor_observation_id": anchor_observation_id,
        "anchor_time_basis": anchor_basis,
        "event_offset_basis": basis,
        "event_offset_ms": round(offset_ms, 3),
        "utc_crosscheck_offset_ms": round(utc_offset_ms, 3),
        "timing_qualification": qualification,
        **daily_coordinate(str(observation["received_at_utc"])),
    }
    if same_monotonic_domain:
        result["monotonic_utc_divergence_ms"] = round(
            offset_ms - utc_offset_ms, 3
        )
    return result
