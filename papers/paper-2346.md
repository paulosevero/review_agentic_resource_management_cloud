---
id: paper-2346
title: Multi-agent deep reinforcement learning-based partial offloading and resource allocation in vehicular edge computing networks
authors:
- Xue, Jianbin
- Wang, Luyao
- Yu, Qingda
- Mao, Peipei
venue: Computer Communications
venue_type: journal
year: 2025
doi: 10.1016/j.comcom.2025.108081
url: https://www.scopus.com/pages/publications/85218272600?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computational offload
- Multi-agent deep reinforcement learning
- Resource allocation
- Task migration
- Vehicular edge computing network
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

# paper-2346 — Multi-agent deep reinforcement learning-based partial offloading and resource allocation in vehicular edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The advancement of intelligent transportation systems and the increase in vehicle density have led to a need for more efficient computation offloading in vehicular edge computing networks (VECNs). However, traditional approaches are unable to meet the service demand of each vehicle due to limited resources and overload. Therefore, in this paper, we aim to minimize the long-term computation overhead (including delay and energy consumption) of vehicles. First, we propose combining the computational resources of local vehicles, idle vehicles, and roadside units (RSUs) to formulate a computation offloading strategy and resource allocation scheme based on multi-agent deep reinforcement learning (MADRL), which optimizes the dual offloading decisions for both total and residual tasks as well as system resource allocation for each vehicle. Furthermore, due to the high mobility of vehicles, we propose a task migration strategy (TMS) algorithm based on communication distance and vehicle movement speed to avoid failure of computation result delivery when a vehicle moves out of the communication range of an RSU service node. Finally, we formulate the computation offloading problem for vehicles as a Markov game process and design a Partial Offloading and Resource Allocation algorithm based on the collaborative Multi-Agent Twin Delayed Deep Deterministic Policy Gradient (PORA-MATD3). PORA-MATD3 optimizes the offloading decisions and resource allocation for each vehicle through a centralized training and distributed execution approach. Simulation results demonstrate that PORA-MATD3 significantly reduces the computational overhead of each vehicle compared to other baseline algorithms in VECN scenarios. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2346.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
