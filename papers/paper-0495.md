---
id: paper-0495
title: Uncertainty-Aware Management of Smart Grids Using Cloud-Based LSTM-Prediction Interval
authors:
- Tajalli, Seyede Zahra
- Kavousi-Fard, Abdollah
- Mardaneh, Mohammad
- Khosravi, Abbas
- Razavi-Far, Roozbeh
venue: IEEE Transactions on Cybernetics
venue_type: journal
year: 2022
doi: 10.1109/TCYB.2021.3089634
url: https://www.scopus.com/pages/publications/85112643250?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9964--9977
keywords:
- Cloud-fog architecture
- deep learning
- demand response
- multiagent system
- prediction intervals
- uncertainty-aware management
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0495 — Uncertainty-Aware Management of Smart Grids Using Cloud-Based LSTM-Prediction Interval

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article introduces an uncertainty-aware cloud-fog-based framework for power management of smart grids using a multiagent-based system. The power management is a social welfare optimization problem. A multiagent-based algorithm is suggested to solve this problem, in which agents are defined as volunteering consumers and dispatchable generators. In the proposed method, every consumer can voluntarily put a price on its power demand at each interval of operation to benefit from the equal opportunity of contributing to the power management process provided for all generation and consumption units. In addition, the uncertainty analysis using a deep learning method is also applied in a distributive way with the local calculation of prediction intervals for sources with stochastic nature in the system, such as loads, small wind turbines (WTs), and rooftop photovoltaics (PVs). Using the predicted ranges of load demand and stochastic generation outputs, a range for power consumption/generation is also provided for each agent called 'preparation range' to demonstrate the predicted boundary, where the accepted power consumption/generation of an agent might occur, considering the uncertain sources. Besides, fog computing is deployed as a critical infrastructure for fast calculation and providing local storage for reasonable pricing. Cloud services are also proposed for virtual applications as efficient databases and computation units. The performance of the proposed framework is examined on two smart grid test systems and compared with other well-known methods. The results prove the capability of the proposed method to obtain the optimal outcomes in a short time for any scale of grid.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0495.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
