---
id: "paper-2467"
title: "Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization"
authors: ["Zheng, Yuan", "Yao, Jiaqing"]
year: 2025
venue: "Proceedings of International Conference on Modern Sustainable Systems, CMSS 2025"
venue_type: "conference"
doi: "10.1109/CMSS66566.2025.11182451"
url: "https://www.scopus.com/pages/publications/105022017510?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "971--977"
keywords: ["Adaptive Auto-Scaling", "Cloud Platforms", "Distributed Databases", "Reinforcement Learning", "Resource Optimization"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2467 — Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization

## Metadata

- **Authors:** Zheng, Yuan and Yao, Jiaqing
- **Year:** 2025
- **Venue:** Proceedings of International Conference on Modern Sustainable Systems, CMSS 2025
- **DOI:** 10.1109/CMSS66566.2025.11182451
- **URL:** https://www.scopus.com/pages/publications/105022017510?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 971--977
- **Language:** English
- **Keywords:** Adaptive Auto-Scaling; Cloud Platforms; Distributed Databases; Reinforcement Learning; Resource Optimization

### Abstract

With the integration and development of cloud platforms and distributed database technologies, how to achieve efficient resource scheduling and dynamic elastic scaling in a multi-tenant, high-concurrency and resource heterogeneous environment has become an important challenge. This study proposes a resource optimization algorithm that integrates deep reinforcement learning and adaptive elastic scaling mechanism. The application scenario is to improve the response efficiency and resource utilization of cloud platform distributed database systems. At the algorithm design level, the study first models the resource scheduling problem as a Markov decision process (MDP) with a continuous state space and action space. At the same time, a deep deterministic policy gradient algorithm is introduced to build an intelligent agent. This operation can realize the self-learning of the CPU allocation strategy of the database node. Secondly, a parameter tuning model based on Bayesian optimization is constructed. This can support the dynamic adjustment of the total amount of resources to realize the automatic increase and decrease of nodes and service level guarantee. Finally, a data integrity coordination mechanism is introduced. This can improve the decoding success rate of the data transmission process while supporting resource scheduling and elastic scaling. To verify the effectiveness of the proposed method, this study built a simulation test platform in a virtualized cloud platform environment. At the same time, the Apache Cassandra distributed database was deployed, in conjunction with the Kubernetes container scheduling environment and the JMeter+Locust business generator. The proposed method maintained the shortest response delay (minimum 192ms) under peak, stable and burst load conditions, and the CPU and memory utilization rates reached 82.5% and 77.8% respectively. The proposed method is significantly superior to traditional algorithms in terms of the system performance improvement, resource optimization and data integrity assurance. © 2025 IEEE.

## 04 — Title Screening

**Title:** Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
