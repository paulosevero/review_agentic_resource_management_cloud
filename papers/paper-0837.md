---
id: paper-0837
title: 'Optimizing Cloud Infrastructure Management Using Large Language Models: A
  DevOps Perspective'
authors:
- Bokkena, Bhargava
venue: 2nd International Conference on Self Sustainable Artificial Intelligence Systems,
  ICSSAS 2024 - Proceedings
venue_type: conference
year: 2024
doi: 10.1109/ICSSAS64001.2024.10760725
url: https://www.scopus.com/pages/publications/85213373171?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1401--1406
keywords:
- Cloud Infrastructure Management
- DevOps
- Large language models (LLMs)
- Predictive Analytics
- Resource Allocation
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
  05-abstract-screening: include
  06-full-text-screening: exclude
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_using_llm
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: Paper sobre DevOpsBERT, um modelo BERT adaptado para tarefas
      DevOps (anomaly detection, predictive maintenance em logs). O LLM não dirige
      decisões de resource management (scheduling, placement, scaling) — a aplicação
      é log analysis e incident prediction, não orquestração autônoma de recursos.
      Fora do escopo agentic-AI-for-RM.
    agrees_with_regex: false
    divergence_reason: Regex sugeriu Include (ovr_using_llm, ovr_abs_llm_orchestrates),
      mas fulltext mostra LLM isolado em tarefas de observabilidade (DevOps), não
      loop agentic dirigindo RM.
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-0837 — Optimizing Cloud Infrastructure Management Using Large Language Models: A DevOps Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Traditional methods often struggle to keep pace with the dynamic nature of cloud resources, necessitating more intelligent and adaptable solutions. This study proposes the integration of large language models (LLMs) into cloud infrastructure management, providing a novel perspective on automating and optimizing DevOps tasks. Our research primarily focuses on enhancing predictive maintenance, resource allocation, and system scalability through the deployment of LLMs.The methodology hinges on the adaptation of LLMs to interpret and respond to cloud management tasks, including real-time decision-making and predictive analytics. Using the Google Cluster Usage traces as a dataset, which details job and task usage across compute clusters, we model various scenarios pertinent to load balancing and system failures. The experiments are designed to measure the impact of LLMs on key performance metrics such as downtime reduction, resource utilization, and operational costs.Preliminary results indicate that LLMs can significantly improve the predictive accuracy of system anomalies and optimize resource allocation. The models demonstrate robustness in managing complex cloud environments, leading to notable enhancements in infrastructure efficiency and reliability. This study not only validates the feasibility of using LLMs for cloud management tasks but also highlights their potential to transform traditional DevOps practices. Further discussions in this paper explore the practical implications of our findings, address the limitations of current approaches, and propose directions for future research. This research contributes to the burgeoning field of AI in cloud computing, offering insights that could lead to more sustainable and scalable cloud management solutions. © 2024 IEEE.

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
- **agrees_with_regex:** True
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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_using_llm', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of Large Language Models (LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Paper sobre DevOpsBERT, um modelo BERT adaptado para tarefas DevOps (anomaly detection, predictive maintenance em logs). O LLM não dirige decisões de resource management (scheduling, placement, scaling) — a aplicação é log analysis e incident prediction, não orquestração autônoma de recursos. Fora do escopo agentic-AI-for-RM.
- **agrees_with_regex:** False
- **divergence_reason:** Regex sugeriu Include (ovr_using_llm, ovr_abs_llm_orchestrates), mas fulltext mostra LLM isolado em tarefas de observabilidade (DevOps), não loop agentic dirigindo RM.
- **evidence_sections:** ['DevOpsBERT functionality', 'Section III (LLM architecture for log analysis)', 'Section V (conclusion: DevOps perspective)']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
