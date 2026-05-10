---
id: paper-2358
title: Task Demand-Oriented Collaborative Offloading and Deployment Strategy in Software-Defined UAV-Assisted Edge Networks
authors:
- Yan, Junjie
- Wang, Wenli
- Liu, Jingxian
- Deng, Junyi
- Yuan, Haohao
- Zhu, Yaxin
venue: IEEE Sensors Journal
venue_type: journal
year: 2025
doi: 10.1109/JSEN.2024.3494028
url: https://www.scopus.com/pages/publications/85209732149?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1641--1655
keywords:
- Mobile edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- Tabu search-based matching (TSM)
- unmanned aerial vehicles (UAVs)
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

# paper-2358 — Task Demand-Oriented Collaborative Offloading and Deployment Strategy in Software-Defined UAV-Assisted Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs), which are a crucial element of the future air-space-ground integrated network, can serve as potential mobile edge computing (MEC) nodes due to their onboard capabilities for storage, communication, and computation. However, current UAV-assisted MEC collaborative offloading methods primarily focus on addressing network requirements for computing tasks, while neglecting the heterogeneity in task demands due to the heterogeneity of task types and UAV service types. To address this, we propose a task demand-oriented collaborative offloading and deployment strategy in software-defined UAV-assisted edge networks. Specifically, to enhance the cache utilization of UAVs, we introduce a software-defined UAV edge network (SD-UEN) architecture, which facilitates cooperation among UAVs under the guidance of a software-defined networking (SDN) controller. In light of the heterogeneity of task demands, we employ the Tabu search-based matching (TSM) algorithm to accurately match computing tasks with the appropriate UAV modes. Furthermore, to enable intelligent UAV mode switching and dynamic UAV location deployment, we leverage the multiagent deep deterministic policy gradient (MADDPG) algorithm. By centrally training the MADDPG model offline, MEC servers and UAVs, acting as learning agents, can efficiently adjust UAV modes and deploy UAVs during online execution. This algorithm dynamically optimizes UAV actions to minimize task completion time and energy consumption. The simulation results highlight that our algorithm substantially reduces task response time and energy consumption compared with other algorithms, demonstrating its effectiveness.  © 2001-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2358.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
