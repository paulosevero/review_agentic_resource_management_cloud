---
id: paper-1489
title: 'Multi-Dimensional Series Forecasting for Multi-Node Microservices: Leveraging Specialized Embedding in LLMs'
authors:
- Cheng, Lefan
- Ge, Jingguo
- Lv, Quanfeng
- Li, Tong
- Wu, Bingzhen
venue: Proceedings - 2025 27th IEEE International Conference on High Performance Computing and Communications, 11th IEEE International Conference on Data Science and Systems, 23rd IEEE International Conference
  on Smart City, 11th IEEE International Conference on Dependability in Sensor, Cloud, and Big Data Systems and Applications and 21st IEEE International Conference on Embedded Software and Systems, HPCC/DSS/SmartCity/DependSys/ICESS
  2025
venue_type: conference
year: 2025
doi: 10.1109/HPCC67675.2025.00030
url: https://www.scopus.com/pages/publications/105022738816?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 80--86
keywords:
- embedding
- fine-tuning
- large language model
- microservice
- time series forecast
- workloads prediction
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
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: LLaMA fine-tuned faz forecasting multi-dimensional para microsserviços; downstream tasks (resource allocation, fault prediction) mencionados como uso futuro, não fechados no paper.
      LLM como ferramenta de previsão sem ação de RM acoplada.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1489 — Multi-Dimensional Series Forecasting for Multi-Node Microservices: Leveraging Specialized Embedding in LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Currently, time series prediction in microservice systems suffers from inaccurate forecasts due to the complex interdependencies and highly dynamic workload characteristics. Traditional small-scale models struggle to understand the temporal patterns embedded within multi-dimensional metrics, leading to suboptimal performance. The advent of large language models (LLMs) offers a promising solution, as their powerful representation learning capabilities can effectively capture these complex temporal patterns. In this study, we propose a novel approach tailored for multi-dimensional time series forecasting in microservice environments. Our method leverages specialized embedding techniques that combine dynamic receptive field convolution and adaptive attention masks to capture temporal dependencies and feature relationships across multiple nodes. Additionally, we fine-tune a pre-trained LLaMA model to enhance its applicability for time series forecasting within microservice contexts. Experimental results demonstrate that our approach achieves higher prediction accuracy compared to baseline methods in different datasets. This research's achievements in time series forecasting provide new insights for downstream tasks such as resource allocation and fault prediction. © 2025 IEEE.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLaMA" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLaMA fine-tuned faz forecasting multi-dimensional para microsserviços; downstream tasks (resource allocation, fault prediction) mencionados como uso futuro, não fechados no paper. LLM como ferramenta de previsão sem ação de RM acoplada."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1489.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
