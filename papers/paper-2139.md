---
id: paper-2139
title: Automated High-Level Code Optimization for Warehouse Performance
authors:
- Shypula, Alexander
- Madaan, Aman
- Zeng, Yimeng
- Alon, Uri
- Gardner, Jacob
- Hashemi, Milad
- Neubig, Graham
- Ranganathan, Parthasarathy
- Bastani, Osbert
- Yazdanbakhsh, Amir
venue: IEEE Micro
venue_type: journal
year: 2025
doi: 10.1109/MM.2025.3590033
url: https://www.scopus.com/pages/publications/105011157266?origin=resultslist
publisher: IEEE Computer Society
pages: 60--71
keywords:
- Artificial intelligence
- C++ (programming language)
- Computer architecture
- Optimization
- Semantics
- Statistical tests
- Warehouses
- Architecture research
- Code optimization
- Code semantics
- Moore Law
- Optimisations
- Optimizing programs
- Performance
- Program performance
- Source optimization
- Warehouse performance
- Codes (symbols)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)
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

# paper-2139 — Automated High-Level Code Optimization for Warehouse Performance

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the twilight of Moore’s law, optimizing program performance has emerged as a central focus in computer architecture research. Yet, high-level source optimization remains challenging due to the intricate nature of understanding code semantics. Our approach unifies machine learning techniques with established insights and tools from computer architecture to tackle the inherent challenges of high-level optimization. In this work, we introduce a framework that harnesses large language models (LLMs) for high-level program optimization. We curate a dataset of competitive C++ submissions, each accompanied by extensive unit tests to capture performance-improving patterns. To mitigate the variability of performance measurements, we develop an evaluation harness using the gem5 full-system simulator. Our results show a mean speedup of 6.86, outperforming the average human optimization of 3.66×. We also give an overview of subsequent work in this space, describing how LLM-driven optimization enables autonomously applying performance-improving edits across billions of lines of code in Google data centers. © 1981-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2139.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
