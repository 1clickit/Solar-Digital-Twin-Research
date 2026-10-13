# Solar Digital Twin Research

**Independent research into hybrid inverter behavior, AC-coupled solar generation, power electronics, and electrical system stability.**

**Status:** Active research and investigation

## Why This Project Exists

Solar Digital Twin was created to investigate recurring electrical and solar-production anomalies in a residential, off-grid-capable solar energy system.

The system combines a hybrid, grid-forming inverter, AC-coupled photovoltaic microinverters, lithium battery storage, and utility backup power.

Although the installation can operate normally for extended periods, it has exhibited unexplained solar-production interruptions, frequency-related behavior, and other electrical anomalies.

We want to understand what occurs electrically before, during, and after these events.

Our objective is not simply to identify a malfunctioning device. It is to understand the interactions among the inverter's power electronics, the artificial AC grid it creates, the microinverters connected to that grid, the battery system, and the loads they collectively support.

The project was developed to collect evidence from independent sources, reconstruct events, evaluate competing explanations, and eventually identify a reproducible mechanism and practical resolution.

## System Configuration

The representative installation consists of:

| Component | Configuration |
|---|---|
| Hybrid inverter | EG4 12000XP V1, split-phase 120/240 V |
| Previous inverter equipment | Two EG4 6000XP units |
| Solar generation | 12 photovoltaic modules, approximately 5.37 kW DC nameplate |
| AC-coupled generation | Six Chilicon CP-720 microinverters |
| Battery storage | Two parallel 16S LiFePO4 battery packs, approximately 32 kWh total |
| Battery management | Independent JK BMS units |
| Monitoring | SolarAssistant and inverter telemetry |
| Independent electrical measurements | ESP32/PZEM AC monitoring |
| Diagnostic platform | Solar Digital Twin |
| Operating priority | Solar and battery operation, utility power as backup |

The installation does not intentionally export power to the utility grid.

This is a simplified engineering configuration, not a complete wiring diagram. Identifying network information, serial numbers, private site data, and credentials are excluded.

## A Curious Pattern: Extended Improvement Following Inverter Replacement

One of our more interesting observations concerns the effect of replacing the hybrid inverter.

The installation previously used two 6000XP units and was subsequently upgraded to a 12000XP, partly to determine whether a different inverter design would eliminate the observed behavior.

Following replacements, the system appeared to operate satisfactorily for extended periods, in some instances approaching six months, before similar concerns returned.

These periods are reported operating history rather than proof of a specific hardware failure.

Nevertheless, they raise an important question:

**What could explain months of apparently satisfactory operation after inverter replacement, followed by the recurrence of similar symptoms in a system whose external configuration remained substantially unchanged?**

Possibilities worth examining include component aging, accumulated electrical or thermal stress, changes in operating conditions, firmware or control behavior, and interactions with connected equipment.

We are also interested in comparing the original 12000XP design with the V2 revision to determine whether changes to the power stages, components, protection circuitry, firmware, or AC-coupling behavior might be relevant.

We have not established that V2 addresses the symptoms under investigation.

## The Central Power-Electronics Question

A major research question concerns what happens inside a grid-forming inverter when AC-coupled solar generation must be curtailed or disconnected.

Consider a system producing several kilowatts of solar power while charging batteries and supporting household loads.

When the battery reaches a configured charging limit, the hybrid inverter may initiate a sequence intended to reduce or stop AC-coupled generation.

However, the microinverters may continue producing for some interval before responding to changed electrical conditions or losing their AC reference.

During that interval, the electrical system must maintain a workable balance between incoming generation, load demand, conversion capability, and available energy storage.

**Where does the incoming energy go during this transition, and how does the inverter maintain electrical stability?**

We are particularly interested in the following questions:

- How does the inverter's H-bridge or other switching power-stage architecture respond to sudden changes in AC-coupled power?
- What role does the DC-link capacitor bank play during transient energy imbalances?
- Can incoming energy be transferred through a bidirectional power-conversion stage into battery storage or another available path?
- What happens when the batteries cannot accept additional charging current?
- Are additional energy-handling, clamping, or protective circuits involved?
- How are switching devices and DC-link voltage protected during curtailment, shutdown, and reconnection?
- What sequence occurs between a control decision and the actual cessation of microinverter output?

DC-link capacitors can buffer transient energy, but they cannot be assumed to absorb sustained kilowatts of excess generation. Any continuing energy transfer requires an appropriate path or a reduction in incoming power.

The actual internal architecture and control sequence have not been independently established.

Understanding these details may help distinguish expected operating behavior from instability or component stress.

## A Major Measurement Gap: The Quality of the Artificial Grid

One of the most important unanswered questions concerns the **quality of the artificial AC grid created by the hybrid inverter**.

In off-grid operation, the inverter is responsible for establishing the voltage and frequency reference used by connected equipment, including the AC-coupled microinverters.

Our existing instruments provide useful measurements of voltage, frequency, current, power, and power factor.

