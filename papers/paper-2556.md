---
id: paper-2556
title:
  "LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence
  With Optimization Guarantees"
authors:
  - Ding, Guanyu
  - Yang, Shiyu
  - Lin, Han
  - Chen, Zifan
  - Yang, Jie Si
venue: IEEE Open Journal of the Computer Society
venue_type: journal
year: 2026
doi: 10.1109/OJCS.2026.3667549
url: https://www.scopus.com/pages/publications/105031664073?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 560--573
keywords:
  - adaptive optimization
  - Cloud computing
  - large language models (LLMs)
  - resource scheduling
  - SLA management
  - task orchestration
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
    my_final_decision: Include
    my_justification: "Reanálise com critério mais flexível: LLMSched posiciona o LLM como policy generator que delega constraint enforcement e fine-grained optimization a módulos algorítmicos. Três estágios (codificação de estado, raciocínio LLM, execução algorítmica) compõem pipeline em que o LLM dirige a política em cloud resource scheduling adaptativo. Caso forte de inclusão."
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

# paper-2556 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud resource scheduling presents a fundamental challenge in modern distributed computing, where heterogeneous workloads, complex task dependencies, and multi-objective optimization requirements exceed the capabilities of traditional rule-based and small-scale machine learning approaches. Existing schedulers struggle to dynamically adapt to evolving workload patterns while simultaneously satisfying Service Level Agreement (SLA) constraints, resource efficiency targets, and fairness policies. This article introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework that synergistically combines the contextual reasoning capabilities of foundation models with the execution guarantees of classical optimization techniques. Our approach transforms heterogeneous cluster states—including task dependency graphs, real-time resource utilization metrics, and SLA specifications—into a unified structured-textual representation that leverages LLMs' few-shot learning and causal reasoning abilities to generate intelligent scheduling candidates. These candidates are subsequently refined through a lightweight Integer Linear Programming (ILP) module that ensures feasibility and optimality under resource constraints. We evaluate LLMSched on Google's production cluster trace dataset, demonstrating significant improvements over state-of-the-art baselines: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations across diverse workload scenarios. Extensive ablation studies validate the contributions of each architectural component, while robustness analysis under workload perturbations confirms the framework's practical viability. Our work establishes a new paradigm for intelligent resource management that bridges the gap between neural reasoning and algorithmic precision, opening avenues for LLM applications in systems optimization domains. © 2020 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "foundation models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Guided" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-guided" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Reanálise com critério mais flexível: LLMSched posiciona o LLM como policy generator que delega constraint enforcement e fine-grained optimization a módulos algorítmicos. Três estágios (codificação de estado, raciocínio LLM, execução algorítmica) compõem pipeline em que o LLM dirige a política em cloud resource scheduling adaptativo. Caso forte de inclusão.
- **agrees_with_regex:** True
- **evidence_sections:** ["Introduction § 2: 'Rather than using LLMs as end-to-end decision makers, LLMSched positions them as policy generators... while delegating constraint enforcement and fine-grained optimization to algorithmic modules.'", "Section IV.C (Optimization-Based Refinement): 'The candidates generated by the LLM, while semantically reasonable, may violate hard resource or temporal constraints. To guarantee feasibility and achieve optimality, we employ a lightweight Integer Linear Programming (ILP) solver...'", "Section IV.D: 'caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur. For routine scheduling decisions, validated strategies are executed by fast heuristic modules.'"]

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                     | location              | rationale (neighbor not chosen)                                                                                                                                                        |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Cloud-Only                                       | "Cloud resource scheduling presents a fundamental challenge in modern distributed computing"                                                 | §Abstract             | Not `Edge-Cloud` because the system targets cloud datacenter clusters; no edge tier.                                                                                         |
| decision                                    | Scheduling                                       | "introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework"                                               | §Abstract             | _multi-select; the framework schedules tasks on cluster nodes — task scheduling, not service placement, scaling, routing, or remediation._                                             |
| agentic_configuration.decision_role         | Sole Decider                                     | "LLM-Guided Candidate Generation employs few-shot and chain-of-thought prompting to produce diverse scheduling candidates"                   | §I Introduction       | Not `Pipeline Contributor` per locked classification; the LLM drives candidate generation, with ILP refining feasibility. The LLM ultimately steers which schedule region is explored. |
| agentic_configuration.coordination_topology | Single Agent                                     | "directly applying LLMs to cloud scheduling poses fundamental challenges"                                                                    | §I Introduction       | Not `Multi-Agent` because a single LLM produces scheduling candidates; ILP is a solver, not an agent.                                                                                  |
| reasoning_approach                          | Prompting                                        | "few-shot adaptability [23], chain-of-thought reasoning [24], and semantic interpretation of natural language constraints"                   | §I Introduction       | _few-shot + chain-of-thought prompting on structured-textual state; no fine-tuning, no external retrieval, no iterative ReAct loop in the agentic sense._                              |
| autonomy_level                              | Autonomous                                       | "LLMSched incorporates caching and workload-aware triggering mechanisms that invoke LLM reasoning only when significant state changes occur" | §I Introduction       | Not `Supervised` because scheduling runs in a closed loop without HITL gating.                                                                                                         |
| metric                                      | RM Performance Metric + Agent Performance Metric | "23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations" | §Abstract             | _multi-select; JCT / utilization / SLA (RM-side) and inference-overhead metrics that motivate the caching/triggering design (agent-side) are both reported._                           |
| evaluation_method                           | Simulation                                       | "Hardware Configuration: Experiments run on a simulated"                                                                                     | §V-A Experiment Setup | Not `Practical Testbed` because the framework is benchmarked through simulation on Google cluster traces, not on a deployed scheduler.                                                      |

**Confidence (weakest axis):** MED
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
- `reasoning-temporal` (anchor: `RQ3.1`) — contributes: `2026` × `Prompting`.
