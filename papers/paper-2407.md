---
id: paper-2407
title: AoI-Based Scalable Edge Computing Resource Allocation in Heterogeneous IIoT Systems
authors:
- Zakamulin, Daniel S.
- Pourghasemian, Mohsen
- Saghezchi, Firooz B.
- Gacanin, Haris
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2025
doi: 10.1109/WCNC61545.2025.10978350
url: https://www.scopus.com/pages/publications/105006448875?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AoI
- Edge Computing
- Energy Efficiency
- Industrial IoT
- Latency
- Multi-Agent DRL
- Resource Allocation
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

# paper-2407 — AoI-Based Scalable Edge Computing Resource Allocation in Heterogeneous IIoT Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing is a sustainable network paradigm that supports resource constrained Industrial Internet of Things (IIoT) devices in performing data-driven tasks. The distributed architecture of computing resources, combined with the heterogeneous and sporadic characteristics of IIoT tasks, presents a substantial challenge to achieving energy-efficient and low-latency task execution. In this paper, we demonstrate that modeling the Age of Information (AoI) as an exponential function can significantly enhance the performance of task scheduling and execution in edge computing systems. Furthermore, we introduce a low over-head Multi-Agent Deep Reinforcement Learning (DRL) algorithm with No Observation (MA-NO) for distributed edge computing resource allocation, where agents (IIoT devices) operate independently without communicating with each other. However, to prevent the divergence of the agents and ensure a Pareto-optimal decision-making, we adopt a common reward that is shared among all agents. That is, all agents receive the same reward, based on their collective performance. Simulation results show that our proposed AoI model reduces the average execution latency of the tasks by 35.2% compared to a linear AoI ones. Furthermore, our proposed MA-NO algorithm reduces the total energy consumption of the IIoT devices by 59.9% and 63.4% compared to the single-agent DRL algorithm and multi-agent DRL algorithm with partial observations, respectively. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2407.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
