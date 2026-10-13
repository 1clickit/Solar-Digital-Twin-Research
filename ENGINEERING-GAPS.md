# Engineering Questions and Critical Measurement Gaps

This project invites independent engineering analysis rather than presupposing a defective component.

## 1. Artificial-grid power quality (highest priority)

The hybrid inverter forms the 120/240 V AC reference during off-grid operation. Current ESP32/PZEM instrumentation retains useful one-leg RMS voltage, current, frequency and power-factor information, but **cannot establish**:

- The shape and THD of both AC waveforms under changing conditions.
- Fast voltage/current switching transients, high-frequency conducted noise or phase discontinuities.
- The L1/L2 phase relationship and simultaneous leg-specific responses.
- Whether observed frequency variations were intentional curtailment commands, uncontrolled excursions or acquisition artifacts.
- Whether an apparently restored 120 V/60 Hz supply satisfies the microinverters' actual synchronization/reconnect criteria.

A calibrated, appropriately isolated, synchronized dual-leg power-quality/waveform measurement is an unresolved research need. Safe measurement design must respect mains energy, grounding, measurement-category ratings and isolation; a hobby PZEM is not a substitute for a suitable instrument.

## 2. Curtailment transition and excess-energy path

During a command to stop AC-coupled generation, incoming power may continue briefly. The actual H-bridge/conversion path, intermediate bus, DC-link capacitance, charging limits, protective switching and possible energy-dissipation elements are not known from a verified internal schematic.

We seek to understand the energy balance, controller chronology and applicable component limits **without assuming** capacitors alone can dissipate kilowatts or asserting an undocumented absorption circuit exists.

## 3. Interaction with individual microinverters

The CP-100 historical and optical evidence provides per-unit clues, but no verified continuous machine-readable feed with native timestamps. We need to distinguish intentional curtailment, grid-reference loss, anti-islanding/protective response, communications silence and ordinary weather-driven variation.

See [CP-100 evidence](CP100-CAPTURE-AND-DATA-ACCESS.md).

## 4. Extended improvement after inverter replacement

Reported periods approaching six months of normal operation after replacement are potentially important comparative observations. They do not establish an aging-related failure mechanism. Hardware revisions, component stresses, firmware, configuration and external conditions remain competing explanations.

## Smallest useful next evidence

The highest-value experiment would align a naturally occurring production interruption using a suitable **independent dual-leg waveform/power-quality capture**, per-unit microinverter state/reason/timing if accessible, inverter commanded/actual AC-coupling state and direct battery evidence. The experiment should be designed for safety, timestamp quality and non-interference before collection.

This is a research objective, **not authorization** to perform energized work, modify firmware, command shutdowns or change inverter settings.
