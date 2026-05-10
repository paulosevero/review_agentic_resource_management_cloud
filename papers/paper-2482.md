---
id: paper-2482
title: Dynamic Priority-Aware Joint Optimization for Multi-UAV Path Planning and Task Offloading in Mobile Edge Computing
authors:
- Zhu, Yaolin
- Li, Xin
- Qin, Xiaolin
venue: Conference Proceedings - IEEE International Conference on Systems, Man and Cybernetics
venue_type: conference
year: 2025
doi: 10.1109/SMC58881.2025.11343123
url: https://www.scopus.com/pages/publications/105033145498?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 788--794
keywords:
- Behavioral research
- Cluster computing
- Computation offloading
- Decision making
- Learning algorithms
- Mobile edge computing
- Optimization
- Quality of service
- Unmanned aerial vehicles (UAV)
- Communication relays
- Continuous services
- Dynamic priority
- Edge computing
- Edge server
- Joint optimization
- Multi UAV
- Service provisions
- Task offloading
- Terminal equipment
- Motion planning
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

# paper-2482 — Dynamic Priority-Aware Joint Optimization for Multi-UAV Path Planning and Task Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We investigate the problem of path planning and task offloading for UAV clusters in a UAV-assisted edge computing scenario. UAVs autonomously make decisions regarding path planning, continuous service provision, and task offloading based on collected information. In this setting, terminal equipment (TE) cannot directly connect to servers; thus, UAVs act as both edge servers and communication relays, proactively providing services to TEs. We construct a fine-grained temporal scale model that decomposes UAV actions into atomic time units, transforming decision-making on specific behaviors into state transition decisions. This approach better accommodates the needs of time-varying environments. Regarding path planning, given the time-sensitive nature of TE requests, we focus on how to provide stable and timely computational services to TEs. We propose a multi-agent reinforcement learning algorithm capable of dynamically sensing task priorities to enhance Quality of Service (QoS), with optimizations made in terms of task completion rate, UAV energy consumption, and processing delay. About task offloading decision, we introduce a dual-keyword-based offloading algorithm to optimize the binary offloading process. Finally, we conduct simulation experiments to demonstrate the effectiveness of the proposed algorithms, and comparative experiments confirm their superiority. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2482.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
