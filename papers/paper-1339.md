---
id: "paper-1339"
title: "A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds"
authors: ["Zhao, Yunfeng", "Wang, Ziwei", "Qiu, Chao", "He, Qiang", "Niyato, Dusit", "Wang, Xin", "Wang, Xiaofei", "Hu, Qinghua"]
year: 2024
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2024.3403048"
url: "https://www.scopus.com/pages/publications/85194043095?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3092--3109"
keywords: ["Deep reinforcement learning", "edge computing", "edge-cloud collaboration", "request dispatch", "service orchestration"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1339 — A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds

## Metadata

- **Authors:** Zhao, Yunfeng and Wang, Ziwei and Qiu, Chao and He, Qiang and Niyato, Dusit and Wang, Xin and Wang, Xiaofei and Hu, Qinghua
- **Year:** 2024
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2024.3403048
- **URL:** https://www.scopus.com/pages/publications/85194043095?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3092--3109
- **Language:** English
- **Keywords:** Deep reinforcement learning; edge computing; edge-cloud collaboration; request dispatch; service orchestration

### Abstract

Edge computing has emerged as a powerful paradigm for efficient scheduling at the network edge to fulfill users' requirements for low latency. Edge servers' and clouds' ability to interact allows them to leverage edge servers' limited computing and storage resources collectively to handle all requests collaboratively. This has unlocked the potential of the edge-cloud system. However, its sophistication (e.g., heterogeneous resources, intertwined dependencies, etc.) also raised unforeseen challenges in request dispatch and service orchestration phases within the scheduling process, including complex hierarchy, limited cooperation and unfocused information. Traditional resource optimization methods for edge-cloud systems cannot address these intricate situations properly, raising concerns over system efficiency, stability, and costs. This article proposes learning-based methods to accommodate time-varying requests and dynamic service prevalence. Specifically, we employ the multi-agent advantage actor-critic (MAA2C) and the graph convolutional networks-based MAA2C (GCN-MAA2C) in two phases, respectively, to enhance individual intelligence and facilitate optimal dispatch and orchestration decisions. Inspired by the regulations in human society, we propose SocialEdge, a socialized learning-based scheduling framework for the edge-cloud system. To leverage the hierarchical correlation, we develop an inter-layer socialized refining mechanism. The inference results from one layer guide the training process of the next layer, enabling the abstraction of optimization-critical knowledge. Moreover, we apply intra-layer socialized cooperating, where federated averaging with MAA2C is implemented to ensure the cooperation of individuals over private data for achieving optimal global solutions. Furthermore, we propose a socialized resonance mechanism across the layers to extract high-value information and induce resonance toward the system objective, aiming to improve the efficiency of scheduling. Experimental evaluations on a proof-of-concept testbed and two real traces demonstrate that SocialEdge reduces scheduling cost by 11.2% while enhancing time efficiency by 77.4%, and system throughput by 17.9%, compared to baseline methods.  © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Socialized Learning-Based Scheduling Framework in Intricate Edge Clouds
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
