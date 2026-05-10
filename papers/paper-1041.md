---
id: paper-1041
title: 'Two-Stage Offloading for an Enhancing Distributed Vehicular Edge Computing and Networks: Model and Algorithm'
authors:
- Li, Xuehan
- Jing, Tao
- Wang, Xiaoxuan
- Han, Dengyu
- Fan, Xin
- Dong, Honghui
- Li, Xiangyu
- Richard Yu, Fei
venue: IEEE Transactions on Intelligent Transportation Systems
venue_type: journal
year: 2024
doi: 10.1109/TITS.2024.3424852
url: https://www.scopus.com/pages/publications/85208735125?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 17744--17761
keywords:
- computation offloading
- Lyapunov optimization
- MADDPG
- peer offloading
- Vehicular edge computing and networks
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

# paper-1041 — Two-Stage Offloading for an Enhancing Distributed Vehicular Edge Computing and Networks: Model and Algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing and Networks (VECoNs) have gained popularity for its enhanced Internet of Vehicles (IoV) capabilities. To satisfy the needs of delay-sensitive and computation-intensive in-vehicle applications, VECoNs need to provide low-latency task offloading services. However, existing offloading frameworks generally overlook the spatially and temporally heterogeneous computation task arrival patterns. The former causes overloading and underloading of RSU computational resources and thus hinders further reduction of offloading latency on the macro-scale, while the latter emphasizes the importance of long-term system performance, especially energy constraints, posing challenges to the design of offloading framework and optimization strategies. This paper introduces a novel distributed two-stage task offloading architecture based on Lyapunov and multi-agent deep deterministic policy gradient (MADDPG). On one hand, it jointly optimizes the initial offloading stage within VEC subsystems and the RSU peer offloading stage to minimize offloading delays for each VEC subsystem. On the other hand, it incorporates RSU energy consumption within long-term constraints to formulate the offloading optimization problem. After decoupling the energy coupling between RSU time slots using the Lyapunov algorithm, a Lyapunov and MADDPG-based distributed task offloading (LAMETO) algorithm is presented to solve the optimal problem in a distributed manner. Simulation results show that the proposed framework and algorithm can reduce the system delay, energy consumption, and energy deficit while stabilizing convergence.  © 2000-2011 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1041.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
