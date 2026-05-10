---
id: paper-1942
title: ML-driven latency optimization for mobile edge computing in fiber-wireless access networks
authors:
- Marmat, Antimbala
- Thankachan, Dolly
venue: MethodsX
venue_type: journal
year: 2025
doi: 10.1016/j.mex.2025.103594
url: https://www.scopus.com/pages/publications/105015073844?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Fiber-wireless networks
- Latency optimization
- Machine learning
- Mobile edge computing
- Process
- Reinforcement Learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1942 — ML-driven latency optimization for mobile edge computing in fiber-wireless access networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The increasing quest for ultra-low latency in mobile edge computing (MEC) over fiber–wireless networks pose challenges in adapting to real-time demands under resource constraints. Congestion-prone methods of centralized learning and static routing waste resources. A machine learning-based latency optimization framework is proposed that integrates multiple advanced paradigms for proactive traffic management, intelligent routing, and efficient task offloading while ensuring data privacy. The framework encompasses self-supervised learning, federated learning, spatiotemporal graph neural networks (GNN), adaptive multi-agent reinforcement learning, and hypergraph transformers. These tools are useful for dynamic congestion-aware routing, accurate spatiotemporal traffic prediction, and optimal resource slicing for latency-sensitive applications. Hypergraph transformers enable dynamic allocation of resources across network slices. The experiments shows significant performance improvements, 34–42 % reduction in end-to-end latency, 29–35 % faster task execution, 50 % less training time, better traffic prediction accuracy, and lower slice switching delays. This framework can underpin some of the most crucial low-latency applications like augmented reality and autonomous driving, providing a powerful solution for the next generation of MEC networks working under stringent performance and privacy constraints. • Dynamic congestion-aware routing using adaptive multi-agent reinforcement learning • Proactive traffic prediction using spatiotemporal GNN • Federated, self-supervised learning to maximize resource slicing and delay-aware task offloading © 2025 The Author(s)

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1942.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
