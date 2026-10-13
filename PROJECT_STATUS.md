# Project Status

**Status:** Sanitized, public technical research reference. Published documentation and a limited previously reviewed code subset.

## Purpose

Provide manufacturer-neutral context and reproducible technical methods for investigating hybrid-inverter AC-coupling behavior, transient energy handling, per-microinverter state, and artificial-grid power quality. Describe the human-directed, AI-assisted engineering approach.

## Published content

- [README](README.md): introductory research questions, hardware context, AI-assisted methodology, outside collaboration.
- [Collector inventory](COLLECTORS.md): implementation/source functions and measured-data categories.
- [Data architecture](DATA-ARCHITECTURE.md): EG4 SQLite and separate evidence streams, with no actual records.
- [Daily operations](DAILY-OPERATIONS.md): design cadence and forensic processing; limited service/file-activity verification dated 2026-10-13.
- [CP-100](CP100-CAPTURE-AND-DATA-ACCESS.md): historical SD-card recovery and Canon optical observations; no verified native live feed.
- [Engineering gaps](ENGINEERING-GAPS.md): unresolved mechanisms and instrumentation needs.
- [Publication manifest](PUBLICATION-MANIFEST.md): included/excluded material and selected reference code.

## Dated runtime check — 2026-10-13

The owner checked the running SolarDT VM using local read-only commands:

- **Five continuous collector services were active/running**: EG4, ESP32/PZEM, direct JK BMS, regional weather and SolarAssistant.
- **All five evidence directories had recent file modification times** during the same inspection. See [the collector inventory](COLLECTORS.md) for qualified observations.
- The installed revision was identified but not fully reconciled against the reviewed private source revision.
- No independent validation of actual sensor readings, full data completeness, live schema, individual configured polling cadence or daily-job completion was performed.
- The **CP-100 and camera remain deliberately offline** for equipment-safety reasons; their demonstrated historical capabilities are unaffected.

These checks support a bounded operational-status claim, not a complete health or forensic certification. No device or service was restarted, repaired or reconfigured as part of the verification.

## Publication boundaries

Private operational repositories, raw records, original Git history, serials, credentials, personal/site/network details and deployment secrets remain private. No live device, collector service or existing private working repository was changed.

## Deferred work

1. Optional narrow validation of measured-data freshness/quality, live schema and daily-job outcomes if needed for a future engineering claim.
2. Further targeted sanitization and publication of selected collector adapters, schema examples and CP-100 decoding/analysis software, subject to review.
3. Optional synthetic sample dataset for outside reviewers.
4. Manufacturer outreach and feedback review, without treating opinions as validated causes.

The public repository is an engineering communication and reference project, not a deployable digital twin or a manufacturer-endorsed product.
