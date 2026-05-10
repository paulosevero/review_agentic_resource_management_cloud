---
id: paper-2496
title: 'Empowering multi-UAV networks: a synergistic approach to task offloading and trajectory optimization'
authors:
- Adhikari, Pronab Kumar
- Tomar, Abhinav
venue: Cluster Computing
venue_type: journal
year: 2026
doi: 10.1007/s10586-025-05912-x
url: https://www.scopus.com/pages/publications/105029978750?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Independent Proximal Policy Optimization
- Mobile edge computing
- Multi-agent reinforcement learning
- Task offloading
- Trajectory optimization
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2496 — Empowering multi-UAV networks: a synergistic approach to task offloading and trajectory optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Abstract: This scholarly article elucidates a holistic approach for enhancing the operational efficacy of UAV-MEC (Unmanned Aerial Vehicle enabled Mobile Edge Computing Server) networks, focusing on the critical aspects of task offloading, trajectory control, energy utilization, and queuing stability. We introduce the Joint Offloading-Trajectory Optimization (JOTO) framework, which facilitates multi-UAV-MEC networks in offloading computational tasks from mobile devices (MDs) to UAV-MECs, and subsequently to base station (BS). The framework employs a hybrid optimization framework where Independent Proximal Policy Optimization (IPPO) handles decentralized trajectory control and maneuvering, while a Lyapunov-based convex optimization model determines adaptive task offloading ratios. This dual methodology enables each UAV-MEC to dynamically adjust its trajectory and offloading strategy to minimize energy consumption, stabilize queues, and maximize MD energy efficiency. Crucially, our model utilizes channel gain information, rather than accurate locational data, for near-optimal decision-making. Empirical simulations reveal that JOTO surpasses other deep reinforcement learning (DRL)-based frameworks in energy consumption, service duration, and decision-making efficacy, achieving performance competitive with convex optimization benchmarks. By jointly optimizing trajectory control and cooperative task offloading, our methodology significantly advances the capabilities of UAV-enabled MEC networks for real-world edge computing scenarios. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2496.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
