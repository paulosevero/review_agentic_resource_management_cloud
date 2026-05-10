---
id: paper-0464
title: 'Task-Aware Multi-UAV Cooperative Computing: A Learning-Based Trajectory and Resource Optimization'
authors:
- Li, Zewu
- Xu, Chen
- Zhang, Zhanpeng
- Wu, Runze
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2022
doi: 10.1109/ICCT56141.2022.10073466
url: https://www.scopus.com/pages/publications/85152290834?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 498--503
keywords:
- cooperative computing
- MADDPG
- resource allocation
- trajectory design
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0464 — Task-Aware Multi-UAV Cooperative Computing: A Learning-Based Trajectory and Resource Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Aerial computing is an important form of mobile edge computing (MEC) to enhance network coverage. In this paper, we focus on a massive access scenario where ground devices with different types of tasks are not in service area of communication infrastructure. Therefore, we propose a task-aware multiple unmanned aerial vehicles (UAV) cooperative computing scheme that each UAV stores the program for executing a certain type of tasks. To minimize the completion time of all tasks, we formulate a problem that jointly considers trajectory design and computation resource allocation for multiple UAVs, as well as user access decision, while guaranteeing quality of services. As the problem is a mixed-integer non-convex optimization which is difficult to solve, we propose a multi-agent deep reinforcement learning-based approach, where the multi-agent deep deterministic policy gradient (MADDPG) algorithm is applied. Considering the high-dimensional continuous action space, a particle swarm optimization (PSO) algorithm for access decision and resource allocation is introduced to reduce the complexity. Simulation results show that the proposed multi-UAV cooperative computing method has a better effect than baseline approaches on reducing the total completion time. © 2022 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0464.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
