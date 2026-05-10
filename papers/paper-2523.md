---
id: paper-2523
title: Evaluating correctness, performance and energy footprint of semantic reasoners in mobile edge computing
authors:
- Bilenchi, Ivano
- Loconte, Davide
- Scioscia, Floriano
- Ruta, Michele
venue: Journal of Systems and Software
venue_type: journal
year: 2026
doi: 10.1016/j.jss.2025.112696
url: https://www.scopus.com/pages/publications/105022430978?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- Automated reasoning
- Energy-aware computing
- Mobile edge computing
- Performance evaluation
- Semantic web
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2523 — Evaluating correctness, performance and energy footprint of semantic reasoners in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The integration of Semantic Web technologies into Mobile Edge Computing (MEC) platforms is enhancing the capabilities of real-time, context-aware applications across diverse domains. MEC brings processing closer to the network edge, reducing latency and allowing for the improvement of data privacy, while Semantic Web technologies provide machine-interpretable knowledge representation and reasoning capabilities. Despite their potential, deploying semantic reasoners on edge devices is challenging due to their resource-intensive nature, which requires significant memory availability, computational power, and energy. Furthermore, correctness, performance and energy consumption are simultaneously important, as MEC semantics-based applications often call for real-time queries for autonomous agent decision or user-oriented decision support. This paper presents an extensive experimental evaluation of Web Ontology Language (OWL) reasoners deployed in MEC environments, assessing correctness, processing time, memory usage, and energy consumption across both a reference tablet and a single-board computer. For energy measurement, both software profiling and hardware monitoring have been exploited and compared. The study is supported by a modular, cross-platform benchmarking framework that automates data collection and ensures reproducibility. The findings highlight the trade-offs between reasoning capabilities and resource consumption, offering valuable insights for refining testing methodologies as well as optimizing semantic reasoners in MEC settings. © 2025 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2523.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
