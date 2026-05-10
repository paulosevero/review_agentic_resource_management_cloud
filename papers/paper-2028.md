---
id: paper-2028
title: LLM-based cost-aware task scheduling for cloud computing systems
authors:
- Pei, Haoran
- Gu, Yan
- Sun, Yajuan
- Wang, Qingle
- Liu, Cong
- Chen, Xiaomin
- Cheng, Long
venue: Journal of Cloud Computing
venue_type: journal
year: 2025
doi: 10.1186/s13677-025-00822-0
url: https://www.scopus.com/pages/publications/105026116476?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: ''
keywords:
- Cloud computing
- Deep reinforcement learning
- Large language models
- Task scheduling
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_llm_modifier
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_cls_llm_present
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2028 — LLM-based cost-aware task scheduling for cloud computing systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings. © The Author(s) 2025.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_llm_modifier']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: llm_as_workload, pattern_id: ovr_llm_modifier, matched_substring: "LLM-based" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings." }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "RESEARCH:  LLM-based cost-aware task scheduling for cloud computing systems: Haoran Pei 1 , Yan Gu 1 , Yajuan Sun 2\* , Qingle Wang 1 , Cong Liu 3 , Xiaomin Chen 4 and Long Cheng 1,2 Abstract: Cloud task scheduling faces significant challenges due to resource heterogeneity, conflicting optimization objectives, and dynamic workload fluctuations. Traditional heuristic algorithms often necessitate comprehensive knowledge of environmental parameters, significantly constraining their efficacy in dynamic cloud computing environments. While Deep Reinforcement Learning (DRL) methods have shown promise in intelligent scheduling via continuous environment interaction, they suffer from limited generalization to diverse cloud scenarios and lack decision interpretability. To address these shortcomings, this paper proposes LarS, a scheduling framework that employs Large Language Models (LLMs) as high-level decision agents for cloud task scheduling. In LarS, DRL agents trained in carefully chosen representative cloud environments generate a high-quality dataset of scheduling decisions, which is used to fine-tune an LLM. By jointly optimizing average response time, task success rate, and average rental cost, LarS achieves strong generalization across heterogeneous cloud deployments. Experimental results demonstrate that LarS surpasses current approaches in average response time, success rate, and average cost, and maintains strong generalization performance under varied experimental settings." }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "To address these challenges, we propose LarS, a cloud task scheduling framework that leverages an LLM as a high-level decision agent. In LarS, GPT-4o generates scheduling decisions with reasoning trajectories for given environments and states. Trained DRL agents evaluate these trajectories, and only the validated ones are retained to form a high-quality dataset. This dataset is then used to fine-tune the LLM via LoRA, enhancing its generalization capability and enabling optimization of cost and QoS across diverse cloud environments. In summary, the key contributions of this paper are as follows:" }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "- We propose a hybrid data generation pipeline where GPT-4o produces reasoning trajectories and DRL agents serve as evaluators to curate high-quality supervision data." }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "| LarS      | DQN+LLM                         | ✓              | ✓              | ✓                    | Large language models for cloud task scheduling: The rapid advancement of LLMs has created opportunities for addressing complex optimization problems, including scheduling tasks, by leveraging their powerful sequence modeling and reasoning capabilities. Recent studies demonstrate that LLMs, pretrained on extensive corpora, can effectively learn intricate scheduling constraints and objectives. For example, Abgaryan et al. [25] demonstrated that with minimal fine-tuning techniques like LoRA, LLMs achieve competitive performance on static job shop scheduling problems. Krishnamurthy and Shiva propose an LLM-guided approach using a SARSA reinforcement learning agent for dynamic task scheduling in the cloud [14]. Similarly, Tang et al. [24] developed a scheduling expert dataset to fine-tune a lightweight LLM for task assignment decisions in multi-cloud environments, showing that LLM-based agents can learn effective scheduling policies from expert demonstrations. However, current LLM-based schedulers primarily operate in offline or semi-static contexts, providing heuristic guidance or refining existing solutions rather than participating in the continuous, real-time decision-making required for dynamic cloud environments [26]." }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "We summarize the related works mentioned above in Table 1. While task scheduling has been extensively studied, traditional heuristic methods often lack flexibility and adaptability to dynamic conditions. DRLbased schedulers, though adaptive, suffer from limited generalization and high computational costs. Existing LLM-driven approaches exhibit strong generalization capabilities, yet they have not fully demonstrated their potential in handling online adaptive scheduling scenarios with streaming workloads and evolving objectives. To remedy these shortcomings, this paper proposes LarS, an effective framework that leverages LLM as cloud task scheduling agent to achieve adaptive, explainable, and efficient cloud task scheduling." }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
