---
id: paper-2037
title: Trajectory Design and Resource Allocation for Multi-UAV-Assisted Sensing, Communication, and Edge Computing Integration
authors:
- Peng, Sicong
- Li, Bin
- Liu, Lei
- Fei, Zesong
- Niyato, Dusit
venue: IEEE Transactions on Communications
venue_type: journal
year: 2025
doi: 10.1109/TCOMM.2024.3478115
url: https://www.scopus.com/pages/publications/105003045020?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2847--2861
keywords:
- data compression
- Mobile edge computing
- multi-agent deep reinforcement learning
- radar sensing
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

# paper-2037 — Trajectory Design and Resource Allocation for Multi-UAV-Assisted Sensing, Communication, and Edge Computing Integration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, we propose a multi-unmanned aerial vehicle (UAV)-assisted integrated sensing, communication, and computation network. Specifically, the treble-functional UAVs are capable of offering communication and edge computing services to mobile users (MUs) in proximity, alongside their target sensing capabilities by using multi-input multi-output arrays. For the purpose of enhance the computation efficiency, we consider task compression, where each MU can partially compress their offloaded data prior to transmission to trim its size. The objective is to minimize the weighted energy consumption by jointly optimizing the transmit beamforming, the UAVs’ trajectories, the compression and offloading partition, the computation resource allocation, while fulfilling the causal-effect correlation between communication and computation as well as adhering to the constraints on sensing quality. To tackle it, we first reformulate the original problem as a multi-agent Markov decision process (MDP), which involves heterogeneous agents to decompose the large state spaces and action spaces of MDP. Then, we propose a multi-agent proximal policy optimization algorithm with attention mechanism to handle the decision-making problem. Simulation results validate the significant effectiveness of the proposed method in reducing energy consumption. Moreover, it demonstrates superior performance compared to the baselines in relation to resource utilization and convergence speed. © 1972-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2037.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
