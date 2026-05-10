---
id: paper-0895
title: Multi-Agent-Deep-Reinforcement-Learning-Enabled Offloading Scheme for Energy Minimization in Vehicle-to-Everything Communication Systems
authors:
- Duan, Wenwen
- Li, Xinmin
- Huang, Yi
- Cao, Hui
- Zhang, Xiaoqiang
venue: Electronics (Switzerland)
venue_type: journal
year: 2024
doi: 10.3390/electronics13030663
url: https://www.scopus.com/pages/publications/85184701191?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning
- mobile edge computing
- offloading
- transmit power
- vehicle-to-everything
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

# paper-0895 — Multi-Agent-Deep-Reinforcement-Learning-Enabled Offloading Scheme for Energy Minimization in Vehicle-to-Everything Communication Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Offloading computation-intensive tasks to mobile edge computing (MEC) servers, such as road-side units (RSUs) and a base station (BS), can enhance the computation capacities of the vehicle-to-everything (V2X) communication system. In this work, we study an MEC-assisted multi-vehicle V2X communication system in which multi-antenna RSUs with liner receivers and a multi-antenna BS with a zero-forcing (ZF) receiver work as MEC servers jointly to offload the tasks of the vehicles. To control the energy consumption and ensure the delay requirement of the V2X communication system, an energy consumption minimization problem under a delay constraint is formulated. The multi-agent deep reinforcement learning (MADRL) algorithm is proposed to solve the non-convex energy optimization problem, which can train vehicles to select the beneficial server association, transmit power and offloading ratio intelligently according to the reward function related to the delay and energy consumption. The improved K-nearest neighbors (KNN) algorithm is proposed to assign vehicles to the specific RSU, which can reduce the action space dimensions and the complexity of the MADRL algorithm. Numerical simulation results show that the proposed scheme can decrease energy consumption while satisfying the delay constraint. When the RSUs adopt the indirect transmission mode and are equipped with matched-filter (MF) receivers, the proposed joint optimization scheme can decrease the energy consumption by 56.90% and 65.52% compared to the maximum transmit power and full offloading schemes, respectively. When the RSUs are equipped with ZF receivers, the proposed scheme can decrease the energy consumption by 36.8% compared to the MF receivers. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0895.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
