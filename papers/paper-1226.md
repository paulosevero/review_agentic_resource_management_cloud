---
id: paper-1226
title: Evaluating DL Model Scaling Trade-Offs During Inference via an Empirical Benchmark Analysis
authors:
- Trihinas, Demetris
- Michael, Panagiotis
- Symeonides, Moysis
venue: Future Internet
venue_type: journal
year: 2024
doi: 10.3390/fi16120468
url: https://www.scopus.com/pages/publications/85213078925?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- artificial intelligence
- benchmarking
- cloud computing
- deep learning
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

# paper-1226 — Evaluating DL Model Scaling Trade-Offs During Inference via an Empirical Benchmark Analysis

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With generative Artificial Intelligence (AI) capturing public attention, the appetite of the technology sector for larger and more complex Deep Learning (DL) models is continuously growing. Traditionally, the focus in DL model development has been on scaling the neural network’s foundational structure to increase computational complexity and enhance the representational expressiveness of the model. However, with recent advancements in edge computing and 5G networks, DL models are now aggressively being deployed and utilized across the cloud–edge–IoT continuum for the realization of in situ intelligent IoT services. This paradigm shift introduces a growing need for AI practitioners, as a focus on inference costs, including latency, computational overhead, and energy efficiency, is long overdue. This work presents a benchmarking framework designed to assess DL model scaling across three key performance axes during model inference: classification accuracy, computational overhead, and latency. The framework’s utility is demonstrated through an empirical study involving various model structures and variants, as well as publicly available datasets for three popular DL use cases covering natural language understanding, object detection, and regression analysis. © 2024 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1226.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
