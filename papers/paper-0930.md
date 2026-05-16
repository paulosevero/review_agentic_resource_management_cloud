---
id: paper-0930
title: Deploying Stateful Network Functions Efficiently using Large Language Models
authors:
  - Ghasemirahni, Hamid
  - Farshin, Alireza
  - Scazzariello, Mariano
  - Chiesa, Marco
  - Kostić, Dejan
venue:
  EuroMLSys 2024 - Proceedings of the 2024 4th Workshop on Machine Learning and
  Systems
venue_type: conference
year: 2024
doi: 10.1145/3642970.3655836
url: https://www.scopus.com/pages/publications/85192276579?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 28--38
keywords:
  - Intra-Server Load Balancing
  - LLMs
  - RSS Configuration
  - Stateful Network Functions
  - Static Code Analysis
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
      management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
      - ovr_with_llm
      - ovr_using_llm
      - ovr_via_llm
      - ovr_llm_modifier
      - ovr_abs_llm_decides
    my_final_decision: Include
    my_justification:
      "FlowMage: sistema que usa LLM para analisar source code de
      network functions (NFs), extrair meta-informações (estado, complexidade), e
      o LLM informa diretamente um solver que gera configuração otimizada de RSS para
      NF chaining. O LLM percebe (code analysis) → razoa (complexidade comparativa)
      → decide (impacta configuração de parallelização). Loop agentic governa placement/scheduling
      de state em cores/servers. Decisão de RM (CPU placement, contention minimization)
      é dirigida pelo LLM."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Cloud-Only
  decision:
    - Placement & Offloading
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

# paper-0930 — Deploying Stateful Network Functions Efficiently using Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Stateful network functions are increasingly used in data centers. However, their scalability remains a significant challenge since parallelizing packet processing across multiple cores requires careful configuration t o avoid compromising the application’s semantics or performance. This challenge is particularly important when deploying multiple stateful functions on multi-core servers. This paper proposes FlowMage, a system that leverages Large Language Models (LLMs) to perform code analysis and extract essential information from stateful network functions (NFs) prior to their deployment on a server. FlowMage uses this data to find an efficient configuration of an NF chain that maximizes performance while preserving the semantics of the NF chain. Our evaluation shows that, utilizing GPT-4, FlowMage is able to find and apply optimized configuration when deploying stateful NFs chain on a server, resulting in significant p erformance i mprovement (up t o 1 1×) in comparison to the default configuration of the system. © 2024 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GPT" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) t" }`
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
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_via_llm', 'ovr_llm_modifier', 'ovr_abs_llm_decides']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "fine-tuning of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) to perform code analysis and extract essential information from statefu" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs RSS Configuration Stateful Network Functions Static Code Analysis
  ***
  title: \"Deploying" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs\"
  - \"Static Code Analysis\"
  - \"RSS Configuration\"

---

# Deploying" }`

