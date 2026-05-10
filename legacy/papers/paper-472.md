---
id: "paper-472"
title: "Data-aware Hierarchical Federated Learning via Task Offloading"
authors: ["Ma, Mulei", "Wu, Liantao", "Liu, Wenxiang", "Chen, Nanxi", "Shao, Ziyu", "Yang, Yang"]
year: 2022
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM48099.2022.10000924"
url: "https://www.scopus.com/pages/publications/85146932846?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3011--3016"
keywords: ["Deep Reinforcement Learning", "Hierarchical Federated Edge Learning", "Multi-Access Edge Computing", "Resource Allocation", "Task Offloading"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-472 — Data-aware Hierarchical Federated Learning via Task Offloading

## Metadata

- **Authors:** Ma, Mulei and Wu, Liantao and Liu, Wenxiang and Chen, Nanxi and Shao, Ziyu and Yang, Yang
- **Year:** 2022
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM48099.2022.10000924
- **URL:** https://www.scopus.com/pages/publications/85146932846?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3011--3016
- **Language:** English
- **Keywords:** Deep Reinforcement Learning; Hierarchical Federated Edge Learning; Multi-Access Edge Computing; Resource Allocation; Task Offloading

### Abstract

To cope with the high communication overhead caused by frequent aggregation of Federated Learning (FL) in Multi-access Edge Computing (MEC) scenarios, Hierarchical Federated Edge Learning (HFEL) is proposed as an evolving framework. HFEL offloads tasks to edge servers for partial model aggregation to reduce network traffic. However, most of the existing research focuses on resource optimization for HFEL without considering the impact of data characteristics and cannot guarantee the quality of FL training. To this end, we propose a task offloading approach based on data and resource heterogeneity under HFEL to improve training performance and reduce system cost. Specifically, we leverage information entropy to incorporate data statistical features into the cost function to reshape edge datasets. In addition, we applied Multi-Agent Deep Deterministic Policy Gradient (MADDPG) with a resource allocation module to generate distributed offloading policy more efficiently. Our algorithm not only adopts local observations to obtain the optimal action but also takes into account device heterogeneity, which can adapt to the unstable edge environment. Extensive experiments under multiple datasets and baselines are carried out, which demonstrate that our algorithm can effectively improve the accuracy of aggregated models while reducing system cost. © 2022 IEEE.

## 04 — Title Screening

**Title:** Data-aware Hierarchical Federated Learning via Task Offloading

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Data-aware Hierarchical Federated Learning via Task Offloading
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Data-aware Hierarchical Federated Learning via Task Offloading
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
