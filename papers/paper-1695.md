---
id: paper-1695
title: Hierarchical Reinforcement Learning for Energy-Efficient API Traffic Optimization in Large-Scale Advertising Systems
authors:
- Ji, Enkai
- Wang, Yihan
- Xing, Suchuan
- Jin, Jianian
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3598712
url: https://www.scopus.com/pages/publications/105013235742?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 142493--142516
keywords:
- adaptive systems
- API traffic management
- digital advertising
- hierarchical decision making
- Reinforcement learning
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
    my_justification: RL
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

# paper-1695 — Hierarchical Reinforcement Learning for Energy-Efficient API Traffic Optimization in Large-Scale Advertising Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital advertising infrastructure represents a substantial component of global computing resources, with significant environmental impact due to its massive energy consumption and carbon footprint. This work addresses the sustainability challenges posed by inefficient API traffic management in large-scale advertising systems, where conventional static approaches lead to resource overprovisioning and energy waste. We propose AdaptiveGate, a sustainability-oriented hierarchical reinforcement learning framework that dynamically optimizes API traffic flows to enhance resource efficiency and reduce environmental impact. The proposed methodology employs a constrained Markov Decision Process formulation with a multi-objective reward function explicitly designed to balance system performance with resource efficiency. Our framework implements a two-tier architecture of twin delayed Deep Deterministic Policy Gradient agents: global agents minimize cross-datacenter energy expenditure through intelligent traffic routing, while local agents maximize resource utilization through service-specific load balancing. Empirical evaluation on production advertising systems processing over 2.5 million requests per second reveals significant sustainability improvements: 42.3% reduction in tail latency, 35.7% increase in throughput, and 18% decrease in overall energy consumption compared to state-of-the-art methods. The system demonstrates exceptional adaptability across diverse traffic conditions and operational scales, providing compelling evidence that AI-driven methods can substantially improve digital infrastructure sustainability. This work contributes to sustainable computing by establishing a framework that optimizes computational resource allocation, minimizes energy waste, and advances environmentally responsible high-performance computing systems, aligning with multiple Sustainable Development Goals including responsible consumption and affordable clean energy. © 2013 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1695.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
