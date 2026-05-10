---
id: paper-2240
title: 'Enriching Clickstream Analytics with Generative AI: A Scalable Serverless Architecture for Real-Time Session Intelligence'
authors:
- Venkatesan, Vivek
- Arunachalam, Chakkaravarthy
- Kanji, Rajesh Kumar
venue: 'AI-SI 2025 - IEEE International Conference on Artificial Intelligence for Sustainable Innovation: Shaping the Future with Intelligent Solutions'
venue_type: conference
year: 2025
doi: 10.1109/AI-SI66213.2025.11341394
url: https://www.scopus.com/pages/publications/105033359631?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Adobe Analytics
- AWS Glue
- behavioral intelligence
- clickstream analytics
- cloud computing
- data engineering
- generative AI
- large language models
- real-time inference
- serverless architecture
- user session enrichment
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2240 — Enriching Clickstream Analytics with Generative AI: A Scalable Serverless Architecture for Real-Time Session Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Understanding user behavior through clickstream data is essential for optimizing digital experiences and conversion funnels. Traditional session analysis methods rely on static rules or manual reconstruction, which are time-consuming and hard to scale. This paper presents a scalable, serverless architecture that integrates generative AI to extract session-level intent and behavioral summaries from Adobe Analytics data. The system combines AWS Glue for aggregation, AWS Lambda for orchestration, and Claude via AWS Bedrock for large language model inference. Deployed in a Fortune 500 financial enterprise, it processes over 200,000 sessions daily, achieving 87% precision in manual validation, subsecond inference latency, and a 40% reduction in enrichment costs through prompt optimization. Unlike prior approaches, this work uniquely delivers real-time, AI-enriched session intelligence using prompt-based reasoning within a cost-efficient, cloud-native pipeline. The enriched data significantly enhance analyst workflows by automating narrative generation, improving segmentation, and enabling intent-aware dashboards. This architecture establishes a blueprint for modern behavioral analytics that combines scalability, interpretability, and operational efficiency. ©2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2240.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
