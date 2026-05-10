---
id: paper-2277
title: 'Multi-UAV Enabled MEC Networks: Optimizing Delay Through Intelligent 3-D Trajectory Planning and Resource Allocation'
authors:
- Wang, Zhiying
- Wei, Tianxi
- Sun, Gang
- Liu, Xinyue
- Yu, Hongfang
- Niyato, Dusit
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2025
doi: 10.1109/TITS.2025.3586874
url: https://www.scopus.com/pages/publications/105011695596?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20897--20911
keywords:
- 3D trajectory design
- Mobile edge computing
- multi-agent deep reinforcement learning
- task offloading
- uncrewed aerial vehicle
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2277 — Multi-UAV Enabled MEC Networks: Optimizing Delay Through Intelligent 3-D Trajectory Planning and Resource Allocation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) reduces the computational burden on terminal devices by shortening the distance between these devices and computing nodes. Integrating Uncrewed Aerial Vehicles (UAVs) with enhanced MEC networks can leverage the high mobility of UAVs to flexibly adjust network topology, further expanding the applicability of MEC. However, in highly dynamic and complex real-world environments, it is crucial to balance task offloading effectiveness with algorithm performance. This paper investigates a multi-UAV communication network equipped with edge computing nodes to assist terminal users in task computation. Our goal is to reduce the task processing delay for users through the joint optimization of discrete computation modes, continuous 3D trajectories, and resource assignment. To address the challenges posed by the mixed action space, we propose a Multi-UAV Edge Computing Resource Scheduling (MUECRS) algorithm, which comprises two key components: 1) trajectory optimization, and 2) computation mode and resource management. Experimental results show that our method effectively plans 3D UAV trajectories and enables rapid user coverage. Compared to state-of-the-art baselines, our approach achieves at least 16.5% reduction in task delay, demonstrating superior adaptability and robustness. © 2000-2011 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2277.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
