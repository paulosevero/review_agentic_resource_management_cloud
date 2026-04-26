---
id: "paper-1912"
title: "Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint"
authors: ["Lu, Xiaoli", "Guo, Gaizhi", "Yu, Zongzuo", "Zhang, Pengjv"]
year: 2025
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-96-9901-8_39"
url: "https://www.scopus.com/pages/publications/105012244851?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "472--483"
keywords: ["Entropy Constraint", "Mobile Edge Computing", "Multi-head Self-attention", "Multi-objective Reinforcement Learning"]
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

# paper-1912 — Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint

## Metadata

- **Authors:** Lu, Xiaoli and Guo, Gaizhi and Yu, Zongzuo and Zhang, Pengjv
- **Year:** 2025
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-96-9901-8_39
- **URL:** https://www.scopus.com/pages/publications/105012244851?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 472--483
- **Language:** English
- **Keywords:** Entropy Constraint; Mobile Edge Computing; Multi-head Self-attention; Multi-objective Reinforcement Learning

### Abstract

In the task offloading scenario of edge computing, user devices commonly suffer from resource constraints. It is difficult for traditional task offloading mechanisms to make efficient decisions when facing complex environments such as dynamically changing network resources and parallel scheduling of multiple tasks. Reinforcement learning methods face the problem of balance between exploration and exploitation in practical applications. To this end, we propose a multi-objective reinforcement learning mechanism based on SAE-PPO, which is an improvement of the traditional Proximal Policy Optimization (PPO) algorithm to achieve efficient task offloading. First, for the dynamics of network resources and the demand of multi-task scheduling, we design an Actor-Critic network model incorporating a multi-head self-attention (MHSA) mechanism. It can capture the complex association between task features and resource distribution, and thus optimize the matching strategy between tasks and resources. Second, to address the balance between exploration and exploitation, we construct an intelligent exploration strategy with entropy constraint by introducing an entropy regularization in the objective function. The strategy prevents premature convergence to a local optimum and adapts to different load and network conditions. Experimental results show that the proposed method outperforms the UCB1, SPEA/R, and NSGA-III algorithms in latency and energy consumption, achieving a 70% reduction in latency and a 46% reduction in energy consumption in complex MEC environments. This paper provides an effective solution for resource scheduling in complex edge environments. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

## 04 — Title Screening

**Title:** Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Objective Reinforcement Learning for Edge Task Offloading with Multi-Head Self-Attention and Entropy Constraint
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
