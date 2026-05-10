---
id: paper-2361
title: An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System
authors:
- Yang, Luyinru
- Zheng, Jun
- Zhang, Yuan
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3635005
url: https://www.scopus.com/pages/publications/105022819734?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- cooperative computation
- edge computing
- MARL
- task scheduling
- UAV
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2361 — An MARL-based Task Scheduling Algorithm for Cooperative Computation in a multi-UAV Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates the task scheduling problem for cooperative computation in a multi-UAV edge computing system. The problem is formulated as an integer nonlinear programming problem with an objective to maximize the average number of computation tasks successfully processed in each time slot. To solve the formulated problem using a reinforcement learning method, the problem is first reformulated as a decentralized partially observable Markov decision process (Dec-POMDP) and transformed into an average-reward maximization problem. Then, a multi-agent reinforcement learning (MARL)-based task scheduling algorithm (MTS) is proposed to solve the transformed problem. The proposed MTS algorithm introduces a QMIX-based training framework, in which the local policies of all agents are jointly trained by a central controller in a centralized manner and each agent executes actions independently according to its local observation and local policy in a decentralized manner. Moreover, recurrent neural networks (RNNs) are also introduced to deal with the partial observability of POMDP. Using the proposed MTS algorithm, each UAV is able to make optimal scheduling decisions independently to enable efficient cooperative computation between UAVs. Simulation results demonstrate that the proposed MTS algorithm can achieve better performance than benchmark algorithms in terms of the number of tasks successfully processed in the system. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2361.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
