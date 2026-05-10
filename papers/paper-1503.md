---
id: paper-1503
title: 'Resource Management for GPT-Based Model Deployed on Clouds: Challenges, Solutions, and Future Directions'
authors:
- Dang, Yongkang
- He, Yiyuan
- Xu, Minxian
- Ye, Kejiang
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-1528-5_7
url: https://www.scopus.com/pages/publications/85218935580?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 95--105
keywords:
- Cloud Computing
- GPT-based Models
- Resource Management Framework
- Task Profiling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-1503 — Resource Management for GPT-Based Model Deployed on Clouds: Challenges, Solutions, and Future Directions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The widespread adoption of large language models (LLMs), such as the Generative Pre-trained Transformer (GPT), on cloud computing platforms (e.g., Azure) has resulted in a substantial increase in resource demand. This increase poses significant challenges for resource management within cloud environments. This paper aims to highlight these challenges by initially delineating the unique characteristics of resource management for GPT-based models. Subsequently, we analyze the specific challenges faced by resource management when applied to GPT-based models deployed on cloud platforms, and we propose algorithms for resource profiling and prediction concerning inference requests. To facilitate effective resource management, we present a comprehensive resource management framework that includes resource profiling and forecasting methodologies specifically designed for GPT-based models. Additionally, we discuss the future directions for resource management in the context of GPT-based models, emphasizing potential areas for further exploration and improvement. Through this analysis, we aim to provide valuable insights into resource management for GPT-based models deployed in cloud environments. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1503.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
