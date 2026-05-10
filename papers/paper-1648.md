---
id: paper-1648
title: 'CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing'
authors:
- Hong, Guihang
- Ouyang, Tao
- Zhao, Kongyange
- Zhou, Zhi
- Chen, Xu
venue: Proceedings - Real-Time Systems Symposium
venue_type: conference
year: 2025
doi: 10.1109/RTSS66672.2025.00022
url: https://www.scopus.com/pages/publications/105032423508?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 162--174
keywords:
- Edge Computing
- LLM
- RAG
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
    my_justification: LLM as workload
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

# paper-1648 — CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Motivated by the imperative for real-time responsiveness and data privacy preservation, large language models (LLMs) are increasingly deployed on resource-constrained edge devices to enable localized inference. To improve output quality, retrieval-augmented generation (RAG) is an efficient technique that seamlessly integrates local data into LLMs. However, existing edge computing paradigms primarily focus on single-node optimization, neglecting opportunities to holistically exploit distributed data and heterogeneous resources through cross-node collaboration. To bridge this gap, we propose CoEdge-RAG, a hierarchical scheduling framework for retrieval-augmented LLMs in collaborative edge computing. In general, privacy constraints preclude accurate a priori acquisition of heterogeneous data distributions across edge nodes, directly impeding RAG performance optimization. Thus, we first design an online query identification mechanism using proximal policy optimization (PPO), which autonomously infers query semantics and establishes cross-domain knowledge associations in an online manner. Second, we devise a dynamic inter-node scheduling strategy that balances workloads across heterogeneous edge nodes by synergizing historical performance analytics with real-time resource thresholds. Third, we develop an intra-node scheduler based on online convex optimization, adaptively allocating query processing ratios and memory resources to optimize the latency-quality trade-off under fluctuating assigned loads. Comprehensive evaluations across diverse QA benchmarks demonstrate that our proposed method significantly boosts the performance of collaborative retrieval-augmented LLMs, achieving performance gains of 4.23% to 91.39% over baseline methods across all tasks. © 2025 IEEE.

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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1648.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
