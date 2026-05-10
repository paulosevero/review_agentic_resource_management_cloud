---
id: paper-2686
title: MADDPG-Based Joint Task Offloading and Trajectory Planning for MEC-Enabled Multi-UAV Collaborative Offshore Networks
authors:
- Liu, Guoqing
- Zhang, Wenqian
- Luo, Ping
- Lü, Zilong
venue: Springer Aerospace Technology
venue_type: book-chapter
year: 2026
doi: 10.1007/978-981-96-6235-7_52
url: https://www.scopus.com/pages/publications/105017962002?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 523--534
keywords:
- Mobile edge computing (MEC)
- Multiagent deep deterministic policy gradient
- Task offloading
- Unmanned aerial vehicle
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

# paper-2686 — MADDPG-Based Joint Task Offloading and Trajectory Planning for MEC-Enabled Multi-UAV Collaborative Offshore Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned Aerial Vehicles (UAVs) offer significant benefits in wireless systems due to their flexible deployment, improving both coverage and communication quality. This paper focuses on a multi-UAV-assisted Mobile Edge Computing (MEC) system in offshore areas, where UAVs provide task offloading services to mobile users (MUs). MUs can offload tasks to UAVs, which either process them directly or forward parts to a base station. The goal is to minimize processing delay by optimizing task offloading, UAV acceleration, and flight speed, while considering energy constraints. Due to the unpredictable nature of task generation and user movements, this problem is complex and requires real-time decision-making and long-term optimization. Traditional offline algorithms struggle with this dynamic Markov Decision Process (MDP) problem. To address this, we propose a multi-agent deep deterministic policy gradient (MADDPG) algorithm, which adapts through continuous learning and optimization. Experimental results show that our approach effectively reduces computation delay and enhances UAV cooperation. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2686.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
