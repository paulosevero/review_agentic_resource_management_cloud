---
id: paper-2863
title: 'Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach'
authors:
- Xu, Yueqiang
- Wang, Lei
- Gao, Qiang
- Zhao, Wei
- Zhang, Heli
- Lin, Fuhong
- Lu, Lu
- He, Jianhua
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3631071
url: https://www.scopus.com/pages/publications/105021405510?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3726--3742
keywords:
- Edge collaboration
- Lyapunov theory
- multiagent deep reinforcement learning (MADRL)
- nonterrestrial networks (NTNs)
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

# paper-2863 — Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite-edge computing offers promising solutions for extending the coverage of terrestrial networks, particularly in remote and harsh environments. By offloading ground data to satellites for processing, this paradigm enables real-time data handling in nonterrestrial networks (NTNs). However, due to limited onboard resources and dynamic task requirements from the Internet of Things (IoT) devices, online energy management becomes a critical challenge that hinders the scalability and deployment of satellite-edge computing systems. In this article, we propose an online energy management framework based on satellite-edge collaboration. A queue-based collaboration scheme is designed to coordinate satellites in handling tasks with random arrival patterns. Building upon this scheme, we formulate a joint optimization problem that integrates transmission resource allocation, computational resource assignment, power control, routing strategies, and collaboration policies, aiming to minimize the energy consumption of the satellite network. Given the dynamic, complex, and distributed nature of the problem, we present a Lyapunov-based multiagent deep reinforcement learning (MADRL) algorithm. Specifically, we first transform the long-term stochastic optimization problem into a sequence of deterministic subproblems using the Lyapunov theory. Subsequently, each subproblem is decomposed into a resource allocation subproblem and an edge collaboration subproblem. Correspondingly, we devise a MADRL-based algorithm for edge collaboration and a Lagrangian multiplier iteration (LMI)-based algorithm for resource allocation. Finally, the overall problem is iteratively optimized using the block coordinate descent (BCD) framework. Simulation results demonstrate that the proposed approach achieves significant performance improvements over both baseline methods and several state-of-the-art pure deep reinforcement learning (DRL) approaches. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2863.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
