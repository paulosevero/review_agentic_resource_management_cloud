---
id: paper-2690
title: Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]
authors:
- Liu, Jiahui
- Zou, Yuan
- Wu, Jinming
- Du, Guodong
- Sun, Wenjing
venue: Qiche Gongcheng/Automotive Engineering
venue_type: journal
year: 2026
doi: 10.19562/j.chinasae.qcgc.2026.01.002
url: https://www.scopus.com/pages/publications/105030473251?origin=resultslist
publisher: SAE-China
pages: 13--23
keywords:
- deep reinforcement learning
- mobile edge computing
- resource allocation
- task offloading
- vehicle platoon
language: Chinese
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

# paper-2690 — Task Offloading and Resource Allocation for ICV Platoon Under Edge Computing; [边缘计算环境下ICV队列的任务卸载与资源分配]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of Intelligent Connected Vehicles （ICV） and vehicle to infrastructure （V2I） technologies， in vehicle application increasingly demand greater computational capacity and lower response latency. Although Mobile Edge Computing （MEC） can alleviate these requirements by offloading tasks to  edge servers， its limited coverage and constrained resources struggle to meet high-density workloads. Vehicle platoon provides an effective solution by leveraging stable inter vehicular communication and shared computational resources. In this paper， for a MEC-assisted edge computing system for ICV platoon， an optimization model to minimize the comprehensive task execution cost is constructed and a two stage Task Offloading and Resource Allocation  algorithm （TS-TORA） is proposed. Based on the system’s “offload-then-execute” process， the algorithm decomposes the task offloading and resource allocation into two levels of optimization problems and heterogeneous scheduling  strategies are designed according to the node type. In the task offloading stage， the platoon leader （PL） employs  Multi-Agent Proximal Policy Optimization （MAPPO） to generate a global offloading strategy, in the resource allocation stage， platoon vehicles （PVs） apply a priority-based greedy algorithm for local resource allocation， while MEC  servers leverage a Double Deep Q-Network （DDQN） for dynamic multi-task scheduling， thus balancing global  scheduling efficiency and node execution flexibility. The simulation results show that TS-TORA consistently outperforms benchmark algorithms across varying platoon sizes， task complexities， and latency constraints. Specifically，  task success rates reach 97.06%， 84.62%， and 78.31% for platoons of 4， 6， and 8 PVs， respectively. Moreover，  the average cost decreases with increasing platoon size， demonstrating the algorithm’s adaptability and scalability. © 2026, SAE-China. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2690.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
