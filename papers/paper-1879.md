---
id: paper-1879
title: 'DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach'
authors:
- Liu, Zhang
- Du, Hongyang
- Lin, Junzhe
- Gao, Zhibin
- Huang, Lianfen
- Hosseinalipour, Seyyedali
- Niyato, Dusit
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3486728
url: https://www.scopus.com/pages/publications/85208696098?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1945--1962
keywords:
- deep reinforcement learning
- diffusion model
- DNN partitioning
- Lyapunov optimization
- resource allocation
- task offloading
- vehicular networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1879 — DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid advancement of Artificial Intelligence (AI) has introduced Deep Neural Network (DNN)-based tasks to the ecosystem of vehicular networks. These tasks are often computation-intensive, requiring substantial computation resources, which are beyond the capability of a single vehicle. To address this challenge, Vehicular Edge Computing (VEC) has emerged as a solution, offering computing services for DNN-based tasks through resource pooling via Vehicle-to-Vehicle/Infrastructure (V2V/V2I) communications. In this paper, we formulate the problem of joint DNN partitioning, task offloading, and resource allocation in VEC as a dynamic long-term optimization. Our objective is to minimize the DNN-based task completion time while guaranteeing the system stability over time. To this end, we first leverage a Lyapunov optimization technique to decouple the original long-term optimization with stability constraints into a per-slot deterministic problem. Afterwards, we propose a Multi-Agent Diffusion-based Deep Reinforcement Learning (MAD2RL) algorithm, incorporating the innovative use of diffusion models to determine the optimal DNN partitioning and task offloading decisions. Furthermore, we integrate convex optimization techniques into MAD2RL as a subroutine to allocate computation resources, enhancing the learning efficiency. Through simulations under real-world movement traces of vehicles, we demonstrate the superior performance of our proposed algorithm compared to existing benchmark solutions. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1879.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
