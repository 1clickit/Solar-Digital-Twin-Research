# Collector Inventory and Functions

**Status:** Source-code inventory reviewed 2026-10-13, supplemented by a limited owner-observed runtime check on the same date. No private endpoint, credential, device identifier, or raw measurement record is published.

## Acquisition sources

| Source / implementation | Function | Retained observations and evidence | Current qualification |
| --- | --- | --- | --- |
| EG4 cloud read-only collector (`collectors/eg4/eg4_sync.py`) | Acquires inverter runtime, energy, daily and monthly history | Inverter operating state, grid/EPS and AC-coupled power, PV, load, voltage/frequency, energy totals, battery estimates, fault/warning context; original responses and SQLite-normalized records | Implemented and historically operated; cloud observations are comparatively coarse and may lag physical transitions |
| EG4 setting-provenance collector | Retrieves bounded configuration-change history and configuration epochs | Reported setting values, timestamps, first/last receipt, source references and setting-change evidence | Implemented, historically operated; a successful reported change is not proof of the exact instant it took effect |
| SolarAssistant REST collector (`collectors/solarassistant.py`) | Polls local monitoring data and retains complete response evidence | AC-coupled generation, load, inverter and battery metrics, individual and combined JK readings, collection sequence and source/receipt metadata | Implemented and historically operated; displayed or REST values can have unknown upstream measurement age |
| ESP32/PZEM SSE collector (`collectors/esp32_sse.py`) | Independently receives electrical instrumentation data | AC-coupling-branch L1 voltage, frequency, current, power, power factor and diagnostic/event status with source freshness and acquisition timing | Implemented and historically tested; only one directly measured leg, no validated full waveform/THD or signed energy-flow direction |
| Direct JK BMS SSE collector (`collectors/jk_bms_sse.py`) | Collects per-battery information from BLE-to-ESPHome bridge | Pack voltage/current/power, cell extrema and imbalance, temperatures, health/cycles and protection/freshness states when available | Implemented and historically operated; separate transport from SolarAssistant for the **same physical BMSs**, not independent physical corroboration |
| Weather METAR/SPECI collector (`collectors/kvbt_continuous.py`) | Retrieves regional weather observations for context | Wind, temperature, humidity, visibility, sky and weather reports, observation and retrieval time | Implemented and historically operated; off-site weather is not measured plane-of-array irradiance |

## Limited runtime verification — 2026-10-13

An owner-performed, read-only check on the running Solar Digital Twin Linux VM found **five continuous systemd services active/running**, with `Result=success`, and recent file modification activity in each corresponding evidence directory. These observations support current service availability and filesystem activity **at the time of inspection**, but not sensor-value validity, end-to-end data completeness or uninterrupted collection.

| Continuous service | Latest observed file modification (CDT, 2026-10-13) |
| --- | --- |
| EG4 cloud | 16:33:23 |
| ESP32/PZEM | 16:33:58 |
| Direct JK BMS | 16:33:58 |
| Regional weather | 16:08:29 |
| SolarAssistant | 16:33:52 |

The two-restart counts observed on the ESP32, JK and SolarAssistant services are compatible with their source-controlled one-day runtime limits and automatic restarts; the precise restart cause was **not** independently established. The EG4 setting-history function is part of the EG4 collection path, not a sixth continuously running service.

The **installed software revision was identified locally**, but not matched to the reviewed private repository revision. Actual cadence, individual measurements, live SQLite definitions, raw-file completeness and scheduled daily-job execution were not independently validated during this bounded check.

### CP-100 evidence acquisition — historical; intentionally offline

| Method | Function | Status and limitation |
| --- | --- | --- |
| CP-100 SD-card forensic recovery and parser | Recover historical per-microinverter binary status dumps and gateway waveform records | Successfully demonstrated on a read-only image; retrospective; CP-100 currently intentionally offline |
| CP-100 Canon optical observer | Capture gateway screens and correlate individual channels, operating state, communication age and power with other sources | Successfully demonstrated historically; camera acquisition intentionally offline to avoid equipment risk; displayed fields can be stale |
| CP-100 native data stream | Ideally deliver individual status, event and waveform records directly to Solar Digital Twin | **Not implemented or verified**; a request for manufacturer/developer guidance |

See [CP-100 data acquisition](CP100-CAPTURE-AND-DATA-ACCESS.md) for the actual results, timing limitations, and desired direct interface.

## Collection cadence and provenance

The source-controlled launch policy specifies SolarAssistant polling at 10 seconds, EG4 sync at 5 minutes during a configured daytime window and 15 minutes otherwise, and a regional weather poll every 30 minutes. ESP32/PZEM and direct JK use streaming events rather than a universal periodic poll. The EG4 setting-history path is bounded to approximately daily retrieval. These are **source-controlled intended cadences**; the dated runtime check above confirms service state and file modifications, not actual per-source polling intervals or validated readings. See [Daily operations](DAILY-OPERATIONS.md).

Each source has its own definition of observation time. Local receipt timestamps are **not** automatically equivalent to physical acquisition time. We preserve raw observations, missing-response intervals, freshness and timing qualification rather than replace absent values with zero.

## Additional sources and proposals

Home Assistant has been used for complementary awareness/integration; it is not presented as an additional independent physical sensor or established standalone SolarDT evidence collector here. Camera/OCR automation, direct CP-100 telemetry, irradiance sensors, dual-leg high-bandwidth waveform instrumentation and a unified multi-source SQL schema remain distinct research/development directions until separately verified.

## Research questions

Can existing devices supply a trustworthy event reason, a per-microinverter status timestamp, a commanded-versus-actual AC-coupling state, and a sufficiently synchronized high-bandwidth waveform to determine which electrical/control action occurred first?
