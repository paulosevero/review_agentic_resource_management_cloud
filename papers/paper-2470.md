---
id: paper-2470
title:
  Intent-Based Multi-Cloud Storage Management Powered by a Fine-Tuned Large Language
  Model
authors:
  - Zheng, Jingya
  - Tao, Gaofeng
  - Qin, Shuxin
  - Wang, Dan
  - Ma, Zhongjun
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3563200
url: https://www.scopus.com/pages/publications/105003458024?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 72736--72753
keywords:
  - Autonomous management
  - cloud computing
  - cloud-network integration
  - intent-based networking
  - large language model
  - multi-cloud
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
      management signal); C3=1.0 (infra/cloud-edge signal)
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
      O LLM aparece em papel de suporte (gera heurísticas, embeddings,
      features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic
      AI dirigindo decisão de RM.
    winning_category: H_llm_supports_other_method
    overrides_applied: []
    my_final_decision: "Include (Borderline)"
    my_justification: "IBSM usa fine-tuned LLM para classificar intents (Seção III.B) e gerar policy tree (Seção III.C) em multi-cloud storage management. LLM exerce papel no pipeline de intent-driven RM. Não toma a decisão diretamente."
    agrees_with_regex: true
    divergence_reason:
      "regex (pass 1) flagou H_llm_supports_other_method e excluiu.
      Full-text confirma: LLM é componente de NLP-to-config (intent parser), não agente
      autônomo dirigindo RM."
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Cloud-Only
  decision:
    - Placement & Offloading
  agentic_configuration:
    decision_role: Pipeline Contributor
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
    - Model Specialization
  autonomy_level: Supervised
  metric:
    - RM Performance Metric
  evaluation_method: Practical Testbed
---

# paper-2470 — Intent-Based Multi-Cloud Storage Management Powered by a Fine-Tuned Large Language Model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Storage resources are essential in heterogeneous multi-cloud environments. In response to the growing demand for efficient storage resource management (SRM) in these environments, this paper proposes an intent-based storage management (IBSM) system powered by a fine-tuned large language model (LLM). To overcome the limitations of existing methods, the IBSM system focuses on enhancing the controllability, completeness, and reliability of SRM in multi-cloud environments. Specifically, the IBSM system employs a dual-phase joint intent classification algorithm, which leverages a fine-tuned LLM to accurately identify user intents across diverse knowledge backgrounds. Additionally, the system constructs a collaborative intent decomposition method, which guarantees the integrity of intents. Furthermore, the system integrates an automated intent deployment mechanism that supports error recovery through checkpoints. Experimental results show that the system achieves a whole end-to-end (E2E) lifecycle for managing user intents. The E2E time is reduced by at least half compared to the manual approach, with an average of 50.14% dedicated to interactive tasks. Performance metrics for intent classification, including accuracy, precision, and recall, all exceed 90%. Moreover, the recovery time is reduced by an average of 30.6%. Therefore, the system provides a valuable solution for the autonomous management of multi-cloud resources. © 2013 IEEE.

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
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-Based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-based" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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
- **regex_justification:** "O LLM aparece em papel de suporte (gera heurísticas, embeddings, features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic AI dirigindo decisão de RM."
- **winning_category:** 'H_llm_supports_other_method'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-assisted" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-assisted" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include (Borderline)
- **my_justification:** IBSM usa fine-tuned LLM para classificar intents (Seção III.B) e gerar policy tree (Seção III.C) em multi-cloud storage management. LLM exerce papel no pipeline de intent-driven RM. Não toma a decisão diretamente.
- **agrees_with_regex:** True
- **divergence_reason:** regex (pass 1) flagou H_llm_supports_other_method e excluiu. Full-text confirma: LLM é componente de NLP-to-config (intent parser), não agente autônomo dirigindo RM.
- **addressed_hint:** hint_categories=[quality]: avaliação foca em accuracy de classificação intent (>90%), não em impacto de decisões RM ou qualidade de alocação de storage. Ciclo fechado (observe estado→ação) ausente.
- **evidence_sections:** ["Section III.A Overall Architecture: 'three subsystems: intent classification, decomposition, deployment'; LLM (MS-LLM) classifica/decompõe, deployer executa", "Section III.B: 'dual-phase joint intent classification'—tradução de linguagem natural", "Section III.C: 'policy generator + policy filler'—mapping a templates pré-definidas, não decisão dinâmica", 'Figure 2: decomposition subsystem sem feedback loop; intent→policy→execution é pipeline, não loop autônomo']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                            | evidence                                                                                                                                                                                                                                        | location                        | rationale (neighbor not chosen)                                                                                                                                                                                          |
| ------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| infrastructure                              | Cloud-Only                       | "this paper proposes an intent-based storage management (IBSM) system powered by a fine-tuned large language model (LLM)"                                                                                                                       | §Abstract                       | Not `Edge-Cloud` because the system targets heterogeneous multi-cloud platforms; edge resources are not in scope.                                                                                              |
| decision                                    | Placement & Offloading           | "Storage resources are essential in heterogeneous multi-cloud environments."                                                                                                                                                                    | §Abstract                       | _multi-select; the system places/allocates storage operations across cloud vendors — multi-cloud storage placement, not job scheduling, autoscaling, routing, or remediation._                                           |
| agentic_configuration.decision_role         | Pipeline Contributor             | "intents are classified into different storage modes using the fine-tuned LLM. In the second stage, intents are further categorized into several basic tasks of the multi-cloud platform"                                                       | §I Introduction (contributions) | Not `Sole Decider` because the LLM performs intent classification and decomposition; the deployment subsystem (FSMs) executes the policy tree.                                                                           |
| agentic_configuration.coordination_topology | Single Agent                     | "the IBSM system employs a dual-phase joint intent classification algorithm, which leverages a fine-tuned LLM to accurately identify user intents"                                                                                              | §Abstract                       | Not `Multi-Agent` because one LLM (MS-LLM) handles the classification and decomposition; FSMs are control structures, not agents.                                                                                        |
| reasoning_approach                          | Prompting + Model Specialization | "the server, equipped with a single Nvidia A100 GPU, efficiently fine-tunes ChatGLM4 using LoRA to form the MS-LLM"                                                                                                                             | §IV-A Experimentation setup     | _prompting plus LoRA fine-tuning of ChatGLM4 (model specialization); no iterative ReAct loop, no external KB retrieval._                                                                                                 |
| autonomy_level                              | Supervised                       | "The specified LLM assists users in providing missing parameter values."                                                                                                                                                                        | §I Introduction (contributions) | Not `Autonomous` because the system explicitly interacts with the user to fill missing intent parameters before deployment.                                                                                              |
| metric                                      | RM Performance Metric            | "The E2E time is reduced by at least half compared to the manual approach, with an average of 50.14% dedicated to interactive tasks. Performance metrics for intent classification, including accuracy, precision, and recall, all exceed 90%." | §Abstract                       | _single-select; E2E lifecycle time and recovery time on the RM side are reported; agent-side overhead metrics are not the primary lens (classification accuracy belongs to MS-LLM evaluation kept in a separate paper)._ |
| evaluation_method                           | Practical Testbed | "the experimental setup of the IBSM system consists of a client, server, and large-scale multi-cloud exchange platform"                                                                                                                         | §IV-A Experimentation setup     | Not `Simulation` because the IBSM is deployed on a real multi-cloud exchange platform with client and server endpoints, not on a simulator.                                                   |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Placement & Offloading`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Supervised`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Cloud-Only`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`, `Model Specialization`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Practical Testbed`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Pipeline Contributor`.
