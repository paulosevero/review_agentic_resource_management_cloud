---
id: paper-0664
title: MADDPG-based joint optimization of task partitioning and computation resource allocation in mobile edge computing
authors:
- Lu, Kun
- Li, Rong-Da
- Li, Ming-Chu
- Xu, Guo-Rui
venue: Neural Computing and Applications
venue_type: journal
year: 2023
doi: 10.1007/s00521-023-08527-8
url: https://www.scopus.com/pages/publications/85153374787?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 16559--16576
keywords:
- Computation offloading
- Deep reinforcement learning
- Mobile edge computing
- Resource allocation
- Task partitioning
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

# paper-0664 — MADDPG-based joint optimization of task partitioning and computation resource allocation in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The continual development of mobile edge computing efficiently solves the problem that mobile devices are unable to handle computation-intensive tasks due to their computation capacity and battery restrictions. In this paper, we consider mobile awareness and dynamic battery charging in a multi-user and multi-server mobile edge computing system, where various tasks are generated successively on the user devices. Servers act as learning agents and collaborate with user devices to develop task partitioning and computation resource allocation strategies. With the purpose of decreasing task failure rate and improving system utility in the long term, which is closely related to latency, energy consumption, and server cost, optimal strategies are demanded by the system. We model the joint optimization problem as a multi-agent Markov decision process game. And a deep reinforcement learning method based on the multi-agent deep deterministic policy gradient algorithm is proposed, which employs neural networks and works in a centralized training and decentralized execution manner to optimize the strategies. Finally, simulation results demonstrate the effectiveness of our proposed algorithm in terms of reducing task failure rate and improving system utility. © 2023, The Author(s), under exclusive licence to Springer-Verlag London Ltd., part of Springer Nature.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0664.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
