---
id: "paper-651"
title: "Task Placement and Resource Allocation for Edge Machine Learning: A GNN-Based Multi-Agent Reinforcement Learning Paradigm"
authors: ["Li, Yihong", "Zhang, Xiaoxi", "Zeng, Tianyu", "Duan, Jingpu", "Wu, Chuan", "Wu, Di", "Chen, Xu"]
year: 2023
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2023.3313779"
url: "https://www.scopus.com/pages/publications/85171554225?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3073--3089"
keywords: ["Edge machine learning", "graph neural networks", "multi-agent reinforcement learning", "resource allocation", "task placement"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-651 — Task Placement and Resource Allocation for Edge Machine Learning: A GNN-Based Multi-Agent Reinforcement Learning Paradigm

## Metadata

- **Authors:** Li, Yihong and Zhang, Xiaoxi and Zeng, Tianyu and Duan, Jingpu and Wu, Chuan and Wu, Di and Chen, Xu
- **Year:** 2023
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2023.3313779
- **URL:** https://www.scopus.com/pages/publications/85171554225?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3073--3089
- **Language:** English
- **Keywords:** Edge machine learning; graph neural networks; multi-agent reinforcement learning; resource allocation; task placement

### Abstract

Machine learning (ML) tasks are one of the major workloads in today's edge computing networks. Existing edge-cloud schedulers allocate the requested amounts of resources to each task, falling short of best utilizing the limited edge resources for ML tasks. This paper proposes TapFinger, a distributed scheduler for edge clusters that minimizes the total completion time of ML tasks through co-optimizing task placement and fine-grained multi-resource allocation. To learn the tasks' uncertain resource sensitivity and enable distributed scheduling, we adopt multi-agent reinforcement learning (MARL) and propose several techniques to make it efficient, including a heterogeneous graph attention network as the MARL backbone, a tailored task selection phase in the actor network, and the integration of Bayes' theorem and masking schemes. We first implement a single-task scheduling version, which schedules at most one task each time. Then we generalize to the multi-task scheduling case, in which a sequence of tasks is scheduled simultaneously. Our design can mitigate the expanded decision space and yield fast convergence to optimal scheduling solutions. Extensive experiments using synthetic and test-bed ML task traces show that TapFinger can achieve up to 54.9% reduction in the average task completion time and improve resource efficiency as compared to state-of-the-art schedulers. © 1990-2012 IEEE.

## 04 — Title Screening

**Title:** Task Placement and Resource Allocation for Edge Machine Learning: A GNN-Based Multi-Agent Reinforcement Learning Paradigm

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Task Placement and Resource Allocation for Edge Machine Learning: A GNN-Based Multi-Agent Reinforcement Learning Paradigm
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Task Placement and Resource Allocation for Edge Machine Learning: A GNN-Based Multi-Agent Reinforcement Learning Paradigm
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
