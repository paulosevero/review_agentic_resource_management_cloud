---
id: paper-2637
title: Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems
authors:
- Khater, Heba M.
- Sallabi, Farag
- Serhani, Mohamed Adel
- Barka, Ezedin
- Khayat, Mohamad
venue: Computers and Operations Research
venue_type: journal
year: 2026
doi: 10.1016/j.cor.2026.107454
url: https://www.scopus.com/pages/publications/105034613612?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Actor-critic
- Collaborative decision-making
- Deep reinforcement learning
- Mobile Edge Computing
- Multi-agent systems
- Offloading optimization
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

# paper-2637 — Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rise of the Internet of Medical Things (IoMT), healthcare systems increasingly rely on Wireless Body Area Networks (WBANs) for continuous, real-time patient monitoring and clinical decision-making. These applications require ultra-low latency, high reliability, and energy efficiency. Typically, they operate via mobile devices, such as smartphones, wearables, or WBAN coordinators, which collect, process, and transmit medical data. However, the limited processing capabilities and energy constraints of these devices often lead to increased delays and degraded system performance. To address these challenges, Mobile Edge Computing (MEC) has emerged as a promising solution that brings computation closer to the network edge. This paper addresses the optimization problem of task offloading and resource allocation in WBAN-MEC systems, where each task can be executed locally on the mobile device, offloaded to the MEC server, or to the cloud. The problem is formulated as a Mixed-Integer Nonlinear Programming (MINLP) model involving offloading decisions and the allocation of communication and computational resources. Our objective is to maximize task completion subject to time constraints, minimize mobile energy consumption, and ensure efficient use of MEC resources. We propose a Collaborative Multi-Agent Task Offloading and Resource Allocation (CoMA-TORA) framework, which decomposes the complex optimization problem into two coordinated components: a decentralized offloading decision component and a centralized resource allocation component. The framework is implemented using an actor-critic reinforcement learning architecture, with a global critic that evaluates a shared reward for coordinated decision-making. Simulation results show that CoMA-TORA outperforms both traditional and DRL-based approaches in delay-sensitive healthcare environments. © 2026 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2637.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
