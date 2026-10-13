# Data Architecture: What We Record, Not the Records

This describes the private research system's **data model and evidence roles**. No actual SQLite files, database rows, raw JSON/NDJSON, device serial numbers, images, operational paths, or home-network details are distributed here.

## Evidence-first model

```text
EG4 cloud ──────────────> immutable original responses ──> EG4 SQLite views
SolarAssistant REST ────> timestamped raw NDJSON ──────────┐
ESP32/PZEM SSE ────────> timestamped raw NDJSON ───────────┤
Direct JK/BMS SSE ─────> timestamped raw NDJSON ───────────┼─> bounded forensic correlation
Weather reports ───────> contextual records ──────────────┤    and derived reports
CP-100 SD/optical ─────> historical forensic material ────┘
```

Raw preserved observations are evidence; the database and analytical reports are derived consumers or query indexes. Missing, stale, cached, invalid, or contradictory observations must remain identifiable instead of being silently corrected.

## Implemented EG4 SQLite database

The working project's EG4-specific SQLite table definitions reside in `collectors/eg4/eg4_database.py`. A separate legacy `database/schema.sql` file is empty; it is **not** the live schema.

| Table or family | What it records |
| --- | --- |
| `sync_runs` | Source collection runs and time/provenance metadata |
| `evidence_files` | Links to original source files and checksums |
| `runtime_snapshots` | Inverter status, battery estimates, selected grid/EPS measurements, AC-couple/load power, temperatures and source timestamps |
| `energy_snapshots` | Per-day and cumulative energy/import/charging/discharging figures |
| `day_multiline_samples` | Time-indexed solar, grid, battery, consumption and AC-coupled production values |
| `month_energy_days` | Day-level energy totals returned by the inverter service |
| `set_records` | Reported configuration-change events and original-source lineage |
| `configuration_history_runs` | Attempts and results for configuration history acquisition |
| `configuration_epochs` | Reconstructed periods with effective reported settings, certainty and provenance |

Some fields store original JSON inside SQLite in addition to normalized values. Those payloads and the actual database are not public.

## Separate evidence streams

- **SolarAssistant:** full-response polling envelopes and selected normalized/retained measurement records in NDJSON; battery and inverter topics, with clear source lineage.
- **ESP32/PZEM:** raw and reviewed SSE event observations, response sequences, electrical-value validity and timing context. A sensor's failure to respond is recorded as a gap rather than invented electrical zero.
- **Direct JK BMS:** source-labeled, sequential per-pack/cell metrics and health/protection/freshness context.
- **Regional weather:** timestamped METAR/SPECI observations used only as context.
- **CP-100:** historical SD-card data and optical image-derived observations; not a verified live native feed.

## Timing and source independence

The implemented acquisition-time model can retain receipt UTC, Linux monotonic time, a host boot identity, collector run identity and ingest sequence. Same-boot monotonic comparisons can support event-relative acquisition ordering; different devices and time domains require qualified alignment.

EG4 cloud data and SolarAssistant inverter telemetry observe **the same inverter** through different transports. Direct JK and JK-through-SolarAssistant observe **the same batteries/BMSs** through different transports. Agreement is useful, but not independent physical confirmation.

## Implemented versus planned

The EG4 SQLite history exists and has been used. A complete unified SQL database containing every SolarAssistant, ESP32, CP-100 and JK source **does not yet exist as a verified integrated implementation**; broader site/device/collector/measurement/event/analysis-run tables are design goals. The independent raw evidence streams and correlation analyses precede that integration.

## Example code

The [reference timing module](src/solar_digital_twin/acquisition_time.py), its [synthetic regression tests](tests/test_acquisition_time.py), and [deterministic identifier module](src/solar_digital_twin/pilot/ids.py) illustrate two reproducibility techniques. They are a curated reference subset, not production collection scripts.
