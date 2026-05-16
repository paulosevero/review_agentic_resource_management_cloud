---
id: paper-1947
title:
  On Combining XAI and LLMs for Trustworthy Zero-Touch Network and Service Management
  in 6G
authors:
  - Mekrache, Abdelkader
  - Mekki, Mohamed
  - Ksentini, Adlen
  - Brik, Bouziane
  - Verikoukis, Christos
venue: IEEE Communications Magazine
venue_type: journal
year: 2025
doi: 10.1109/MCOM.002.2400276
url: https://www.scopus.com/pages/publications/105003271705?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 154--160
keywords:
  - Problem oriented languages
  - Advanced networks
  - Artificial intelligence learning
  - Human intervention
  - Language model
  - Machine learning models
  - Management IS
  - Management procedures
  - Network and service managements
  - Networks management
  - Servicelevel agreement (SLA)
  - Artificial intelligence
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
    proposed_justification:
      C1=1.0 (agentic/LLM signal in title); C2=0 (no resource
      management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
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
      - ovr_abs_llm_orchestrates
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification:
      Tarefa de DevOps/observabilidade (incident triage, RCA,
      geração de manifestos) — não é decisão de resource management.
    winning_category: D_devops_or_logs_not_rm
    overrides_applied: []
    my_final_decision: Include
    my_justification: "NOTA: o framing 6G é decoração — o use case real construído é autoscaling de microsserviços cloud-native. Pipeline: XGBoost detecta anomaly, SHAP extrai feature importance, e Llama2 gera explicações em linguagem natural + sugere/aplica corrective actions de scaling para prevenir SLA violations em microsserviços cloud-native. Avaliação com experimentos reais em pipeline cloud-native (não em RAN/PHY). LLM em papel material no loop RM (corrective scaling actions). Inclusão; framing 6G ignorado."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Edge-Cloud
  decision:
    - Remediation
  agentic_configuration:
    decision_role: Sole Decider
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
  autonomy_level: Autonomous
  metric:
    - RM Performance Metric
    - Agent Performance Metric
  evaluation_method: Practical Testbed
---

# paper-1947 — On Combining XAI and LLMs for Trustworthy Zero-Touch Network and Service Management in 6G

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Zero-touch network and service management (ZSM) is a key pillar of 6G networks. It allows the 6G management and orchestration framework to operate the networks without external (e.g., human) intervention. To effectively achieve ZSM, advanced network management procedures are required to detect and resolve anomalies within the 6G network autonomously, which usually requires artificial intelligence (AI) and machine learning (ML) models. However, relying solely on AI can raise concerns about trust due to their lack of explainability. Indeed, as these models are not explainable, it is difficult to understand and trust their decisions. To overcome this limitation, this article introduces a novel pipeline for ensuring trustworthy ZSM in 6G networks by combining AI for detecting anomalies; eXplainable AI (XAI) to identify the root causes of anomalies using feature importance analysis; and large language models (LLMs) to generate user-friendly explanations and suggest/apply corrective actions to resolve anomalies. A use case is presented using XGBoost as AI, SHAP as XAI, and Llama2 as LLM to address service level agreement (SLA) latency violations within cloud-native 6G microservices. Evaluation results obtained through real experiments demonstrate the framework's efficiency in scaling cloud resources to prevent SLA violations while providing understandable explanations to users, thereby enhancing trust in the system. © 1979-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_orchestrates, matched_substring: "LLMs for Trustworthy Zero-Touc" }`
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
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "root cause analysis" }`
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "root cause analysis" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** NOTA: o framing 6G é decoração — o use case real construído é autoscaling de microsserviços cloud-native. Pipeline: XGBoost detecta anomaly, SHAP extrai feature importance, e Llama2 gera explicações em linguagem natural + sugere/aplica corrective actions de scaling para prevenir SLA violations em microsserviços cloud-native. Avaliação com experimentos reais em pipeline cloud-native (não em RAN/PHY). LLM em papel material no loop RM (corrective scaling actions). Inclusão; framing 6G ignorado.
- **agrees_with_regex:** True
- **addressed_hint:** support
- **evidence_sections:** ['Abstract: zero-touch management', 'System Design: incident detection/network management', 'Evaluation: not SLA/scaling/placement metrics']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                 | location                        | rationale (neighbor not chosen)                                                                                                                                    |
| ------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| infrastructure                              | Edge-Cloud                             | "The use case was deployed on an edge computing cluster managed by Kubernetes."                                                          | §I Introduction (contributions) | Not `Cloud-Only` because the testbed is an edge Kubernetes cluster servicing cloud-native microservices.                                                           |
| decision                                    | Remediation                                      | "novel anomaly detection and resolution pipeline"                                                                                        | §I Introduction                 | _multi-select; the loop scales CPU/RAM in response to detected SLA-violation anomalies — fault-driven remediation, not steady-state scheduling/placement/routing._ |
| agentic_configuration.decision_role         | Sole Decider                                     | "if ZSM is enabled, Llama2 autonomously resolves the anomaly"                                                                            | §I Introduction                 | Not `Pipeline Contributor` because in the ZSM mode the LLM directly issues the corrective scaling action; XAI feeds context but does not decide.                   |
| agentic_configuration.coordination_topology | Single Agent                                     | "Llama2 was deployed on a single NVIDIA A100 GPU."                                                                                       | §I Introduction (contributions) | Not `Multi-Agent` because a single LLM produces the resolution; XGBoost and SHAP are auxiliary models, not agents.                                                 |
| reasoning_approach                          | Prompting                                        | "LLMs excel in reasoning tasks without requiring additional training [4], which can be leveraged to resolve anomalies"                   | §Introduction                   | _structured single-shot prompting with XAI explanation context; no iterative ReAct loop, no external KB retrieval, no fine-tuning._                                |
| autonomy_level                              | Autonomous                                       | "if ZSM is enabled, Llama2 autonomously resolves the anomaly; otherwise, it offers recommendations"                                      | §I Introduction                 | Not `Supervised` because the ZSM-enabled path closes the loop without human approval.                                                                              |
| metric                                      | RM Performance Metric + Agent Performance Metric | "Comprehensive real-world tests, including multiple LLM evaluations, were conducted to optimize performance for this specific use case." | §I Introduction (contributions) | _multi-select; the framework's SLA-latency outcome (RM) and multiple LLM evaluation results (agent side) are both reported._                                       |
| evaluation_method                           | Practical Testbed                                     | "The use case was deployed on an edge computing cluster managed by Kubernetes. Llama2 was deployed on a single NVIDIA A100 GPU."         | §I Introduction (contributions) | Not `Simulation` because the evaluation runs on real Kubernetes + GPU hardware, not a simulator.                                                                   |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Remediation`.
