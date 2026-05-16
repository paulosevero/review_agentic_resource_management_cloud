---
id: paper-2723
title: "AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks"
authors:
  - Moreira, Rodrigo
  - Rodrigues Moreira, Larissa Ferreira
  - Leone Maciel Peixoto, Maycon
  - de Oliveira Silva, Flávio
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2026.3672699
url: https://www.scopus.com/pages/publications/105032804808?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 43519--43532
keywords:
  - Agentic
  - B5G
  - energy-aware
  - intents
  - MEC
  - monitoring
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
      - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
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
    my_justification:
      "AGORA implementa agentic loop explícito (§III.B). LLM-backed
      agent: percebe estado infra → traduz intents (§III.C) → decide orchestration
      (scheduling/routing/slicing/scaling, §III.E) → atua. Avaliação (§V) mede comportamento
      agent-driven (energy-QoS tradeoff). Regex hint ('devops') não procede; core
      é resource management (energy + QoS), não incident triage. Boundaries A+B satisfeitos."
    agrees_with_regex: false
    divergence_reason:
      Regex pattern 'D_devops_or_logs_not_rm' inadequado. AGORA foca
      orquestração de recursos (energy-QoS) dirigida por agente LLM, não análise de
      logs/RCA.
    locked_at_iteration: null
    locked_at: null
taxonomy:
  infrastructure: Edge-Cloud
  decision:
    - Routing & Slicing
    - Scaling
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

