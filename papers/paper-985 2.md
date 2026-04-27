---
id: "paper-985"
title: "Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms"
authors: ["Khoramnejad, Fahime", "Syed, Aisha", "Kennedy, W. Sean", "Erol-Kantarci, Melike"]
year: 2024
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2024.3375839"
url: "https://www.scopus.com/pages/publications/85187989783?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5647--5661"
keywords: ["Lyapunov optimization", "ML accuracy", "Multi-agent reinforcement learning", "offloading", "stability"]
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

# paper-985 — Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms

## Metadata

- **Authors:** Khoramnejad, Fahime and Syed, Aisha and Kennedy, W. Sean and Erol-Kantarci, Melike
- **Year:** 2024
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2024.3375839
- **URL:** https://www.scopus.com/pages/publications/85187989783?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5647--5661
- **Language:** English
- **Keywords:** Lyapunov optimization; ML accuracy; Multi-agent reinforcement learning; offloading; stability

### Abstract

This study introduces an intelligent task offloading framework designed for smart farms that seamlessly integrates IoT devices, Unmanned Aerial Vehicles (UAVs), and Mobile Edge Computing (MEC) technology. At the heart of our methodology is the utilization of multi-agent reinforcement learning (RL) and Lyapunov theory to optimize task offloading decisions. Our primary contributions are ensuring system stability, task inference accuracy, and minimizing both task loss and delay. System stability is rigorously assessed by formalizing it based on the queue lengths of the MEC server, UAVs, and IoT devices. Furthermore, diverse machine learning (ML) models with varying complexities, such as different numbers of neurons or hidden layers, are deployed by the MEC server, UAVs, and IoT devices. This approach allows us to define task losses in relation to the inference error tolerance of the ML models. Our ultimate goal is to minimize UAV costs, taking into account energy requirements and error tolerance, all the while ensuring system stability. The growing stochastic optimization challenge, particularly with the increasing number of IoT devices, is addressed through the application of Lyapunov optimization theory and a stochastic game framework. However, due to the dynamic nature of the network environment, addressing the game proves to be a challenge, prompting us to develop and implement a multi-agent deep RL (DRL) approach. Our derived intelligent offloading scheme decreases the delay per task by about 35% with respect to the intelligent algorithm without jeopardizing the inference accuracy.  © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
