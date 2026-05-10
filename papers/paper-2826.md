---
id: paper-2826
title: 'Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability'
authors:
- Wang, Peng
- Qi, Kaiyuan
- Zhen, Feng
- Yan, Bingheng
- Guo, Tao
venue: 'Concurrency and Computation: Practice and Experience'
venue_type: journal
year: 2026
doi: 10.1002/cpe.70705
url: https://www.scopus.com/pages/publications/105035843575?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- cross-architecture code migration
- explainable software transformation
- large language models
- multi-ISA optimization
- QA-driven interaction
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-2826 — Interactive LLM-Driven Framework for Cross-Architecture Code Migration: Balancing Efficiency, Accuracy, and Explainability

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cross-architecture code migration has become essential as data centers transition from homogeneous x86 systems to heterogeneous “one-cloud, multi-chip” infrastructures that include ARM64, RISC-V, and domestic processors. Traditional approaches, such as manual refactoring and rule-based rewriting, face challenges in maintaining semantic correctness, scalability, and explainability. This paper presents an interactive, question-answering (QA)-driven framework that uses a frozen large language model (LLM) as a semantic reasoning engine. The framework combines static analysis, AST-based semantic-distance modeling, and a self-evolving rule base for validated transformations, ensuring transparency, explainability, and architecture-aware migration. It supports multiple languages (C++, Python, Java) and ISAs (x86, ARM64, RISC-V) without the need for fine-tuning the LLM. Evaluation on 30 real-world codebases shows an average migration accuracy of 92.4%, approaching expert-level performance (95.1%), with a 4.2× reduction in migration errors and significant reduction in developer time (from 20–25 h to 8 h). These results demonstrate that the QA-driven, LLM-based migration framework significantly improves efficiency, accuracy, and scalability. © 2026 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2826.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
