---
id: paper-2126
title: 'Design of an Iterative AI-Driven Latency Prediction and QoS-Aware Task Scheduling in Mobile Edge Computing: A Federated and Reinforcement Learning Process'
authors:
- Sharma, Garima
- Khare, Rashi
- Kulkarni, Neha
- Pagare, Sanjay
- Tiwari, Vanshika
venue: EPJ Web of Conferences
venue_type: conference
year: 2025
doi: 10.1051/epjconf/202532801071
url: https://www.scopus.com/pages/publications/105011028737?origin=resultslist
publisher: EDP Sciences
pages: ''
keywords: []
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

# paper-2126 — Design of an Iterative AI-Driven Latency Prediction and QoS-Aware Task Scheduling in Mobile Edge Computing: A Federated and Reinforcement Learning Process

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The tremendous upsurge of latency-sensitive applications in Mobile Edge Computing (MEC), thus requiring an efficient task scheduler depending on precise and adaptive latency prediction. The traditional latency estimation models predict the latency using either a static or heuristic-based approach whose shortcoming is overlooking the dynamic changes in network conditions, available resources, and task characteristics. Such limitations invariably lead to either suboptimal scheduling, higher task failure rates, or inefficient use of resources. Therefore, to remedy such downfalls, we propose to develop an AI-Enhanced Latency Prediction Model for QoS-Aware Task Scheduling in MEC by synergizing several new and promising machine-learning techniques. Adaptive Spatio-Temporal Graph Transformer (AST-GT) captures the real-time variations in latency across the edge nodes with help from attention-based graph representation and temporal modeling. Federated Self-Supervised Contrastive Learning (FSSCL) makes possible decentralized latency prediction such that privacy is conserved by capitalizing inter-node similarity in latency patterns. Hypernetwork-Driven Task-Specific Latency Estimator (HTSLE) dynamically generates task-adaptive latency models to maintain high prediction accuracy on heterogeneous workloads. To enhance decision reliability, Bayesian Uncertainty-Aware Prediction (BUAP) quantifies uncertainty in latency estimate results and reduces scheduling risk. Lastly, Multi-Agent Reinforcement Learning with Meta-Learning (MARL-Meta) refines task scheduling by dynamically adjusting policies with respect to predicted latencies, task priorities, and constraints of MEC resources. This synchronized AI-based framework achieves a 74.4% gain in reducing latency prediction error, 35% enhancement in task execution time, 67.5% decline in task failure rates, and 30.6% increase in resource utilization when compared to conventional MEC scheduling methods. By marrying dynamic latency prediction, federated privacy-aware learning, uncertainty quantification, and intelligent reinforcement-based scheduling, our model stands out for significantly enhancing the QoS-aware task execution and establishing itself as a reliable and adaptive solution to next-generation MEC scenarios.  © The Authors, published by EDP Sciences, 2025.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2126.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
