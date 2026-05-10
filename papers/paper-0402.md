---
id: paper-0402
title: Application of Profile Prediction for Proactive Scheduling; [Previsão de Perfis de Aplicações para Escalonamento Proativo]
authors:
- Dos Santos, Allan Matheus Marques
- Pinto, Raquel Coelho Gomes
- Duarte, Julio Cesar
- Schulze, Bruno Richard
venue: Revista de Informatica Teorica e Aplicada
venue_type: journal
year: 2022
doi: 10.22456/2175-2745.120399
url: https://www.scopus.com/pages/publications/85145024043?origin=resultslist
publisher: Federal University of Rio Grande do Sul, Institute of Informatics
pages: 65--75
keywords:
- application profile
- cloud computing
- intelligent agents
- scheduling
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

# paper-0402 — Application of Profile Prediction for Proactive Scheduling; [Previsão de Perfis de Aplicações para Escalonamento Proativo]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Today, cloud environments are widely used as execution platforms for most applications. In these environments, virtualized applications often share computing resources. Although this increases hardware utilization, resources competition can cause performance degradation, and knowing which applications can run on the same host without causing too much interference is key to a better scheduling and performance. Therefore, it is important to predict the resource consumption profile of applications in their subsequent iterations. This work evaluates the use of machine learning techniques to predict the increase or decrease in computational resources consumption. The prediction models are evaluated through experiments using real and benchmark applications. Finally, we conclude that some models offer significantly better performance when compared to the current trend of resource usage. These models averaged up to 94% on the F<sub>1</sub> metric for this task. © 2022, Federal University of Rio Grande do Sul, Institute of Informatics. All rights reserved.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0402.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
