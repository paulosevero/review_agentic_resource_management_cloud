---
id: paper-1496
title: Investigating Neurosymbolic AI for Intent-based Service Management
authors:
  - Colombi, Lorenzo
  - Cavicchi, Sara
  - Poltronieri, Filippo
  - Tortonesi, Mauro
  - Stefanelli, Cesare
  - Varga, Pal
venue: "Proceedings of the 2025 21st International Conference on Network and Service Management: AI and Sustainability in the Future of Network and Service Management, CNSM 2025"
venue_type: conference
year: 2025
doi: 10.23919/CNSM67658.2025.11297547
url: https://www.scopus.com/pages/publications/105032150681?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ""
keywords:
  - Intent-based Service Management
  - Large Language Model
  - Neurosymbolic AI
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez Intent-Based e Neurosymbolic AI sejam indicativos que o artigo é interessante para a review (e.g., intent-based é comumente usado em conjunto com LLM-based agents, e Neurosymbolic AI pode usar LLMs por baixo dos panos).
    agrees_with_regex: false
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: "Include (Borderline)"
    my_justification: "LLM converte intents de usuário em representação estruturada (JSON) que alimenta o solver ASP (Clingo) responsável pela decisão de service management. Ou seja, quem toma a decisão é o Solver ASP, não o LLM."
    agrees_with_regex: true
    divergence_reason: "Categoria regex 'D_devops_or_logs_not_rm' é imprecisa. O paper NÃO é DevOps/logging (não há incident triage, log summarization, RCA, ou IaC). O padrão real é 'LLM-support-to-symbolic-solver': LLM faz intent translation (NL → JSON), ASP faz placement decisions. Classificação corrigida: H_llm_supports_other_method (suporte a método simbólico)."
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
  autonomy_level: Supervised
  metric:
    - RM Performance Metric
  evaluation_method: Simulation
---

