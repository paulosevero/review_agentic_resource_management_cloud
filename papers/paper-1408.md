---
id: paper-1408
title: Intelligent Kubernetes Scheduling with Large Language Models
authors:
- Bai, Xinyu
- Tang, Zhiqing
- Yao, Zhi
- Chen, Yao
- Guo, Jianxiong
- Wang, Tian
- Jia, Weijia
venue: Proceedings - 2025 IEEE International Conference on Security, Privacy, Anonymity in Computation and Communication and Storage, SpaCCS 2025
venue_type: conference
year: 2025
doi: 10.1109/SpaCCS67922.2025.00012
url: https://www.scopus.com/pages/publications/105033212483?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 16--23
keywords:
- Edge computing
- Large Language Models
- Scheduling
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_with_llm
    - ovr_using_llm
    - ovr_llm_modifier
    - ovr_llm_as_judge
    - ovr_intent_driven
    - ovr_abs_llm_decides
    - ovr_abs_llm_orchestrates
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: "LLMScheduler (Seção IV) posiciona o LLM como participante ativo do ciclo de scheduling: pontua nós candidatos e seleciona o ótimo em tempo real para o cluster Kubernetes heterogêneo. Loop perceive→reason→act explícito — LLM recebe estado real do cluster e dos pods pendentes, raciocina sobre constraints e objetivos, emite decisão de binding pod→node. HybridScheduler complementa: LLM gera offline strategic intents que parametrizam a scoring function de produção, padrão análogo ao anchor paper-1644. Avaliação (Seção V) mostra +7% scheduling success rate em alta contenção e latência ms-level no HybridScheduler. Escopo Kubernetes em edge computing confirmado."
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1408 — Intelligent Kubernetes Scheduling with Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The impressive natural language understanding and inference abilities of recent Large Language Models (LLMs) have enabled their use in scheduling tasks. Existing scheduling methods often neglect the integration of LLMs with schedulers. To fill in such gaps and address complex scheduling challenges in heterogeneous Kubernetes clusters, we propose two LLM-based approaches. Specifically: 1) LLMScheduler, an adaptive online scheduling framework in which the LLM actively participates in decision-making. It scores candidate nodes and selects the optimal one in real time for the clusters. 2) HybridScheduler, an offline intelligence injection framework that leverages LLMs to proactively generate strategic intents for the scoring function, informed by job profiles and node configurations. It then rapidly scores and selects nodes, similar to a traditional Kubernetes scheduler. 3) We validate our methods with large-scale simulations, demonstrating that LLMScheduler improves scheduling success rates by up to 7% on average compared to the best traditional scheduler, particularly under extreme cluster pressure. Moreover, HybridScheduler consistently outperforms all traditional heuristics in high-contention scenarios, while reliably maintaining millisecond-level decision latency. Our experimental results offer a quantitative foundation for designing future AI-driven systems that balance performance, latency, and cost. © 2025 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_with_llm', 'ovr_using_llm', 'ovr_llm_modifier', 'ovr_llm_as_judge', 'ovr_intent_driven', 'ovr_abs_llm_decides', 'ovr_abs_llm_orchestrates', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "LLMs elegantly bypass this training" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models 
 The impressive natural language understanding and inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference abilities of recent Large Language Models (LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference abilities of recent Large Language Models (LLMs" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: agent_llm_based, pattern_id: agent_llm_combo, matched_substring: "Furthermore, the impracticality of the online approach presents our second research challenge: How t" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** LLMScheduler (Seção IV) posiciona o LLM como participante ativo do ciclo de scheduling: pontua nós candidatos e seleciona o ótimo em tempo real para o cluster Kubernetes heterogêneo. Loop perceive→reason→act explícito — LLM recebe estado real do cluster e dos pods pendentes, raciocina sobre constraints e objetivos, emite decisão de binding pod→node. HybridScheduler complementa: LLM gera offline strategic intents que parametrizam a scoring function de produção, padrão análogo ao anchor paper-1644. Avaliação (Seção V) mostra +7% scheduling success rate em alta contenção e latência ms-level no HybridScheduler. Escopo Kubernetes em edge computing confirmado.
- **agrees_with_regex:** True


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
