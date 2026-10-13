# Daily Collection and Forensic Review

**Important:** This describes collector design and historically validated practices. A **bounded read-only check on 2026-10-13** confirmed that all five continuous collector services were running and their respective evidence directories had recent file modifications. It **did not** validate measurement contents, full capture cadence, live database schema or daily-job execution. CP-100 and camera acquisition remain intentionally offline for equipment protection; see [Collector inventory](COLLECTORS.md).

## Source-controlled collection policy

| Stream | Designed behavior | Major limitation |
| --- | --- | --- |
| EG4 cloud history | Sync approximately every **5 minutes** during the configured daytime interval (06:20–18:26 local in the reviewed launcher), **15 minutes** otherwise | Cloud timestamps and update/transport delay are too coarse for sub-second causality |
| EG4 settings history | Bounded acquisition of setting changes/epochs, approximately once each local day | Reported state is not an exact physical switching timestamp |
| SolarAssistant REST | Complete-response poll every **10 seconds** in the reviewed continuous launcher | Different metrics may be cached or updated at different upstream times |
| ESP32/PZEM | Streaming; qualified electrical response records have been observed at approximately **1-second** intervals | Currently one physical leg; meter readings cannot prove waveform purity |
| Direct JK BMS | Streaming changes from a BLE/ESPHome bridge; independent per-field refresh/freshness | BMS entities are not one simultaneous pack-wide measurement |
| Weather | Poll **every 30 minutes**; retained reports follow their own observation times | Regional conditions cannot establish sunlight on the panels |
| CP-100 historical/optical | SD-card recovery on demand and bounded attended/recorded optical observation | No established always-on native CP-100 collection |

## How evidence is handled

1. A collector obtains a source observation or response without commanding the electrical system.
2. Host acquisition/receipt time, sequence and source provenance are attached where supported.
3. Original evidence is retained; validated/selected records provide faster downstream analysis.
4. Availability, gaps, stale values, source/receipt disagreement and communications interruption are explicitly recorded.
5. An analysis identifies candidate solar-production changes and distinguishes known expected curtailment, source transfers, weather-like variation and unresolved events.
6. For a credible candidate, relevant source observations are reconstructed before/during/after and compared with similar normal intervals.
7. Reports state supporting evidence, contradictions, timing uncertainty and what next measurement would distinguish hypotheses.

The forensic project includes code for deterministic audits and bounded reports. Their existence does not alone prove that a particular report is automatically generated each day in the currently running environment.

## Typical measurement categories

- **Inverter:** AC-coupled power, operating mode, source/grid/EPS state, voltage/frequency, load and energy totals.
- **Battery:** voltage/current/power, per-pack state, cell differences, temperatures, charge/discharge and protection context.
- **Independent branch sensor:** voltage, current, power, frequency, PF and response/quality status on one measured AC-coupling leg.
- **Microinverters:** retrospective per-unit production and status via CP-100 SD/optical evidence; no proven direct native live feed.
- **Context:** regional weather, reporting changes, collector health, time quality and configuration epoch.

## Limitations that matter

A normal-looking 120 V / 60 Hz RMS measurement does not validate harmonic distortion, switching noise or short transients. An apparent inverter-dashboard zero may disagree with contemporaneous independent evidence. Sources need qualified clocks and a method to distinguish aged displayed data from newly observed measurements.

For those gaps, see [Engineering questions](ENGINEERING-GAPS.md) and [CP-100 findings](CP100-CAPTURE-AND-DATA-ACCESS.md).
