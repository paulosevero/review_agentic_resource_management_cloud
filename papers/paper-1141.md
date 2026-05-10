---
id: paper-1141
title: 'Dynamic Task Offloading and Resource Allocation in Vehicle Edge Computing and Networks: A Graph Attention-Based Deep Reinforcement Learning Approach'
authors:
- Qin, Baolin
- He, Ang
- Pan, Heng
- Si, Xueming
- Dai, Yueyue
- Huang, Xiaoyan
- Zhang, Yan
venue: Proceedings - 2024 IEEE International Conference on High Performance Computing and Communications, HPCC 2024
venue_type: conference
year: 2024
doi: 10.1109/HPCC64274.2024.00158
url: https://www.scopus.com/pages/publications/105013072309?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1168--1175
keywords:
- deep reinforcement learning
- graph attention networks
- resource allocation
- task offloading
- Vehicular edge computing
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

# paper-1141 — Dynamic Task Offloading and Resource Allocation in Vehicle Edge Computing and Networks: A Graph Attention-Based Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle edge computing (VEC) leverages the computational and communication resources available from vehicles and mobile edge computing (MEC) servers to provide computing services for mobile vehicles. However, traditional task offloading and resource allocation methods based on deep reinforcement learning (DRL) often ignore the latent relationships between vehicles and MEC servers. This oversight results in a lack of robustness in highly mobile and complex environments. Therefore, this paper proposes a distributed dynamic task offloading and resource allocation (DDTORA) strategy in the context of vehicle-assisted multi-vehicle VEC scenarios. DDTORA aims to utilize idle computational resources of vehicles and find optimal task offloading and resource allocation schemes to minimize the weighted summation of latency and energy consumption for all tasks. To find the optimal solution, we propose a graph attention network based multi-agent deep reinforcement learning (GAMDRL) algorithm for distributed task offloading and resource allocation. Numerical simulations demonstrate that DDTORA converges faster than the benchmark algorithms, significantly reducing latency and energy consumption by 25.44% to 34.19%.  © 2024 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1141.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