# paper-1496 — Investigating Neurosymbolic AI for Intent-based Service Management

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing complexity and increasing demands of IT applications, especially in federated multi-cluster environments, pose significant challenges for service orchestration. To address these, Zero-Touch Service Management (ZSM) and intent-based management paradigms are gaining traction, allowing users to specify high-level goals rather than low-level configurations. However, current intent-driven approaches often rely on rigid Domain Specific Languages (DSLs) or graphic user interfaces, limiting expressiveness and usability. In this work, we propose a neurosymbolic intent-based platform that leverages Large Language Models (LLMs) for natural language intent ingestion and Answer Set Programming (ASP), a declarative programming paradigm used for solving complex combinatorial problems. The system translates natural language descriptions of microservice requirements into structured policies, enabling explainable service-to-cluster matching across federated Kubernetes environments. We validate our approach through experiments that evaluate both the syntactic correctness and efficiency of various LLMs in intent translation, as well as the computational time of the symbolic placement algorithm. © 2025 IFIP.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Talvez Intent-Based e Neurosymbolic AI sejam indicativos que o artigo é interessante para a review (e.g., intent-based é comumente usado em conjunto com LLM-based agents, e Neurosymbolic AI pode usar LLMs por baixo dos panos)."
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Neurosymbolic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "neurosymbolic" }`
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

- **regex_decision:** Exclude
- **regex_justification:** "Tarefa de DevOps/observabilidade (incident triage, RCA, geração de manifestos) — não é decisão de resource management."
- **winning_category:** 'D_devops_or_logs_not_rm'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "log analysis" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include (Borderline)
- **my_justification:** LLM converte intents de usuário em representação estruturada (JSON) que alimenta o solver ASP (Clingo) responsável pela decisão de service management. Ou seja, quem toma a decisão é o Solver ASP, não o LLM.
- **agrees_with_regex:** True
- **divergence_reason:** Categoria regex 'D_devops_or_logs_not_rm' é imprecisa. O paper NÃO é DevOps/logging (não há incident triage, log summarization, RCA, ou IaC). O padrão real é 'LLM-support-to-symbolic-solver': LLM faz intent translation (NL → JSON), ASP faz placement decisions. Classificação corrigida: H_llm_supports_other_method (suporte a método simbólico).

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                  | evidence                                                                                                                                                              | location                     | rationale (neighbor not chosen)                                                                                                                                                                |
| ------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Edge-Cloud   | "a unified API-driven infrastructure that spans cloud, edge, and fog layer, the so-called compute continuum"                                                          | §I Introduction              | Not `Cloud-Only` because the platform explicitly addresses federated multi-cluster Kubernetes across the compute continuum (cloud + edge + fog).                                               |
| decision                                    | Placement & Offloading | "automatically derive valid, explainable, and optimized service placements across many Kubernetes (K8s) clusters"                                                     | §I Introduction              | _multi-select; the system maps microservices to clusters (placement), with no scheduling, scaling, routing, or remediation actions._                                                           |
| agentic_configuration.decision_role         | Pipeline Contributor   | "the use of ASP and Clingo is limited to cluster filtering; thus, the output consists of a list of service placement solutions that satisfy the required constraints" | §III NeSy Solution           | Not `Sole Decider` because the LLM only translates natural-language intent to JSON; the placement decision is made by the symbolic Clingo/ASP solver.                                          |
| agentic_configuration.coordination_topology | Single Agent           | "both the ingestion and the translation components could be implemented using a single LLM"                                                                           | §III NeSy Solution           | Not `Multi-Agent` because a single LLM does ingestion + translation; ASP solver is not an agent in the agentic sense.                                                                          |
| reasoning_approach                          | Prompting              | "we prompted the LLMs with natural language inputs alongside a predefined JSON template and a series of illustrative examples"                                        | §IV-A LLM Intent Translation | _one-shot / few-shot prompting with template schema; no iterative self-reflection, no retrieval over external KB, no fine-tuning._                                                             |
| autonomy_level                              | Supervised             | "In case of ambiguity, the user is asked to provide the missing details necessary for a correct translation."                                                         | §III NeSy Solution           | Not `Autonomous` because the pipeline expects user interaction whenever the intent is unclear or the JSON fails validation.                                                                    |
| metric                                      | RM Performance Metric  | "we measured the execution time of Clingo, an ASP solver, to compute all possible stable models, or, in other words, the service-to-cluster matching solutions"       | §IV-B ASP experiments        | _single-select reported here; RM-side computation time of the placement solver is reported, alongside LLM accuracy/latency in §IV-A, but the locked classification keeps only RM Performance._ |
| evaluation_method                           | Simulation             | "We randomly generated a series of clusters and services with their respective constraints using Python and the Clingo Python module."                                | §IV-B ASP experiments        | Not `Practical Testbed` because clusters and services are randomly generated synthetic scenarios, not measurements on a deployed federation.                                                        |

**Confidence (weakest axis):** MED
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Placement & Offloading`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Supervised`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Edge-Cloud`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Simulation`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Pipeline Contributor`.
- `agentic-config-cross` (anchor: `RQ1.1`) — contributes: `Pipeline Contributor` × `Single Agent`.
- `infrastructure-by-decision` (anchor: `RQ1.2`) — contributes: `Placement & Offloading` × `Edge-Cloud`.
- `decision-by-autonomy` (anchor: `RQ2.2`) — contributes: `Placement & Offloading` × `Supervised`.
- `reasoning-by-decision` (anchor: `RQ3.1`) — contributes: `Prompting` × `Placement & Offloading`.
- `evaluation-by-decision` (anchor: `RQ4.1`) — contributes: `Placement & Offloading` × `Simulation`.
- `metric-by-autonomy` (anchor: `RQ4.4`) — contributes: `RM Performance Metric` × `Supervised`.
- `reasoning-temporal` (anchor: `RQ3.1`) — contributes: `2025` × `Prompting`.
