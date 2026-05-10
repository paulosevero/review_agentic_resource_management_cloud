---
id: paper-1601
title: 'A dual-layer UAV-assisted mobile edge computing system for disaster rescue: Coordinated optimization of coverage, obstacle-avoidance path planning and task offloading'
authors:
- Gu, Weiyu
- Qin, Tuanfa
- Chen, Dan
- Xian, Shixuan
- Jiang, Xiao
- Guo, Wenhao
- Hu, Yongle
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.103981
url: https://www.scopus.com/pages/publications/105011586330?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Mobile edge computing
- Path planning
- Post-disaster rescue
- Reinforcement learning
- Unmanned aerial vehicles (UAVs)
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

# paper-1601 — A dual-layer UAV-assisted mobile edge computing system for disaster rescue: Coordinated optimization of coverage, obstacle-avoidance path planning and task offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study addresses critical challenges in urban disaster rescue operations, such as fires, including communication failures, complex environments, and information scarcity. We propose a novel Dual-layer UAV-assisted Mobile Edge Computing (DUAMEC) system, leveraging an air–space–ground collaborative communication framework and intelligent task scheduling to overcome traditional limitations like information blind spots, decision-making delays, and inefficient response. DUAMEC innovatively combines a high-altitude upper-layer UAV (U-UAV) for wide-area coverage and a low-altitude down-layer UAV (D-UAV) for task processing, achieving strong coverage, low latency, and high energy efficiency. The core innovations of the DUAMEC system are manifested in the following aspects: First, we propose a grid-based adaptive multi-stage greedy optimization algorithm for optimal UAV deployment, dynamically generating multi-level candidate grids and employing adaptive step-size contraction. An uncovered-point compensation mechanism ensures continuous area coverage. Second, we design a Multi-Agent TD3 with Hindsight Priority Experience Replay (MATD3-HP) algorithm, utilizing a multi-dimensional state space and compound reward mechanism to optimize resource allocation, path planning, and task offloading in dynamic obstacle environments. Experimental results demonstrate that compared to conventional single-layer UAV-MEC systems and fixed path planning schemes, the DUAMEC system achieves an 66.78% reduction in system overhead while maintaining 98% user coverage. Simultaneously, it sustains stable performance with low task processing latency and energy consumption even in scenarios with dense user distribution and highly dynamic obstacles, thereby providing an efficient and reliable intelligent solution for urban disaster rescue operations. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1601.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
