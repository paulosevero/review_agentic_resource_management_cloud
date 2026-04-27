---
id: "paper-295"
title: "Tailored learning-based scheduling for kubernetes-oriented edge-cloud system"
authors: ["Han, Yiwen", "Shen, Shihao", "Wang, Xiaofei", "Wang, Shiqiang", "Leung, Victor C.M."]
year: 2021
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM42981.2021.9488701"
url: "https://www.scopus.com/pages/publications/85111926111?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Hierarchical systems", "Multi agent systems", "Scheduling", "Actor-critic algorithm", "Graph neural networks", "Heterogeneous resources", "Hierarchical distribution", "Implementation design", "Modeling and scheduling", "Scheduling frameworks", "Service orchestration", "Learning systems"]
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

# paper-295 — Tailored learning-based scheduling for kubernetes-oriented edge-cloud system

## Metadata

- **Authors:** Han, Yiwen and Shen, Shihao and Wang, Xiaofei and Wang, Shiqiang and Leung, Victor C.M.
- **Year:** 2021
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM42981.2021.9488701
- **URL:** https://www.scopus.com/pages/publications/85111926111?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Hierarchical systems; Multi agent systems; Scheduling; Actor-critic algorithm; Graph neural networks; Heterogeneous resources; Hierarchical distribution; Implementation design; Modeling and scheduling; Scheduling frameworks; Service orchestration; Learning systems

### Abstract

Kubernetes (k8s) has the potential to merge the distributed edge and the cloud but lacks a scheduling framework specifically for edge-cloud systems. Besides, the hierarchical distribution of heterogeneous resources and the complex dependencies among requests and resources make the modeling and scheduling of k8s-oriented edge-cloud systems particularly sophisticated. In this paper, we introduce KaiS, a learning-based scheduling framework for such edge-cloud systems to improve the long-term throughput rate of request processing. First, we design a coordinated multi-agent actor-critic algorithm to cater to decentralized request dispatch and dynamic dispatch spaces within the edge cluster. Second, for diverse system scales and structures, we use graph neural networks to embed system state information, and combine the embedding results with multiple policy networks to reduce the orchestration dimensionality by stepwise scheduling. Finally, we adopt a two-time-scale scheduling mechanism to harmonize request dispatch and service orchestration, and present the implementation design of deploying the above algorithms compatible with native k8s components. Experiments using real workload traces show that KaiS can successfully learn appropriate scheduling policies, irrespective of request arrival patterns and system scales. Moreover, KaiS can enhance the average system throughput rate by 14.3% while reducing scheduling cost by 34.7% compared to baselines. © 2021 IEEE.

## 04 — Title Screening

**Title:** Tailored learning-based scheduling for kubernetes-oriented edge-cloud system

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Tailored learning-based scheduling for kubernetes-oriented edge-cloud system
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Tailored learning-based scheduling for kubernetes-oriented edge-cloud system
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
