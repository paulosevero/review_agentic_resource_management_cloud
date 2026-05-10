---
id: paper-0689
title: A Delay-Optimal Task Scheduling Strategy for Vehicle Edge Computing Based on the Multi-Agent Deep Reinforcement Learning Approach
authors:
- Nie, Xuefang
- Yan, Yunhui
- Zhou, Tianqing
- Chen, Xingbang
- Zhang, Dingding
venue: Electronics (Switzerland)
venue_type: journal
year: 2023
doi: 10.3390/electronics12071655
url: https://www.scopus.com/pages/publications/85152925643?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- deep reinforcement learning
- Internet of Vehicles
- task scheduling
- vehicle edge computing
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

# paper-0689 — A Delay-Optimal Task Scheduling Strategy for Vehicle Edge Computing Based on the Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloudlet-based vehicular networks are a promising paradigm to enhance computation services through a distributed computation method, where the vehicle edge computing (VEC) cloudlet are deployed in the vicinity of the vehicle. In order to further improve the computing efficiency and reduce the task processing delay, we present a parallel task scheduling strategy based on the multi-agent deep reinforcement learning (DRL) approach for delay-optimal VEC in vehicular networks, where multiple computation tasks select the target threads in a VEC server to execute the computing tasks. We model the target thread decision of computation tasks as a multi-agent reinforcement learning problem, which is further solved by using a task scheduling algorithm based on multi-agent DRL that is implemented in a distributed manner. The computation tasks, with each selection acting on the target thread acting as an agent, collectively interact with the VEC environment and receive observations with respect to a common reward and learn to reduce the task processing delay by updating the multi-agent deep Q network (MADQN) using the obtained experiences. The experimental results show that the proposed DRL-based scheduling algorithm can achieve significant performance improvement, reducing the task processing delay by 40% and increasing the processing probability of success for computation tasks by more than 30% compared with the traditional task scheduling algorithms. © 2023 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0689.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
