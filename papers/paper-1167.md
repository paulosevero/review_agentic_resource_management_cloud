---
id: paper-1167
title: Multi-agent Task Assignment in Unmanned Aerial Vehicle Edge Computing based on Deep Learning Approach
authors:
- Samuel, Amalorpava Mary Rajee
- Yamuna Devi, M.M.
- Madhusudhanan, S.
venue: 3rd International Conference on Automation, Computing and Renewable Systems, ICACRS 2024 - Proceedings
venue_type: conference
year: 2024
doi: 10.1109/ICACRS62842.2024.10841480
url: https://www.scopus.com/pages/publications/85217373519?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 173--178
keywords:
- DRL
- Lyapunov Optimization
- Task assignment
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: DL
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

# paper-1167 — Multi-agent Task Assignment in Unmanned Aerial Vehicle Edge Computing based on Deep Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) are used as supportive edge computing for sparsely located user equipment on a large scale. In this work, we propose and address a collaborative edge computing system involving multiple UAVs as agents in deep reinforcement learning (DRL) approach due to the restricted computation and energy capabilities of UAVs. The challenge of task offloading is being tackled to reduce the total delays in execution and energy usage by simultaneously planning the paths, assigning computation tasks, and managing communication resources of UAVs. Additionally, Lyapunov optimization is incorporated for the system stability of mobile edge computing assisted by multiple UAVs. Exploring a multi-agent deep reinforcement learning framework to achieve a combined strategy to manage task allocation, and power management. The sum rate results of the evaluation show that our method for task offloading using multi-UAV and multi-EC achieves superior performance with 25 % increase when compared to other optimization methods and ability to reduce cost and delay. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "DL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1167.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
