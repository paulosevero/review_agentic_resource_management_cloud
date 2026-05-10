---
id: paper-0924
title: Combinatorial Client-Master Multiagent Deep Reinforcement Learning for Task Offloading in Mobile Edge Computing
authors:
- Gebrekidan, Tesfay Zemuy
- Stein, Sebastian
- Norman, Timothy J.
venue: Proceedings of the International Joint Conference on Autonomous Agents and Multiagent Systems, AAMAS
venue_type: conference
year: 2024
doi: ''
url: https://www.scopus.com/pages/publications/85186350595?origin=resultslist
publisher: International Foundation for Autonomous Agents and Multiagent Systems (IFAAMAS)
pages: 2273--2275
keywords:
- Client-Master Multiagent Deep Reinforcement Learning
- Combinatorial Action Selection
- Distributed Solution
- Mixed Constraints
- Multiagent Deep Reinforcement Learning
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

# paper-0924 — Combinatorial Client-Master Multiagent Deep Reinforcement Learning for Task Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Deep reinforcement learning (DRL) is gaining popularity in task-offloading problems because it can adapt to dynamic changes and minimize online computational complexity. However, the various types of continuous and discrete resource constraints on user devices (UDs) and mobile edge computing (MEC) servers pose challenges to the design of an efficient DRL-based task-offloading strategy. Existing DRL-based task-offloading algorithms focus on the constraints of the UDs, assuming the availability of enough storage resources on the server. Moreover, existing multiagent DRL (MADRL)-based task-offloading algorithms are homogeneous agents and consider homogeneous constraints as a penalty in their reward function. In this work, we propose a novel combinatorial client-master MADRL (CCM_MADRL) algorithm for task offloading in mobile edge computing (CCM_MADRL_MEC) that allows UDs to decide their resource requirements and the server to make a combinatorial decision based on the UDs' requirements. CCM_MADRL_MEC is the first MADRL approach in task offloading to consider server storage capacity in addition to the constraints of the UDs. By taking advantage of the combinatorial action selection, CCM_MADRL_MEC has shown superior convergence over existing benchmark and heuristic algorithms. © 2024 International Foundation for Autonomous Agents and Multiagent Systems.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0924.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
