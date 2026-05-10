---
id: paper-2022
title: 'Streaming Intelligence: Securing, Scaling and Observing Cloud-Native Data Pipelines with LLMOps'
authors:
- Patel, Devarsh Hemantbhai
- Sharath, Manish Ravindra
- Jain, Sudhanshu
- Singh, Ramkinker
venue: 2025 IEEE 11th International Conference on Computing, Engineering and Design, ICCED 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.1109/ICCED68324.2025.11324471
url: https://www.scopus.com/pages/publications/105033038280?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- LLMOps
- Native Data Pipelines
- Observing Cloud
- Scaling
- Securing
- Streaming Intelligence
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    - ovr_with_llm
    - ovr_modifier_by_llm
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: Securing/scaling/observing pipelines cloud-native — observabilidade/segurança, não loop agentic de RM.
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

# paper-2022 — Streaming Intelligence: Securing, Scaling and Observing Cloud-Native Data Pipelines with LLMOps

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The intelligent automation, security, and observability have been propelled in the cloud-native environment by proliferation of real-time data pipelines. Traditional MLOps workflows are ideal to the execution of fixed training tasks, yet not ideal to the execution of continuous high-rate data streams. The paper suggests a unified Streaming Intelligence Framework (SIF) driven by Large Language Model Operations (LLMOps) to ensure, manage, and oversee end-to-end data streams. The architecture combines event-based architectures, anomaly detection that is fine-tuned with LLM and policy-aware observability that provide a reliable and adaptive data processing. Experimental validation in simulated Kafka-Kubernetes environments showed that the accuracy of anomaly detection was improved by 47 percent, the latency was reduced by 38 percent and the recovery time of security breach was six times faster than baseline data pipeline systems. The current work adds a volume blueprint to integrate the implementation of the intelligence of the LLMOps into cloud-native streaming systems with a focus on cross-layer observability, automation, and explainability.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_with_llm', 'ovr_modifier_by_llm', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_with_llm, matched_substring: "with LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_modifier_by_llm, matched_substring: "driven by Large Language" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "Large Language Model Operation" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Securing/scaling/observing pipelines cloud-native — observabilidade/segurança, não loop agentic de RM."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2022.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
