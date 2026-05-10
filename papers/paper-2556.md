---
id: paper-2556
title: 'LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees'
authors:
- Ding, Guanyu
- Yang, Shiyu
- Lin, Han
- Chen, Zifan
- Yang, Jie Si
venue: IEEE Open Journal of the Computer Society
venue_type: journal
year: 2026
doi: 10.1109/OJCS.2026.3667549
url: https://www.scopus.com/pages/publications/105031664073?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 560--573
keywords:
- adaptive optimization
- Cloud computing
- large language models (LLMs)
- resource scheduling
- SLA management
- task orchestration
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
    proposed_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
    winning_category: mas_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_using_llm
    - ovr_via_llm
    - ovr_llm_modifier
    - ovr_prompt_based
    - ovr_abs_llm_orchestrates
    - ovr_cls_llm_present
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2556 — LLM-Driven Adaptive Cloud Resource Scheduling: Bridging Reasoning Intelligence With Optimization Guarantees

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud resource scheduling presents a fundamental challenge in modern distributed computing, where heterogeneous workloads, complex task dependencies, and multi-objective optimization requirements exceed the capabilities of traditional rule-based and small-scale machine learning approaches. Existing schedulers struggle to dynamically adapt to evolving workload patterns while simultaneously satisfying Service Level Agreement (SLA) constraints, resource efficiency targets, and fairness policies. This article introduces LLMSched, a novel Large Language Model (LLM)-driven adaptive scheduling framework that synergistically combines the contextual reasoning capabilities of foundation models with the execution guarantees of classical optimization techniques. Our approach transforms heterogeneous cluster states—including task dependency graphs, real-time resource utilization metrics, and SLA specifications—into a unified structured-textual representation that leverages LLMs' few-shot learning and causal reasoning abilities to generate intelligent scheduling candidates. These candidates are subsequently refined through a lightweight Integer Linear Programming (ILP) module that ensures feasibility and optimality under resource constraints. We evaluate LLMSched on Google's production cluster trace dataset, demonstrating significant improvements over state-of-the-art baselines: 23.7% reduction in average job completion time, 18.4% improvement in resource utilization efficiency, and 31.2% decrease in SLA violations across diverse workload scenarios. Extensive ablation studies validate the contributions of each architectural component, while robustness analysis under workload perturbations confirms the framework's practical viability. Our work establishes a new paradigm for intelligent resource management that bridges the gap between neural reasoning and algorithmic precision, opening avenues for LLM applications in systems optimization domains. © 2020 IEEE.

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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "foundation models" }`
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS+LLM)."
- **winning_category:** 'mas_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_using_llm', 'ovr_via_llm', 'ovr_llm_modifier', 'ovr_prompt_based', 'ovr_abs_llm_orchestrates', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "Learning-Based Scheduling Approaches: Recent years have seen extensive efforts to apply learning-based methods to cluster and resource scheduling. Early work such as DeepRM [12] formulates scheduling as an MDP and demonstrates that deep reinforcement learning can outperform heuristic policies. Subsequent systems explore richer models and learning paradigms, including GNN-based dependency modeling for DAG jobs (Decima [38]), performance prediction via Bayesian optimization (Auto-Tune [39]), temporal workload modeling with RNNs (NNS [40]), and multi-agent reinforcement learning" }`
  - `{ category: llm_as_workload, pattern_id: wl_train_llm_a, matched_substring: "Training compute-optimal large language models" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM inference" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM inference" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM Inference**: explore model quantization" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM inference" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_a, matched_substring: "LLM prompting strategies and ILP solver objectives based on real deployment" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference latency of LLMs" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "inference time (100-500 ms for GPT" }`
  - `{ category: llm_as_workload, pattern_id: wl_inference_llm_b, matched_substring: "Deployment Feedback**: incorporate online learning mechanisms that refine LLM" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
  - `{ category: mas_llm_based, pattern_id: mas_llm_combo, matched_substring: "Learning-Based Scheduling Approaches: Recent years have seen extensive efforts to apply learning-based methods to cluster and resource scheduling. Early work such as DeepRM [12] formulates scheduling as an MDP and demonstrates that deep reinforcement learning can outperform heuristic policies. Subsequent systems explore richer models and learning paradigms, including GNN-based dependency modeling for DAG jobs (Decima [38]), performance prediction via Bayesian optimization (Auto-Tune [39]), temporal workload modeling with RNNs (NNS [40]), and multi-agent reinforcement learning for distributed scheduling (Chronus [41]). Despite promising results, learning-based schedulers suffer from practical limitations, including heavy reliance on representative training traces [42], sensitivity to distribution shift [43], limited interpretability [44], and restricted state representations that overlook high-level semantic information [45]. To mitigate these issues, hybrid systems combine learning with optimization, using learned models for demand or cost estimation while relying on mathematical solvers for decision making (e.g., Cilantro [46], Harmony [47]). Our work follows this hybrid philosophy and further extends it by leveraging the reasoning capabilities of large language models." }`

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
