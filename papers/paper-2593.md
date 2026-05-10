---
id: paper-2593
title: MARL-Driven Decentralized Crowdsourcing Logistics for Time-Critical Multi-UAV Networks
authors:
- Han, Juhyeong
- Kim, Hyunbum
venue: Electronics (Switzerland)
venue_type: journal
year: 2026
doi: 10.3390/electronics15020331
url: https://www.scopus.com/pages/publications/105028658580?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- collision avoidance
- decentralized crowdsourcing
- edge computing
- emergency logistics
- Multi-Agent Reinforcement Learning (MARL)
- path planning
- task allocation
- Unmanned Aerial Vehicles (UAVs)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2593 — MARL-Driven Decentralized Crowdsourcing Logistics for Time-Critical Multi-UAV Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Centralized UAV logistics controllers can achieve strong navigation performance in controlled settings, but they do not capture key deployment factors in crowdsourcing-enabled emergency logistics, where heterogeneous UAV owners participate with unreliability and dropout, and incentive expenditure and fairness must be accounted for. This paper presents a decentralized crowdsourcing multi-UAV emergency logistics framework on an edge-orchestrated architecture that (i) performs urgency-aware dispatch under distance/energy/payload constraints, (ii) tracks reliability and participation dynamics under stress (unreliable agents and dropout), and (iii) quantifies incentive feasibility via total payment and payment inequality (Gini). We adopt a hybrid decision design in which PPO/DQN policies provide real-time navigation/control, while GA/ACO act as planning-level route refinement modules (not reinforcement learning) to improve global candidate quality under safety constraints. We evaluate the framework in a controlled grid-world simulator and explicitly report stress-matched re-evaluation results under matched stress settings, where applicable. In the nominal comparison, centralized DQN attains high navigation-centric success (e.g., 0.970 ± 0.095) with short reach steps, but it omits incentives by construction, whereas the proposed crowdsourcing method reports measurable payment and fairness outcomes (e.g., payment and Gini) and remains evaluable under unreliability and dropout sweeps. We further provide a utility decomposition that attributes negative-utility regimes primarily to collision-related costs and secondarily to incentive expenditure, clarifying the operational trade-off between mission value, safety risk, and incentive cost. Overall, the results indicate that navigation-only baselines can appear strong when participation economics are ignored, while a deployable crowdsourcing system must explicitly expose incentive/fairness and robustness characteristics under stress. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2593.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
