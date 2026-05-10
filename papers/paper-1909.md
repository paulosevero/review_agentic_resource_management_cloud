---
id: paper-1909
title: An Enhanced Q-learning Algorithm for the Batch Production Scheduling Problem of Monocrystalline Silicon Rods
authors:
- Lu, Jin-You
- Hu, Rong
- Zhu, Yu-Hang
- Qian, Bin
- Jin, Huai-Ping
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-9901-8_25
url: https://www.scopus.com/pages/publications/105012244923?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 303--313
keywords:
- Batch planning
- Hybrid flow shop scheduling
- Monocrystalline silicon rods
- Q-learning
- Variable neighborhood search
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1909 — An Enhanced Q-learning Algorithm for the Batch Production Scheduling Problem of Monocrystalline Silicon Rods

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Monocrystalline silicon rods (MSR) are key materials in the semiconductor industry and are crucial for the development of information technology. Therefore, this paper addresses the integrated problem of MSR’s batch planning and hybrid flow shop scheduling problem with batch sequence dependent setup times (MSR_BPHFSP_BSDST), which is commonly encountered in monocrystalline silicon production activities. A mixed-integer programming model is established with the objective of minimizing the makespan. Since this problem is NP-hard, a novel Q-learning based variable neighborhood search (QVNS) algorithm is designed for solving it. Firstly, to tackle two highly coupled subproblems (i.e., the batch planning subproblem and the hybrid flow shop scheduling subproblem with batch sequence dependent setup times) within the MSR_BPHFSP_BSDST, the new encoding and decoding strategies are developed to decouple them. Subsequently, five efficient neighborhood search operators are designed for this problem. The Q-learning algorithm is employed to dynamically determine the execution order of search operations during the search process. This intelligent search mode can reduce ineffective search caused by randomly selecting neighborhood search operators in traditional VNS, and can execute deeper search within a limited time. Finally, the effectiveness of the proposed algorithm is validated through simulation experiments and comparisons with other algorithms. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1909.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
