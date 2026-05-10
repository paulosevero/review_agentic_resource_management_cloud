---
id: paper-2600
title: 'GenAI-5GS Fusion Approach: A New Path for Enhancing Computation Offloading
  Efficiency of Complex Tasks in Internet of Vehicles'
authors:
- He, Chao
- Jiang, Wenhui
- Wang, Xing
- Wang, Wanting
- Na, Hong
- Xie, Xin
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2026.3660468
url: https://www.scopus.com/pages/publications/105029867800?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- 5G Slicing
- Complex Task Offloading
- Generative Adversarial Network
- Graph Neural Network
- Internet of Vehicles
- Mobile Edge Computing
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
      management signal); C3=0 (no infra signal)
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
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Paper propõe Graph-GAN vehicle trajectory prediction integrado
      com 5G resource slicing para task offloading em IoV/MEC. GAI (Generative AI
      / GAN) é usada apenas para trajectory prediction (input); a decisão de offloading/slicing
      segue modelo de otimização clássico (delay model, modulation schemes, bandwidth
      allocation). Não há agentic loop — GAI não dirige o raciocínio de RM. Loop de
      decisão é determinístico/otimizado, não autônomo reasoning+acting de agente.
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2600 — GenAI-5GS Fusion Approach: A New Path for Enhancing Computation Offloading Efficiency of Complex Tasks in Internet of Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advancement of real-time communication and data interaction technologies in the Internet of Vehicles (IoV), the pivotal role of Mobile Edge Computing (MEC) in optimising vehicle service efficiency has become increasingly prominent. However, existing task offloading strategies still present significant room for improvement in handling complex tasks, delay control, and resource allocation for Roadside Units (RSUs). To reduce task offloading delay and enhance resource utilization, this paper proposes an offloading method integrating Generative Artificial Intelligence (GAI) with 5G Slicing (GenAI-5GS). First, a Graph-GAN-based vehicle trajectory prediction model is constructed. Operating with CPU/GPU utilization below 50% on resource-constrained RSUs, it enables precise prediction of vehicle movements to support proactive RSU deployment. Secondly, it innovatively integrates 5G slicing technology to dynamically allocate Resource Blocks (RB) within the dedicated 5.9GHz IoV band. By combining multiple Modulation and Coding Schemes (MCS) to accommodate tasks of varying priorities, which enables slicing-based management and flexible resource allocation for RSUs. Finally, research findings demonstrate that the proposed method enhances trajectory prediction accuracy and resource utilization while reducing offloading delay, all while safeguarding multi-dimensional Quality of Service (QoS) requirements. Furthermore, this approach significantly improves IoV complex task processing performance and system stability, delivering safer and more efficient service experiences for in-vehicle users, thereby possessing clear engineering deployment value. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Generative Artificial Intellig" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GenAI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Generative Artificial Intellig" }`
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "To optimise delay and energy consumption, researchers often use methods such as reinforcement learni" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "- [22] Q. Cui, X. Zhao, W. Ni et al., 'Multi-Agent Deep Reinforcement Learning" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "Agent" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative Artificial Intelligence" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative Artificial Intelligence" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai_full, matched_substring: "Generative Artificial Intelligence" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Paper propõe Graph-GAN vehicle trajectory prediction integrado com 5G resource slicing para task offloading em IoV/MEC. GAI (Generative AI / GAN) é usada apenas para trajectory prediction (input); a decisão de offloading/slicing segue modelo de otimização clássico (delay model, modulation schemes, bandwidth allocation). Não há agentic loop — GAI não dirige o raciocínio de RM. Loop de decisão é determinístico/otimizado, não autônomo reasoning+acting de agente.
- **agrees_with_regex:** False
- **addressed_hint:** support — GAI como preditor/feature extractor para método clássico de resource slicing, não como decisor agentic
- **evidence_sections:** ['§B Graph-GAN Vehicle Trajectory Prediction Model — GAN gera previsões; não toma decisão', '§C RSUs Resource Slicing Model — formulas de otimização clássicas (delay, bandwidth, MCS allocation)', '§IV Problem Description — model determinístico de alocação sem agentic reasoning']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
