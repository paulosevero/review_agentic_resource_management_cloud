---
id: paper-0250
title: 'Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach'
authors:
- Yang, Zhong
- Liu, Yuanwei
- Chen, Yue
- Al-Dhahir, Naofal
venue: IEEE Transactions on Wireless Communications
venue_type: conference
year: 2020
doi: 10.1109/TWC.2020.3006922
url: https://www.scopus.com/pages/publications/85092763769?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 6899--6915
keywords:
- Bayesian learning automata (BLA)
- mobile edge computing (MEC)
- multi-Agent Q-learning (MAQ-learning)
- non-orthogonal multiple access (NOMA)
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-0250 — Cache-Aided NOMA Mobile Edge Computing: A Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A novel non-orthogonal multiple access (NOMA) based cache-Aided mobile edge computing (MEC) framework is proposed. For the purpose of efficiently allocating communication and computation resources to users' computation tasks requests, we propose a long-short-Term memory (LSTM) network to predict the task popularity. Based on the predicted task popularity, a long-Term reward maximization problem is formulated that involves a joint optimization of the task offloading decisions, computation resource allocation, and caching decisions. To tackle this challenging problem, a single-Agent Q-learning (SAQ-learning) algorithm is invoked to learn a long-Term resource allocation strategy. Furthermore, a Bayesian learning automata (BLA) based multi-Agent Q-learning (MAQ-learning) algorithm is proposed for task offloading decisions. More specifically, a BLA based action select scheme is proposed for the agents in MAQ-learning to select the optimal action in every state. We prove that the BLA based action selection scheme is instantaneously self-correcting and the selected action is an optimal solution for each state. Extensive simulation results demonstrate that: 1) The prediction error of the proposed LSTMs based task popularity prediction decreases with increasing learning rate. 2) The proposed framework significantly outperforms the benchmarks like all local computing, all offloading computing and non-cache computing. 3) The proposed BLA based MAQ-learning achieves an improved performance compared to conventional MAQ-learning algorithm. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0250.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
