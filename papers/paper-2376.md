---
id: paper-2376
title: Multi-Agent Reinforcement Learning for Task Offloading in Crowd-Edge Computing
authors:
- Yao, Su
- Wang, Mu
- Ren, Ju
- Xia, Tianyu
- Wang, Weiqiang
- Xu, Ke
- Xu, Mingwei
- Zhang, Hongke
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3531793
url: https://www.scopus.com/pages/publications/85216222772?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9289--9302
keywords:
- distributed optimization
- edge computing
- multi-agent reinforcement learning
- Task offloading
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

# paper-2376 — Multi-Agent Reinforcement Learning for Task Offloading in Crowd-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Crowd-edge (CE) computing paradigm facilitates the utilization of the computational resources through simultaneously relying the edge computing and the collaboration among various mobile devices (MDs). Most existing works, focusing on offloading tasks from device to edge servers by centralized solutions, are unable to distribute tasks to massive MDs in CE. Meanwhile, designing a decentralized task offloading solution enabling task subscribers to individually make offloading decisions can be challenging given the randomness of crowd resource provisioning and limited knowledge of global status variations. In this paper, we propose a decentralized crowd-edge task offloading solution that enables users to optimally offload tasks to the CE in a distributed manner. Specifically, we formulate the corresponding problem as a stochastic optimization with partially observable status. By observing network and process delays at the crowd side, we further reform the optimization forms and provide a novel approximation policy, enabling users to optimize their offloading strategy based on local observations without interaction with each other. We then solve this task offloading problem by developing a Mixed Multi-Agent Proxy Policy Optimization algorithm (mixed MAPPO). Extensive testing, including numerical and system-level simulations, was conducted to validate the performance of the proposed algorithm in terms of task delay (including the processing delay and transmission delay), load rate, and resource utilization. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2376.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
