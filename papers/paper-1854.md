---
id: paper-1854
title: 'Leveraging Large Language Models for Network Security: A Multi-Expert Approach'
authors:
- Lin, Tianshun
- Xu, Changgui
- Zhang, Jianshan
- Lin, Nan
- Liu, Yuxin
- Zheng, Yuanjun
venue: Internet Technology Letters
venue_type: journal
year: 2025
doi: 10.1002/itl2.70016
url: https://www.scopus.com/pages/publications/105000820043?origin=resultslist
publisher: John Wiley and Sons Inc
pages: ''
keywords:
- deep reinforcement learning
- industrial edge computing
- large language models
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource
      management signal); C3=0.5 (infra/cloud-edge signal)
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
    my_justification: "LLM atua como gate network roteando entre policies expert do DRL multi-expert — o RL ainda é o executor final das policies. LLM subordinado ao RL — exclui per Gate B."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1854 — Leveraging Large Language Models for Network Security: A Multi-Expert Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The optimization of diverse industrial edge computing tasks presents a significant challenge due to the dynamic and heterogeneous nature of industrial operational demands. While deep reinforcement learning (DRL) has shown promise, task-specific DRL models are often required in complex industrial edge networks, such as real-time anomaly detection and latency-sensitive decision-making, increasing computational overhead. This leads to large computational overheads, unstable performance, and increased energy consumption. Such a cost has become a concern in resource-limited industrial edge networks. In this paper, we propose a novel multi-expert optimization approach with the help of powerful large language models (LLMs). Our goals are to dynamically interpret industrial task requirements, activate specialized DRL experts, and synthesize their outputs into context-aware decisions. Specifically, we replace conventional gate networks with an LLM-based orchestrator. LLMs provide the benefits of semantic reasoning and contextual understanding when managing expert selection and collaboration. This approach eliminates the need to train unique DRL models for each industrial optimization task, thereby reducing deployment costs and improving scalability. Our experiments indicate that our approach achieves 13% higher anomaly detection accuracy when compared with traditional DRL methods. © 2025 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-empowered" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Empowered" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-empowered" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-empowered" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-empowered" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** LLM atua como gate network roteando entre policies expert do DRL multi-expert — o RL ainda é o executor final das policies. LLM subordinado ao RL — exclui per Gate B.
- **agrees_with_regex:** True
- **addressed_hint:** Pre-flagged hint='support' procede: LLM governa seleção de expert (gating), DRL especialista toma ação.
- **evidence_sections:** ['Introduction § Critical bottleneck / task-specific customization', 'LLM-Based Orchestration § How can ... adaptive optimizations', 'Multiple Experts § LLM-based orchestrator']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
