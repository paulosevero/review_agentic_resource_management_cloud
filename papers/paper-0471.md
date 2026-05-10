---
id: paper-0471
title: 'Coordinated Load Balancing in Mobile Edge Computing Network: a Multi-Agent DRL Approach'
authors:
- Ma, Manyou
- Wu, Di
- Xu, Yi Tian
- Li, Jimmy
- Jang, Seowoo
- Liu, Xue
- Dudek, Gregory
venue: IEEE International Conference on Communications
venue_type: conference
year: 2022
doi: 10.1109/ICC45855.2022.9838615
url: https://www.scopus.com/pages/publications/85137274967?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 619--624
keywords:
- Deep learning
- Mobile telecommunication systems
- Multi agent systems
- Reinforcement learning
- Edge nodes
- Handover decision
- Load-Balancing
- Mobility load balancing
- Multi agent
- Optimal networks
- Physical separation
- Reinforcement learnings
- Resource-efficient
- Resources utilizations
- Mobile edge computing
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-0471 — Coordinated Load Balancing in Mobile Edge Computing Network: a Multi-Agent DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) networks have been recently adopted to accommodate the fast-growing number of mobile devices performing complicated tasks with limited hardware capability. Recently, edge nodes with communication, computation, and caching capacities are starting to be deployed in MEC networks. Due to the physical separation of these resources, efficient coordination and scheduling are important for efficient resource utilization and optimal network performance. In this paper, we study mobility load balancing for communication, computation, and caching-enabled heterogeneous MEC networks. Specifically, we propose to tackle this problem via a multi-agent deep reinforcement learning-based framework. Users served by overloaded edge nodes are handed over to less loaded ones, to minimize the load in the most loaded base station in the network. In this framework, the handover decision for each user is made based on the user's own observation which comprises the user's task at hand and the load status of the MEC network. Simulation results show that our proposed multi-agent deep reinforcement learning-based approach can reduce the time-average maximum load by up to 30% and the end-to-end delay by 50% compared to baseline algorithms. © 2022 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0471.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
