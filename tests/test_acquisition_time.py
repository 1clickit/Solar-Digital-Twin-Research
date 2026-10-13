import unittest

from solar_digital_twin.acquisition_time import (
    ACQUISITION_TIME_SCHEMA,
    MONOTONIC_CLOCK,
    AcquisitionClock,
    daily_coordinate,
    event_relative_coordinate,
)


BOOT_A = "11111111-1111-4111-8111-111111111111"
BOOT_B = "22222222-2222-4222-8222-222222222222"


def observation(utc, monotonic_ns, boot=BOOT_A, run="run-a", sequence=1):
    return {
        "acquisition_time_schema": ACQUISITION_TIME_SCHEMA,
        "received_at_utc": utc,
        "received_monotonic_ns": monotonic_ns,
        "monotonic_clock": MONOTONIC_CLOCK,
        "host_boot_id": boot,
        "collector_run_id": run,
        "ingest_sequence": sequence,
    }


class AcquisitionTimingTests(unittest.TestCase):
    def test_clock_stamps_one_run_boot_and_advancing_sequence(self):
        utc_values = iter(
            ["2026-08-12T01:00:00.000Z", "2026-08-12T01:00:00.250Z"]
        )
        mono_values = iter([100, 250_000_100])
        clock = AcquisitionClock(
            collector_run_id="run-a",
            host_boot_id=BOOT_A,
            utc_reader=lambda: next(utc_values),
            monotonic_ns_reader=lambda: next(mono_values),
        )
        first = clock.stamp(1)
        second = clock.stamp(2)
        self.assertEqual(first.host_boot_id, second.host_boot_id)
        self.assertEqual(first.collector_run_id, second.collector_run_id)
        self.assertLess(first.received_monotonic_ns, second.received_monotonic_ns)
        self.assertEqual(second.ingest_sequence, 2)

    def test_new_process_run_id_changes_within_same_boot(self):
        first = AcquisitionClock(host_boot_id=BOOT_A)
        second = AcquisitionClock(host_boot_id=BOOT_A)
        self.assertNotEqual(first.collector_run_id, second.collector_run_id)

    def test_daily_coordinate_handles_utc_midnight_rollover(self):
        self.assertEqual(
            daily_coordinate("2026-08-12T00:00:00.000Z"),
            {"utc_day_id": "2026-08-12", "daily_offset_ms": 0.0},
        )
        self.assertEqual(
            daily_coordinate("2026-08-11T23:59:59.999Z"),
            {"utc_day_id": "2026-08-11", "daily_offset_ms": 86_399_999.0},
        )

    def test_event_offset_prefers_monotonic_across_process_restart_same_boot(self):
        anchor = observation("2026-08-12T01:00:00.000Z", 1_000_000, run="a")
        later = observation(
            "2026-08-12T01:00:00.318Z", 319_000_000, run="b"
        )
        result = event_relative_coordinate(
            anchor, later, anchor_observation_id="esp32:collapse"
        )
        self.assertEqual(result["event_offset_basis"], "host_monotonic_same_boot")
        self.assertEqual(result["event_offset_ms"], 318.0)
        self.assertEqual(result["utc_crosscheck_offset_ms"], 318.0)

    def test_different_boot_ids_prohibit_monotonic_subtraction(self):
        anchor = observation("2026-08-12T01:00:00.000Z", 9_000_000, BOOT_A)
        later = observation("2026-08-12T01:00:00.500Z", 1_000, BOOT_B)
        result = event_relative_coordinate(
            anchor, later, anchor_observation_id="anchor"
        )
        self.assertEqual(result["event_offset_basis"], "solardt_utc_fallback")
        self.assertEqual(result["event_offset_ms"], 500.0)
        self.assertNotIn("monotonic_utc_divergence_ms", result)

    def test_utc_reversal_and_monotonic_utc_divergence_remain_visible(self):
        anchor = observation("2026-08-12T01:00:01.000Z", 1_000_000_000)
        later = observation("2026-08-12T01:00:00.900Z", 2_000_000_000)
        result = event_relative_coordinate(
            anchor, later, anchor_observation_id="anchor"
        )
        self.assertEqual(result["event_offset_ms"], 1000.0)
        self.assertEqual(result["utc_crosscheck_offset_ms"], -100.0)
        self.assertEqual(result["monotonic_utc_divergence_ms"], 1100.0)

    def test_missing_acquisition_stamp_uses_utc_fallback(self):
        anchor = {"received_at_utc": "2026-08-12T01:00:00.000Z"}
        later = {"received_at_utc": "2026-08-12T01:00:00.125Z"}
        result = event_relative_coordinate(
            anchor, later, anchor_observation_id="historical"
        )
        self.assertEqual(result["event_offset_basis"], "solardt_utc_fallback")
        self.assertEqual(result["event_offset_ms"], 125.0)


if __name__ == "__main__":
    unittest.main()