# paper-2723 — AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Effective management and operational decision-making for complex mobile network systems present significant challenges, particularly when addressing conflicting requirements such as efficiency, user satisfaction, and energy-efficient traffic steering. The literature presents various approaches aimed at enhancing network management, including the Zero-Touch Network (ZTN) and Self-Organizing Network (SON); however, these approaches often lack a practical and scalable mechanism to consider human sustainability goals as input, translate them into energy-aware operational policies, and enforce them at runtime. In this study, we address this gap by proposing the AGORA: Agentic Green Orchestration Architecture for Beyond 5G Networks. AGORA embeds a local tool-augmented Large Language Model (LLM) agent in the mobile network control loop to translate natural-language sustainability goals into telemetry-grounded actions, actuating the User Plane Function (UPF) to perform energy-aware traffic steering. The findings indicate a strong latency-energy coupling in tool-driven control loops and demonstrate that compact models can achieve a low energy footprint while still facilitating correct policy execution, including non-zero migration behavior under stressed Multi-access Edge Computing (MEC) conditions. Our approach paves the way for sustainability-first, intent-driven network operations that align human objectives with executable orchestration in Beyond-5G infrastructures. © 2013 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Agentic" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
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
  - `{ category: D_devops_or_logs_not_rm, pattern_id: devops_logs_incidents, matched_substring: "root cause analysis" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** AGORA implementa agentic loop explícito (§III.B). LLM-backed agent: percebe estado infra → traduz intents (§III.C) → decide orchestration (scheduling/routing/slicing/scaling, §III.E) → atua. Avaliação (§V) mede comportamento agent-driven (energy-QoS tradeoff). Regex hint ('devops') não procede; core é resource management (energy + QoS), não incident triage. Boundaries A+B satisfeitos.
- **agrees_with_regex:** False
- **divergence_reason:** Regex pattern 'D_devops_or_logs_not_rm' inadequado. AGORA foca orquestração de recursos (energy-QoS) dirigida por agente LLM, não análise de logs/RCA.
- **addressed_hint:** networks flagged, mas escopo é B5G orchestration (continuum edge-MEC), não telecom puro.
- **evidence_sections:** ['III.B Agentic Control Loop (explicit loop diagram)', 'III.C Intent Suite and Classification (intent→decision)', 'III.E Policy and Decision Compliance', 'V Results on energy-QoS characterization of agents']

## 07 — Taxonomy

### 07b — Final classification

| axis                                        | value                                            | evidence                                                                                                                                                                                     | location                                  | rationale (neighbor not chosen)                                                                                                                                                              |
| ------------------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| infrastructure                              | Edge-Cloud                             | "decisions must span heterogeneous domains, including the data plane, Multi-access Edge Computing (MEC), and the 5G core"                                                                    | §I Introduction                           | Not `Cloud-Only` because AGORA targets the 5G core + MEC continuum with UPF steering across edge sites.                                                                                      |
| decision                                    | Routing & Slicing + Scaling                      | "actuating the User Plane Function (UPF) to perform energy-aware traffic steering"                                                                                                           | §Abstract                                 | _multi-select; UPF-level routing/slicing is the primary action, and the policy includes migration to alternate MEC sites under energy stress — together routing + service-instance scaling._ |
| agentic_configuration.decision_role         | Sole Decider                                     | "AGORA embeds a local tool-augmented Large Language Model (LLM) agent in the mobile network control loop to translate natural-language sustainability goals into telemetry-grounded actions" | §Abstract                                 | Not `Pipeline Contributor` because the agent itself selects and executes the UPF action; no downstream rule-based decider.                                                                   |
| agentic_configuration.coordination_topology | Single Agent                                     | "We deploy free5GC, a 5G core, to provide end-to-end connectivity... The user plane is anchored at a UPF that exposes a simple control interface used by the agent"                          | §IV-C 5G Core and MEC Setup               | Not `Multi-Agent` because one LLM agent owns the closed-loop perceive-reason-act path.                                                                                                       |
| reasoning_approach                          | Iterative Reasoning                              | "Leveraging an Large Language Model (LLM), the agentic framework can perform reasoning and planning, use tools, manage memory, and collaborate with other agents"                            | §I Introduction                           | _tool-augmented iterative reasoning over telemetry-grounded tool calls; not bare prompting, not RAG over a knowledge base, no fine-tuning._                                                  |
| autonomy_level                              | Autonomous                                       | "an agentic LLM driven closed-loop architecture that translates natural language intents into telemetry-grounded tool calls and UPF routing actions"                                         | §I Introduction (contributions)           | Not `Supervised` because the loop executes UPF actions without HITL approval after the operator declares intent.                                                                             |
| metric                                      | RM Performance Metric + Agent Performance Metric | "an experimental comparison of multiple local LLMs, including a non-English capable model, quantifying energy footprint, latency, and migration behavior"                                    | §I Introduction (contributions)           | _multi-select; energy / latency / migration (RM side) and per-LLM behaviour (agent side) are jointly reported._                                                                              |
| evaluation_method                           | Practical Testbed | "All experiments were conducted on the FABRIC testbed [40] using an OpenStack-based compute node"                                                                                            | §IV-B Infrastructure and Compute Platform | Not `Simulation` because experiments run on the FABRIC testbed with free5GC and MEC on OpenStack compute, not on a simulator.             |

**Confidence (weakest axis):** HIGH
**Adversarial mode:** off

---

## 08 — Analysis contributions

- `decision-distribution` (anchor: `RQ2.1`) — contributes: `Routing & Slicing`, `Scaling`.
- `autonomy-distribution` (anchor: `RQ2.2`) — contributes: `Autonomous`.
- `infrastructure-distribution` (anchor: `RQ1.2`) — contributes: `Edge-Cloud`.
- `reasoning-distribution` (anchor: `RQ3.1`) — contributes: `Iterative Reasoning`.
- `evaluation-distribution` (anchor: `RQ4.1`) — contributes: `Practical Testbed`.
- `metric-distribution` (anchor: `RQ4.2`) — contributes: `RM Performance Metric`, `Agent Performance Metric`.
- `agent-coordination-distribution` (anchor: `RQ1.1`) — contributes: `Single Agent`.
- `decision-role-distribution` (anchor: `RQ1.3`) — contributes: `Sole Decider`.
- `agentic-config-cross` (anchor: `RQ1.1`) — contributes: `Sole Decider` × `Single Agent`.
- `infrastructure-by-decision` (anchor: `RQ1.2`) — contributes: `Routing & Slicing` × `Edge-Cloud`, `Scaling` × `Edge-Cloud`.
- `decision-by-autonomy` (anchor: `RQ2.2`) — contributes: `Routing & Slicing` × `Autonomous`, `Scaling` × `Autonomous`.
