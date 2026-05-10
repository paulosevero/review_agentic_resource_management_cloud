---
id: paper-1917
title: Edge-Aware 3D Trajectory and Bandwidth Co-Optimization in UAV-Assisted IoT Network
authors:
- Luo, Ping
- Zhang, Wenqian
- Liu, Guoqing
venue: Proceedings - 2025 IEEE Annual Congress on Artificial Intelligence of Things, AIoT 2025
venue_type: conference
year: 2025
doi: 10.1109/AIoT66900.2025.00051
url: https://www.scopus.com/pages/publications/105035765208?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 294--301
keywords:
- bandwidth allocation
- MADDPG
- Mobile Edge Computing (MEC)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1917 — Edge-Aware 3D Trajectory and Bandwidth Co-Optimization in UAV-Assisted IoT Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study extends prior research on IoT edge intelligence into three-dimensional space by proposing an extended Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm that optimizes bandwidth allocation at the edge. Our approach enhances resource utilization for distributed Unmanned aerial vehicle (UAV) networks acting as intelligent edge nodes. The system is modeled as a Partially Observable Markov Decision Process (POMDP) to address multi-agent non-stationarity in dynamic edge environments, while experience replay and soft update mechanisms ensure strategy optimization and operational stability. Extensive simulations confirm a significant latency reduction achieved by the proposed edge-aware algorithm-sensitive Internet of Things (IoT) applications - while improving edge resource utilization and Quality of Service (QoS). Compared to baseline methods using fixed-speed or stationary drones, our intelligent speed adjustment scheme achieves a 19.5% performance gain in 3D edge deployments. Comprehensive scalability testing across diverse drone densities, channel capacities, and user configurations validates the solution's robustness for adaptive edge computing under heterogeneous IoT operational demands.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1917.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
