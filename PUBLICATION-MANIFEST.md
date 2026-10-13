# Public Release: Provenance and Sanitization

**Release scope:** Technical introduction, collector inventory, database model, typical acquisition workflow, CP-100 SD/optical findings, AI-assisted methodology, open measurement questions and a **limited source-code reference subset**.

**Date prepared:** 2026-10-13

## Authoritative boundaries

- The working Solar Digital Twin project and live instrumentation remain separate and private.
- This publication has **fresh public Git history**; it does not mirror private history.
- No private database, raw telemetry, SD-card forensic image, local IP/MAC, device serial, camera frame, home identity, authentication material, or deployment configuration is included.
- Historical results are described as historical; implementation and current runtime availability are not conflated.
- No physical-system control, firmware, service, credential or collector change was made for this release.

## Included reference source

The following files are reproduced **byte-for-byte** from a previously curated and privacy-reviewed September 2026 technical review of the project (the earlier review used source commit `edcf72c8f090f0d470c52a4ca17e03cd6bdfb491`):

| File | Purpose | Publication status |
| --- | --- | --- |
| `src/solar_digital_twin/acquisition_time.py` | UTC/monotonic acquisition stamps, same-boot event-relative timing and provenance | Included, reviewed reference |
| `src/solar_digital_twin/pilot/ids.py` | Stable deterministic content-derived observation, record and run IDs | Included, reviewed reference |
| `tests/test_acquisition_time.py` | Synthetic timing and clock-domain regression checks | Included, synthetic test |

This code is **not** a complete data collector, operational source tree, supported installation or complete representation of the present deployed revision. Publication does not imply an open-source license; licensing of additional code is a separate owner decision.

## Deliberately not included

- Installed EG4, SolarAssistant, ESP32/PZEM and JK collector transport code with site-specific endpoints, logins, installation bindings or runtime configuration.
- Installation/service definitions, authentication setup, device firmware, real camera or gateway parsing pipelines pending separate sanitization.
- Original and derivative raw forensic records, historical databases, binary SD captures, waveform samples, images and logs.
- Private equipment identifiers, remote-access topology, personal paths, operational issue history and correspondence.

## Known limits

Public technical descriptions were derived from repository source and previously recorded forensic work. A fresh read-only check against the running installation has **not** yet established the present health or version of every source. Live deployment details and a broader safe code export may be considered separately.
