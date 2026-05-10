---
id: paper-2551
title: Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning
authors:
- Das, Tapas K.
- Das, Santosh K.
- Bissoyi, Swarupananda
- Patel, Deepak K.
venue: International Journal of Intelligent Systems and Applications
venue_type: journal
year: 2026
doi: 10.5815/ijisa.2026.01.08
url: https://www.scopus.com/pages/publications/105030148932?origin=resultslist
publisher: Modern Education and Computer Science Press
pages: 107--118
keywords:
- Cloud Computing
- Deep RL
- Fog Computing
- Meta-Learning
- Multi-Agent Reinforcement Learning
- Resource Allocation
- Task Offloading
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
  04-title-screening: exclude
  05-abstract-screening: pending
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
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2551 — Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of IoT ecosystems has intensified the complexity of fog–cloud infrastructures, necessitating adaptive and energy-efficient task offloading strategies. This paper proposes MADRL-MAML, a Multi-Agent Deep Reinforcement Learning framework enhanced with Model-Agnostic Meta-Learning for dynamic fog–cloud resource allocation. The approach integrates curriculum learning, centralized attention-based critics, and KL-divergence regularization to ensure stable convergence and rapid adaptation to unseen workloads. A unified cost-based reward formulation is used, where less negative values indicate better joint optimization of energy, latency, and utilization. MADRL-MAML is benchmarked against six baselines Greedy, Random, Round-Robin, PPO, Federated PPO, and Meta-RL using consistent energy, latency, utilization, and reward metrics. Across these baselines, performance remains similar: energy (3.64–3.71 J), latency (85.4–86.7 ms), and utilization (0.51–0.54). MADRL-MAML achieves substantially better results with a reward of $-21.92 \pm 3.88$, energy 1.16 J, latency 12.80 ms, and utilization 0.39, corresponding to 68\% lower energy and 85\% lower latency than Round-Robin. For unseen workloads characterized by new task sizes, arrival rates, and node heterogeneity, the meta-learned variant (MADRL-MAML-Unseen) achieves a reward of $-6.50 \pm 3.98$, energy 1.14 J, latency 12.76 ms, and utilization 0.73, demonstrating strong zero-shot generalization. Experiments were conducted in a realistic simulated environment with 10 fog and 2 cloud nodes, heterogeneous compute capacities, and Poisson task arrivals. Inference latency remains below 5 ms, confirming real-time applicability. Overall, MADRL-MAML provides a scalable and adaptive solution for energy-efficient and latency-aware orchestration in fog–cloud systems. © 2026, Modern Education and Computer Science Press. All rights reserved.

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
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2551.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
