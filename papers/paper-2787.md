---
id: paper-2787
title: LLM-Based Task Offloading and Resource Allocation in Satellite Edge Computing
  Networks
authors:
- Sun, Minghao
- Hou, Jinbo
- Qiu, Kehai
- Wang, Kezhi
- Chu, Xiaoli
- Zhang, Zitian
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2025.3612207
url: https://www.scopus.com/pages/publications/105017044680?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5262--5267
keywords:
- Internet of Things
- large language model
- resource allocation
- Satellite mobile edge computing
- task offloading
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM).
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_llm_modifier
    - ovr_prompt_based
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: "Escopo satellite edge computing — próximo a Orbital Edge Computing, fora do escopo per Gate A."
    agrees_with_regex: false
    divergence_reason: Regex flagged as mas_llm_based; full-text reveals LLM is sub-solver,
      not agentic multi-agent system. Aligns with hint_status=pre_flagged_disagree.
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2787 — LLM-Based Task Offloading and Resource Allocation in Satellite Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite Mobile Edge Computing (MEC) networks offer a promising solution for delivering global services to terrestrial Internet of Things (IoT) terminals in 5G and beyond. However, satellite MEC systems face challenges such as underutilization of resources and task congestion, leading to resource waste and increased latency. In this paper, we investigate the joint resource allocation and task offloading problem in multi-satellite MEC networks, aiming to minimize the average latency of IoT terminals. To solve the joint optimization problem involving IoT terminals' task offloading decisions, uplink transmission power and sub-channel allocation, and satellite computation resource allocation, we propose an iterative optimization algorithm that uses the Lagrange multipliers method to optimize the satellite computation resource allocation and a Large Language Model (LLM) based optimizer to optimize the other variables in each iteration. Prompts and templated parameters are designed to enhance the LLM's inference accuracy and generalization capability across scenarios with varying numbers of satellites and IoT terminals. Simulation results show that our proposed LLM-based algorithm outperforms benchmark algorithms in convergence speed and average latency of IoT terminals. © 1967-2012 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_llm_modifier', 'ovr_prompt_based', 'ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: C_llm_as_workload, pattern_id: wl_train_llm_b, matched_substring: "LLM's inference and generalization capabilities while avoiding the costs of dedicated model training" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM's inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM's inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "Large Language Models (LLMs) have emerged as a promising approach to solve these issues with their c" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM's inference" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment of LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deploying high-performance LLMs" }`
  - `{ category: C_llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "deployment-based LLMs" }`

**Pass-2 LLM reviewer (Haiku 4.5):**

- **my_final_decision:** Exclude
- **my_justification:** Escopo satellite edge computing — próximo a Orbital Edge Computing, fora do escopo per Gate A.
- **agrees_with_regex:** False
- **divergence_reason:** Regex flagged as mas_llm_based; full-text reveals LLM is sub-solver, not agentic multi-agent system. Aligns with hint_status=pre_flagged_disagree.
- **addressed_hint:** hint_categories=[networks] partially applies — satellite MEC is edge infrastructure, but LLM role is optimization tool (support) not agentic RM loop.
- **evidence_sections:** ["ABSTRACT: 'iterative optimization algorithm that uses Lagrange multipliers...and LLM-based optimizer'", 'SYSTEM MODEL: problem (15) solved via LLM-based Generator Module (prompt+example pool)', 'Algorithm 1: LLM-based Alternating Optimization with Lagrange sub-solver and LLM generator as decoupled components']


## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
