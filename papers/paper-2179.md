---
id: paper-2179
title: Large Models for Resource Allocation in Edge Computing Power Networks
authors:
- Sui, Liyan
- Zhang, Ke
- Wu, Fan
- Huang, Xiaoyan
venue: IEEE Network
venue_type: journal
year: 2025
doi: 10.1109/MNET.2024.3524611
url: https://www.scopus.com/pages/publications/85214121405?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 82--89
keywords:
- edge computing power network (ECPN)
- Large models
- resource allocation
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management
      signal); C3=1.0 (infra/cloud-edge signal)
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
    - ovr_abs_llm_decides
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: Out of scope
    winning_category: F_out_of_scope_domain
    overrides_applied:
    - ovr_with_llm
    - ovr_leveraging_llm
    - ovr_llm_modifier
    - ovr_abs_llm_decides
    - ovr_abs_llm_orchestrates
    my_final_decision: Exclude
    my_justification: Paper propõe LLM + Graph MADRL para 'task matching' em Edge
      Computing Power Networks (ECPN) — domain é redes eléctricas/smart grids, não
      cloud/edge/continuum computing. Sec. 2-3 ('Architecture of Large Model-Enabled
      ECPN', 'Application for Large Model-Enabled ECPN') focam em power-load balancing
      e demand prediction em infraestruturas de energia. Embora mencione 'edge computing',
      refere-se a ponto de acesso para smart devices de energia, não a continuum cloud-edge
      para aplicações/serviços. LLM é integrado a MADRL mas domínio é fora de escopo
      (power networks, manufatura, não RM em cloud/edge/continuum).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2179 — Large Models for Resource Allocation in Edge Computing Power Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computing Power Network (CPN), as an integration of heterogeneous computing resources, has turned to be difficult to cope with the rapid growth of end users and strict task delay constraints due to the possible long-distance transmission between its service facilities and remote users. To overcome this problem, we propose an Edge Computing Power Network (ECPN), which reduces long-distance transmission overhead, optimizes resource utilization, and improves system performance by fully utilizing edge computing resources. In the area of resource scheduling, traditional machine learning is widely used due to its fast problem solving capabilities. However, traditional machine learning faces challenges in ECPN, particularly with handling heterogeneous tasks and adapting to highly dynamic network conditions. To address these challenges, we propose a large model-enabled ECPN framework that enhances the capabilities of ECPN in task offloading and resource allocation while optimizing the deployment of large models in the framework. To demonstrate the advantages of this framework, we introduce a smart transportation application scenario and employ a large language model based graph multi-agent deep reinforcement learning algorithm to determine optimal task matching strategies that balance energy consumption and privacy protection in the ECPN. Experimental results demonstrate that the algorithm applied in this framework reduces energy consumption, decreases the convergence time for task matching, and enhances privacy protection in ECPN. © 1986-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_abs_llm_decides']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Computing Power Network (CPN)" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
  - `{ category: llm_as_workload, pattern_id: ovr_abs_llm_decides, matched_substring: "large language model based gra" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

- **regex_decision:** Exclude
- **regex_justification:** "Out of scope"
- **winning_category:** 'F_out_of_scope_domain'
- **overrides_applied:** ['ovr_with_llm', 'ovr_leveraging_llm', 'ovr_llm_modifier', 'ovr_abs_llm_decides', 'ovr_abs_llm_orchestrates']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "training large models" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "LLMs is a type of deep learning-based artificial intelligence model that can process large-scale tas" }`
  - `{ category: F_out_of_scope_domain, pattern_id: oos_smart_manufacturing, matched_substring: "smart manufacturing" }`
  - `{ category: F_out_of_scope_domain, pattern_id: oos_smart_manufacturing, matched_substring: "smart manufacturing" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Paper propõe LLM + Graph MADRL para 'task matching' em Edge Computing Power Networks (ECPN) — domain é redes eléctricas/smart grids, não cloud/edge/continuum computing. Sec. 2-3 ('Architecture of Large Model-Enabled ECPN', 'Application for Large Model-Enabled ECPN') focam em power-load balancing e demand prediction em infraestruturas de energia. Embora mencione 'edge computing', refere-se a ponto de acesso para smart devices de energia, não a continuum cloud-edge para aplicações/serviços. LLM é integrado a MADRL mas domínio é fora de escopo (power networks, manufatura, não RM em cloud/edge/continuum).
- **agrees_with_regex:** True
- **addressed_hint:** no_hint
- **evidence_sections:** ['Sec. 2 The Architecture of Large Model-Enabled ECPN', 'Sec. 3 Application for Large Model-Enabled ECPN', 'Sec. 4 LLMs and Graph MADRL Driven Task Matching']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
