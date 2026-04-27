---
id: "paper-650"
title: "TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning"
authors: ["Li, Yihong", "Zeng, Tianyu", "Zhang, Xiaoxi", "Duan, Jingpu", "Wu, Chuan"]
year: 2023
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM53939.2023.10229031"
url: "https://www.scopus.com/pages/publications/85148467042?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Computation theory", "Fertilizers", "Multi agent systems", "Reinforcement learning", "Edge clouds", "Edge computing", "Edge resources", "Fine grained", "Learning tasks", "Machine-learning", "Multi-agent reinforcement learning", "Performance optimizations", "Resources allocation", "Task performance", "Resource allocation"]
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

# paper-650 — TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning

## Metadata

- **Authors:** Li, Yihong and Zeng, Tianyu and Zhang, Xiaoxi and Duan, Jingpu and Wu, Chuan
- **Year:** 2023
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM53939.2023.10229031
- **URL:** https://www.scopus.com/pages/publications/85148467042?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Computation theory; Fertilizers; Multi agent systems; Reinforcement learning; Edge clouds; Edge computing; Edge resources; Fine grained; Learning tasks; Machine-learning; Multi-agent reinforcement learning; Performance optimizations; Resources allocation; Task performance; Resource allocation

### Abstract

Machine learning (ML) tasks are one of the major workloads in today's edge computing networks. Existing edge-cloud schedulers allocate the requested amounts of resources to each task, falling short of best utilizing the limited edge resources flexibly for ML task performance optimization. This paper proposes TapFinger, a distributed scheduler that minimizes the total completion time of ML tasks in a multi-cluster edge network, through co-optimizing task placement and fine-grained multi-resource allocation. To learn the tasks' uncertain resource sensitivity and enable distributed online scheduling, we adopt multi-agent reinforcement learning (MARL), and propose several techniques to make it efficient for our ML-task resource allocation. First, TapFinger uses a heterogeneous graph attention network as the MARL backbone to abstract inter-related state features into more learnable environmental patterns. Second, the actor network is augmented through a tailored task selection phase, which decomposes the actions and encodes the optimization constraints. Third, to mitigate decision conflicts among agents, we novelly combine Bayes' theorem and masking schemes to facilitate our MARL model training. Extensive experiments using synthetic and test-bed ML task traces show that TapFinger can achieve up to 28.6% reduction in the average task completion time and improve resource efficiency as compared to state-of-the- art resource schedulers. © 2023 IEEE.

## 04 — Title Screening

**Title:** TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** TapFinger: Task Placement and Fine-Grained Resource Allocation for Edge Machine Learning
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
