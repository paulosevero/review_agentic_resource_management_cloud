---
id: paper-2595
title: Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud
  Collaboration
authors:
- He, Xinxin
- Yang, Yang
- Yang, Zhiyong
- Gao, Yifei
- Yin, Changchuan
- Chen, Shanzhi
venue: IEEE Communications Magazine
venue_type: journal
year: 2026
doi: 10.1109/MCOM.001.2500421
url: https://www.scopus.com/pages/publications/105031504551?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 34--41
keywords:
- Agents
- Autonomous agents
- Behavioral research
- Cloud computing architecture
- Decision making
- Dynamics
- Highway administration
- Highway planning
- Intelligent agents
- Life cycle
- Natural resources management
- Network architecture
- Resource allocation
- Road vehicles
- Roads and streets
- Agent based
- Architecture management
- Cloud agents
- Collaborative systems
- Dynamic resources
- Intelligence models
- Management method
- Multi tasks
- Resource management
- Resources allocation
- Global optimization
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: include
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource
      management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: LLM as workload
    winning_category: llm_as_workload
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_abs_llm_orchestrates
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: Paper apresenta agent-based architecture com cloud agent, RSU
      agents, e vehicle agents que coletam telemetria (state), usam D-LAM e DM-LAM
      (large AI models com sequence modeling) para inferência e decision-making em
      tempo real, e atuam sobre alocação de recursos (task offloading, power allocation).
      Loop perceive→(telemetry)→reason(LAM inference)→act(resource allocation) está
      claramente descrito (§Workflow, §Multi-layer architecture). Satisfaz RQ1 (arquitetura),
      RQ2 (task offloading como decisão delegada), RQ3 (reasoning via LAM com RAG/multi-scenario
      dataset), RQ4 (avaliação em IoV scenarios).
    agrees_with_regex: true
    divergence_reason: 'regex classificou como ''networks'' (hint exclude), mas paper
      é claramente agentic-RM: describe loop completo perceive-reason-act com LAM
      dirigindo decisões de RM em edge-cloud-vehicle continuum.'
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2595 — Agent-Based Network Architecture and Resource Management for Vehicle-Road-Cloud Collaboration

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large artificial intelligence models (LAMs) have introduced new opportunities to 6G networks, whereas their integration into vehicle-road-cloud collaborative systems remains challenging due to insufficient model coordination and difficulties in dynamic resource adaptation. To address these issues, this article proposes an agent-based network architecture and a resource management method for vehicle-road-cloud collaboration. In this architecture, the cloud agent conducts largescale pretraining to characterize global resource allocation dynamics, while lightweight models are deployed at the road-side unit (RSU) agent and vehicle agent to enable real-time inference and decision-making. To balance model performance and resource consumption, we introduce a lifecycle management strategy for the agent network. By analyzing the relationship between performance gain and the consumption of communication and computation resources, we jointly optimize training data sampling rates, model pruning ratio, and resource allocation strategies. This enables dynamic adjustment of the update frequency for cloud-based large models and the fine-tuning frequency for edge-side models, thereby ensuring continuous and high-efficiency model inference in resource-constrained dynamic scenarios. Additionally, we design a decision LAM (D-LAM) for single-task scenarios, which employs sequence modeling and temporal embedding to achieve dynamic coordination of multidimensional resources. We further develop a decision multitask LAM (DM-LAM) to address complex multitask scenarios, which integrates a mixture-of-experts (MoE) mechanism with a gating network to support both personalized resource allocation for individual tasks and global optimization across heterogeneous tasks. Experimental results demonstrate that the proposed method significantly improves resource utilization efficiency and achieves 10±$1.2% higher task completion rates compared to decision transformer model.  © 2026 IEEE.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "LLM as workload"
- **winning_category:** 'llm_as_workload'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "transformer" }`
  - `{ category: llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "large models and the fine-tuni" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_abs_llm_orchestrates', 'ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "large models and the fine-tuning" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "large models and the fine-tuning" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "With the advent of the 6G era, integrating AI into network ecosystems and constructing natively inte" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "task To address diverse requirements across these applications, such as minimizing task latency, max" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "strat MultI-scenArIo dAtAset curAtIon And AggregAtIon To accommodate diverse vehicular scenarios wit" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "To validate the model's generalization capacity, we conducted the experiment under diverse scenarios" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Paper apresenta agent-based architecture com cloud agent, RSU agents, e vehicle agents que coletam telemetria (state), usam D-LAM e DM-LAM (large AI models com sequence modeling) para inferência e decision-making em tempo real, e atuam sobre alocação de recursos (task offloading, power allocation). Loop perceive→(telemetry)→reason(LAM inference)→act(resource allocation) está claramente descrito (§Workflow, §Multi-layer architecture). Satisfaz RQ1 (arquitetura), RQ2 (task offloading como decisão delegada), RQ3 (reasoning via LAM com RAG/multi-scenario dataset), RQ4 (avaliação em IoV scenarios).
- **agrees_with_regex:** True
- **divergence_reason:** regex classificou como 'networks' (hint exclude), mas paper é claramente agentic-RM: describe loop completo perceive-reason-act com LAM dirigindo decisões de RM em edge-cloud-vehicle continuum.
- **addressed_hint:** networks flag não procede — apesar do contexto 6G/V2X, o foco é agentic AI para resource management, não telecom/network slicing per se
- **evidence_sections:** ['§Multi-layer collaborative resource management architecture — descreve cloud agent, RSU agent, vehicle agent layers', '§Multi-scenario Dataset Curation — estado (CSI, topologia, recursos, comportamento veicular)', '§Model Pre-training And Multi-dimensional Assessment — D-LAM e DM-LAM realizam decision-making em tempo real', '§Decision-making — agents decidem sobre task offloading, power allocation, model fine-tuning schedules']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
