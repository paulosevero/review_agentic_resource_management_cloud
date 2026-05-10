---
id: paper-0701
title: Multi-Agent Deep Reinforcement Learning Offloading Algorithm Based on Resource Reservation and Task Adjustment
authors:
- Qu, Hua
- Gao, Qian
- Zhao, Jihong
- Xue, Yucheng
venue: 2023 4th International Conference on Computer Engineering and Application, ICCEA 2023
venue_type: conference
year: 2023
doi: 10.1109/ICCEA58433.2023.10135410
url: https://www.scopus.com/pages/publications/85162705964?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 417--424
keywords:
- Computing offloading
- Deep reinforcement learning
- Edge computing
- long-term and short-term memory network
- Multi-agent reinforcement learning
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

# paper-0701 — Multi-Agent Deep Reinforcement Learning Offloading Algorithm Based on Resource Reservation and Task Adjustment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the popularization of the Internet of Things and mobile Internet, the data shows explosive growth. Adopting cloud computing mode will lead to network congestion and high energy consumption, and can't meet the low latency requirements of applications. Computing offloading technology offloads tasks to the edge of the network for processing, which can effectively make up for the shortcomings of the cloud computing model. However, in the multi-user and multi-server edge system, it is challenging to formulate the task offloading strategy. In this paper, we consider divisible and latency sensitive tasks and edge server load dynamics. Then we model the edge computing scenario, and formulates a task offloading problem to minimize the overall task processing latency while meeting the application latency requirements. We propose a resource reservation strategy to expand the candidate destination nodes for task offloading and propose task adjustment strategy to adjust the resource allocation of elastic tasks which can improve the task carrying capacity of MEC system and then improve the average quality of experience. We use a multi-agent deep reinforcement learning method to solve optimization problems. The simulation results show that our method can significantly reduce the application latency rate and improve the average quality of experience and resource utilization of MEC system.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0701.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
