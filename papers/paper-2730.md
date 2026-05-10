---
id: paper-2730
title: An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants
authors:
- Ni, Haochen
- Wang, Yonghua
- Tang, Xinfa
- Wang, Jingjing
venue: Processes
venue_type: journal
year: 2026
doi: 10.3390/pr14050743
url: https://www.scopus.com/pages/publications/105032755008?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- adaptive exploration
- carbon emission reduction
- deep reinforcement learning
- MEVPPs
- two-stage scheduling
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2730 — An Intelligent Two-Stage Dispatch Framework for Cost and Carbon Reduction in Multi-Energy Virtual Power Plants

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenge of coordinating economic and environmental objectives for Multi-energy Virtual Power Plants (MEVPPs), particularly under ambitious decarbonization policies such as China’s “dual carbon” goals, this paper proposes a novel two-stage scheduling framework that integrates Deep Reinforcement Learning (DRL) with Model Predictive Control (MPC). The core innovations include the following: (1) high-fidelity physical models capturing wind turbulence correction, photovoltaic temperature-irradiation coupling, and state-of-charge-dependent energy storage efficiency, improving equipment dynamic characterization accuracy by 12.7% compared to conventional models; (2) an enhanced Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm incorporating priority experience replay and adaptive noise exploration, which accelerates convergence by 15.6%; (3) a pioneering coordination architecture of “Day-Ahead MADDPG—Real-Time MPC” that manages uncertainties through bidirectional feedback, where real-time deviations refine the long-term policy via experience replay. Simulation results using historical data from a North China industrial park demonstrate that the framework reduces operating costs by 13.3% and carbon emissions by 17.7% compared to particle swarm optimization, outperforms standard DDPG with 3.2% lower operating costs, 5.8% lower carbon emissions, and a 3.3% higher renewable utilization rate (88.6%), and achieves 55% renewable penetration with only 4.1% curtailment. These results validate the framework’s scalability for high-renewable penetration grids and its real-time feasibility, as confirmed by edge computing deployment with latency below 50 ms. This study offers a technically viable and scalable solution for the operation of low-carbon virtual power plants (VPPs), supporting the transition towards sustainable power systems. © 2026 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2730.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
