---
id: paper-0319
title: A Healthcare Resource Management Optimization Framework for ECG Biomedical Sensors
authors:
- Mutlag, Ammar Awad
- Ghani, Mohd Khanapi Abd
- Mohammed, Mazin Abed
venue: Internet of Things
venue_type: book-chapter
year: 2021
doi: 10.1007/978-3-030-66633-0_10
url: https://www.scopus.com/pages/publications/85114439122?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 229--244
keywords:
- Cloud computing
- Critical task
- Fog computing
- Healthcare
- Multi-agent systems
- Resource management
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

# paper-0319 — A Healthcare Resource Management Optimization Framework for ECG Biomedical Sensors

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Healthcare applications require a fast response because any delay in processing a task may affect a patient’s life. Cloud computing has an excellent contribution in healthcare application task processing and storing. However, for complex healthcare environment (critical task), cloud computing still faces many challenges especially in resource management. Fog computing has been proposed to overcome cloud computing limitations. Although fog computing has overcome cloud limitations, fog computing itself has some limitations in resource management such as fog devices’ processing and storage limitations. Therefore, to use these resources optimally, there is a need for a proper task scheduling strategy. In this study, a healthcare resource management optimization (HRMO) framework is proposed to mitigate the issue – fog computing as an intermediate layer has been implemented to overcome the limitation of cloud computing. The main duty of fog computing in this work is to process healthcare critical tasks by chain fog nodes through the implementation of multi-agent systems (MAS). In this study, three levels of processing are provided – edge, fog, and cloud – in which MAS has the main role to connect all processing levels. A deployment scenario of a smart home has been explained, and the expected result is shown. © 2021, The Author(s), under exclusive license to Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0319.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
