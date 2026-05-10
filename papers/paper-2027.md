---
id: paper-2027
title: Leveraging Large Language Models for Anomaly Detection in Microservices Architectures
authors:
- Pedroso, Diego Frazatto
- Almeida, Luís
- Alves Aisawa, William Akihiro
- Dutra, Inês
- Bruschi, Sarita Mazzini
venue: Proceedings - 2025 IEEE/SBC 37th International Symposium on Computer Architecture and High Performance Computing Workshops, SBAC-PADW 2025
venue_type: conference
year: 2025
doi: 10.1109/SBAC-PADW69789.2025.00021
url: https://www.scopus.com/pages/publications/105030538765?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 92--99
keywords:
- Anomaly Detection
- AWS
- LLM
- Microservices
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
    - ovr_leveraging_llm
    my_final_decision: Exclude
    my_justification: LLM para detecção de anomalias em microsserviços — monitoramento/análise, sem loop fechado de RM (Boundary B).
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

# paper-2027 — Leveraging Large Language Models for Anomaly Detection in Microservices Architectures

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —Cloud computing has become a key enabler of scalable and high-performance applications, allowing systems to be deployed rapidly. At the same time, the increasing sophistication of cloud-native environments brings new challenges related to system dependability. Ensuring resilience under such conditions is a fundamental responsibility of IT providers, who must safeguard service continuity and operational stability. The widespread use of microservice-based designs has created an ecosystem with a growing number of interacting components, including frameworks, application layers, hypervisors, and orchestration platforms. This distributed and layered environment produces a massive volume of log data originating from heterogeneous sources. Without automated support, extracting useful insights from these logs becomes a highly complex task. One promising direction to mitigate this challenge is the use of Machine Learning, particularly methods grounded in Large Language Models (LLMs), which can dynamically detect recurring structures and anomalies in event streams. Building on this idea, our work introduces an anomaly detection framework deployed within a microservices environment running on Kubernetes with Istio. The framework integrates an LLM trained on a diverse set of fault scenarios. To create these scenarios, we relied on Chaos Mesh for fault injection and Locust for workload stress testing. The evaluation confirmed that the model achieved high accuracy in identifying anomalies. It consistently detected all injected faults, although a small number of false positives were observed. Importantly, these false alarms remained at acceptable levels, highlighting the approach’s practical applicability. ©2025 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_leveraging_llm']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_leveraging_llm, matched_substring: "Leveraging Large Language" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM para detecção de anomalias em microsserviços — monitoramento/análise, sem loop fechado de RM (Boundary B)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2027.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
