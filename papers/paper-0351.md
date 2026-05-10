---
id: paper-0351
title: Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing
authors:
- Wang, Liang
- Wang, Kezhi
- Pan, Cunhua
- Xu, Wei
- Aslam, Nauman
- Hanzo, Lajos
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2021
doi: 10.1109/TCCN.2020.3027695
url: https://www.scopus.com/pages/publications/85091953434?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 73--84
keywords:
- MADDPG
- mobile edge computing
- Multi-agent deep reinforcement learning
- trajectory control
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
    my_justification: RL
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

# paper-0351 — Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> An unmanned aerial vehicle (UAV)-aided mobile edge computing (MEC) framework is proposed, where several UAVs having different trajectories fly over the target area and support the user equipments (UEs) on the ground. We aim to jointly optimize the geographical fairness among all the UEs, the fairness of each UAV' UE-load and the overall energy consumption of UEs. The above optimization problem includes both integer and continues variables and it is challenging to solve. To address the above problem, a multi-agent deep reinforcement learning based trajectory control algorithm is proposed for managing the trajectory of each UAV independently, where the popular Multi-Agent Deep Deterministic Policy Gradient (MADDPG) method is applied. Given the UAVs' trajectories, a low-complexity approach is introduced for optimizing the offloading decisions of UEs. We show that our proposed solution has considerable performance over other traditional algorithms, both in terms of the fairness for serving UEs, fairness of UE-load at each UAV and energy consumption for all the UEs. © 2015 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0351.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
