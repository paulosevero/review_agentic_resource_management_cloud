---
id: paper-2639
title: 'Bauhaus: Restructuring Vector Database for LLM Retrieval on CXL-Based Tiered Memory'
authors:
- Kim, Kyungbin
- Ahn, Sungsu
- Jeong, Wonjung
- Kim, Jongmin
- Choi, Sangun
- Gil, Minseong
- Kim, Minseong
- Jung, Dongha
- Hong, Yunjay
- Jung, Haekang
- Oh, Yunho
venue: IEEE Transactions on Computers
venue_type: journal
year: 2026
doi: 10.1109/TC.2026.3656215
url: https://www.scopus.com/pages/publications/105029168857?origin=resultslist
publisher: IEEE Computer Society
pages: 1309--1322
keywords:
- CXL-based tiered memory systems
- Embedding-aware memory management
- Retrieval-Augmented Generation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2639 — Bauhaus: Restructuring Vector Database for LLM Retrieval on CXL-Based Tiered Memory

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Retrieval-augmented generation pipelines store large volumes of embedding vectors in vector databases for semantic search. In Compute Express Link (CXL)-based tiered memory systems, page-level placement often promotes pages containing both hot and cold vectors, leaving many hot vectors in the long-latency, lower-bandwidth CXL tier. This imbalance increases memory access time, reduces throughput, and worsens tail latency. This paper presents Bauhaus, a software-based memory management technique that increases the share of hot vectors in host memory, thereby improving access efficiency, reducing backend stalls, and lowering tail latency. Bauhaus monitors and reorders embedding vectors at vector-level granularity using Processor Event-Based Sampling (PEBS) and Virtual Memory Area (VMA) metadata, clustering hot vectors into contiguous pages to raise hot-page density and enhance the effectiveness of page promotion. Bauhaus, integrated into the Heterogeneous Memory Software Development Kit (HMSDK) developed and publicly released by SK hynix, is evaluated on a production-grade CXL platform. Across various embedding models, datasets, and CXL-to-host memory ratios, Bauhaus achieves 42.0% higher throughput over the baseline and 15.8% over HMSDK. Bauhaus sustains high RAG performance under constrained host memory capacity, offering a practical solution for large-scale vector database deployments in modern datacenter environments. © 2026 IEEE. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2639.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
