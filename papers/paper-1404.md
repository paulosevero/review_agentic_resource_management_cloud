---
id: paper-1404
title: "ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control"
authors:
  - Avgerinos, Vasilis
  - Ramantas, Kostas
  - Alonso, Luis
  - Verikoukis, Christos
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3648858
url: https://www.scopus.com/pages/publications/105025885742?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ""
keywords:
  - Agentic Systems
  - AIOps
  - Autonomous Infrastructure Management
  - Closed-Loop Control
  - Edge Computing
  - Intent-Based Networking
  - IoT Orchestration
  - Kubernetes
  - Large Language Models (LLMs)
  - SLA Monitoring
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
      - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: "Revisita ao critério: o full-text confirma escopo cloud-native + edge + IoT (não 6G/RAN puro) e LLM como decisor do loop de RM. Flipado para Include."
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-09T00:00:00+00:00"
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: "Agentic LLM com closed-loop RCA + mitigação executando ações de RM via MCP/kubectl."
    winning_category: agent_llm_based
    overrides_applied: []
    my_final_decision: Include
    my_justification: "ARM (Avgerinos et al., IEEE IoT Journal 2026) implementa loop fechado agentic LLM para autonomous remediation em cloud-native + edge + IoT (Sec III). Pipeline: monitoramento contínuo de SLA (Sec III-C, latência p95 + taxa de sucesso) → ao detectar violação, dispara LLM agent (GPT-5/GPT-5-mini) → o agente investiga via tool calls expostos por Model Context Protocol (MCP) server (Sec IV) → emite ações corretivas (pod rescheduling, scaling deployments, deleting pods, configuration updates via kubectl_scale, kubectl_delete_pod) → re-mede métricas e replan se necessário. LLM é decisor explícito do ciclo de RM. Avaliação (Sec V-VI) em K3s cluster com 7 nós (2 cloud + 4 edge + 1 mgmt), 3 aplicações IoT (real-time monitoring, smart manufacturing 8 μservices, smart city traffic 12 μservices), chaos engineering fault injection, comparativo GPT-5 vs GPT-5-mini. Métricas: 52.9% diagnostic accuracy, 70.7% remediation success rate, decision rounds, wall-clock time, tool utilization. Boundaries A (escopo cloud-edge-IoT), B (LLM decisor — não LLM-subordinate-to-RL) e C (RM em loop fechado: rescheduling/scaling/config) todos satisfeitos. Include puro."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: "2026-05-15T00:00:00+00:00"
taxonomy:
  infrastructure: Edge-Cloud
  decision:
    - Remediation
  agentic_configuration:
    decision_role: Sole Decider
    coordination_topology: Single Agent
  reasoning_approach:
    - Iterative Reasoning
  autonomy_level: Autonomous
  metric:
    - RM Performance Metric
    - Agent Performance Metric
  evaluation_method: Practical Testbed
---

