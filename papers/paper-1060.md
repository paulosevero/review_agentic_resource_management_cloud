---
id: paper-1060
title: 'Multidimensional Resource Management for Distributed MEC Networks in Jamming Environment: A Hierarchical DRL Approach'
authors:
- Liu, Songyi
- Xu, Yuhua
- Li, Guoxin
- Xu, Yifan
- Zhang, Xiaokai
- Gu, Fanglin
- Ma, Wenfeng
- Chen, Taoyi
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3366009
url: https://www.scopus.com/pages/publications/85187242480?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16859--16872
keywords:
- Actor-critic (AC) model
- anti-jamming communication
- Markov decision process (MDP)
- multiagent reinforcement learning (MARL)
- multidimensional resource management
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

# paper-1060 — Multidimensional Resource Management for Distributed MEC Networks in Jamming Environment: A Hierarchical DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article investigates the problem of multidimensional resource management in multiaccess mobile edge computing (MEC) networks against external dynamic jamming. The objective is to minimize the long-term computational cost of the MEC network while satisfying the task computation delay requirements of user equipment (UE) by jointly optimizing computing and communication resource allocation. To overcome challenges, such as frequency conflict and dynamic jamming attacks, a distributed multiagent hierarchical deep reinforcement learning (MAHDRL) MEC framework based on hybrid heterogeneous decision making is proposed. Specifically, a hierarchical MEC anti-jamming data offloading optimization model is constructed, and the MEC resource management problem is formulated as a decentralized partially observable Markov decision process (Dec-POMDP). Based on this, a distributed MAHDRL algorithm based on the actor-critic (AC) model is designed to solve the multiagent high-dimensional nonlinear hybrid integer programming NP-hard problem: the high-level network in the base station (BS) optimizes discrete channel access strategies, while the low-level network in UEs learns data offloading strategies. Additionally, the computational complexity is discussed and a theoretical proof of the algorithm convergence is presented. Simulation results demonstrate the superiority of the proposed algorithm, which reduces energy consumption and data processing delay across the network. © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1060.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
