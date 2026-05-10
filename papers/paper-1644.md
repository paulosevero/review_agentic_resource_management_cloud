---
id: paper-1644
title: LLM-Based Adaptive Digital Twin Allocation for Microservice Workloads
authors:
- Henrique Sachete Garcia, Pedro
- de Souza Oribes, Ester
- Mangini Lopes, Ivan
- Marques de Souza, Braulio
- Nery Vieira Crestani, Angelo
- Francisco Lorenzon, Arthur
- Caggiani Luizelli, Marcelo
- Silas Severo De Souza, Paulo
- Rossi, Fábio Diniz
venue: International Conference on Cloud Computing and Services Science, CLOSER -
  Proceedings
venue_type: conference
year: 2025
doi: 10.5220/0013427300003950
url: https://www.scopus.com/pages/publications/105003534722?origin=resultslist
publisher: Science and Technology Publications, Lda
pages: 61--71
keywords:
- Cloud-Native Applications
- Digital Twins
- Large Language Models
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
  06-full-text-screening: pending
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
    - ovr_with_llm
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
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1644 — LLM-Based Adaptive Digital Twin Allocation for Microservice Workloads

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient resource allocation in programmable datacenters is a critical challenge due to the diverse and dynamic nature of workloads in cloud-native environments. Traditional methods often fall short in addressing the complexities of modern datacenters, such as inter-service dependencies, latency constraints, and optimal resource utilization. This paper introduces the Dynamic Intelligent Resource Allocation with Large Language Models and Digital Twins (DIRA-LDT) framework, a cutting-edge solution that combines real-time monitoring capabilities of Digital Twins with the predictive and reasoning strengths of Large Language Models (LLMs). DIRA-LDT systematically optimizes resource management by achieving high allocation accuracy, minimizing communication latency, and maximizing bandwidth utilization. By leveraging detailed real-time insights and intelligent decision-making, the framework ensures balanced resource distribution across the datacenter while meeting stringent performance requirements. Among the key results, DIRA-LDT achieves an allocation accuracy of 98.5%, an average latency reduction to 5.3 ms, and a bandwidth utilization of 82.4%, significantly outperforming heuristic-based, statistical, machine learning, and reinforcement learning approaches. Copyright © 2025 by SCITEPRESS - Science and Technology Publications, Lda.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_with_llm']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: llm_as_workload, pattern_id: ovr_with_llm, matched_substring: "with Large Language Models" }`
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
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
