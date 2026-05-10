---
id: paper-1938
title: A scalable machine learning strategy for resource allocation in database
authors:
- Manhary, Fady Nashat
- Mohamed, Marghny H.
- Farouk, Mamdouh
venue: Scientific Reports
venue_type: journal
year: 2025
doi: 10.1038/s41598-025-14962-5
url: https://www.scopus.com/pages/publications/105013798868?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- Cloud computing
- Energy efficiency
- Multi-Agent Reinforcement Learning
- Resource allocation
- Scalability
- Workload forecasting
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1938 — A scalable machine learning strategy for resource allocation in database

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern cloud computing systems require intelligent resource allocation strategies that balance quality-of-service (QoS), operational costs, and energy sustainability. Existing deep Q-learning (DQN) methods suffer from sample inefficiency, centralization bottlenecks, and reactive decision-making during workload spikes. Transformer-based forecasting models such as Temporal Fusion Transformer (TFT) offer improved accuracy but introduce computational overhead, limiting real-time deployment. We propose LSTM-MARL-Ape-X, a novel framework integrating bidirectional Long Short-Term Memory (BiLSTM) for workload forecasting with Multi-Agent Reinforcement Learning (MARL) in a distributed Ape-X architecture. This approach enables proactive, decentralized, and scalable resource management through three innovations: high-accuracy forecasting using BiLSTM with feature-wise attention, variance-regularized credit assignment for stable multi-agent coordination, and faster convergence via adaptive prioritized replay. Experimental validation on real-world traces demonstrates 94.6% SLA compliance, 22% reduction in energy consumption, and linear scalability to over 5,000 nodes with sub-100 ms decision latency. The framework converges 3.2 faster than uniform sampling baselines and outperforms transformer-based models in both accuracy and inference speed. Unlike decoupled prediction-action frameworks, our method provides end-to-end optimization, enabling robust and sustainable cloud orchestration at scale. © The Author(s) 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1938.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
