---
id: "paper-1265"
title: "Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach"
authors: ["Wang, Yupeng", "He, Jinbo", "Shi, Haiyong", "Han, Weizhen", "Liu, Bingyi"]
year: 2024
venue: "2024 International Conference on Information and Communication Technologies for Disaster Management, ICT-DM 2024"
venue_type: "conference"
doi: "10.1109/ICT-DM62768.2024.10798952"
url: "https://www.scopus.com/pages/publications/85216536499?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["5G", "constrained reinforcement learning", "Disaster management", "multi-access edge computing", "task offloading"]
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

# paper-1265 — Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach

## Metadata

- **Authors:** Wang, Yupeng and He, Jinbo and Shi, Haiyong and Han, Weizhen and Liu, Bingyi
- **Year:** 2024
- **Venue:** 2024 International Conference on Information and Communication Technologies for Disaster Management, ICT-DM 2024
- **DOI:** 10.1109/ICT-DM62768.2024.10798952
- **URL:** https://www.scopus.com/pages/publications/85216536499?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 5G; constrained reinforcement learning; Disaster management; multi-access edge computing; task offloading

### Abstract

With the boom in fifth-generation (5G) communication technology, task offloading using multi-access edge computing (MEC) technologies has become an effective approach to satisfy the computation demand of various types of users. Nevertheless, most of the existing task offloading schemes overlook the unavailability of computational resources in disaster areas, failing to guarantee the quality of service (QoS) requirements of task computation in such scenarios. Therefore, this paper treats each edge node as an agent and designs a cooperative multi-agent constrained reinforcement learning (CMACRL) framework for learning the adaptive task offloading policy for each agent, ensuring the performance of emergency services and enhancing the utilization of available computational resources in disaster areas. Specifically, to satisfy the QoS requirements of applications, we formulate the constraints of applications' performance requirements and then adopt the reward constrained policy optimization algorithm to meet the target constraints. Moreover, to mitigate the resource imbalance between disaster and safe areas, we leverage the heterogeneous-agent proximal policy optimization algorithm to generate cooperative resource use strategies for edge nodes. To evaluate the performance of CMACRL, we develop a simulator based on a real-world urban scenario. Extensive experiments are conducted, and experimental results demonstrate that CMACRL significantly improves the task offloading success rate by up to 22.49% and reduces the average service latency by up to 22.69% compared to all the baselines.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Towards Efficient Task Offloading in Disaster Areas: a Constrained RL-based Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
