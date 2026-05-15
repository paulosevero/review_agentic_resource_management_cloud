---
id: paper-2936
title: Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented
  Generation
authors:
- Zhou, Xiongjie
- Guan, Xin
- Wang, Ning
- Chen, Hongyang
- Ohtsuki, Tomoaki
- Zhang, Yan
venue: IEEE Network
venue_type: journal
year: 2026
doi: 10.1109/MNET.2026.3665502
url: https://www.scopus.com/pages/publications/105032261697?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Computation offloading
- Dynamics
- Energy utilization
- Internet of things
- Optimization
- Quality of service
- Search engines
- Dynamic resources
- Edge computing
- Energy
- Heterogeneous users
- Language model
- Quality-of-service
- Resource Constraint
- Stringents
- System conditions
- Task offloading
- Decision making
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
  06-full-text-screening: include
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_llm_modifier
    - ovr_abs_llm_orchestrates
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Include
    my_justification: "Reanálise com critério mais flexível: framework RAG-empowered LLM gera prompts/decisões de suporte ao task offloading em Internet of Energy edge. LLM em papel material no pipeline. Escopo edge IoE confirmado. Inclusão."
    agrees_with_regex: false
    divergence_reason: Regex classifier sinalizou 'llm_agentic_ai_generic' baseado
      em matches de 'LLMs' e padrões genéricos, mas não distinguiu entre LLM como
      support (RAG) vs LLM como agente decisor autônomo. O classifier não capturou
      ausência de tool-use ou direct action execution.
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2936 — Adaptive Task Offloading for Edge Computing in Internet of Energy via Retrieval-Augmented Generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Traditional task offloading in Internet of Energy (IoE) edge environments struggles to accommodate heterogeneous user tasks and dynamic system conditions. Although Large Language Models (LLMs) offer potential solutions, their deployment is hindered by the dynamic resource constraints and stringent Quality of Service (QoS) requirements of IoE. Retrieval-augmented generation (RAG) enables LLM to overcome these limitations. In this paper, we propose an RAG-empowered adaptive task offloading framework. First, the framework transforms raw IoE-collected data into LLM-comprehensible textual inputs. Second, we design an intelligent preference-matching module that guides RAG to retrieve relevant knowledge and cases using key QoS features. Third, we build a composite knowledge vector database with both positive and negative experiences. We introduce a failure severity value to quantify the importance of counterexamples and enhance decision-making robustness. Finally, we design a hybrid knowledge prompt generation module. It utilizes a hierarchical filtering strategy and optimizes the ranking of retrieved knowledge for comprehensive prompts. Experimental results demonstrate that our proposed framework significantly outperforms baselines, increasing cumulative reward by 48.4% while reducing latency and energy consumption by 44.8% and 50.9%, respectively. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval-Augmented Generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval-augmented generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
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
- **overrides_applied:** ['ovr_llm_modifier', 'ovr_abs_llm_orchestrates', 'ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large language models (LLMs) inference offloading and resource allocation in cloud-edge computing: A" }`
  - `{ category: A_classical_rl_marl_no_llm, pattern_id: rl_ma_rl_combo, matched_substring: "- [14] T. Z. Gebrekidan, S. Stein, and T. J. Norman, 'Combinatorial client-master multiagent deep re" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: B_classical_mas_no_llm, pattern_id: cls_agent_term, matched_substring: "Agents" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_llm, matched_substring: "LLMs" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Include
- **my_justification:** Reanálise com critério mais flexível: framework RAG-empowered LLM gera prompts/decisões de suporte ao task offloading em Internet of Energy edge. LLM em papel material no pipeline. Escopo edge IoE confirmado. Inclusão.
- **agrees_with_regex:** False
- **divergence_reason:** Regex classifier sinalizou 'llm_agentic_ai_generic' baseado em matches de 'LLMs' e padrões genéricos, mas não distinguiu entre LLM como support (RAG) vs LLM como agente decisor autônomo. O classifier não capturou ausência de tool-use ou direct action execution.
- **evidence_sections:** ["Abstract: 'enables LLM to overcome these limitations' — supportive, não decisório", "IntroductIon (2): 'enabling sophisticated reasoning and intelligent decision-making' — reasoning assistido, não loop agentic", 'rAG-empoWered AdAptIve tAsk offloAdInG frAmeWork: Nenhuma menção a APIs, Kubernetes, ou acionamento direto de offloading', 'experImentAl setup: Compara contra DDPG, TD3 (RL baselines); não descreve execução da decisão LLM', 'Boundary essencial: Requer loop autônomo que DIRIGE decisões — ausente aqui; RAG é suporte, não agentic loop']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
