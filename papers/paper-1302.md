---
id: paper-1302
title: 'F3A: Fairness-Aware AI-Workloads Allocation Considering Multidimensional User Demands in JointCloud'
authors:
- Yang, Jiacheng
- Yi, Guodong
- Gao, Fei
- Shi, Peichang
- Wang, Huaimin
venue: Proceedings - 2024 IEEE International Conference on Joint Cloud Computing, JCC 2024
venue_type: conference
year: 2024
doi: 10.1109/JCC62314.2024.00015
url: https://www.scopus.com/pages/publications/85206810226?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 53--56
keywords:
- AI data center
- AI Workloads
- Fairness
- JointCloud Computing
- Task Scheduling
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

# paper-1302 — F3A: Fairness-Aware AI-Workloads Allocation Considering Multidimensional User Demands in JointCloud

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid growth of large language models, cloud computing has become an indispensable component of the AI industry. Cloud service providers(CSPs) are establishing AI data centers to service AI workloads. In the face of this surging need for AI computing power, building a connected computing environment across various clouds and forming a JointCloud presents an attractive solution. However, scheduling AI tasks across multiple AI data centers within a JointCloud environment presents a significant challenge: how to balance users' demands while ensuring CSPs' fairness in scheduling. Existing research primarily focuses on optimizing scheduling quality with limited consideration for fairness. Therefore, this paper proposes a Fairness-Aware AI-Workloads Allocation method (F3A), a fair cross-cloud allocation technique for AI tasks. F3A utilizes Point and Token to reflect both the resource status and historical task allocations of AI data centers, enabling the consideration of users' multidimensional demands and facilitating fair task allocation across multiple centers. In order to better assess the fairness of scheduling, we also devised a fairness indicator(FI), based on the Gini coefficient to measure the fairness of task allocation. The experimental results demonstrate that F3A consistently maintains FI within 0.1 across various cluster sizes and different task quantities, representing an improvement of 76.45% compared to classical fair scheduling algorithms round-robin. F3A exhibits commendable performance in ensuring fairness in task allocation while also demonstrating effectiveness in cost reduction and enhancing user satisfaction.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1302.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
