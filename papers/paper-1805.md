---
id: paper-1805
title: Intelligent Offloading and Driving Strategy for Delay Minimization and Collision Avoidance in V2X Network
authors:
- Li, Xinmin
- Yan, Chenwen
- Duan, Wenwen
- Wang, Xiaobo
venue: 2025 IEEE/CIC International Conference on Communications in China, ICCC Workshops 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCCWorkshops67136.2025.11147218
url: https://www.scopus.com/pages/publications/105017784987?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- mobile edge computing
- system delay
- vehicle-to-everything
- vehicles collision
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1805 — Intelligent Offloading and Driving Strategy for Delay Minimization and Collision Avoidance in V2X Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The task processing delay and road safety were the key challenges of vehicle-to-everything (V2X) network in sixth generation (6G) system. By offloading delay-intensive task of the vehicles to road side unit (RSU) and base station (BS), mobile edge computing (MEC) technology can reduce the processing delay of V2X network. However, it was difficult to dynamically associate between vehicles and MEC servers and offload the task for the moving vehicles, especially the low collision scenario. Thus, we considered the MEC-assisted multi-vehicle V2X system, where the vehicles can offload delay-intensive task to the multi-antenna RSUs and BS with the zero-forcing (ZF) receivers, and formulate the system delay minimization problem under the delay and collision constraints to satisfy the task processing delay and safety requirements in the V2X system. The multi-agent deep reinforcement learning (MADRL) algorithm was proposed to handle the non-convex problem by optimizing the offloading and driving strategy of vehicles. In this work, the reward function was designed bases on the task processing delay and vehicle collision, thus, the proposed MADRL algorithm can train vehicles to obtain the superior MEC server association, offloading ratio, and driving acceleration. Simulation results demonstrate that the system delay of the proposed MADRL algorithm can reduce by 16.78% and 4.55% compared to the Q-learning and full offloading schemes, respectively. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1805.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
