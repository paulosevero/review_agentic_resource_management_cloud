---
id: paper-1521
title: Strategies for Flow-Based Deployment and Orchestration in Cloud-Edge Interactive Computing
authors:
- Di Martino, Beniamino
- D’Angelo, Salvatore
- Pezzullo, Gennaro Junior
- Esposito, Antonio
- Spinatelli, Gianmarco
- Polzella, Francesco
- Carollo, Andrea
- Corridori, Giacomo
venue: Lecture Notes on Data Engineering and Communications Technologies
venue_type: book-chapter
year: 2025
doi: 10.1007/978-3-031-87778-0_39
url: https://www.scopus.com/pages/publications/105002966515?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 400--407
keywords:
- Edge computing
- Interactive computer systems
- Program compilers
- Code annotation
- Computing platform
- Distributed environments
- Flow based
- Heterogeneous environments
- Interactive computing
- Modified kernels
- Preliminary analysis
- Toward integration
- Work-flows
- Cloud platforms
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

# paper-1521 — Strategies for Flow-Based Deployment and Orchestration in Cloud-Edge Interactive Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper is intended as a preliminary analysis for defining and orchestrating workflows in a Cloud Continuum (CC) environment. Starting from an analysis of interactive computing platforms, in particular some modified kernels of Jupyter Notebook for executing code in heterogeneous and distributed environments, it moves towards integration with a source-to-source compiler based on code decomposition and annotation for parallelization and automatic distribution through templates. Finally, integration with tools for defining and executing workflows in heterogeneous environments is discussed. Within the project and in the paper, several different approaches are presented to integrate the two techniques at different levels (from notebook to modified kernel). The aim is to facilitate the definition and execution of workflows for fine-tuning basic artificial intelligence models and large language models. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1521.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
