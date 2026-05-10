---
id: paper-2930
title: Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System
authors:
- Zhao, Hui
- Luan, Mingan
- Liyanage, Madhusanka
- Chang, Zheng
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2026
doi: 10.1109/TWC.2025.3590253
url: https://www.scopus.com/pages/publications/105012265176?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1272--1286
keywords:
- aerial edge computing
- Internet of Things
- multi-agent deep reinforcement learning
- resource management
- UAV
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

# paper-2930 — Joint Optimization of Sensing, Communication, and Computing for Collaborative Multi-UAV Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV) and high-altitude platform (HAP)-enabled aerial edge computing (AEC) networks facilitate diverse Internet of Things (IoT) applications. In this paper, we investigate the average task completion time and energy consumption by jointly optimizing sensing, communication and computing in cooperative AEC networks facilitated by multiple UAVs and HAP. The sensing times, multi-UAV trajectories, transmission power control, offloading strategy and communication resource allocation are jointly optimized. We transform the original optimization problem into minimizing the average task completion time while ensuring energy consumption stability by introducing Lyapunov optimization theory. The problem is then decomposed into multiple subproblems, which are solved through numerical analysis, successive convex approximation, and the Dinkelbach algorithm, respectively. These algorithms are embedded into the proximal policy optimization (PPO)-based multi-agent deep reinforcement learning (MADRL) framework to speed up the convergence performance of the MADRL model. Simulation results demonstrate that the proposed algorithm achieves superior performance in terms of average task completion time and energy consumption. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2930.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
