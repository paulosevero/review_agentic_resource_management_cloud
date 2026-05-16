---
id: paper-1593
title: Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions
authors:
  - Ginarsa, Nyoman Agus Nugraha
  - Santoso, Bagus Jati
venue:
  "Proceedings - 2025 4th International Conference on Electronics Representation
  and Algorithm: Artificial Intelligence: Creating Tomorrow's World Today, ICERA
  2025"
venue_type: conference
year: 2025
doi: 10.1109/ICERA66156.2025.11087276
url: https://www.scopus.com/pages/publications/105013473906?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 400--404
keywords:
  - Amazon Bedrock
  - autoscaling
  - generative AI
  - Kubernetes
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
      C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
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
    my_final_decision: Include
    my_justification:
      "Paper implementa loop agentic para autoscaling Kubernetes.
      Seção III.D descreve predição via generative AI (Claude 3.7 Sonnet via Amazon
      Bedrock) que analisa métricas coletadas em Prometheus e gera recomendação de
      pod count para próximos 5 min. Loop: coleta dados → LLM raciocina sobre estado
      → decisão de scaling executada em EKS. Seção IV.3 confirma sistema integrado,
      automático e adaptativo. Satisfaz C18 (design agentic descrito) e C19 (avaliação
      apresentada com resultados)."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Cloud-Only
  decision:
    - Scaling
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

# paper-1593 — Intelligent Kubernetes Autoscaling Through Generative AI-Driven Workload Predictions

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the context of cloud-native architecture, the need for an efficient autoscaling mechanism is crucial to ensure service availability while avoiding resource waste. The Horizontal Pod Autoscaler (HPA) in Kubernetes has limitations in responding to real-time load spikes. This research aims to develop a prediction-based autoscaling approach using the Claude 3.7 Sonnet generative AI model via Amazon Bedrock. Historical CPU and memory data were collected by Prometheus at certain intervals, then converted to CSV format and sent to Claude 3.7 to generate a prediction of the number of pods needed in the next five minutes. The prediction results are then automatically applied to the Amazon EKS cluster via the Kubernetes API. The test results show that this approach can improve resource utilization efficiency and maintain service stability during traffic fluctuations, when compared to conventional HPA. This research also reveals that the accuracy of the prediction is highly dependent on the quality of the historical data, prompt, and AI model used. In the future, this research will expand the scope by adding other metrics such as latency, request rate, and I/O, and comparing the performance between generative AI models on Amazon Bedrock. © 2025 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "generative AI" }`
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
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative  AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative AI" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "generative AI" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Paper implementa loop agentic para autoscaling Kubernetes. Seção III.D descreve predição via generative AI (Claude 3.7 Sonnet via Amazon Bedrock) que analisa métricas coletadas em Prometheus e gera recomendação de pod count para próximos 5 min. Loop: coleta dados → LLM raciocina sobre estado → decisão de scaling executada em EKS. Seção IV.3 confirma sistema integrado, automático e adaptativo. Satisfaz C18 (design agentic descrito) e C19 (avaliação apresentada com resultados).
- **agrees_with_regex:** True
- **evidence_sections:** ['III.D Prediction Through Generative AI', 'I.INTRODUCTION (motivation e CloudNative scope)', 'IV.RESULTS AND DISCUSSION (implementação e avaliação)']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                            | location                                | rationale (neighbor not chosen)                                                                                                                                        |
| ------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Cloud-Only                                       | "This research uses Amazon Web Services (AWS) as a cloud infrastructure provider... Amazon Elastic Kubernetes Service (Amazon EKS)" | §III-A Kubernetes Cluster Preparation   | Not `Edge-Cloud` because the deployment runs entirely on AWS EKS in the cloud; no edge tier.                                                                 |
| decision                                    | Scaling                                          | "prediction-based autoscaling approach using the Claude 3.7 Sonnet generative AI model"                                             | §Abstract                               | _multi-select; the agent adjusts replica count of a Kubernetes deployment over time — horizontal autoscaling, not job-scheduling, placement, routing, or remediation._ |
| agentic_configuration.decision_role         | Sole Decider                                     | "this service will update the number of replicas on the sample application deployment"                                              | §III-D Prediction Through Generative AI | Not `Pipeline Contributor` because the LLM's predicted pod count is applied directly via the Kubernetes API.                                                           |
| agentic_configuration.coordination_topology | Single Agent                                     | "the Claude 3.7 Sonnet model from Anthropic accessed through the Amazon Bedrock service is used"                                    | §I Introduction                         | Not `Multi-Agent` because a single LLM call per cycle generates the predicted replica count.                                                                           |
| reasoning_approach                          | Prompting                                        | "To obtain the appropriate prompt, prompt testing was carried out through the playground on the Amazon Bedrock console."            | §III-C Optimal Prompt Determination     | _structured prompt + CSV context; no chain-of-thought reflection ("No explanation needed"), no retrieval over external KB, no fine-tuning._                            |
| autonomy_level                              | Autonomous                                       | "The prediction results are then automatically applied to the Amazon EKS cluster via the Kubernetes API."                           | §Abstract                               | Not `Supervised` because the service rewrites the deployment replicas without HITL gating.                                                                             |
| metric                                      | RM Performance Metric + Agent Performance Metric | "this approach can improve resource utilization efficiency and maintain service stability during traffic fluctuations"              | §Abstract                               | _multi-select; CPU/memory utilization + stability (RM side) and prompt-accuracy / model-quality dependence (agent side) are both reported._                            |
| evaluation_method                           | Practical Testbed                                     | "The system was tested under various conditions, including when CPU utilization increased significantly"                            | §III-E Testing                          | Not `Simulation` because load testing runs against a deployed Go REST API on an EKS cluster with K6 generating real traffic.                                           |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Scaling`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Cloud-Only`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Practical Testbed`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
