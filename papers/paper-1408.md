---
id: paper-1408
title: Intelligent Kubernetes Scheduling with Large Language Models
authors:
  - Bai, Xinyu
  - Tang, Zhiqing
  - Yao, Zhi
  - Chen, Yao
  - Guo, Jianxiong
  - Wang, Tian
  - Jia, Weijia
venue: Proceedings - 2025 IEEE International Conference on Security, Privacy, Anonymity in Computation and Communication and Storage, SpaCCS 2025
venue_type: conference
year: 2025
doi: 10.1109/SpaCCS67922.2025.00012
url: https://www.scopus.com/pages/publications/105033212483?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16--23
keywords:
  - Edge computing
  - Large Language Models
  - Scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
      - ovr_with_llm
      - ovr_using_llm
      - ovr_llm_modifier
      - ovr_llm_as_judge
      - ovr_intent_driven
      - ovr_abs_llm_decides
      - ovr_abs_llm_orchestrates
      - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: "LLMScheduler (Seção IV) posiciona o LLM como participante ativo do ciclo de scheduling: pontua nós candidatos e seleciona o ótimo em tempo real para o cluster Kubernetes heterogêneo. Loop perceive→reason→act explícito — LLM recebe estado real do cluster e dos pods pendentes, raciocina sobre constraints e objetivos, emite decisão de binding pod→node. HybridScheduler complementa: LLM gera offline strategic intents que parametrizam a scoring function de produção, padrão análogo ao anchor paper-1644. Avaliação (Seção V) mostra +7% scheduling success rate em alta contenção e latência ms-level no HybridScheduler. Escopo Kubernetes em edge computing confirmado."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Cloud-Only
  decision:
    - Scheduling
  agentic_configuration:
    decision_role: Sole Decider
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
  autonomy_level: Autonomous
  metric:
    - RM Performance Metric
    - Agent Performance Metric
  evaluation_method: Simulation
---

