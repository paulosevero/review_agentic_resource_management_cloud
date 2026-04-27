---
id: "paper-2817"
title: "Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence"
authors: ["Wang, Peng", "Huang, Long", "Sun, Wen", "Yang, Yi", "Niyato, Dusit", "Wu, Dapeng Oliver"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3675369"
url: "https://www.scopus.com/pages/publications/105033388354?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge intelligence", "energy efficiency", "inference offloading", "multi-agent reinforcement learning"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2817 — Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence

## Metadata

- **Authors:** Wang, Peng and Huang, Long and Sun, Wen and Yang, Yi and Niyato, Dusit and Wu, Dapeng Oliver
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3675369
- **URL:** https://www.scopus.com/pages/publications/105033388354?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge intelligence; energy efficiency; inference offloading; multi-agent reinforcement learning

### Abstract

Edge intelligence deploys artificial intelligence models on edge nodes proximal to data sources, and delivers real-time inference support for resource-constrained devices. To realize this vision, inference offloading differs from conventional computation offloading by tailoring offloading strategies to the intrinsic characteristics of AI inference tasks. In this field, existing researchs generally lack fine-grained model partitioning capabilities and long-term resource adaptability, failing to optimize resource utilization and sustain stable performance in mobile environments. To address these issues, we propose an adaptive inference acceleration framework that dynamically partitions inference models into hierarchical subtasks and offloads these subtasks to heterogeneous edge servers. We formulate a joint optimization problem for task partitioning, offloading and resource allocation, which takes queue stability as the constraint and aims to minimize the long-term average task completion time. To realize the optimal trade-off between latency and stability without future state prediction, we adopt Lyapunov optimization to decompose the long-term stochastic optimization into slot-by-slot solvable deterministic subproblems. For these slot-by-slot subproblems, we design a Q-network Mixing (QMIX)-based multi-agent reinforcement learning method to enable collaborative strategy selection across edge servers. Experimental simulations show that, compared with baseline algorithms including the greedy, genetic and MAD2RL methods, our proposed framework achieves a substantial reduction in task completion time while preserving inference accuracy and queue stability. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Inference Acceleration With Fine-Grained Model Partitioning for Mobile Edge Intelligence
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
