---
id: paper-2744
title: 'ServLessSense: Serverless Smell Detection Tool'
authors:
- Perera, Hasini Sumalee
- Codabux, Zadia
- Palomba, Fabio
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-04403-7_3
url: https://www.scopus.com/pages/publications/105016155413?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 21--28
keywords:
- Code Smell Detection
- Refactoring
- Serverless Computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2744 — ServLessSense: Serverless Smell Detection Tool

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing has gained widespread adoption due to its scalability, cost-efficiency, and abstraction of infrastructure management. However, the shift toward event-driven, function-based architectures introduces new code quality challenges and development practices that differ from traditional paradigms. While recent research has identified serverless-specific bad practices commonly referred to as “smells,” there remains a lack of automated tools to support their detection and remediation. This paper presents ServLessSense, a tool designed to detect code smells automatically in serverless applications written in JavaScript and TypeScript. Built using a custom ESLint plugin, ServLessSense identifies five serverless-specific smells, provides visualizations through an interactive dashboard, and integrates Large Language Models to offer automated refactoring suggestions. We evaluated the precision and recall of the tool using five open-source serverless applications and conducted a pilot survey study to assess its potential usefulness from the practitioners’ perspective. The results indicate that ServLessSense is helpful in detecting serverless-specific smells and generating refactoring suggestions. The survey participants showed an overall favorable perspective towards ServLessSense. Tool & Data: https://doi.org/10.5281/zenodo.15477162 Demo Video: https://youtu.be/3WDCiqBpQ9c © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2744.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
