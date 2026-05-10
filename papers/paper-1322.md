---
id: paper-1322
title: Joint optimization of multi-dimensional resource allocation and task offloading for QoE enhancement in Cloud-Edge-End collaboration
authors:
- Zeng, Chao
- Wang, Xingwei
- Zeng, Rongfei
- Li, Ying
- Shi, Jianzhi
- Huang, Min
venue: Future Generation Computer Systems
venue_type: journal
year: 2024
doi: 10.1016/j.future.2024.01.025
url: https://www.scopus.com/pages/publications/85185310661?origin=resultslist
publisher: Elsevier B.V.
pages: 121--131
keywords:
- Cloud–edge–end collaboration
- Multi-agent reinforcement learning
- Quality of experience
- Resources allocation
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

# paper-1322 — Joint optimization of multi-dimensional resource allocation and task offloading for QoE enhancement in Cloud-Edge-End collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud-Edge-End Collaboration (CEEC) computing architecture inherits many merits from both edge computing and cloud computing and thus is considered as a promising candidate for future network services. In CEEC, user's QoE is impacted by offload performance which should consider offload strategy, computational resources and network status simultaneously. However, previous offload optimization studies neglect the joint consideration of dependent task offloading, computational resources and channel resources, which may not produce potential performance improvement. In this paper, we investigate the joint optimization of dependent task offloading, computational resource allocation, user transmission power control, and channel resource allocation in the CEEC scenario, with the goal of maximizing user's QoE. Initially, a new QoE metric is defined to capture the impacts of delay and energy consumption on user's QoE. Following this definition, we formulate the joint optimization problem as a Mixed Integer Nonlinear Programming (MINLP) problem and introduce a method of multi-agent deep reinforcement learning to solve our MINLP problem with high computation complexity. Extensive experiments are performed, and experimental results show that our proposed scheme outperforms baselines in a series of metrics. © 2024 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1322.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
