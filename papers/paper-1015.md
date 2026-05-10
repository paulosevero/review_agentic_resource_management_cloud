---
id: paper-1015
title: 'DCScaler: Spatiotemporal Prediction Aided Distributed Collaborative Autoscaling of Microservices'
authors:
- Li, Jiangming
- Li, Sen
- Tan, Jian
- Jin, Dong
- Chen, Shuangwu
- Yang, Jian
venue: Proceedings - 2024 IEEE 10th International Conference on Edge Computing and Scalable Cloud, EdgeCom 2024
venue_type: conference
year: 2024
doi: 10.1109/EdgeCom62867.2024.00015
url: https://www.scopus.com/pages/publications/85202444940?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 42--47
keywords:
- Autoscaling
- Deep Reinforcement Learning
- Microservices
- Spatiotemporal Prediction
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

# paper-1015 — DCScaler: Spatiotemporal Prediction Aided Distributed Collaborative Autoscaling of Microservices

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The autoscaling function dynamically adjusts the resource configuration of microservice applications in response to workload changes, thereby ensuring service quality. However, designing an effective scaling strategy for each service remains challenging due to the heterogeneity of services. To address this challenge, we introduce DCScaler, a distributed collaborative scaler that leverages spatiotemporal predictions to optimize Service Level Agreement (SLA) guarantess and resource utilization by proactive resource allocation adjustments. DCScaler adopts (i) a spatiotemporal graph attention network to learn the spatiotemporal dependencies among service metrics; (ii) a multi-agent Deep Reinforcement Learning (DRL) based scaler to learn the optimal scaling strategy tailored to each service. DCScaler accurately predicts future workloads and adjusts resource allocation accordingly for each service. Experimental results obtained in a real microservice environment demonstrate that DCScaler effectively enhances resource utilization and reduces SLA violations.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1015.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
