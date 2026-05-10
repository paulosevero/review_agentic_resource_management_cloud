---
id: paper-2268
title: Joint trajectory and offloading optimization in UAV-assisted MEC via federated multi-agent reinforcement learning and potential fields
authors:
- Wang, Cong
- Liu, Ke
- Yuan, Ying
- Peng, Sancheng
- Li, Guorui
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2025.111681
url: https://www.scopus.com/pages/publications/105015370865?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Federated learning
- Multi-agent reinforcement learning
- Potential fields
- Task offloading
- Trajectory planning
- Unmanned aerial vehicles
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

# paper-2268 — Joint trajectory and offloading optimization in UAV-assisted MEC via federated multi-agent reinforcement learning and potential fields

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) assisted mobile edge computing (MEC) is characterized by flexible deployment, high mobility, and dynamic coverage. It facilitates an efficient execution of latency-sensitive tasks in scenarios such as emergency rescue and dynamic computility support, thereby demonstrating significant application prospect. However, joint scheduling of computility and task is still an open issue in optimizing task efficiency and UAVs’ energy consumption. To address this problem, we propose an UAV-assisted MEC framework based on federated multi-agent reinforcement learning (MARL) and potential fields (PF), which jointly optimizes UAV trajectories and task offloading strategies to minimize age of information (AoI) under latency and energy constraints. The decision-making process of multiple UAVs is to be modeled as a Partially Observable Markov Decision Process (POMDP) and to be solved by using a distributed federated MARL architecture. An adaptive federated collaboration model is designed for periodic parameter sharing based on credit allocation to enhance UAV collaboration and to alleviate partial observability. Additionally, a deep reinforcement learning (DRL) trajectory planning algorithm based on PF to enhance agents’ environment perception and decision-making ability. Experimental results show the effectiveness and feasibility of our proposed framework. It outperforms several existing RL-based approaches in terms of data freshness, task efficiency, and other key metrics while demonstrating strong adaptability in dynamic and complex MEC environments. © 2025

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2268.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
