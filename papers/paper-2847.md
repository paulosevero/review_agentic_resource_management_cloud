---
id: "paper-2847"
title: "Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters"
authors: ["Wu, Qingfu", "Chen, Pengfei", "Wang, Yilun"]
year: 2026
venue: "SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing"
venue_type: "conference"
doi: "10.1145/3772052.3772242"
url: "https://www.scopus.com/pages/publications/105028583037?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "402--415"
keywords: ["Deep Reinforcement Learning", "Fragmentation", "GPU Sharing", "Large Language Model"]
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

# paper-2847 — Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters

## Metadata

- **Authors:** Wu, Qingfu and Chen, Pengfei and Wang, Yilun
- **Year:** 2026
- **Venue:** SoCC 2025 - Proceedings of the 2025 ACM Symposium on Cloud Computing
- **DOI:** 10.1145/3772052.3772242
- **URL:** https://www.scopus.com/pages/publications/105028583037?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 402--415
- **Language:** English
- **Keywords:** Deep Reinforcement Learning; Fragmentation; GPU Sharing; Large Language Model

### Abstract

Modern GPU clusters in computing centers face significant challenges in resource utilization due to fragmentation caused by GPU-sharing mechanisms, job diversity and asynchronous job lifecycles. Existing methods fail to address GPU fragmentation in dynamic scheduling scenarios under GPU sharing. To tackle this issue, this paper proposes DRR, a defragmentation scheduler with deep reinforcement learning (DRL) and rescheduling to mitigate GPU fragmentation. DRR employs a DRL agent trained via imitation learning from heuristic algorithms to overcome cold-start issues, and further enhanced by multi-scale policy optimization for balanced exploration and exploitation to reduce GPU fragmentation. Additionally, the rescheduling strategy in DRR further optimizes GPU utilization by relocating the running jobs. Evaluations conducted on the physical Kubernetes-based testbed and large-scale simulated clusters demonstrate that DRR reduces the average GPU fragmentation rate by 50% compared to state-of-the-art methods, while maintaining Quality of Service (QoS) and ensuring fairness for users.  © 2025 Copyright is held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Defragmentation Scheduling with Deep Reinforcement Learning in Shared GPU Clusters
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
