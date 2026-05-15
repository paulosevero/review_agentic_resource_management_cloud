---
id: paper-2362
title: 'AutoHMA-LLM: Efficient Task Coordination and Execution in Heterogeneous Multi-Agent
  Systems Using Hybrid Large Language Models'
authors:
- Yang, Tingting
- Feng, Ping
- Guo, Qixin
- Zhang, Jindi
- Zhang, Xiufeng
- Ning, Jiahong
- Wang, Xinghan
- Mao, Zhongyang
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TCCN.2025.3528892
url: https://www.scopus.com/pages/publications/105002485279?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 987--998
keywords:
- cloud computing
- communication coordination
- dynamic task allocation
- Generative AI
- heterogeneous multi-agent system (HMAS)
- large language model (LLM)
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource
      management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_with_llm
    - ovr_using_llm
    - ovr_llm_modifier
    - ovr_llm_agents
    - ovr_abs_llm_decides
    - ovr_abs_llm_orchestrates
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: "Reanálise com critério mais flexível: AutoHMA-LLM coordena multi-agentes heterogêneos via LLM para task coordination/execution. Considerando que ambientes heterogêneos podem mapear a edge/cloud e o LLM exerce papel material na coordenação, inclusão por flexibilidade. Anotada como candidata a verificação fina de domínio."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2362 — AutoHMA-LLM: Efficient Task Coordination and Execution in Heterogeneous Multi-Agent Systems Using Hybrid Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Heterogeneous multi-agent systems (HMAS) comprise various intelligent agents with specialized functions, such as drones, ground robots, and automated devices, working in coordinated settings. This paper presents AutoHMA-LLM, a novel framework that combines Large Language Models (LLMs) with classical control algorithms to address the challenges of task coordination and scheduling in complex, dynamic environments. The framework is designed with a multi-tier architecture, utilizing a cloud-based LLM as the central planner alongside device-specific LLMs and Generative Agents to improve task execution efficiency and accuracy. Specifically targeting dynamic scenarios, the system enhances resource utilization and stabilizes task execution through refined task scheduling and real-time feedback mechanisms. In experiments conducted across logistics, inspection, and search & rescue scenarios, AutoHMA-LLM demonstrated a 5.7% improvement in task completion accuracy, a 46% reduction in communication steps, and a 31% decrease in token usage and API calls compared to baseline methods. These results highlight our framework’s scalability and efficiency, offering substantial support for effective multi-agent collaboration in complex, resource-constrained environments. © 2015 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening


### iter-0 (initial classification)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_llm_modifier', 'ovr_llm_agents', 'ovr_abs_llm_decides', 'ovr_abs_llm_orchestrates', 'ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "Deployment structure of the AutoHMA-LLM" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_abs_llm_infra, matched_substring: "LLM system" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_abs_llm_infra, matched_substring: "LLM system" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_ppo, matched_substring: "MA-PPO" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "In Section I, the paper introduces the background of heterogeneous multi-agent systems and briefly s" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "## A. Multiagent Deep Reinforcement Learning" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "Multiagent Deep Reinforcement Learning (MARL) [9] has enhanced agent capabilities in various jobs, s" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "models could be better in actual simulation experiments. The reason is that the large models are rel" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Reanálise com critério mais flexível: AutoHMA-LLM coordena multi-agentes heterogêneos via LLM para task coordination/execution. Considerando que ambientes heterogêneos podem mapear a edge/cloud e o LLM exerce papel material na coordenação, inclusão por flexibilidade. Anotada como candidata a verificação fina de domínio.
- **agrees_with_regex:** True
- **addressed_hint:** Hint 'support' não procedia. LLM não é suporte a outro método — é central planner dirigindo dynamic task allocation + scheduling + communication coordination em multi-agent system.
- **evidence_sections:** ["Abstract: 'task coordination and scheduling in complex, dynamic environments'", "Section I: LLM for 'communication coordination, dynamic task decomposition, and scheduling'", 'Section III (System Definition): multi-tier architecture with Cloud LLM planner + Device LLM + Generative Agents', 'Section V.B–E: Task completion accuracy, communication steps, token usage metrics (RM outcomes)']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
