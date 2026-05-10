---
id: paper-2467
title: Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization
authors:
- Zheng, Yuan
- Yao, Jiaqing
venue: Proceedings of International Conference on Modern Sustainable Systems, CMSS 2025
venue_type: conference
year: 2025
doi: 10.1109/CMSS66566.2025.11182451
url: https://www.scopus.com/pages/publications/105022017510?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 971--977
keywords:
- Adaptive Auto-Scaling
- Cloud Platforms
- Distributed Databases
- Reinforcement Learning
- Resource Optimization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2467 — Adaptive Auto-Scaling of Distributed Databases on Cloud Platforms via Reinforcement Learning-based Resource Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the integration and development of cloud platforms and distributed database technologies, how to achieve efficient resource scheduling and dynamic elastic scaling in a multi-tenant, high-concurrency and resource heterogeneous environment has become an important challenge. This study proposes a resource optimization algorithm that integrates deep reinforcement learning and adaptive elastic scaling mechanism. The application scenario is to improve the response efficiency and resource utilization of cloud platform distributed database systems. At the algorithm design level, the study first models the resource scheduling problem as a Markov decision process (MDP) with a continuous state space and action space. At the same time, a deep deterministic policy gradient algorithm is introduced to build an intelligent agent. This operation can realize the self-learning of the CPU allocation strategy of the database node. Secondly, a parameter tuning model based on Bayesian optimization is constructed. This can support the dynamic adjustment of the total amount of resources to realize the automatic increase and decrease of nodes and service level guarantee. Finally, a data integrity coordination mechanism is introduced. This can improve the decoding success rate of the data transmission process while supporting resource scheduling and elastic scaling. To verify the effectiveness of the proposed method, this study built a simulation test platform in a virtualized cloud platform environment. At the same time, the Apache Cassandra distributed database was deployed, in conjunction with the Kubernetes container scheduling environment and the JMeter+Locust business generator. The proposed method maintained the shortest response delay (minimum 192ms) under peak, stable and burst load conditions, and the CPU and memory utilization rates reached 82.5% and 77.8% respectively. The proposed method is significantly superior to traditional algorithms in terms of the system performance improvement, resource optimization and data integrity assurance. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2467.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