- `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) to perform code analysis and extract essential information from statefu" }`
- `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs in the context of packet processing and (ii) address the challenges of deploying" }`
- `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs before deploying a chain of stateful NFs;
- Evaluated FlowMage and showed the benefits of optim" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLMs help to efficiently deploy" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** FlowMage: sistema que usa LLM para analisar source code de network functions (NFs), extrair meta-informações (estado, complexidade), e o LLM informa diretamente um solver que gera configuração otimizada de RSS para NF chaining. O LLM percebe (code analysis) → razoa (complexidade comparativa) → decide (impacta configuração de parallelização). Loop agentic governa placement/scheduling de state em cores/servers. Decisão de RM (CPU placement, contention minimization) é dirigida pelo LLM.
- **agrees_with_regex:** True
- **evidence_sections:** ['Section 3.1 (LLM analyzes NF source code, extracts cost/complexity)', "Section 3.2 (Solver uses LLM's output to decide RSS configuration — direct RM decision)", 'Figure 2 (feature tracker → LLM → solver → optimized config)']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                                                                             | location                           | rationale (neighbor not chosen)                                                                                                                                                                     |
| ------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Cloud-Only                                       | "Stateful network functions are increasingly used in data centers."                                                                                                                                  | §Abstract                          | Not `Edge-Cloud` because the paper targets single multi-core commodity servers in data centers, with no edge tier in scope.                                                               |
| decision                                    | Placement & Offloading                           | "FlowMage employs a solver to leverage the extracted data from the LLM to identify an optimal RSS configuration"                                                                                     | §3 FlowMage                        | _multi-select; RSS configuration places stateful NF flows on specific CPU cores (intra-server placement), not scheduling jobs over time, scaling instances, routing/slicing, or fault remediation._ |
| agentic_configuration.decision_role         | Sole Decider                                     | "the solver automatically uses the LLM to compare the code complexity of NFs in terms of the average processing required per packet"                                                                 | §3.2 Solver                        | Not `Pipeline Contributor` because the LLM-derived analysis directly drives the deployed configuration without a separate human/algorithmic decision-maker.                                         |
| agentic_configuration.coordination_topology | Single Agent                                     | "FlowMage harnesses LLMs through a two-step process."                                                                                                                                                | §3.1 Prompt Formulation            | Not `Multi-Agent` because a single LLM is invoked sequentially per NF; there is no coordinated set of agents debating or planning.                                                                  |
| reasoning_approach                          | Prompting                                        | "FlowMage sends a comprehensive prompt containing (i) a general introduction... (ii) a section detailing the specific information... (iii) a brief directive specifying the desired response format" | §3.1 Prompt Formulation            | _structured prompting only; no iterative reflection/ReAct loop, no retrieval over external KB, and the paper explicitly notes "without the need for in-context learning or model fine-tuning"._     |
| autonomy_level                              | Autonomous                                       | "FlowMage to automatically find and apply the optimal configuration via LLMs before deploying a chain of stateful NFs"                                                                               | §1 Introduction (contributions)    | Not `Supervised` because FlowMage applies the optimized configuration automatically; HITL is mentioned only as a future-direction caveat, not as a runtime gate.                                    |
| metric                                      | RM Performance Metric + Agent Performance Metric | "the average token count utilized for analyzing each NF stood at 7164... costing $0.31 per analysis using GPT-4 Turbo"                                                                               | §4.1 Accuracy of Code Analysis     | _multi-select; throughput in Mpps (Figs 4–5) is the RM metric, and token usage / per-analysis dollar cost / LLM accuracy are agent-side metrics._                                                   |
| evaluation_method                           | Practical Testbed | "we conducted experiments in a testbed containing two commodity servers interconnected via a 32 × 100-Gbps Edgecore Networks DCS800 Wedge 100BF-32X switch"                                          | §4 Evaluation (Experimental Setup) | Not `Simulation` because the experiments run on real commodity servers and a hardware switch, not on a simulated substrate.                                        |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Placement & Offloading`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Cloud-Only`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Prompting`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Practical Testbed`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Sole Decider`.
- `agentic-config-cross` (anchor: `RQ1.1`) — contributes: `Sole Decider` × `Single Agent`.
- `infrastructure-by-decision` (anchor: `RQ1.2`) — contributes: `Placement & Offloading` × `Cloud-Only`.
- `decision-by-autonomy` (anchor: `RQ2.2`) — contributes: `Placement & Offloading` × `Autonomous`.
- `reasoning-by-decision` (anchor: `RQ3.1`) — contributes: `Prompting` × `Placement & Offloading`.
- `evaluation-by-decision` (anchor: `RQ4.1`) — contributes: `Placement & Offloading` × `Practical Testbed`.
- `metric-by-autonomy` (anchor: `RQ4.4`) — contributes: `RM Performance Metric` × `Autonomous`, `Agent Performance Metric` × `Autonomous`.
- `reasoning-temporal` (anchor: `RQ3.1`) — contributes: `2024` × `Prompting`.
- `temporal-included` (anchor: `RQ1`) — contributes: `2024`.
