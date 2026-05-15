---
id: paper-2700
title: Large Language Model-Empowered Energy-Efficient Multi-UAV-Assisted MEC Heterogeneous
  Networks
authors:
- Lv, Ke
- Huang, Sai
- Yao, Yuanyuan
- Jiang, Weiwei
- Feng, Zhiyong
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2026
doi: 10.1109/TCCN.2025.3645407
url: https://www.scopus.com/pages/publications/105025456015?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5281--5294
keywords:
- Artificial general intelligence
- deep reinforcement learning
- large language model
- mobile edge computing
- unmanned aerial vehicle
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
  06-full-text-screening: exclude
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
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: O LLM aparece em papel de suporte (gera heurísticas, embeddings,
      features ou recompensas para RL/MARL/otimização clássica). Não há loop agentic
      AI dirigindo decisão de RM.
    winning_category: H_llm_supports_other_method
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: "LLM gera reward design e orientações pré-treinamento para o agente D3QN, decisor de RM em multi-UAV MEC. LLM subordinado ao RL — exclui per Gate B."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2700 — Large Language Model-Empowered Energy-Efficient Multi-UAV-Assisted MEC Heterogeneous Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The artificial general intelligence (AGI) based on large language models (LLMs) and deep reinforcement learning (DRL) possesses cross-domain empowerment capabilities, offering task scheduling and resource allocation in mobile edge computing (MEC), presenting significant potential. This paper proposes an LLM-driven DRL framework named L2D2, which autonomously generates reward functions for DRL through LLMs and enables dynamic model optimization through a self-refinement loop mechanism. The reward function within the L2D2 framework can adjust the strategy based on environmental feedback, eliminating the need for manual redesign in complex low-altitude scenarios and reducing debugging costs. To validate the performance of L2D2, the framework is utilized in a multi-unmanned aerial vehicle (UAV)-assisted MEC heterogeneous network operating in the low-altitude airspace to enhance system energy efficiency. A novel dueling double deep Q-network (D3QN) is utilized as the DRL method within L2D2, named the L2D2-D3QN algorithm. To evaluate its effectiveness in enhancing system energy efficiency, a comprehensive comparison is conducted across various LLMs, including Deepseek-R1, GPT-4o, Llama-3.1-70B, Claude-3.7-Sonnet, and Qwen-2.5. The simulation results demonstrate that the L2D2-D3QN algorithm achieves up to 56% higher energy efficiency compared to DRL with human-designed reward function. Furthermore, the influence of LLM tokenization strategies on the performance of LLM-driven DRL is also explored. © 2015 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: llm_as_feature_extractor, matched_substring: "LLM-Empowered Reward Design" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "DRL with LLM" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Empowered" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** LLM gera reward design e orientações pré-treinamento para o agente D3QN, decisor de RM em multi-UAV MEC. LLM subordinado ao RL — exclui per Gate B.
- **agrees_with_regex:** True
- **addressed_hint:** support — LLM apenas suporta RL via reward engineering
- **evidence_sections:** ['IV.B: LLM-Empowered Reward Design', 'Algorithm 1: D3QN without LLM in closed loop']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
