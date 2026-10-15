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

## Technical Research Materials

The linked documents present methods and engineering questions without exposing the operating installation or its raw datasets:

- [Collector inventory and functions](COLLECTORS.md) — implemented acquisition paths, recorded fields, cadence, and limitations.
- [Data architecture](DATA-ARCHITECTURE.md) — what the SQLite database and raw evidence streams contain, without database contents.
- [Daily operations and evidence workflow](DAILY-OPERATIONS.md) — collection cadence, time bases, and event reconstruction.
- [CP-100 data recovery and optical capture](CP100-CAPTURE-AND-DATA-ACCESS.md) — demonstrated results and the case for direct read-only access.
- [Engineering and measurement gaps](ENGINEERING-GAPS.md) — artificial-grid waveform quality, excess-energy handling, and evidence needed.
- [Publication manifest](PUBLICATION-MANIFEST.md) — the scope, provenance, and limits of the published code examples.

The `src/` and `tests/` directories contain a **limited, previously reviewed reference-code subset** demonstrating acquisition timing and deterministic identifiers. They are not the complete operating collectors or a deployable installation.

## An AI-Assisted Engineering Research Project

Solar Digital Twin is an independent, owner-directed research effort developed with extensive assistance from artificial intelligence.

The project owner has a background in IT infrastructure, systems integration, and technical troubleshooting, but is not a professional power-electronics designer or embedded-software developer.

The investigation began with firsthand observations of electrical behavior that could not be adequately explained using conventional monitoring tools.

Rather than attempting to diagnose the system through speculation or replacing components without understanding the underlying mechanism, the owner began working with AI assistants to develop a more systematic approach.

### How AI Contributes

See the separate [October 2026 AI collaboration discussion](review-2026-10/) for an independent review of the engineering workflow.

AI assistants, including ChatGPT and Claude, have been used extensively for:

- Researching electrical and electronic engineering concepts.
- Developing software architecture, data collectors, and diagnostic tools.
- Designing ESP32-based instrumentation and supporting firmware.
- Analyzing CP-100 binary records and waveform data.
- Developing camera-based diagnostic acquisition methods.
- Designing databases and evidence-preservation methods.
- Correlating observations from multiple independent data sources.
- Constructing and evaluating competing engineering hypotheses.
- Producing reproducible analysis software, tests, and technical documentation.

The owner provides the physical equipment, real-world observations, operating knowledge, experimental objectives, and practical validation. AI provides assistance with research, programming, analysis, and the development of specialized tools.

Technical decisions and physical-system operations remain under human direction.

### Why This Approach Matters

Many technically capable equipment owners encounter problems that are difficult to investigate without access to specialized engineering expertise, manufacturer documentation, or expensive laboratory instruments.

AI-assisted development can significantly lower the barrier to creating useful diagnostic tools and conducting structured technical investigations.

Our work with Solar Digital Twin illustrates this potential. Tools that would previously have been difficult for an individual to develop can now be designed, implemented, tested, and improved through collaboration between a technically experienced operator and AI systems.

This does not eliminate the need for engineering expertise.

AI-generated designs, software, measurements, and interpretations can contain errors. Observations must be validated, conclusions must remain proportional to the available evidence, and safety-critical questions require appropriate professional expertise and instrumentation.

### An Invitation to Collaborate

We are sharing this project not only to investigate an electrical problem, but also to demonstrate an emerging approach to independent technical research.

We welcome contributions from electrical engineers, equipment manufacturers, software developers, researchers, and others who can challenge our assumptions, identify weaknesses in our methodology, or suggest more effective measurements.

**The objective is not to demonstrate that AI can replace engineering expertise. It is to demonstrate how AI can help an individual ask better questions, construct better tools, and produce evidence that qualified engineers can meaningfully evaluate.**

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