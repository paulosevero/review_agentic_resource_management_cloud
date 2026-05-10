---
id: paper-1782
title: 'ATPSO: Adaptive Task Priority Scheduling and Offloading Optimization Scheme for vehicles in harsh environments'
authors:
- Li, Xiguang
- Zhao, Yuchen
- Sun, Yunhe
- Muthanna, Ammar
- Hawbani, Ammar
- Zhao, Liang
venue: Ad Hoc Networks
venue_type: journal
year: 2025
doi: 10.1016/j.adhoc.2025.103861
url: https://www.scopus.com/pages/publications/105003580361?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Scheduling algorithms
- Task offloading resource allocation
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

# paper-1782 — ATPSO: Adaptive Task Priority Scheduling and Offloading Optimization Scheme for vehicles in harsh environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In harsh environments, vehicle driving risks significantly increase. Safety enhancing applications can mitigate these risks, but can also introduce delay-sensitive and computationally intensive tasks that challenge vehicle data processing and communication. This paper proposes an Adaptive Task Priority Scheduling and Offloading Optimization Scheme (ATPSO) based on the Vehicular Edge Computing (VEC) paradigm to improve Quality of Service (QoS) for safety tasks. Firstly, a multifactor prioritization mechanism using environment awareness is developed, leveraging SHapley Additive ExPlanations (SHAP) and XGBoost models to quantify safety priorities from real-time data and assess vehicle risks. A Transformer model dynamically adjusts priority weights to minimize risk. Secondly, the local queue stability problem is addressed as a Lyapunov optimization problem, proposing a multi-queue priority scheduling and distributed resource allocation scheme. Lastly, a Markov Decision Process (MDP) model is constructed to handle dynamic computational offloading, and the Entropy-Enhanced Multi-Agent Soft Actor–Critic (EE-MASAC) algorithm is introduced to optimize offloading strategies and resource allocation. Simulation results demonstrate that ATPSO effectively reduces safety task delays, improves task completion rates, and lowers vehicle risk scores, outperforming existing methods in adaptability and performance, offering a solid foundation for practical deployment of vehicle safety applications. © 2025

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1782.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
