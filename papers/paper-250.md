---
id: "paper-250"
title: "Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach"
authors: ["Yang, Zhong", "Liu, Yuanwei", "Chen, Yue", "Al-Dhahir, Naofal"]
year: 2020
venue: "IEEE Transactions on Wireless Communications"
venue_type: "conference"
doi: "10.1109/TWC.2020.3006922"
url: "https://www.scopus.com/pages/publications/85092763769?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6899--6915"
keywords: ["Bayesian learning automata (BLA)", "mobile edge computing (MEC)", "multi-Agent Q-learning (MAQ-learning)", "non-orthogonal multiple access (NOMA)"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-250 — Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach

## Metadata

- **Authors:** Yang, Zhong and Liu, Yuanwei and Chen, Yue and Al-Dhahir, Naofal
- **Year:** 2020
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2020.3006922
- **URL:** https://www.scopus.com/pages/publications/85092763769?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6899--6915
- **Language:** English
- **Keywords:** Bayesian learning automata (BLA); mobile edge computing (MEC); multi-Agent Q-learning (MAQ-learning); non-orthogonal multiple access (NOMA)

### Abstract

A novel non-orthogonal multiple access (NOMA) based cache-Aided mobile edge computing (MEC) framework is proposed. For the purpose of efficiently allocating communication and computation resources to users' computation tasks requests, we propose a long-short-Term memory (LSTM) network to predict the task popularity. Based on the predicted task popularity, a long-Term reward maximization problem is formulated that involves a joint optimization of the task offloading decisions, computation resource allocation, and caching decisions. To tackle this challenging problem, a single-Agent Q-learning (SAQ-learning) algorithm is invoked to learn a long-Term resource allocation strategy. Furthermore, a Bayesian learning automata (BLA) based multi-Agent Q-learning (MAQ-learning) algorithm is proposed for task offloading decisions. More specifically, a BLA based action select scheme is proposed for the agents in MAQ-learning to select the optimal action in every state. We prove that the BLA based action selection scheme is instantaneously self-correcting and the selected action is an optimal solution for each state. Extensive simulation results demonstrate that: 1) The prediction error of the proposed LSTMs based task popularity prediction decreases with increasing learning rate. 2) The proposed framework significantly outperforms the benchmarks like all local computing, all offloading computing and non-cache computing. 3) The proposed BLA based MAQ-learning achieves an improved performance compared to conventional MAQ-learning algorithm. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach
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
