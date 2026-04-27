---
id: "paper-751"
title: "SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems"
authors: ["Wang, Ziwei", "Zhao, Yunfeng", "Qiu, Chao", "He, Qiang", "Wang, Xin", "Wang, Xiaofei", "Hu, Qinghua"]
year: 2023
venue: "Proceedings - International Conference on Distributed Computing Systems"
venue_type: "conference"
doi: "10.1109/ICDCS57875.2023.00066"
url: "https://www.scopus.com/pages/publications/85175073095?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "853--863"
keywords: ["cloud-edge collaboration", "deep reinforcement learning", "edge computing", "Request dispatch", "service orchestration"]
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
    human_justification: "Talvez a ideia de socialização indique Agents."

---

# paper-751 — SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems

## Metadata

- **Authors:** Wang, Ziwei and Zhao, Yunfeng and Qiu, Chao and He, Qiang and Wang, Xin and Wang, Xiaofei and Hu, Qinghua
- **Year:** 2023
- **Venue:** Proceedings - International Conference on Distributed Computing Systems
- **DOI:** 10.1109/ICDCS57875.2023.00066
- **URL:** https://www.scopus.com/pages/publications/85175073095?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 853--863
- **Language:** English
- **Keywords:** cloud-edge collaboration; deep reinforcement learning; edge computing; Request dispatch; service orchestration

### Abstract

The ability for cloud data centres and edge data centres to collaborate unleashes the potential of the edge-cloud system. However, its sophistication causes unexpected issues in request scheduling, such as Insufficient intelligence, complicated hierarchy and limited cooperation. Traditional resource optimization methods for the edge-cloud system struggle to accommodate such intricate situations. In this paper, inspired by the behaviors and regulations in human society, we propose a socialized learning-based scheduling approach for the edge-cloud system, namely SocialEdge. In order to adapt to time-varying requests and dynamic service prevalence, we propose a learning-based approach, multi-agent advantage actor-critic (MAA2C) and graph convolutional networks-based MAA2C for two phases, respectively, which can improve individual intelligence to achieve optimal dispatch and orchestration decisions. Then, to make use of hierarchy correlation, we develop the socialized refining inter the layers, where inference results from one layer guide the training process of the other layer so that optimization-critical knowledge can be abstracted. Besides, we apply socialized cooperation to each layer, where federated averaging with MAA2C is implemented to ensure cooperation over private data for achieving optimal global solutions. Experimental evaluations on a proof-of-concept testbed along with two real traces demonstrate that baselines have 105% more delay than SocialEdge while being 76.6% less time efficiency and 21.6% less throughput. © 2023 IEEE.

## 04 — Title Screening

**Title:** SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SocialEdge: Socialized Learning-Based Request Scheduling for Edge-Cloud Systems
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
