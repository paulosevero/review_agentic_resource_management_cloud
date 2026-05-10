---
id: paper-0985
title: Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms
authors:
- Khoramnejad, Fahime
- Syed, Aisha
- Kennedy, W. Sean
- Erol-Kantarci, Melike
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2024
doi: 10.1109/TNSM.2024.3375839
url: https://www.scopus.com/pages/publications/85187989783?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5647--5661
keywords:
- Lyapunov optimization
- ML accuracy
- Multi-agent reinforcement learning
- offloading
- stability
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0985 — Stability and Accuracy-Aware Learning for Task Offloading in UAV-MEC-Assisted Smart Farms

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study introduces an intelligent task offloading framework designed for smart farms that seamlessly integrates IoT devices, Unmanned Aerial Vehicles (UAVs), and Mobile Edge Computing (MEC) technology. At the heart of our methodology is the utilization of multi-agent reinforcement learning (RL) and Lyapunov theory to optimize task offloading decisions. Our primary contributions are ensuring system stability, task inference accuracy, and minimizing both task loss and delay. System stability is rigorously assessed by formalizing it based on the queue lengths of the MEC server, UAVs, and IoT devices. Furthermore, diverse machine learning (ML) models with varying complexities, such as different numbers of neurons or hidden layers, are deployed by the MEC server, UAVs, and IoT devices. This approach allows us to define task losses in relation to the inference error tolerance of the ML models. Our ultimate goal is to minimize UAV costs, taking into account energy requirements and error tolerance, all the while ensuring system stability. The growing stochastic optimization challenge, particularly with the increasing number of IoT devices, is addressed through the application of Lyapunov optimization theory and a stochastic game framework. However, due to the dynamic nature of the network environment, addressing the game proves to be a challenge, prompting us to develop and implement a multi-agent deep RL (DRL) approach. Our derived intelligent offloading scheme decreases the delay per task by about 35% with respect to the intelligent algorithm without jeopardizing the inference accuracy.  © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0985.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
