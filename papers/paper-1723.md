---
id: paper-1723
title: A Hybrid Mobile-Cloud Architecture for Intelligent Document Processing
authors:
- Kappassova, Sabina
- Maratova, Aray
venue: Procedia Computer Science
venue_type: conference
year: 2025
doi: 10.1016/j.procs.2025.10.262
url: https://www.scopus.com/pages/publications/105023982450?origin=resultslist
publisher: Elsevier B.V.
pages: 651--656
keywords:
- document classification
- hybrid document processing
- intelligent document processing
- mobile-cloud architecture
- mobile-first workflows
- optical character recognition
- semantic field extraction
- structured information extraction
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1723 — A Hybrid Mobile-Cloud Architecture for Intelligent Document Processing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile devices with high-resolution cameras and computational capabilities have become ubiquitous tools for document digitization. However, existing on-device OCR solutions primarily focus on text recognition, lacking the ability to capture document structure or extract semantic context. This paper introduces a hybrid mobile-cloud architecture for Intelligent Document Processing (IDP) that combines real-time on-device document capture with cloud-based OCR, document classification, and semantic information extraction. Smartphones function as intelligent sensing nodes, performing image enhancement, perspective correction, keyframe selection, and secure transmission to a cloud backend. The backend employs Transformer-based classifiers and multi-modal language models to extract structured data, including dates, financial amounts, and reference numbers, supporting multiple languages and document types. Experiments on real-world invoices demonstrate that the hybrid system reduces end-to-end processing time compared to cloud-only approaches while maintaining high extraction accuracy, even under variable network conditions. Video capture further enhances reliability by selecting optimal frames. The architecture also addresses practical enterprise needs, including data security, compliance, and integration with ERP, CRM, and document management systems. Future work will explore lightweight on-device semantic pre-processing, expanded document type support, and adaptive transmission strategies to improve efficiency and resilience in large-scale enterprise applications. © 2025 The Authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1723.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
