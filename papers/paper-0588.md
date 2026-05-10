---
id: paper-0588
title: Dispatching and Scheduling Dependent Tasks Based on Multi-agent Deep Reinforcement Learning
authors:
- Feng, Shuaishuai
- Wu, Xi
- Zhao, Yongxin
- Li, Yongjian
venue: Proceedings of the International Conference on Software Engineering and Knowledge Engineering, SEKE
venue_type: conference
year: 2023
doi: 10.18293/SEKE2023-059
url: https://www.scopus.com/pages/publications/85170066842?origin=resultslist
publisher: Knowledge Systems Institute Graduate School
pages: 280--285
keywords:
- deep reinforcement learning
- dependent task
- edge computing
- multi-agent deep reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0588 — Dispatching and Scheduling Dependent Tasks Based on Multi-agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of edge computing, a large number of tasks can be offloaded to the edge server for computing, among which the dispatching and scheduling of dependent tasks has attracted extensive attention. The offloading of dependent tasks mainly has the following problems: how to select an appropriate edge server for dispatching, how to arrange the scheduling order of edge servers to better schedule tasks, and how to solve the task dependency problem. In this paper, we proposal a dispatching and scheduling method DAMD, based on reinforcement learning and multi-agent reinforcement learning, to solve the above three problems. Specifically, as the first step of DAMD, a reinforcement learning approach is designed to estimate the network load and dynamically dispatch tasks to the appropriate edge servers. Each edge server is regarded as an agent by a multi-agent reinforcement learning method, the second step of DAMD, which comprehensively considers the dependency relationship between tasks and the scheduling relationship between servers to achieve the efficiency and fairness of task scheduling. Finally, the results show that our method can better complete the task within the deadline and greatly reduce the average response time according to the time sensitivity requirement. © 2023 Knowledge Systems Institute Graduate School. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0588.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
