---
id: paper-2830
title: Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks
authors:
- Wang, Yaqing
- Tang, Lun
- Wang, Weili
- He, Xiaoqiang
- Chen, Qianbin
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3683128
url: https://www.scopus.com/pages/publications/105036065449?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Deep reinforcement learning
- edge intelligence
- large language model
- Multi-UAV cooperative edge computing
- re source allocation
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
    proposed_decision: Exclude
    proposed_justification: "Review"
    winning_category: review
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2830 — Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In 6G multiple unmanned aerial vehicles (UAVs) cooperative edge computing networks, strongly coupled system states and limited single-UAV observability lead to inefficient resource management and difficulty in guaranteeing Quality of Service (QoS). To address these issues, we propose a QoS-aware resource allocation method based on a large language model (LLM) for Multi-UAV Cooperative Edge Computing Networks. First, we construct an LLM-based teacher–student resource allo cation framework, operating with a global perspective, generates high-quality expert policies that are subsequently injected into distributed student agents via policy distillation, enabling effi cient online decision-making in dynamic environments. Second, we design an LLM-based teacher model for accurate expert decision-making under dynamic network conditions. Specifically, we construct a time-varying network knowledge graph (NKG) to represent the complex spatiotemporal states of multi-UAV networks, employ a relation-aware graph attention network (R-GAT) to aggregate crucial neighborhood information and capture node importance, and further combine a fine-tuned LLM with a Tree-of-Thoughts (ToT) reasoning framework to produce high-quality expert resource allocation policies. Finally, we develop a multi-agent student model with policy distillation for efficient management of dynamic, multi-dimensional resources. We formulate a QoS objective that jointly considers delay and fairness, and jointly optimize user association, UAV trajectories, computing allocation, bandwidth allocation, and air-to-air (A2A) migration ratios. The student utilizes the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm and learns from the teacher efficiently via policy distillation, adapting adeptly to dynamic environments. Simulation results demonstrate that the proposed method achieves significantly faster convergence, lower steady-state delay, and higher fairness compared to baseline approaches, while also exhibiting robustness and scalability across different network sizes and resource conditions. © 2002-2012 IEEE.

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_mappo, matched_substring: "MAPPO" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language model" }`
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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

### iter-0 (initial classification)

- **regex_decision:** Exclude
- **regex_justification:** "Review"
- **winning_category:** 'review'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: review, pattern_id: rev_a_roadmap_survey, matched_substring: "A Comprehensive Survey" }`
  - `{ category: review, pattern_id: rev_a_roadmap_survey, matched_substring: "A Comprehensive Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_survey, matched_substring: "Survey" }`
  - `{ category: review, pattern_id: rev_comprehensive_survey, matched_substring: "Comprehensive Survey" }`
  - `{ category: review, pattern_id: rev_comprehensive_survey, matched_substring: "Comprehensive Survey" }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
