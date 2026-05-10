---
id: paper-0794
title: QoS-Driven Distributed Cooperative Data Offloading and Heterogeneous Resource Scheduling for IIoT
authors:
- Zhang, Fan
- Han, Guangjie
- Li, Aohan
- Lin, Chuan
- Liu, Li
- Zhang, Yu
- Peng, Yan
venue: IEEE Internet of Things Magazine
venue_type: journal
year: 2023
doi: 10.1109/IOTM.001.2200264
url: https://www.scopus.com/pages/publications/85193948618?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 118--124
keywords:
- Decision making
- Deep learning
- Linear programming
- Mathematical transformations
- Multi agent systems
- Reinforcement learning
- Decision-making frameworks
- Distributed decision making
- Distributed-decision makings
- Edge server
- Heterogeneous resources
- Quality-of-service
- Resource-scheduling
- Service demand
- Sub-problems
- Terminal devices
- Quality of service
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0794 — QoS-Driven Distributed Cooperative Data Offloading and Heterogeneous Resource Scheduling for IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing has become a powerful paradigm to fulfill the diversified quality of service (QoS) demands of the Industrial Internet of Things (IIoT) applications. This study examines the cooperative data offloading (DO) and heterogeneous resource scheduling (RS) problem for maximizing long-term system utility. Owing to the dynamics, high connectivity density, and diverse QoS demands of IIoT, a QoS-driven distributed decision-making (QDDM) framework is proposed to address this problem. Specifically, this framework decomposes the primal problem into two subproblems: industrial terminal device (ITD)-side DO and edge server (EDS)-side RS. Then, a modified soft actor-critic (SAC)-based multi-agent deep reinforcement learning (MSMD) algorithm is proposed to address the ITD-side DO subproblem, which can achieve more accurate estimation of the Q-values and solve both the centralized-decentralized mismatch and the multi-agent credit assignment issues. Based on the DO decisions of each ITD, a linear approximation method is proposed to transform the EDS-side RS subproblem into an easily-solved linear programming subproblem. Finally, a real-world IIoT experiment platform is built to evaluate the performance of the QDDM framework. The evaluation results demonstrate that the QDDM framework effectively increases the long-term system utility.  © 2018 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0794.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
