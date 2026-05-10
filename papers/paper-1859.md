---
id: paper-1859
title: 'Resource-Performance Trade-offs in Open-Source Large Language Models: A Comparative Analysis of Deployment Optimization and Lifecycle Management'
authors:
- Lin, Tingting
- Zheng, Zaoyi
venue: 2025 8th International Symposium on Big Data and Applied Statistics, ISBDAS 2025
venue_type: conference
year: 2025
doi: 10.1109/ISBDAS64762.2025.11117056
url: https://www.scopus.com/pages/publications/105016664088?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 55--60
keywords:
- Compliance
- Large Language Models
- Lifecycle Management
- Model Deployment
- Performance Tradeoffs
- Resource Optimization
- Resource Utilization Efficiency
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-1859 — Resource-Performance Trade-offs in Open-Source Large Language Models: A Comparative Analysis of Deployment Optimization and Lifecycle Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Organizations face significant challenges when deploying Large Language Models (LLMs) in production environments. High computational requirements and resource constraints are the main causes of these challenges, particularly in situations where optimizing resources is necessary. While recent studies primarily focused on training efficiency, deployment optimization, and lifecycle management have received limited attention. To address this gap, we introduce (1) A comprehensive framework to evaluate resource-performance trade-offs across deployment scenarios, as well as metrics like Resource Utilization Efficiency (RUE) and Lifecycle Impact Factor (LIF), and (2) A thorough analysis of four well-known 7B-parameter models in various production environments, from cloud to edge computing. This study provides useful insights for organizations that use open-source LLMs in resource-constrained environments. Our findings offer practical guidelines for organizations to enhance their deployment strategies while sustaining performance standards and regulatory compliance. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1859.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
