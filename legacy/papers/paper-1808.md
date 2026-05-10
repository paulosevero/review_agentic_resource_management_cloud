---
id: "paper-1808"
title: "Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks"
authors: ["Li, Yangchen", "Zhao, Lingzhi", "Wang, Tianle", "Ding, Lianghui", "Yang, Feng"]
year: 2025
venue: "IEEE Transactions on Machine Learning in Communications and Networking"
venue_type: "journal"
doi: "10.1109/TMLCN.2025.3534754"
url: "https://www.scopus.com/pages/publications/105027882275?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers"
pages: "332--352"
keywords: ["algorithm parameter configuration", "deep reinforcement learning", "edge computing", "Federated learning", "multi-agent reinforcement learning", "worker selection"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1808 — Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks

## Metadata

- **Authors:** Li, Yangchen and Zhao, Lingzhi and Wang, Tianle and Ding, Lianghui and Yang, Feng
- **Year:** 2025
- **Venue:** IEEE Transactions on Machine Learning in Communications and Networking
- **DOI:** 10.1109/TMLCN.2025.3534754
- **URL:** https://www.scopus.com/pages/publications/105027882275?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers
- **Pages:** 332--352
- **Language:** English
- **Keywords:** algorithm parameter configuration; deep reinforcement learning; edge computing; Federated learning; multi-agent reinforcement learning; worker selection

### Abstract

In this paper, we investigate federated learning (FL) efficiency improvement in practical edge computing systems, where edge workers have non-independent and identically distributed (non-IID) local data, as well as dynamic and heterogeneous computing and communication capabilities. We consider a general FL algorithm with configurable parameters, including the number of local iterations, mini-batch sizes, step sizes, aggregation weights, and quantization parameters, and provide a rigorous convergence analysis. We formulate a joint optimization problem for FL worker selection and algorithm parameter configuration to minimize the final test loss subject to time and energy constraints. The resulting problem is a complicated stochastic sequential decision-making problem with an implicit objective function and unknown transition probabilities. To address these challenges, we propose knowledge/model-driven single-agent and multi-agent deep reinforcement learning (DRL) frameworks. We transform the primal problem into a Markov decision process (MDP) for the single-agent DRL framework and a decentralized partially-observable Markov decision process (Dec-POMDP) for the multi-agent DRL framework. We develop efficient single-agent and multi-agent asynchronous advantage actor-critic (A3C) approaches to solve the MDP and Dec-POMDP, respectively. In both frameworks, we design a knowledge-based reward to facilitate effective DRL and propose a model-based stochastic policy to tackle the mixed discrete-continuous actions and large action spaces. To reduce the computational complexities of policy learning and execution, we introduce a segmented actor-critic architecture for the single-agent DRL and a distributed actor-critic architecture for the multi-agent DRL. Numerical results demonstrate the effectiveness and advantages of the proposed frameworks in enhancing FL efficiency.  © 2025 CCBY.

## 04 — Title Screening

**Title:** Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Knowledge- and Model-Driven Deep Reinforcement Learning for Efficient Federated Edge Learning: Single- and Multi-Agent Frameworks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
