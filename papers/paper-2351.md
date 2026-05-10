---
id: paper-2351
title: Sparse Matrix Factorization for Scalable Machine Learning in Cloud Environments
authors:
- Yalamati, Srinivasu
venue: International Conference on NexGen Networks and Cybernetics, IC2NC 2025 - Proceedings
venue_type: conference
year: 2025
doi: 10.1109/IC2NC67409.2025.11376338
url: https://www.scopus.com/pages/publications/105035602758?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 333--338
keywords:
- Adaptive Resource Management
- AI-Augmented Service Fabric
- Cloud Orchestration
- Energy Efficiency
- LSTM Forecasting
- Multi-Agent Deep Reinforcement Learning
- Predictive Scaling
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
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

# paper-2351 — Sparse Matrix Factorization for Scalable Machine Learning in Cloud Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Demand for intelligent and versatile resource management techniques has increased with the proliferation of cloud computing and acceleration of industry adoption of microservice-style architectures. Dynamic, heterogenous, and dynamic workloads encountered by large-scale cloud systems are commonly not appropriate to be served by classic static or rule-based orchestration systems. AISF is a decentralized intelligent orchestration architecture that exploits predictive modeling and mutants-enabled deep reinforcement learning for contextually-aware, real-time resource allocation. In order to forecast load dynamics and dynamically re-distribute resources automatically using hierarchical control loops, including always evaluating system telemetry data, the AISF architecture makes use of learning agents that are deployed directly at service fabric level. AISF surpasses other baselines that include static-auto scaling and single-agent reinforcement learning in Google Cluster Workload Traces. It maintains 98.6% SLA satisfaction and demonstrates up to 25% resources saving, 40% latency reduction, and 21.9% energy expenditure mitigation. The model also possesses advantages of the better scalability, faster policy convergence, fault tolerance through distributed multi-agent coordination. AISF realizes energy-efficient and greening of cloud by the help of prediction with energy-awareness to stimulate carbon-conscious operation. The proposed solution positions AI as a fundamental power supply for future intelligent infrastructure management solutions and is a major step toward self-learning, self-healing, and self-optimization in the cloud. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2351.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
