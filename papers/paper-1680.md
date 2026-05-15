---
id: paper-1680
title: 'MicroIntent: Intent-Based Placement Strategy for Microservice Application
  in the Compute Continuum Using LLMs'
authors:
- Islam, Koushikur
- Da Cunha Rodrigues, Guilherme
- Javadi, Bahman
- Calheiros, Rodrigo N.
venue: Proceedings - 2025 IEEE International Conference on Smart Internet of Things,
  SmartIoT 2025
venue_type: conference
year: 2025
doi: 10.1109/SmartIoT66867.2025.00026
url: https://www.scopus.com/pages/publications/105032178663?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 124--131
keywords:
- Application placement
- Compute continuum
- Intent-based networking
- Large language models
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
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource
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
    - ovr_using_llm
    - ovr_cls_llm_present
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
    my_final_decision: Include
    my_justification: "Reanálise com critério mais flexível: MicroIntent usa LLM para fazer parsing de intents naturais em SLOs estruturados (Seção III-B); o placement generator determinístico (Seção III-C) consome essa saída para decidir microservice placement. Padrão idêntico ao anchor paper-1644 — LLM em papel material de pre-processing semântico para RM em edge. Inclusão."
    agrees_with_regex: false
    divergence_reason: Regex 'agent_llm_based' é permissivo demais; exige agentic
      loop (perceive-reason-act autônomo). Aqui apenas fase 1 (parse) é LLM; fases
      2-3 (generate+deploy) não têm autonomous reasoning.
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1680 — MicroIntent: Intent-Based Placement Strategy for Microservice Application in the Compute Continuum Using LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The placement of microservices in the compute continuum plays a vital role in delivering services that comply with customers' needs, such as reduced latency, storage requirements, quality of service and availability. To achieve customers' needs in the geographically dispersed architecture of the compute continuum, Service Level Objectives (SLOs) have been largely used in decision-making to place microservices. However, because low-level SLOs increase the barrier to entry for continuum users, placement decisions based on high-level business vocabulary are required if the compute continuum is to be adopted at scale. This paper proposes an architecture for microservices placement decisions in the computing continuum utilizing highlevel user intents described in natural language as input. The approach utilizes Generative Artificial Intelligence to translate the intents to low-level SLOs, which are used along with the infrastructure description to decide where different microservices that compose an application must be deployed so that SLOs are met. We implement and evaluate a prototype of the architecture to demonstrate the approach's feasibility. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_using_llm', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-Based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: llm_as_workload, pattern_id: ovr_using_llm, matched_substring: "Using LLMs" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Intent-Based" }`
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
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLM" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Reanálise com critério mais flexível: MicroIntent usa LLM para fazer parsing de intents naturais em SLOs estruturados (Seção III-B); o placement generator determinístico (Seção III-C) consome essa saída para decidir microservice placement. Padrão idêntico ao anchor paper-1644 — LLM em papel material de pre-processing semântico para RM em edge. Inclusão.
- **agrees_with_regex:** False
- **divergence_reason:** Regex 'agent_llm_based' é permissivo demais; exige agentic loop (perceive-reason-act autônomo). Aqui apenas fase 1 (parse) é LLM; fases 2-3 (generate+deploy) não têm autonomous reasoning.
- **evidence_sections:** ['III. PROPOSED ARCHITECTURE', 'III-B. Intent Parser', 'III-C. Placement Generator', 'IV. EVALUATION']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
