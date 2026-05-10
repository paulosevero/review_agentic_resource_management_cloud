---
id: paper-0774
title: Trajectory and Offloading Policy Optimization in Age-of-Information-Aware UAV-Assisted MEC Systems
authors:
- Yang, Yulu
- Yang, Jingce
- Xu, Han
- Hu, Jing
- Song, Tiecheng
venue: Proceedings - 2023 International Conference on Networking and Network Applications, NaNA 2023
venue_type: conference
year: 2023
doi: 10.1109/NaNA60121.2023.00037
url: https://www.scopus.com/pages/publications/85176800432?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 175--180
keywords:
- Age of Information (AoI)
- Mobile Edge Computing (MEC)
- Multi-Agent Deep Reinforcement Learning
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

# paper-0774 — Trajectory and Offloading Policy Optimization in Age-of-Information-Aware UAV-Assisted MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) have been studied in Mobile Edge Computing (MEC) networks in many researches due to their distinctive advantages, especially in emergency and dynamic scenarios. In this paper, we propose a UAV-assisted MEC system in the disaster scenario, where the UAVs are deployed to undertake the computing and relaying tasks. To ensure the freshness of data as well as the energy efficiency of the system, we jointly minimize the Age of Information (AoI) of the User Equipment (UE) and the energy consumption of the UAVs by optimizing the UAVs' trajectories and the offloading strategies. The non-convex optimization problem is solved in two steps: firstly we propose a Multi-Agent Deep Reinforcement Learning (MADRL) based algorithm to find the optimal trajectory, and then we use a traversal-based algorithm to optimize the offloading policy greedily. Numerical simulations are carried out to verify the validity of the proposed algorithm. It is shown that it has better performance than the baseline algorithms, and is highly reliable in random environments.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0774.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
