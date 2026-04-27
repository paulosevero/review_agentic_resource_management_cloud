---
id: "paper-2030"
title: "A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems"
authors: ["Peng, Yue", "Sinnott, Richard"]
year: 2025
venue: "Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025"
venue_type: "conference"
doi: "10.1145/3773274.3774258"
url: "https://www.scopus.com/pages/publications/105027154636?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: ""
keywords: ["Generative AI", "GPU Sharing", "Kubernetes", "Reinforcement Learning", "Time Series Forecasting"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: ""
    human_justification: ""

---

# paper-2030 — A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems

## Metadata

- **Authors:** Peng, Yue and Sinnott, Richard
- **Year:** 2025
- **Venue:** Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
- **DOI:** 10.1145/3773274.3774258
- **URL:** https://www.scopus.com/pages/publications/105027154636?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 
- **Language:** English
- **Keywords:** Generative AI; GPU Sharing; Kubernetes; Reinforcement Learning; Time Series Forecasting

### Abstract

The increasing popularity of generative AI applications has introduced new challenges in how to effectively utilize hardware (GPUs). As generative AI models become more widely adopted, optimising the deployment of models emerges as a critical concern due to the substantial computational overheads, variable workloads, and the need for low-latency inference of many AI applications needing GPUs with often limited availability. In this paper, we investigate strategies for the efficient deployment of a text-to-image application, treating the underlying generative model as a black box. Leveraging Kubernetes and the Ray distributed computing framework, we explore the integration of NVIDIA GPU sharing techniques to improve resource utilization and train an auto-scaling agent using Proximal Policy Optimization (PPO) reinforcement learning with time-series forecasting enhancements to tackle real-world workloads. We identify that our forecasting-enhanced PPO agent outperforms traditional threshold-based strategies by reducing the number of required replicas and better adapting to fluctuating user demand, whilst exhibiting reduced latency and requiring fewer provisioning operations in scenarios with long replica startup times. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Hybrid Forecasting and Reinforcement Learning Approach for Latency-Constrained Scaling of Generative AI Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