# paper-1404 — ARM: Autonomous Remediation & Management with LLM Agents for Intent-Driven Control

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The growing complexity of cloud-native, edge, and IoT infrastructures has made manual configuration, fault remediation, and lifecycle management increasingly unsustainable. Traditional automation techniques—such as rule-based logic or bespoke machine learning pipelines—struggle with adaptability and explainability in dynamic environments. Recent advances in Large Language Models (LLMs), however, have introduced new opportunities for autonomous, intent-driven infrastructure control. In this work, we present a closed-loop framework that integrates LLM agents for automated Root Cause Analysis (RCA) and mitigation of faults within cloud-edge and IoT systems. When SLA violations are detected, the agent identifies likely root causes and selects corrective actions—such as pod rescheduling, scaling, or configuration updates—executed via a Model Context Protocol (MCP) server exposing management tool functionalities through an API. This RCA-plus-mitigation loop enables fault handling that is both explainable and adaptive. We evaluate our system on a cluster running synthetic IoT workloads under emulated stressors using a reproducible benchmarking setup. Results show that the agent identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully. Notably, the agent incorporates validation steps to ensure system stability after interventions. These findings highlight the feasibility of LLMs for real-time infrastructure healing and their potential role in future AIOps workflows. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Revisita ao critério: o full-text confirma escopo cloud-native + edge + IoT (não 6G/RAN puro) e LLM como decisor do loop de RM. Flipado para Include."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Agentic LLM com closed-loop RCA + mitigação executando ações de RM via MCP/kubectl."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: agent_llm_based, pattern_id: llm_agent_decisor, matched_substring: "LLM agent" }`
  - `{ category: agent_llm_based, pattern_id: closed_loop, matched_substring: "closed-loop framework" }`

**Pass-2 LLM reviewer (manual full-text review):**

- **my_final_decision:** Include
- **my_justification:** ARM (Avgerinos et al., IEEE IoT Journal 2026) implementa loop fechado agentic LLM para autonomous remediation em cloud-native + edge + IoT (Sec III). Pipeline: monitoramento contínuo de SLA (Sec III-C, latência p95 + taxa de sucesso) → ao detectar violação, dispara LLM agent (GPT-5/GPT-5-mini) → o agente investiga via tool calls expostos por Model Context Protocol (MCP) server (Sec IV) → emite ações corretivas (pod rescheduling, scaling deployments, deleting pods, configuration updates via kubectl_scale, kubectl_delete_pod) → re-mede métricas e replan se necessário. LLM é decisor explícito do ciclo de RM. Avaliação (Sec V-VI) em K3s cluster com 7 nós (2 cloud + 4 edge + 1 mgmt), 3 aplicações IoT (real-time monitoring, smart manufacturing 8 μservices, smart city traffic 12 μservices), chaos engineering fault injection, comparativo GPT-5 vs GPT-5-mini. Métricas: 52.9% diagnostic accuracy, 70.7% remediation success rate, decision rounds, wall-clock time, tool utilization. Boundaries A (escopo cloud-edge-IoT), B (LLM decisor — não LLM-subordinate-to-RL) e C (RM em loop fechado: rescheduling/scaling/config) todos satisfeitos. Include puro.
- **agrees_with_regex:** True
- **divergence_reason:** None
- **addressed_hint:** Hint categoria: agent_llm_based. Confirmado pelo full-text.
- **evidence_sections:** ['Sec III (Framework + Performance Monitoring)', 'Sec IV (MCP tools, kubectl_scale, kubectl_delete_pod)', 'Sec V (Experimental Framework: K3s 7-node cluster, 3 IoT apps, chaos engineering)', 'Sec VI (Results: 52.9% diagnostic accuracy, 70.7% remediation success)']

---

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                                                       | location                              | rationale (neighbor not chosen)                                                                                                                                                 |
| ------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Edge-Cloud | "two cloud nodes, four edge nodes (two per edge site), and one management node"                                                                                                | §V-A Infrastructure and Cluster Setup | Not `Cloud-Only` because the testbed explicitly spans cloud and edge tiers with edge nodes participating in decisions. |
| decision                                    | Remediation                                      | "the agent identifies likely root causes and selects corrective actions—such as pod rescheduling, scaling, or configuration updates"                                           | §Abstract                             | _multi-select; the closed loop is triggered by SLA violations and executes fault-recovery actions, not steady-state scheduling/placement._                                      |
| agentic_configuration.decision_role         | Sole Decider                                     | "an LLM agent is triggered to investigate the underlying cause and execute an appropriate mitigation strategy"                                                                 | §I Introduction                       | Not `Pipeline Contributor` because the LLM agent both diagnoses and executes corrective tool calls without a downstream rule-based decider.                                     |
| agentic_configuration.coordination_topology | Single Agent                                     | "An LLM-powered control agent capable of investigating anomalies and executing infrastructure-level reconfiguration using tool calling and dynamic planning."                  | §I Introduction (contributions)       | Not `Multi-Agent` because one agent owns the full RCA + mitigation loop; no peer agents debate or coordinate.                                                                   |
| reasoning_approach                          | Iterative Reasoning                              | "Influenced by the React framework [14], which interleaving reasoning and acting in a more interactive manner"                                                                 | §IV (Agent design)                    | _ReAct-style interleaved reasoning + tool calls + replanning; not bare prompting, no external KB retrieval, no fine-tuning._                                                    |
| autonomy_level                              | Autonomous                                       | "this is the first LLM-driven agentic system that not only identifies root causes of SLA violations but also autonomously mitigates them through infrastructure-level actions" | §I Introduction                       | Not `Supervised` because the closed loop executes kubectl actions without HITL approval.                                                                                        |
| metric                                      | RM Performance Metric + Agent Performance Metric | "Results show that the agent identifies SLA violations with 52.9% accuracy and mitigates 70.7% of them successfully."                                                          | §Abstract                             | _multi-select; mitigation success (RM) and reasoning rounds / wall-clock per recovery (agent-side) are both reported._                                                          |
| evaluation_method                           | Practical Testbed                                     | "Cluster management and workload scheduling are handled by a k3s Kubernetes distribution deployed on top of QEMU-virtualized servers."                                         | §V-A Infrastructure and Cluster Setup | Not `Simulation` because workloads run on a virtualized K3s cluster with chaos injection on real Kubernetes — not an event-driven simulator.                                    |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Remediation`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Edge-Cloud`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Iterative Reasoning`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Practical Testbed`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Sole Decider`.
