# CP-100 Capture Equipment and the Case for Direct Data Access

## Summary

We have successfully used **two independent approaches** to extract useful diagnostic information from a Chilicon CP-100 gateway: forensic recovery from an SD-card image and a Canon-camera optical observer of the live CP-100 diagnostic display. These are **historical, demonstrated methods**, not a claim of continuous native CP-100 telemetry.

Both approaches reveal per-microinverter information unavailable in ordinary aggregate hybrid-inverter telemetry.

**Current operating status (2026-10-13):** The CP-100 gateway and camera-based acquisition equipment are **intentionally offline because of equipment/camera risk**. This is a protective operator decision, **not** evidence of collector malfunction. Neither device nor its capture services were activated or tested in the October 13 runtime check. The results below describe completed historical acquisition only; resuming capture would require separate owner authorization and an equipment-safety review.

## 1. Historical SD-card acquisition

A read-only forensic image of the CP-100 SD card was preserved and analyzed without changing the live gateway.

The historical analysis reported:

| Recovered artifact | Quantity / property |
| --- | --- |
| Status-dump files | **209** |
| Complete microinverter status records | **729,194**, with an 84-byte record format |
| Identified microinverter channels | **Six**, correlated by gateway identifiers |
| Waveform recording CSV files | **Ten** |
| Retained waveform records | **15,664**, with **512 samples** per record |

Parsing and selected power-field interpretations were validated against the gateway's own displays. Waveform reconstruction permitted exploratory RMS, sag/swell, symmetry and distortion analyses, although the original trigger algorithm, measurement reference and all binary-field semantics are not yet fully established.

The data can support retrospective inquiry; it does not demonstrate a live export capability or prove that every transient was captured.

## 2. Canon optical observer

A camera-based observation workflow captured retained JPEGs of the CP-100's diagnostic display, enabling comparisons with inverter, SolarAssistant, PZEM and BMS data. Capture and delivery were used successfully during bounded observation periods.

Visible diagnostic information includes per-microinverter production, operating/process status, voltage/frequency and diagnostic indicators, temperature, and the gateway's **Last OOK Received** age.

This gave the investigation a valuable independent source when aggregate power readings appeared anomalous.

### Demonstrated event correlation

During a reviewed event, retained JPEGs showed the six channels receiving recent updates, followed by their displayed communication-age indicators ceasing to refresh before a later aggregate production decline and system transfer.

This was evidence of a near-group OOK communication-age change over the display's update cycle—not proof that all six devices electrically disconnected at the same instant or that the microinverters initiated the event.

The optical audit identified an important limit: channel values were refreshed asynchronously over approximately **42 seconds**. Camera frame time does not make a field's displayed value a fresh, simultaneous electrical measurement. Some automated recognizer values were rejected in event windows; the retained original JPEGs remained the more defensible evidence.

## 3. Why this is not yet native CP-100 telemetry

- An SD-card image is **retrospective**, not a continuous source.
- Optical acquisition depends on view, capture interval, per-screen refresh and interpretation quality.
- A camera timestamp is **not** a microinverter's measurement timestamp.
- Neither method supplies a verified continuous machine-readable CP-100 interface into Solar Digital Twin.
- CP-100 waveform records do **not** substitute for a synchronized, calibrated dual-leg measurement of the grid-forming inverter's artificial AC waveform.

## 4. The highest-value direct access

A documented **read-only local** API, stream or export would be valuable if it supplied:

- Individual microinverter identity, operating state, AC/DC quantities and output power.
- Protective-trip, synchronization, curtailment, reconnection and fault/reason indications where supported.
- Each observation's **native timestamp or measurement age**, channel identity, update sequence and freshness.
- Gateway communications statistics, missed packets, OOK status and last-good-update time.
- Original diagnostic waveform records, measurement scales, sampling rate, trigger reason and acquisition time, when recorded.

Direct collection could remove camera/display interpretation errors and gaps. It would **not** automatically make the underlying telemetry faster than the hardware's sampling and communications behavior.

## Questions for interested engineers

1. Is there a documented local read-only CP-100 interface, or a supported way to export raw status records and original timestamps?
2. What is the precise relationship among microinverter sample time, OOK reception time, screen refresh and gateway record time?
3. How are SD-card status and waveform files generated, and what triggers a waveform recording?
4. Can per-unit protection/reconnection reason codes be obtained without interfering with the grid, microinverters or normal gateway operation?
5. Could a direct feed safely provide enough synchronized per-unit evidence to distinguish a source disturbance from the protective response it caused?

## Public code and privacy

This release does **not** include the private SD-card image, real gateway dump, screenshots, optical recognizer runtime, binary parser or installation-specific camera firmware. Those components require separate technical/provenance and privacy review before any source release. The present documentation records verified achievements and outstanding interface questions.

The purpose of access is better **system-level diagnosis**, not assigning fault to the gateway or any particular manufacturer.
