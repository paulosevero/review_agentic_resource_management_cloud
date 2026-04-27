---
id: "paper-438"
title: "Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration"
authors: ["Jiang, Feibo", "Dong, Li", "Wang, Kezhi", "Yang, Kun", "Pan, Cunhua"]
year: 2022
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2021.3113872"
url: "https://www.scopus.com/pages/publications/85115674476?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6597--6610"
keywords: ["Distributed deep reinforcement learning (DRL)", "Imitation learning", "Levy flight", "Multiagent reinforcement learning", "Resource scheduling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-438 — Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration

## Metadata

- **Authors:** Jiang, Feibo and Dong, Li and Wang, Kezhi and Yang, Kun and Pan, Cunhua
- **Year:** 2022
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2021.3113872
- **URL:** https://www.scopus.com/pages/publications/85115674476?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6597--6610
- **Language:** English
- **Keywords:** Distributed deep reinforcement learning (DRL); Imitation learning; Levy flight; Multiagent reinforcement learning; Resource scheduling

### Abstract

In large-scale mobile edge computing (MEC) systems, the task latency, and energy consumption are important for massive resource-consuming and delay-sensitive Internet of Things Devices (IoTDs). Against this background, we propose a distributed intelligent resource scheduling (DIRS) framework to minimize the sum of task latency and energy consumption for all IoTDs, which can be formulated as a mixed-integer nonlinear programming. The DIRS framework includes centralized training relying on the global information and distributed decision making by each agent deployed in each MEC server. Specifically, we first introduce a novel multiagent ensemble-assisted distributed deep reinforcement learning (DRL) architecture, which can simplify the overall neural network structure of each agent by partitioning the state space and also improve the performance of a single agent by combining decisions of all the agents. Second, we apply action refinement to enhance the exploration ability of the proposed DIRS framework, where the near-optimal state-action pairs are obtained by a novel Levy flight search. Finally, an imitation acceleration scheme is presented to pretrain all the agents, which can significantly accelerate the learning process of the proposed framework through learning the professional experience from a small amount of demonstration data. The simulation results in three typical scenarios demonstrate that the proposed DIRS framework is efficient and outperforms the existing benchmark schemes.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Distributed Resource Scheduling for Large-Scale MEC Systems: A Multiagent Ensemble Deep Reinforcement Learning with Imitation Acceleration
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
