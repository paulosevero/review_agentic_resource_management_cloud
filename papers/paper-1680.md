---
id: paper-1680
title:
  "MicroIntent: Intent-Based Placement Strategy for Microservice Application
  in the Compute Continuum Using LLMs"
authors:
  - Islam, Koushikur
  - Da Cunha Rodrigues, Guilherme
  - Javadi, Bahman
  - Calheiros, Rodrigo N.
venue:
  Proceedings - 2025 IEEE International Conference on Smart Internet of Things,
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
    merge_reason: ""
status:
  04-title-screening: include
  05-abstract-screening: include
  06-full-text-screening: include
  07-taxonomy-development: classified
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification:
      C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
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
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied: []
    my_final_decision: "Include (Borderline)"
    my_justification: "Reanálise com critério mais flexível: MicroIntent usa LLM para fazer parsing de intents naturais em SLOs estruturados (Seção III-B); o placement generator determinístico (Seção III-C) consome essa saída para decidir microservice placement. Ou seja, quem toma a decisão ainda é uma heurística."
    agrees_with_regex: false
    divergence_reason:
      Regex 'agent_llm_based' é permissivo demais; exige agentic
      loop (perceive-reason-act autônomo). Aqui apenas fase 1 (parse) é LLM; fases
      2-3 (generate+deploy) não têm autonomous reasoning.
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Edge-Cloud
  decision:
    - Placement & Offloading
  agentic_configuration:
    decision_role: Pipeline Contributor
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
    - Knowledge Retrieval
  autonomy_level: Supervised
  metric:
    - RM Performance Metric
  evaluation_method: Simulation
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

- **my_final_decision:** Include (Borderline)
- **my_justification:** Reanálise com critério mais flexível: MicroIntent usa LLM para fazer parsing de intents naturais em SLOs estruturados (Seção III-B); o placement generator determinístico (Seção III-C) consome essa saída para decidir microservice placement. Ou seja, quem toma a decisão ainda é uma heurística.
- **agrees_with_regex:** False
- **divergence_reason:** Regex 'agent_llm_based' é permissivo demais; exige agentic loop (perceive-reason-act autônomo). Aqui apenas fase 1 (parse) é LLM; fases 2-3 (generate+deploy) não têm autonomous reasoning.
- **evidence_sections:** ['III. PROPOSED ARCHITECTURE', 'III-B. Intent Parser', 'III-C. Placement Generator', 'IV. EVALUATION']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                           | evidence                                                                                                                                                                               | location                        | rationale (neighbor not chosen)                                                                                                                                |
| ------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Edge-Cloud            | "an architecture that provides recommendations regarding microservices placement in the compute continuum based on high-level user intents"                                            | §I Introduction                 | Not `Cloud-Only` because the compute continuum (edge + cloud) is the explicit target.                                                                          |
| decision                                    | Placement & Offloading          | "an architecture for microservices placement decisions in the computing continuum utilizing high-level user intents described in natural language"                                     | §Abstract                       | _multi-select; choosing the node/layer hosting each service is placement; no scheduling, scaling, routing, or remediation actions._                            |
| agentic_configuration.decision_role         | Pipeline Contributor            | "The Intent Parser translates high-level, natural language intents to SLOs based on the available infrastructure description"                                                          | §III-B Intent Parser            | Not `Sole Decider` because the LLM extracts SLOs only; the SLO-Driven Node Matching Algorithm (Algorithm 1) generates the final placement.                     |
| agentic_configuration.coordination_topology | Single Agent                    | "The NLP Prompt Formulator is responsible for creating an LLM request from the OpenAI provided GPT-4 model."                                                                           | §IV Implementation              | Not `Multi-Agent` because one LLM instance handles the SLO extraction.                                                                                         |
| reasoning_approach                          | Prompting + Knowledge Retrieval | "The Intent Parser initially collects high-level user intents and augments this description with information about the compute continuum infrastructure. Then, it formulates a prompt" | §III-B Intent Parser            | _structured prompting + infrastructure-description augmentation (knowledge retrieval of the topology metadata); no iterative reflection loop, no fine-tuning._ |
| autonomy_level                              | Supervised                      | "MicroIntent, an architecture that provides recommendations regarding microservices placement"                                                                                         | §I Introduction                 | Not `Autonomous` because the system outputs placement recommendations consumed by an operator; deployment is not closed-loop.                                  |
| metric                                      | RM Performance Metric           | "single-point (bandwidth, queue depth, port-utilization, congestion-level) network metrics"                                                                                            | §IV-B Validation                | _single-select; SLO/network metrics on the RM side are reported; agent inference cost is not quantified._                                                      |
| evaluation_method                           | Simulation                      | "We present experiments conducted on a Minimum Viable Prototype (MVP) demonstrating the feasibility of the approach for placement strategy generation."                                | §I Introduction (contributions) | Not `Practical Testbed` because the validation uses an MVP processing JSON descriptions of synthetic infrastructure topologies.                                     |

**Confidence (weakest axis):** MED
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Placement & Offloading`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Supervised`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Edge-Cloud`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`, `Knowledge Retrieval`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Simulation`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`.
