---
id: "paper-2551"
title: "Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning"
authors: ["Das, Tapas K.", "Das, Santosh K.", "Bissoyi, Swarupananda", "Patel, Deepak K."]
year: 2026
venue: "International Journal of Intelligent Systems and Applications"
venue_type: "journal"
doi: "10.5815/ijisa.2026.01.08"
url: "https://www.scopus.com/pages/publications/105030148932?origin=resultslist"
publisher: "Modern Education and Computer Science Press"
pages: "107--118"
keywords: ["Cloud Computing", "Deep RL", "Fog Computing", "Meta-Learning", "Multi-Agent Reinforcement Learning", "Resource Allocation", "Task Offloading"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-2551 — Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning

## Metadata

- **Authors:** Das, Tapas K. and Das, Santosh K. and Bissoyi, Swarupananda and Patel, Deepak K.
- **Year:** 2026
- **Venue:** International Journal of Intelligent Systems and Applications
- **DOI:** 10.5815/ijisa.2026.01.08
- **URL:** https://www.scopus.com/pages/publications/105030148932?origin=resultslist
- **Publisher:** Modern Education and Computer Science Press
- **Pages:** 107--118
- **Language:** English
- **Keywords:** Cloud Computing; Deep RL; Fog Computing; Meta-Learning; Multi-Agent Reinforcement Learning; Resource Allocation; Task Offloading

### Abstract

The rapid growth of IoT ecosystems has intensified the complexity of fog–cloud infrastructures, necessitating adaptive and energy-efficient task offloading strategies. This paper proposes MADRL-MAML, a Multi-Agent Deep Reinforcement Learning framework enhanced with Model-Agnostic Meta-Learning for dynamic fog–cloud resource allocation. The approach integrates curriculum learning, centralized attention-based critics, and KL-divergence regularization to ensure stable convergence and rapid adaptation to unseen workloads. A unified cost-based reward formulation is used, where less negative values indicate better joint optimization of energy, latency, and utilization. MADRL-MAML is benchmarked against six baselines Greedy, Random, Round-Robin, PPO, Federated PPO, and Meta-RL using consistent energy, latency, utilization, and reward metrics. Across these baselines, performance remains similar: energy (3.64–3.71 J), latency (85.4–86.7 ms), and utilization (0.51–0.54). MADRL-MAML achieves substantially better results with a reward of $-21.92 \pm 3.88$, energy 1.16 J, latency 12.80 ms, and utilization 0.39, corresponding to 68\% lower energy and 85\% lower latency than Round-Robin. For unseen workloads characterized by new task sizes, arrival rates, and node heterogeneity, the meta-learned variant (MADRL-MAML-Unseen) achieves a reward of $-6.50 \pm 3.98$, energy 1.14 J, latency 12.76 ms, and utilization 0.73, demonstrating strong zero-shot generalization. Experiments were conducted in a realistic simulated environment with 10 fog and 2 cloud nodes, heterogeneous compute capacities, and Poisson task arrivals. Inference latency remains below 5 ms, confirming real-time applicability. Overall, MADRL-MAML provides a scalable and adaptive solution for energy-efficient and latency-aware orchestration in fog–cloud systems. © 2026, Modern Education and Computer Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Self-adaptive Resource Allocation in Fog-Cloud Systems Using Multi-agent Deep Reinforcement Learning with Meta-learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
