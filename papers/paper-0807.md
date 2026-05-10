---
id: paper-0807
title: Auxiliary-Task-Based Energy-Efficient Resource Orchestration in Mobile Edge Computing
authors:
- Zhu, Kaige
- Zhang, Zhenjiang
- Zhao, Mingxiong
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2023
doi: 10.1109/TGCN.2022.3201615
url: https://www.scopus.com/pages/publications/85137544302?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 313--327
keywords:
- Auxiliary task
- computation offloading
- deep reinforcement learning
- edge computing
- resource allocation
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

# paper-0807 — Auxiliary-Task-Based Energy-Efficient Resource Orchestration in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Advances in edge computing significantly impact the development of mobile networks. As the most important research goal related to edge networks, resource orchestration has been well studied in recent years; however, existing approaches based on deep reinforcement learning share similar bottlenecks in training inefficiency. In this paper, we treat drones, whose available time is significantly limited by their batteries, as the mobile terminals of a target edge network and aim to maximize the energy efficiency. The battery-constrained resource orchestration problem is formulated as a nonconvex optimization problem with consideration of both operating costs and available battery. Owing to the NP-hard nature of mixed-integer programming, the Auxiliary-Task-based dynamic Weighting Resource Orchestration (ATWRO) algorithm is proposed. To improve the sample efficiency, related parameters serving as auxiliary tasks are employed to provide additional gradient information. We further refine the exploration space and apply an alternative replay buffer to develop a customized reinforcement learning approach. Extensive experiments demonstrate the effectiveness of the proposed scheme, as they prove that by employing auxiliary tasks, reinforcement learning agents can be trained with higher efficiency. Moreover, the service time of the whole system can be prolonged, and a higher number of completed tasks can be guaranteed.  © 2023 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0807.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
