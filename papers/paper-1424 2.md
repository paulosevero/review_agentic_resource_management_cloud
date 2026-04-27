---
id: "paper-1424"
title: "GraphCC: A practical graph learning-based approach to Congestion Control in datacenters"
authors: ["Bern\u00e1rdez, Guillermo", "Su\u00e1rez-Varela, Jos\u00e9", "Shi, Xiang", "Xiao, Shihan", "Cheng, Xiangle", "Barlet-Ros, Pere", "Cabellos-Aparicio, Albert"]
year: 2025
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2024.110981"
url: "https://www.scopus.com/pages/publications/85212587690?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Congestion control", "Datacenters", "Graph neural networks", "Multi-agent reinforcement learning"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1424 — GraphCC: A practical graph learning-based approach to Congestion Control in datacenters

## Metadata

- **Authors:** Bernárdez, Guillermo and Suárez-Varela, José and Shi, Xiang and Xiao, Shihan and Cheng, Xiangle and Barlet-Ros, Pere and Cabellos-Aparicio, Albert
- **Year:** 2025
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2024.110981
- **URL:** https://www.scopus.com/pages/publications/85212587690?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Congestion control; Datacenters; Graph neural networks; Multi-agent reinforcement learning

### Abstract

Congestion Control (CC) plays a fundamental role in optimizing traffic in Datacenter Networks (DCNs). Currently, DCNs implement two main CC protocols: DCTCP and DCQCN. Both protocols are based on Explicit Congestion Notification (ECN), where switches mark packets when they detect congestion. Nowadays, network experts carefully set ECN parameters to optimize the average network performance. However, today's DCNs experience rapid and abrupt changes that severely affect the network state (e.g., dynamic workloads, incasts), which leads to under-utilization and sub-optimal performance. In this paper we present GraphCC, a framework for in-network CC optimization. GraphCC relies on Multi-agent Reinforcement Learning (MARL) and Graph Neural Networks (GNN), and is compatible with widely deployed ECN-based CC protocols. The proposed solution deploys distributed agents on switches that communicate with their neighbors to cooperate and optimize the global ECN configuration. In our evaluation, we test GraphCC with three real-world traffic workloads, focusing on its capability to accommodate scenarios unseen during training (e.g., traffic changes, failures). We compare GraphCC with a state-of-the-art MARL solution for ECN tuning, and observe that our method outperforms the state-of-the-art baseline in all evaluation scenarios, with improvements up to 20% in average Flow Completion Time, similar mean throughput (within 1%), and significant reductions in buffer occupancy (38.0–85.7%). © 2024 The Authors

## 04 — Title Screening

**Title:** GraphCC: A practical graph learning-based approach to Congestion Control in datacenters

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** GraphCC: A practical graph learning-based approach to Congestion Control in datacenters
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** GraphCC: A practical graph learning-based approach to Congestion Control in datacenters
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
