---
id: paper-2854
title: 'Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation'
authors:
- Wu, Bing
- Zou, Sai
- Liwang, Minghui
- Ni, Wei
- Wang, Xianbin
- Tian, Youliang
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3678546
url: https://www.scopus.com/pages/publications/105034780951?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 6 G edge intelligence
- application intent
- knowledge distillation
- knowledge graph
- large language model
- network service request
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
      management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_justification: 'Paper propõe pipeline LLM para traduzir intents (APPIs) em
      network service requests (NSRs) via knowledge graphs, mas foco é network automation
      em 6G—não resource management em cloud/edge/continuum. Motivação: intent-driven
      network management (seção I), não scheduling/placement/scaling. Mesmo com LLM+KG
      grounding, domínio é strictly RAN/6G, fora scope (§boundary C: out-of-scope
      unless edge node in continuum).'
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2854 — Toward 6G Edge Intelligence: Lightweight LLMs for Intent-Driven Network Automation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Future 6 G networks are envisaged to tightly integrate communication, sensing, and computing, demanding real-time, intent-driven intelligence at the edge. While large language models (LLMs) excel in intent recognition and semantic reasoning, their application to real-time network lifecycle management at the edge is limited by heterogeneous application intents (APPIs), dynamic network conditions, and severe resource constraints. This paper proposes a novel lightweight LLM architecture, KGLlama-KD, that synergizes knowledge graphs (KGs) with knowledge distillation (KD) to enable intent-driven networking and enhance 6 G edge intelligence. Specifically, a KG is constructed to formally describe the relationships among application scenarios, functional primitives, performance requirements within APPIs, and the correspondences between APPIs and network service requests (NSRs), thereby producing a structured intent training dataset. Building upon the Llama 3 foundation model, a two-phase optimization framework is designed to support lightweight edge deployment while preserving translation fidelity. The LLM is first fine-tuned with KG guidance and compressed via KD in the cloud, and then deployed on resource-constrained edge nodes to perform real-time, accurate, and efficient APPIs interpretation. Experiments validate that KGLlama-KD achieves 95% accuracy for APPI understanding, surpassing DeepSeek and Qwen by an average of 8%. The distilled model reduces inference latency by 60% compared to full-scale LLMs, fulfilling the sub-100 ms requirement for 6 G latency-sensitive services. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Intent-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "intent-driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
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
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-empowered" }`
  - `{ category: H_llm_supports_other_method, pattern_id: hybrid_llm_rl_llm_subordinate, matched_substring: "LLM-Enhanced" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Paper propõe pipeline LLM para traduzir intents (APPIs) em network service requests (NSRs) via knowledge graphs, mas foco é network automation em 6G—não resource management em cloud/edge/continuum. Motivação: intent-driven network management (seção I), não scheduling/placement/scaling. Mesmo com LLM+KG grounding, domínio é strictly RAN/6G, fora scope (§boundary C: out-of-scope unless edge node in continuum).
- **agrees_with_regex:** True
- **addressed_hint:** networks — intent translation é tarefa de rede 6G/RAN, não decisão de RM em infra cloud/edge.
- **evidence_sections:** ['Abstract: APPIs→NSRs translation for 6G intent-driven management', 'I. Intro: closed-loop autonomy for 6G, not cloud/edge resource allocation', 'II.A: Studies on APPIs in networking context (SDN, 5G slicing)']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
