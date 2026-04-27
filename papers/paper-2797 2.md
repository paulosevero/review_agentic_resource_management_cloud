---
id: "paper-2797"
title: "QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads"
authors: ["Tao, Xi", "Lu, Dongji", "Cao, Weipeng", "Gu, Jiongjiong", "Cai, Zhiyuan", "Xu, Chuanfei", "Zhang, Liang-Jie", "Ming, Zhong"]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2026.3676714"
url: "https://www.scopus.com/pages/publications/105034077540?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["cloud workload", "CPU pinning", "Deep reinforcement learning", "quality of service"]
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

# paper-2797 — QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads

## Metadata

- **Authors:** Tao, Xi and Lu, Dongji and Cao, Weipeng and Gu, Jiongjiong and Cai, Zhiyuan and Xu, Chuanfei and Zhang, Liang-Jie and Ming, Zhong
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2026.3676714
- **URL:** https://www.scopus.com/pages/publications/105034077540?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** cloud workload; CPU pinning; Deep reinforcement learning; quality of service

### Abstract

In cloud computing, static resource configurations create a trade-off: tenants overprovision to avoid resource starvation, causing inefficiency and cost, while providers suffer low utilization despite high allocations. To improve efficiency, providers often use overcommitted environments where multiple workloads share hosts, but this leads to interference and potential Quality-of-Service (QoS) violations. This paper introduces a realtime dynamic control framework that mitigates interference by adaptively pinning workloads to CPU groups. Using deep reinforcement learning (DRL) with the Proximal Policy Optimization (PPO) algorithm, an intelligent agent continuously adjusts CPU pinning based on real-time feedback to maintain Service- Level-Agreement (SLA) compliance. Experiments under two optimization objectives—overall-performance-first and priorityperformance- first—show that the proposed approach improves overall QoS by ≈25% compared with static pinning. When prioritization is enabled, high-priority workloads gain significant performance improvements while lower-priority ones remain within SLA limits. These results demonstrate that a DRL-based CPU-pinning strategy effectively manages resource contention in overcommitted clouds, enhancing utilization while upholding tenant SLAs. © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads
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
