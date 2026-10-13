"""Deterministic collision-resistant identifiers for canonical pilot records."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Mapping


def _identifier(kind: str, descriptor: Mapping[str, Any]) -> str:
    payload = json.dumps(
        descriptor,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    digest = hashlib.sha256(kind.encode("ascii") + b"\0" + payload).hexdigest()
    return f"solardt-{kind}-v1:{digest}"


def observation_id(descriptor: Mapping[str, Any]) -> str:
    """Return a semantic observation ID; copy-local fields belong elsewhere."""
    return _identifier("observation", descriptor)


def record_id(descriptor: Mapping[str, Any]) -> str:
    """Return a record ID including observation and copy provenance."""
    return _identifier("record", descriptor)


def run_id(descriptor: Mapping[str, Any]) -> str:
    """Return a deterministic run ID from an explicit launch descriptor."""
    return _identifier("run", descriptor)
