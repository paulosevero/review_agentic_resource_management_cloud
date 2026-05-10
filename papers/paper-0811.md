---
id: paper-0811
title: 'Evergreen: Comprehensive Carbon Model for Performance-Emission Tradeoffs'
authors:
- Adem, Tersiteab
- Mccrabb, Andrew
- Goyal, Vidushi
- Bertacco, Valeria
venue: Proceedings - 2024 IEEE International Symposium on Workload Characterization, IISWC 2024
venue_type: conference
year: 2024
doi: 10.1109/IISWC63097.2024.00021
url: https://www.scopus.com/pages/publications/85214578526?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 132--143
keywords:
- Carbon Emissions
- Computing Emissions
- Data Centers
- Sustainable Computing
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

# paper-0811 — Evergreen: Comprehensive Carbon Model for Performance-Emission Tradeoffs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The pervasive proliferation of computing infrastructure in recent decades has led to an increase in the fraction of worldwide energy and greenhouse gas (GHG) emissions associated with computing. A further steep increase is projected for the future, especially in light of the computational demands of large language models. While computing research has traditionally focused on performance, power, and area optimization, climate change concerns demand that the carbon footprint (CF) associated with computation be raised to a primary design parameter on par with power, performance, and area.To address this need, we propose Evergreen, a framework that augments computing tradeoffs with emission metrics. Evergreen offers the first complete carbon model for computing emission analysis, taking into account all major sources contributing to the carbon emissions associated with the execution of an application in a data center. The Evergreen carbon model considers both operational and embodied emissions associated with the computing hardware executing the application, the data transmission infrastructure, the renewable energy sources, and the battery energy storage systems. Using this model, our framework provides both an emissions predictor and a user-driven, emission-aware scheduler. The Evergreen scheduler allows users to select the data center to execute their workloads based on emissions and performance constraints associated with their execution in a cloud environment. Our evaluation shows how, for a given workload, Evergreen can provide multiple Pareto-optimal solutions in the performance-emission domain. Depending on the power source and data center values, Evergreen can identify carbon-optimal solutions that offer emission reduction with minimal latency overhead.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0811.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
