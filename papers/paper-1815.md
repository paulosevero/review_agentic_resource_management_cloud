---
id: "paper-1815"
title: "Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach"
authors: ["Li, Zixin", "Liang, Xin", "Liu, Juan", "He, Xiaofan", "Xie, Lingfu", "Qu, Long", "Feng, Guinian"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3580468"
url: "https://www.scopus.com/pages/publications/105009599205?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "35756--35772"
keywords: ["Mobile-edge computing (MEC)", "multiagent deep reinforcement learning (MARL)", "uncrewed aerial vehicle (UAV)", "virtual reality (VR)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1815 — Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Li, Zixin and Liang, Xin and Liu, Juan and He, Xiaofan and Xie, Lingfu and Qu, Long and Feng, Guinian
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3580468
- **URL:** https://www.scopus.com/pages/publications/105009599205?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 35756--35772
- **Language:** English
- **Keywords:** Mobile-edge computing (MEC); multiagent deep reinforcement learning (MARL); uncrewed aerial vehicle (UAV); virtual reality (VR)

### Abstract

Virtual reality (VR) demands extensive computation while imposing strict requirements for ultralow latency, placing a significant burden on wireless communication systems. In recent years, there has been a growing interest in leveraging uncrewed aerial vehicle (UAV)-assisted mobile-edge computing (MEC) as a promising technology to provide flexible computing resources at the edge of wireless networks. To meet the computational demands of VR, we propose a collaborative three-layer edge computing framework assisted by multiple UAVs. This framework enables VR rendering tasks to be executed locally on user devices or offloaded to UAVs and base station (BS) for execution. By jointly optimizing the flight trajectories of UAVs and the rendering modes of users, we aim to maximize the average rendering completion rate, defined as the ratio of successfully completed VR rendering tasks within the specified delay constraints, while minimizing the average energy consumption of UAVs. To enhance adaptability, we adopt a multiagent twin delayed deep deterministic policy gradient (MATD3) approach that provides an efficient strategy for multi-UAV-assisted VR rendering, even in partially observable scenarios. Simulation results validate our proposed approach and demonstrate that the MATD3 algorithm surpasses the classical multiagent deep deterministic policy gradient (MADDPG) algorithm in terms of convergence speed and the average rendering completion rate. © 2014 IEEE.

## 04 — Title Screening

**Title:** Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach
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
