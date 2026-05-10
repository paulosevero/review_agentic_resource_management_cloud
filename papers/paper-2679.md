---
id: paper-2679
title: Device-satellite-satellite collaborative task offloading computing and resource allocation in 6G satellite-ground edge computing network
authors:
- Liu, Sai
- Zhang, Zhenjiang
- Zeadally, Sherali
venue: Computer Networks
venue_type: journal
year: 2026
doi: 10.1016/j.comnet.2025.111871
url: https://www.scopus.com/pages/publications/105022466808?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Collaborative computing
- Internet of things
- Multi-agent deep reinforcement learning
- Resource allocation
- Satellite edge computing
- Task offloading
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

# paper-2679 — Device-satellite-satellite collaborative task offloading computing and resource allocation in 6G satellite-ground edge computing network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The popularity of smart devices extends emerging intelligent applications to remote areas. The limited computing capacity of devices and inadequate ground computing facilities make it a challenge to efficiently process computation-intensive tasks. Fortunately, satellite edge computing networks can provide powerful computing services for users in remote areas. However, the mobility of satellites and the spatio-temporal characteristics of networks bring great challenges to multi-satellite collaborative computing. To address these challenges, we propose a device-satellite-satellite collaborative edge computing network that jointly optimizes task offloading decision and ratio, bandwidth and computing resource allocation. Since traditional optimization algorithms cannot handle time-varying NP-hard problem, we propose an intelligent task offloading method based on multi-agent twin delayed deep deterministic policy gradient. To address the high algorithm complexity brought by high-dimensional action space, we decompose the joint optimization problem into task offloading subproblem and computing resource allocation subproblem. We combine the Lagrangian optimization method to establish a satellite computing resource allocation mechanism, which is convenient for satellite to quickly allocate its edge computing capability according to task requirements, and reduces the dimension of the agent action space. Finally, we propose an Intelligent Task Offloading and Lagrange Optimization Assisted Resource Allocation (ITO-LOARA) algorithm to maximize the task success rate and minimize the task execution delay and energy consumption. Simulation results show that our proposed scheme achieves efficient task offloading and collaborative computing between ground devices and satellite edge computing nodes, and has superior performance, better scalability, and higher stability compared with the baseline and mainstream algorithms. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2679.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
