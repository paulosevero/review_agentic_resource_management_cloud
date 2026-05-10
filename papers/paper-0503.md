---
id: paper-0503
title: A Load-Balanced and Energy-Efficient Navigation Scheme for UAV-Mounted Mobile Edge Computing
authors:
- Wang, Zhenqian
- Rong, Huigui
- Jiang, Hongbo
- Xiao, Zhu
- Zeng, Fanzi
venue: IEEE Transactions on Network Science and Engineering
venue_type: journal
year: 2022
doi: 10.1109/TNSE.2022.3188670
url: https://www.scopus.com/pages/publications/85134214573?origin=resultslist
publisher: IEEE Computer Society
pages: 3659--3674
keywords:
- deep reinforcement learning
- Mobile edge computing
- path planning
- task offloading
- unmanned aerial vehicles
- user equipments
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0503 — A Load-Balanced and Energy-Efficient Navigation Scheme for UAV-Mounted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of Unmanned Aerial Vehicles (UAVs) in recent years, UAV-mounted Mobile Edge Computing (MEC) systems are widely used for broadband connectivity and emergency communications in areas without internet. However, the onboard energy of UAVs is limited, and how to provide long-term computing services for ground User Equipments (UEs) still faces significant challenges. In this paper, UAVs are used as mobile base stations to offer MEC services for UEs. Unlike existing solutions that mainly solve UAV path planning from convex optimization methods, we propose a Multi-Agent Path planning (MAP) scheme based on deep reinforcement learning. We aim to minimize the total energy consumption of UAVs while completing the offloading tasks of UEs. At the same time, fairness is taken into account to ensure UE offloading balance and UAV load balance. To this end, we establish the optimization problem and design the state space, action space, and reward function for modeling each UAV through Deep Neural Networks (DNNs). Extensive simulation experiments show that the proposed scheme outperforms other benchmark schemes. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0503.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
