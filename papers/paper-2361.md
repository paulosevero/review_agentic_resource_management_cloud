---
id: "paper-2361"
title: "An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System"
authors: ["Yang, Luyinru", "Zheng, Jun", "Zhang, Yuan"]
year: 2025
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2025.3635005"
url: "https://www.scopus.com/pages/publications/105022819734?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["cooperative computation", "edge computing", "MARL", "task scheduling", "UAV"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2361 — An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System

## Metadata

- **Authors:** Yang, Luyinru and Zheng, Jun and Zhang, Yuan
- **Year:** 2025
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2025.3635005
- **URL:** https://www.scopus.com/pages/publications/105022819734?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** cooperative computation; edge computing; MARL; task scheduling; UAV

### Abstract

This paper investigates the task scheduling problem for cooperative computation in a multi-UAV edge computing system. The problem is formulated as an integer nonlinear programming problem with an objective to maximize the average number of computation tasks successfully processed in each time slot. To solve the formulated problem using a reinforcement learning method, the problem is first reformulated as a decentralized partially observable Markov decision process (Dec-POMDP) and transformed into an average-reward maximization problem. Then, a multi-agent reinforcement learning (MARL)-based task scheduling algorithm (MTS) is proposed to solve the transformed problem. The proposed MTS algorithm introduces a QMIX-based training framework, in which the local policies of all agents are jointly trained by a central controller in a centralized manner and each agent executes actions independently according to its local observation and local policy in a decentralized manner. Moreover, recurrent neural networks (RNNs) are also introduced to deal with the partial observability of POMDP. Using the proposed MTS algorithm, each UAV is able to make optimal scheduling decisions independently to enable efficient cooperative computation between UAVs. Simulation results demonstrate that the proposed MTS algorithm can achieve better performance than benchmark algorithms in terms of the number of tasks successfully processed in the system. © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System
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