However, our independent ESP32/PZEM measurements presently cover one leg of the AC-coupling circuit and do not provide a sufficiently detailed view of the waveform itself.

Consequently, we cannot yet establish the full power quality of the inverter-generated AC supply.

Important unmeasured or inadequately characterized properties include:

- Voltage waveform shape and total harmonic distortion.
- High-frequency switching noise and conducted disturbances.
- Short-duration frequency excursions and phase discontinuities.
- Voltage transients during switching, load changes, and source transfers.
- Dynamic response to inductive loads and compressor startup.
- Differences between L1 and L2, including balance and phase relationship.
- How effectively the grid-forming inverter maintains its AC reference when generation and loads change rapidly.

This distinction is critical.

A monitoring system reporting approximately 120 V and 60 Hz does not necessarily establish that the underlying waveform is clean or stable under rapidly changing conditions.

Likewise, intentional frequency changes used for AC-coupled generation control must be distinguished from unintended disturbances.

**We would particularly welcome recommendations for safely obtaining independent, time-synchronized measurements of both legs of the artificial grid, with sufficient bandwidth and accuracy to characterize waveform and transient behavior.**

Until such measurements are available, power quality remains an important unresolved part of the investigation.

## Other Engineering Questions

We are examining several related areas without presuming a particular cause.

### AC-Coupling Control

How do frequency-based curtailment, voltage thresholds, protection limits, and relay sequencing interact?

What control behavior should occur when the battery approaches its charging limit?

How long should generation shutdown and reconnection take?

### Microinverter Response

How should grid-following microinverters react to changes in frequency, voltage, waveform quality, or loss of the grid-forming reference?

Could temporary synchronization or protection responses explain some of the observed production interruptions?

What additional status or event information would help separate a microinverter response from the condition that triggered it?

### Loads and System Stability

Can load changes expose weaknesses in voltage regulation, control-loop behavior, or AC-coupling stability?

How do compressor-driven loads and other electrical equipment affect the inverter-generated grid?

### Hardware and Long-Term Behavior

Could thermal cycling, component characteristics, accumulated stress, or protection behavior explain the apparent delay between inverter replacement and symptom recurrence?

Are differences between hardware revisions relevant?

### Measurement Accuracy

Could some apparent anomalies result from telemetry delays, cached values, communication interruptions, or measurements taken at different times?

What independent observations would distinguish genuine electrical events from monitoring artifacts?

## What Solar Digital Twin Does

Solar Digital Twin is an independent diagnostic platform that combines information from multiple sources:

- SolarAssistant operating and historical data.
- Hybrid inverter state and configuration telemetry.
- Direct battery-management-system observations.
- ESP32/PZEM electrical measurements.
- Available weather and environmental information.

The platform preserves the original evidence and supports time-correlated analysis.

Its engineering approach emphasizes separating:

1. Direct physical measurements.
2. Device-reported telemetry.
3. Derived calculations.
4. Operator observations and historical context.
5. Hypotheses that remain unverified.

This helps reconstruct events without assuming that every source reports the same physical instant.

## What We Have Learned So Far

Our investigations indicate that visually similar solar-production interruptions can represent different events.

Some shutdown and restart cycles are strongly consistent with configured battery-voltage-based AC-coupling control.

Other large production reductions have occurred below the expected shutdown threshold, without corresponding inverter control-state changes.

These remain unresolved.

Available measurements have helped distinguish some real production reductions from instrumentation failures, but do not yet explain every initiating mechanism.

The research therefore separates expected control behavior, unexplained electrical events, environmental effects, and monitoring limitations.

No particular internal inverter component has been demonstrated to be defective, and no single manufacturer has been established as the cause.

## Where We Would Welcome Engineering Input

This repository is intended to encourage constructive technical discussion among engineers, researchers, developers, and others familiar with distributed power systems.

We welcome insight into:

- Grid-forming inverter architecture.
- H-bridge and bidirectional power-conversion design.
- DC-link capacitor behavior and transient energy management.
- AC-coupled solar generation and curtailment methods.
- Microinverter synchronization and protection responses.
- Power-quality measurement and waveform analysis.
- Time-synchronized data collection and diagnostic instrumentation.
- Hardware revisions, design margins, and long-term operating reliability.

We are especially interested in suggestions for **the smallest number of additional measurements that could distinguish the leading hypotheses**.

The objective is not to collect endless telemetry, but to identify the measurements that will actually answer the engineering questions.

## Research and Publication Principles

This public repository is a deliberately sanitized presentation of an independently operated research project.

Private operational records, raw evidence, network configurations, device identifiers, and credentials remain outside this repository.

Results will distinguish established observations from interpretations and open questions. Planned capabilities will not be represented as completed work.

The material is intended for technical discussion and should not be treated as installation guidance, proof of a product defect, or a manufacturer-endorsed engineering assessment.

**Our objective is to understand why the system behaves as it does, determine what can be measured to explain it, and share useful findings with the wider engineering community.**