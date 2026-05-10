---
id: paper-1215
title: 'CarbonOracle: Automating Energy Mix & Renewable Energy Source Forecast Modeling for Carbon-Aware Micro Data Centers'
authors:
- Symeonides, Moysis
- Tsiopani, Nicoletta
- Maouris, Georgios
- Trihinas, Demetris
- Pallis, George
- Dikaiakos, Marios D.
venue: Proceedings - 2024 IEEE/ACM 17th International Conference on Utility and Cloud Computing, UCC 2024
venue_type: conference
year: 2024
doi: 10.1109/UCC63386.2024.00042
url: https://www.scopus.com/pages/publications/105004728120?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 246--255
keywords:
- Data centers
- Energy Modeling
- Machine Learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1215 — CarbonOracle: Automating Energy Mix & Renewable Energy Source Forecast Modeling for Carbon-Aware Micro Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Geo-distributed data centers (DCs) have a substantial impact on global electricity consumption and carbon emissions, with their energy demands expected to increase alongside emerging technologies such as Generative Artificial Intelligence (GenAI) and Natural Language Understanding (NLU). In response to environmental and operational concerns, major cloud providers are investing in DC infrastructures powered by renewable energy sources (RES). However, the design and management of energy-efficient data centers present new challenges. Current forecasting models for RES production and electricity grid energy mix are often limited in accuracy and forecasting horizon, hindering carbon-aware service management. To tackle these challenges, we introduce CarbonOracle, a Machine Learning (ML) service that automates data extraction from self-hosted RES, energy grids, and weather APIs, while also simplifying the ML training and forecast of RES production and electricity grid carbon emissions. Its application programming interface serves ML-based forecasts for RES production (e.g., solar, wind) and energy mix metrics, designed to support carbon-aware deployments, enabling integration with container schedulers and other applications. Through a comprehensive evaluation over a real data center testbed, our results show that CarbonOracle has an error rate of approximately 9% for forecasts related to self-hosted photovoltaic (PV) panels, while its forecasts for electricity grid carbon emissions have an error rate of less than 4%. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1215.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
