---
id: "paper-2725"
title: "Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models"
authors: ["Muller, Kilian", "Ruhland, Tim", "Guimaraes, Carlos", "Kaiser, Joachim", "Franchi, Norman"]
year: 2026
venue: "IEEE Open Journal of the Communications Society"
venue_type: "journal"
doi: "10.1109/OJCOMS.2026.3672750"
url: "https://www.scopus.com/pages/publications/105032783783?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2733--2764"
keywords: ["Delay-tolerant networking", "edge computing", "Internet of Things (IoT)", "probabilistic forecasting", "task offloading", "time-series foundation models"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2725 — Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models

## Metadata

- **Authors:** Muller, Kilian and Ruhland, Tim and Guimaraes, Carlos and Kaiser, Joachim and Franchi, Norman
- **Year:** 2026
- **Venue:** IEEE Open Journal of the Communications Society
- **DOI:** 10.1109/OJCOMS.2026.3672750
- **URL:** https://www.scopus.com/pages/publications/105032783783?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2733--2764
- **Language:** English
- **Keywords:** Delay-tolerant networking; edge computing; Internet of Things (IoT); probabilistic forecasting; task offloading; time-series foundation models

### Abstract

Low-power, resource-constrained Internet of Things (IoT) devices are increasingly used for remote monitoring and predictive maintenance, but many modern Machine Learning (ML) workloads exceed their compute and energy budgets. Offloading tasks to nearby edge servers is attractive, yet many real deployments rely on Delay-/Disruption-Tolerant Networking (DTN) via data mules such as public transport or Low Earth Orbit (LEO) satellites, where connectivity is intermittent, stochastic, and often difficult to predict. This paper introduces Firefly, an edge-driven, probabilistic task-offloading framework that enables constrained IoT devices to make deadline-aware offloading decisions over such DTN links. Firefly passively monitors bundle transmissions and aggregates them into contacts, time intervals during which the device can communicate with an edge node. At the edge, Time-Series Foundation Models (TSFMs) are used to forecast distributions over future contact start time, duration, and end-to-end latency for both uplink and downlink. These forecasts are compressed into small probabilistic lookup tables that are periodically sent to the devices. On-device, a lightweight probabilistic forecaster uses these tables to estimate the success probability and response-time distribution of offloading a given task under a configurable risk threshold and soft real-time deadline, and chooses between local execution and offload. We further derive analytical expressions for offloading success probability under our contact model, which we use to instantiate a simple greedy decision policy. We evaluate Firefly using event-driven simulations parametrized by real commuter-train timetables and real LEO satellite orbits. In our train-based DTN scenario, Firefly achieves up to 27% higher task-offloading success rates compared to a Schedule-Aware Bundle Routing (SABR) baseline, and in the satellite scenario up to 19% higher, while remaining executable on constrained devices without any on-device heavy ML.  © 2026 The Authors.

## 04 — Title Screening

**Title:** Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Firefly: Probabilistic Edge-Driven Task Offloading for Real-Time DTN-IoT Using Time-Series Foundation Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
