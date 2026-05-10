---
id: paper-1693
title: Energy Efficient Deadline Aware Scientific Workflow Scheduling in IOT- Cloud Environment
authors:
- Jeevith, U.
- Gopu, Dr Arunkumar
- Sutrave, Mehul N.
- Vaishnavi Santa, K.
- Baretto, Norman
venue: Proceedings of 2025 International Conference on Emerging Technologies in Computing and Communication, ETCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ETCC65847.2025.11108543
url: https://www.scopus.com/pages/publications/105015803301?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Adaptive Task Scheduling
- Cloud Sim Simulation
- Cloud Workflow Scheduling
- Deadline-Aware Scheduling
- Directed Acyclic Graph (DAG)
- IoT-Cloud Environment
- Multi-Agent Reinforcement Learning (MARL)
- Policy Gradient Methods
- Q-Learning
- Resource Optimization
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

# paper-1693 — Energy Efficient Deadline Aware Scientific Workflow Scheduling in IOT- Cloud Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With growing complexity in cloud computing environments, effective task scheduling has become an essential requirement to optimize resource allocation while maintaining adherence to deadlines. This paper proposes the Adaptive Multi-Agent Reinforcement Learning for Cloud Workflow Optimization (AMARL-CWO) algorithm, where multi-agent reinforcement learning (MARL) is used to optimize cloud resource assignment for scientific workflows. The model is proposed to include three main agents: Task Scheduling Agent (TSA), Resource Management Agent (RMA), and Task Dependency Agent (TDA) that work synergistically to optimize workflow execution. The reward function is designed to balance cost savings, deadline, resource usage, and penalty. The algorithm follows a hierarchical scheduling approach, taking advantage of Directed Acyclic Graphs (DAGs) for task dependency, while utilizing Q-learning and policy gradient for adaptive learning. Also, an adaptive exploration strategy refines scheduling choices with respect to the complexity of workload. Simulation evidence in Cloud Sim shows better performance compared to classical scheduling techniques. The AMARL-CWO algorithm offers an energy- efficient, scalable, and deadline-aware approach to workflow scheduling in IoT-cloud systems, overcoming major challenges of dynamic resource handling. Future improvement involves multi-cloud integration and energy- aware optimizations. ©2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1693.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
