---
id: paper-0377
title: Task-oriented Resource Allocation for Mobile Edge Computing with Multi-Agent Reinforcement Learning
authors:
- Zou, Yue
- Shen, Fei
- Yan, Feng
- Tang, Liang
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2021
doi: 10.1109/VTC2021-Fall52928.2021.9625217
url: https://www.scopus.com/pages/publications/85123017487?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Mobile edge computing
- multi-agent reinforcement learning
- resource allocation
- serial tasks
- task of-floading
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

# paper-0377 — Task-oriented Resource Allocation for Mobile Edge Computing with Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) enables terminals to migrate their tasks to edge servers instead of the central cloud for efficient execution. However, most researches on task offloading are limited to binary offloading for atomic tasks with a single edge server, while in practice, serial tasks of computation-intensive applications are more important. Therefore, we jointly study the task offloading and resource allocation for serial tasks in the multi-terminal multi-server scenario. A serial task is divided into multiple sub-tasks that are executed sequentially, leading to a better utilization of fragmented resources. The offloading mechanism of inter-coupled terminals is formulated as a noncooperative stochastic game, with evaluation indexes defined by the joint task priority, average task delay and energy consumption. Aiming at minimizing the long-term cost of the whole system, we adopt a multi-agent reinforcement learning (MARL) algorithm with dynamically adjusted offloading strategies, subchannels, transmit power, and allocated resources with only the partial state information. Simulation results demonstrate the feasibility of the proposed algorithm to solve the formulated problem in a distributed way. Compared with the other five benchmark algorithms, it has better system cost performance, and can schedule delay-sensitive tasks with higher priority earlier on the basis of a lower task failure rate.  © 2021 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0377.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
