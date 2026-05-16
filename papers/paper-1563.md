---
id: paper-1563
title:
  Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice
  Deployment
authors:
  - Fang, Zhengxin
  - Ma, Hui
  - Chen, Gang
  - Hartmann, Sven
  - Wang, Chen
venue:
  Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial
  Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2025
doi: 10.1007/978-981-96-0348-0_7
url: https://www.scopus.com/pages/publications/85210811923?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 86--97
keywords:
  - cloud computing
  - dynamic microservice deployment
  - genetic programming
  - hyper-heuristics
  - LLM
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
    my_justification: "LLM-enhanced Genetic Programming Hyper-Heuristic (LLM-GPHH) para dynamic microservice deployment em cloud. O LLM desempenha papel decisório material gerando os operadores genéticos do GP (mutação/crossover); o GP é apenas o framework dentro do qual o LLM opera. Não é família LLM-subordinate-to-RL (é GP, não RL). Escopo cloud confirmado. Inclusão."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Edge-Cloud
  decision:
    - Scheduling
  agentic_configuration:
    decision_role: Pipeline Contributor
    coordination_topology: Single Agent
  reasoning_approach:
    - Prompting
  autonomy_level: Autonomous
  metric:
    - RM Performance Metric
    - Agent Performance Metric
  evaluation_method: Simulation
---

# paper-1563 — Leveraging LLM in Genetic Programming Hyper-heuristics for Dynamic Microservice Deployment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Microservice deployment in cloud computing is a challenging combinatorial optimization problem due to the complex dependencies among microservices and the intricate trade-offs among different QoS requirements, e.g., minimizing Energy Consumption (EC) vs. minimizing Communication Overhead (CO). Recently, some hyper-heuristics methods, particularly Genetic Programming Hyper-Heuristics (GPHH), have been proposed to automatically generate heuristics for solving dynamic microservice deployment problems. Meanwhile, Large Language Models (LLMs) are becoming popular for solving various domain-specific problems thanks to their strong ability to learn problem-related knowledge. However, hybridizing GPHH with LLM by combining their abilities in solving complex optimization problems remains unexplored. In this paper, we propose an LLM-enhanced Genetic Programming Hyper-Heuristic (LLM-GPHH) algorithm to evolve heuristics for the dynamic deployment of applications composed of microservices, to jointly optimize EC and CO. Our experiments on real-world datasets demonstrate the effectiveness of the newly proposed LLM-GPHH. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-enhanced" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-enhanced" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** LLM-enhanced Genetic Programming Hyper-Heuristic (LLM-GPHH) para dynamic microservice deployment em cloud. O LLM desempenha papel decisório material gerando os operadores genéticos do GP (mutação/crossover); o GP é apenas o framework dentro do qual o LLM opera. Não é família LLM-subordinate-to-RL (é GP, não RL). Escopo cloud confirmado. Inclusão.
- **agrees_with_regex:** True
- **addressed_hint:** support
- **evidence_sections:** ['4.5 LLM Evolution', '3 Problem Definition (GPHH é o método principal)', '4.1 Overview (role de LLM em geração de heurísticas)']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                           | location                        | rationale (neighbor not chosen)                                                                                                                                                                                                        |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Edge-Cloud                             | "to improve the performance of GPHH in terms of jointly optimizing CO and EC for dynamic MEC problems"                                             | §I Introduction (contributions) | Not `Cloud-Only` per locked classification; the body emphasizes container-based clouds, but the contributions reference dynamic MEC problems, motivating the continuum label. FLAG: most of the formulation is data-center cloud only. |
| decision                                    | Scheduling                                       | "a VM selection heuristic is required to either select existing VMs or create new VM instances for real-time microservice applications deployment" | §I Introduction                 | _multi-select; the heuristic chooses which existing VM/PM serves an arriving microservice at runtime — scheduling assignment, not capacity scaling or routing._                                                                        |
| agentic_configuration.decision_role         | Pipeline Contributor                             | "the most effective method... use heuristics in the prompt and the number of response heuristics"                                                  | §V Experimental Evaluation      | Not `Sole Decider` because the LLM generates GP individuals (candidate heuristics) inside an evolutionary loop; the evolved heuristic, not the LLM, makes the runtime deployment decisions.                                            |
| agentic_configuration.coordination_topology | Single Agent                                     | "GPT-3.5-turbo-0613 API is used in this paper"                                                                                                     | §V Experimental Evaluation      | Not `Multi-Agent` because one LLM endpoint produces heuristics each generation; no agents collaborate or debate.                                                                                                                       |
| reasoning_approach                          | Prompting                                        | "a prompt is generated... which includes three parts: task description... promising heuristics... response heuristics"                             | §IV Algorithm                   | _structured prompt with few-shot exemplars (high-fitness heuristics); no ReAct/reflection loop, no external retrieval, no fine-tuning._                                                                                                |
| autonomy_level                              | Autonomous                                       | "automatically generate VM selection heuristic and PM selection heuristic to minimize both EC and CO in cloud data centers"                        | §I Introduction                 | Not `Supervised` because heuristic generation runs without HITL approval inside the GP evolutionary loop.                                                                                                                              |
| metric                                      | RM Performance Metric + Agent Performance Metric | "Our experiments demonstrate that the proposed LLM-GPHH can effectively generate better heuristics than existing algorithms in most scenarios"     | §I Introduction (contributions) | _multi-select; EC and CO (RM metrics) are evaluated alongside LLM-side prompt configuration / generated-individuals counts in §V._                                                                                                     |
| evaluation_method                           | Simulation                                       | "Simulation. We simulate the state of a cloud data center by using a real-..."                                                                     | §V Experimental Evaluation      | Not `Practical Testbed` because the evaluation is a cloud data-center simulator driven by a real-world dataset.                                                                                                                             |

**Confidence (weakest axis):** MED
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Scheduling`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Edge-Cloud`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Simulation`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Pipeline Contributor`.
- `agentic-config-cross` (anchor: `RQ1.1`) — contributes: `Pipeline Contributor` × `Single Agent`.
- `infrastructure-by-decision` (anchor: `RQ1.2`) — contributes: `Scheduling` × `Edge-Cloud`.