# paper-1408 — Intelligent Kubernetes Scheduling with Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The impressive natural language understanding and inference abilities of recent Large Language Models (LLMs) have enabled their use in scheduling tasks. Existing scheduling methods often neglect the integration of LLMs with schedulers. To fill in such gaps and address complex scheduling challenges in heterogeneous Kubernetes clusters, we propose two LLM-based approaches. Specifically: 1) LLMScheduler, an adaptive online scheduling framework in which the LLM actively participates in decision-making. It scores candidate nodes and selects the optimal one in real time for the clusters. 2) HybridScheduler, an offline intelligence injection framework that leverages LLMs to proactively generate strategic intents for the scoring function, informed by job profiles and node configurations. It then rapidly scores and selects nodes, similar to a traditional Kubernetes scheduler. 3) We validate our methods with large-scale simulations, demonstrating that LLMScheduler improves scheduling success rates by up to 7% on average compared to the best traditional scheduler, particularly under extreme cluster pressure. Moreover, HybridScheduler consistently outperforms all traditional heuristics in high-contention scenarios, while reliably maintaining millisecond-level decision latency. Our experimental results offer a quantitative foundation for designing future AI-driven systems that balance performance, latency, and cost. © 2025 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_llm_modifier', 'ovr_llm_as_judge', 'ovr_intent_driven', 'ovr_abs_llm_decides', 'ovr_abs_llm_orchestrates', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "LLMs elegantly bypass this training" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models 
The impressive natural language understanding and inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference abilities of recent Large Language Models (LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference abilities of recent Large Language Models (LLMs" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "Furthermore, the impracticality of the online approach presents our second research challenge: How t" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** LLMScheduler (Seção IV) posiciona o LLM como participante ativo do ciclo de scheduling: pontua nós candidatos e seleciona o ótimo em tempo real para o cluster Kubernetes heterogêneo. Loop perceive→reason→act explícito — LLM recebe estado real do cluster e dos pods pendentes, raciocina sobre constraints e objetivos, emite decisão de binding pod→node. HybridScheduler complementa: LLM gera offline strategic intents que parametrizam a scoring function de produção, padrão análogo ao anchor paper-1644. Avaliação (Seção V) mostra +7% scheduling success rate em alta contenção e latência ms-level no HybridScheduler. Escopo Kubernetes em edge computing confirmado.
- **agrees_with_regex:** True

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                                                                                                  | location                         | rationale (neighbor not chosen)                                                                                                                               |
| ------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Cloud-Only                                       | "complex scheduling challenges in heterogeneous Kubernetes clusters"                                                                                                                                                      | §Abstract                        | Not `Edge-Cloud` because the scheduler targets Kubernetes data-center clusters; edge tier is mentioned only as related-work motivation.             |
| decision                                    | Scheduling                                       | "LLMScheduler, an adaptive online scheduling framework in which the LLM actively participates in decision-making. It scores candidate nodes and selects the optimal one in real time"                                     | §Abstract                        | _multi-select; the agent chooses which node hosts each pending pod (job-to-node scheduling), not placement of services, scaling, routing, or fault recovery._ |
| agentic_configuration.decision_role         | Sole Decider                                     | "we propose the LLMScheduler, an adaptive online scheduling framework. At each scheduling cycle, this approach supplies the LLM with complete, real-time cluster data, enabling tactically optimal scheduling decisions." | §I Introduction                  | Not `Pipeline Contributor` because the LLM picks the target node directly in the online variant rather than handing a score to another decider.               |
| agentic_configuration.coordination_topology | Single Agent                                     | "leveraging an LLM as a omniscient oracle, establishing an upper bound for AI-driven scheduling quality"                                                                                                                  | §I Introduction (contribution 1) | Not `Multi-Agent` because a single LLM oracle handles each scheduling request; no agent debate or hierarchy.                                                  |
| reasoning_approach                          | Prompting                                        | "LLMs elegantly bypass this training bottleneck with their powerful zero-shot and few-shot reasoning capabilities"                                                                                                        | §I Introduction                  | _zero/few-shot prompting; no iterative ReAct loop, no retrieval over external KB, no fine-tuning._                                                            |
| autonomy_level                              | Autonomous                                       | "scores candidate nodes and selects the optimal one in real time for the clusters"                                                                                                                                        | §Abstract                        | Not `Supervised` because the scheduler picks and binds nodes online without human approval.                                                                   |
| metric                                      | RM Performance Metric + Agent Performance Metric | "LLMScheduler improves scheduling success rates by up to 7% on average compared to the best traditional scheduler... while reliably maintaining millisecond-level decision latency"                                       | §Abstract                        | _multi-select; scheduling success (RM) and decision latency (agent-side) are both quantified._                                                                |
| evaluation_method                           | Simulation                                       | "We validate our methods with large-scale simulations"                                                                                                                                                                    | §Abstract                        | Not `Practical Testbed` because evaluation runs on a simulator, not on a real Kubernetes cluster.                                                                  |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Scheduling`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Cloud-Only`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Simulation`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Sole Decider`.
- `agentic-config-cross` (anchor: `RQ1.1`) — contributes: `Sole Decider` × `Single Agent`.
- `infrastructure-by-decision` (anchor: `RQ1.2`) — contributes: `Scheduling` × `Cloud-Only`.
- `decision-by-autonomy` (anchor: `RQ2.2`) — contributes: `Scheduling` × `Autonomous`.
- `reasoning-by-decision` (anchor: `RQ3.1`) — contributes: `Prompting` × `Scheduling`.
- `evaluation-by-decision` (anchor: `RQ4.1`) — contributes: `Scheduling` × `Simulation`.
- `metric-by-autonomy` (anchor: `RQ4.4`) — contributes: `RM Performance Metric` × `Autonomous`, `Agent Performance Metric` × `Autonomous`.
- `reasoning-temporal` (anchor: `RQ3.1`) — contributes: `2025` × `Prompting`.
- `temporal-included` (anchor: `RQ1`) — contributes: `2025`.
