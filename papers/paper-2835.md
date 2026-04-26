---
id: "paper-2835"
title: "Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems"
authors: ["Wang, Shanshan", "Luo, Zhiyong"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3663103"
url: "https://www.scopus.com/pages/publications/105029975118?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["deep reinforcement learning (DRL)", "mobile edge computing (MEC)", "resource allocation", "service reliability", "trajectory planning", "Unmanned aerial vehicles (UAVs)"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2835 — Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems

## Metadata

- **Authors:** Wang, Shanshan and Luo, Zhiyong
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3663103
- **URL:** https://www.scopus.com/pages/publications/105029975118?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning (DRL); mobile edge computing (MEC); resource allocation; service reliability; trajectory planning; Unmanned aerial vehicles (UAVs)

### Abstract

Cellular-connected unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has emerged as a key enabler for the low-altitude economy network (LAEN), supporting task offloading from UAVs to ground base stations (GBSs) in aerial Internet of Things (IoT) applications. However, existing studies focus on conventional stochasticity such as fading channels and random task arrivals, while largely overlooking the dynamic service availability of rapidly deployed ad-hoc GBSs in extreme, high-demand scenarios, characterized by a stress-driven lifecycle including resource depletion, probabilistic service disruptions, and delayed recovery. Such dynamics may cause severe energy inefficiency and queue backlogs, undermining system reliability. To address these issues, we formulate a joint optimization problem of resource allocation and 3D trajectory planning, which explicitly integrates a multi-dimensional GBS reliability-aware model to capture this service lifecycle, aiming to minimize the weighted energy–delay system cost while ensuring long-term queue stability. We develop a dual-layer online optimization framework: the outer layer reformulates the objective function using a time-adaptive velocity-triggered penalty term (TA-VTPT) to suppress energy spikes from abrupt velocity changes, then leverages Lyapunov drift-plus-penalty to decompose the original problem into per-slot subproblems; the inner layer proposes a Lyapunov-guided multi-agent dual actor-critic (LyMADAC) algorithm to generate real-time decentralized decisions without future information. Simulations show that our approach effectively reduces the system cost while ensuring queue stability across heterogeneous traffic patterns and extreme stress scenarios, and further demonstrates robustness under representative non-idealities (e.g., wind disturbance and battery aging). © 2014 IEEE.

## 04 — Title Screening

**Title:** Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Reliability-Aware Multi-Agent Deep Reinforcement Learning for Stochastic Optimization in Cellular-Connected UAV-Assisted MEC Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
