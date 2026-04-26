---
id: "paper-715"
title: "Collaborative Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud Network"
authors: ["Shen, Shihao", "Han, Yiwen", "Wang, Xiaofei", "Wang, Shiqiang", "Leung, Victor C. M."]
year: 2023
venue: "IEEE/ACM Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TNET.2023.3267168"
url: "https://www.scopus.com/pages/publications/85159691959?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2950--2964"
keywords: ["Edge computing", "Kubernetes", "reinforcement learning", "scheduling algorithms"]
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

# paper-715 — Collaborative Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud Network

## Metadata

- **Authors:** Shen, Shihao and Han, Yiwen and Wang, Xiaofei and Wang, Shiqiang and Leung, Victor C. M.
- **Year:** 2023
- **Venue:** IEEE/ACM Transactions on Networking
- **DOI:** 10.1109/TNET.2023.3267168
- **URL:** https://www.scopus.com/pages/publications/85159691959?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2950--2964
- **Language:** English
- **Keywords:** Edge computing; Kubernetes; reinforcement learning; scheduling algorithms

### Abstract

Kubernetes (k8s) has the potential to coordinate distributed edge resources and centralized cloud resources, but currently lacks a specialized scheduling framework for edge-cloud networks. Besides, the hierarchical distribution of heterogeneous resources makes the modeling and scheduling of k8s-oriented edge-cloud network particularly challenging. In this paper, we introduce KaiS, a learning-based scheduling framework for such edge-cloud network to improve the long-term throughput rate of request processing. First, we design a coordinated multiagent actor-critic algorithm to cater to decentralized request dispatch and dynamic dispatch spaces within the edge cluster. Second, for diverse system scales and structures, we use graph neural networks to embed system state information, and combine the embedding results with multiple policy networks to reduce the orchestration dimensionality by stepwise scheduling. Finally, we adopt a two-time-scale scheduling mechanism to harmonize request dispatch and service orchestration, and present the implementation design of deploying the above algorithms compatible with native k8s components. Experiments using real workload traces show that KaiS can successfully learn appropriate scheduling policies, irrespective of request arrival patterns and system scales. Moreover, KaiS can enhance the average system throughput rate by 15.9% while reducing scheduling cost by 38.4% compared to baselines.  © 1993-2012 IEEE.

## 04 — Title Screening

**Title:** Collaborative Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud Network

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Collaborative Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud Network
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Collaborative Learning-Based Scheduling for Kubernetes-Oriented Edge-Cloud Network
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
