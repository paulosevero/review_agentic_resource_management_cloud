---
id: "paper-643"
title: "Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System"
authors: ["Li, Si", "Li, Wei", "Shi, Huaguang", "Yan, Wenhao", "Zhou, Yi"]
year: 2023
venue: "ACM International Conference Proceeding Series"
venue_type: "conference"
doi: "10.1145/3640912.3640991"
url: "https://www.scopus.com/pages/publications/85186955718?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "403--407"
keywords: ["reinforcement learning", "task offload", "trajectory optimization", "Unmanned air vehicle"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-643 — Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System

## Metadata

- **Authors:** Li, Si and Li, Wei and Shi, Huaguang and Yan, Wenhao and Zhou, Yi
- **Year:** 2023
- **Venue:** ACM International Conference Proceeding Series
- **DOI:** 10.1145/3640912.3640991
- **URL:** https://www.scopus.com/pages/publications/85186955718?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 403--407
- **Language:** English
- **Keywords:** reinforcement learning; task offload; trajectory optimization; Unmanned air vehicle

### Abstract

Unmanned Aerial Vehicles (UAVs) equipped with Multi-Access Edge Computing (MEC) servers can assist Terminal Devices (TDs) in offloading data tasks. In this paper, we investigate a resource allocation and trajectory optimization problem of multiple UAVs assisting TDs in task computation, and our main goal is to improve the task computation efficiency of the system to meet the high-quality experience of TDs. We consider the fairness of TD's computing data volume and the fairness of UAV energy consumption. The problem is transformed into a Partially Observable Markov Decision Process (POMDP). The large action space generated during the UAV flight and resource allocation decision-making process leads to a policy overfitting problem for Multi-Agent Proximal Policy Optimization (MAPPO) method. Policy overfitting causes the UAV to update the policy gradient in the suboptimization direction, preventing it from exploring better flight trajectories. To meet this challenge, we propose a novel method of policy regularization, NV-MAPPO. Simulation results show that NV-MAPPO has significant advantages in latency and energy consumption.  © 2023 ACM.

## 04 — Title Screening

**Title:** Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Fairness-Aware Computation Efficiency Maximization for Multi-UAV-Enabled MEC System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
