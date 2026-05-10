---
id: "paper-1274"
title: "A Novel Joint Optimization Method of Multi-Agent Task Offloading and Resource Scheduling for Mobile Inspection Service in Smart Factory"
authors: ["Wu, Yiming", "Zhu, Xiaorong", "Fei, Jichao", "Xu, Honghua"]
year: 2024
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2024.3361492"
url: "https://www.scopus.com/pages/publications/85184323029?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "8563--8575"
keywords: ["multi-agent", "patrol service", "resource allocation", "Smart factory", "task offloading"]
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-1274 — A Novel Joint Optimization Method of Multi-Agent Task Offloading and Resource Scheduling for Mobile Inspection Service in Smart Factory

## Metadata

- **Authors:** Wu, Yiming and Zhu, Xiaorong and Fei, Jichao and Xu, Honghua
- **Year:** 2024
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2024.3361492
- **URL:** https://www.scopus.com/pages/publications/85184323029?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 8563--8575
- **Language:** English
- **Keywords:** multi-agent; patrol service; resource allocation; Smart factory; task offloading

### Abstract

In smart factories, Automated Guided Vehicles (AGVs) are usually used for patrol service, which can carry out such tasks as detecting abnormal device status, transporting material and simultaneously making their own path plan. Hence, these tasks require intensive computational power and real-time response and it is difficult to complete them by a single node. Therefore, in this paper, we propose a joint optimization method of task offloading and resource scheduling of multiple AGVs for smart factory patrol service. The goal is to minimize the overall energy consumption of the AGVs, by jointly using MEC and D2D offloading, while meeting the constraints of the delay, power, available computing capacity and bandwidth of AGVs. We first analyze the impact of information collection and cooperation tasks on transmission delay and formulate an energy consumption minimization problem. Then, we propose a two-step algorithm to get the solutions of the optimization problem. For resource allocation sub-problem, we design an efficient algorithm for power and bandwidth allocation by using the Karush-Kuhn-Tucker (KKT) condition based on the properties of convex bandwidth. To solve the nonlinear task offloading problem, we transform it into a linear mixed integer problem by introducing slack variables and use Gurobi for the solution. Simulation results show that compared with other methods, the proposed algorithm has good performances on convergence speed and energy conservation of AGVs in the process of patrol tasks under different scenarios. © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

## 04 — Title Screening

**Title:** A Novel Joint Optimization Method of Multi-Agent Task Offloading and Resource Scheduling for Mobile Inspection Service in Smart Factory

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A Novel Joint Optimization Method of Multi-Agent Task Offloading and Resource Scheduling for Mobile Inspection Service in Smart Factory
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Novel Joint Optimization Method of Multi-Agent Task Offloading and Resource Scheduling for Mobile Inspection Service in Smart Factory
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
