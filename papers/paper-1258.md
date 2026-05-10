---
id: paper-1258
title: 'NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing'
authors:
- Wang, Yitu
- Li, Shiyu
- Zheng, Qilin
- Song, Linghao
- Li, Zongwang
- Chang, Andrew
- Li, Hai lHelenr
- Chen, Yiran
venue: Proceedings - International Symposium on Computer Architecture
venue_type: conference
year: 2024
doi: 10.1109/ISCA59077.2024.00035
url: https://www.scopus.com/pages/publications/85201143773?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 368--381
keywords:
- Approximate Nearest Neighbor Search
- Hardware/Software Co-Design
- Near Data Processing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1258 — NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Approximate nearest neighbor search (ANNS) is a key retrieval technique for vector database and many data center applications, such as person re-identification and recommendation systems. It is also fundamental to retrieval augmented generation (RAG) for large language models (LLM) now. Among all the ANNS algorithms, graph-traversal-based ANNS achieves the highest recall rate. However, as the size of dataset increases, the graph may require hundreds of gigabytes of memory, exceeding the main memory capacity of a single workstation node. Although we can do partitioning and use solid-state drive (SSD) as the backing storage, the limited SSD I/O bandwidth severely degrades the performance of the system. To address this challenge, we present NDSEARCh, a hardware-software co-designed near-data processing (NDP) solution for ANNS processing. NDSeARCH consists of a novel in-storage computing architecture, namely, SEARSSD, that supports the ANNS kernels and leverages logic unit (LUN)-level parallelism inside the NAND flash chips. NDSEARCH also includes a processing model that is customized for NDP and cooperates with SearSSD. The processing model enables us to apply a two-level scheduling to improve the data locality and exploit the internal bandwidth in NDSearch, and a speculative searching mechanism to further accelerate the ANNS workload. Our results show that NDSEARCH improves the throughput by up to 31.7 ×, 14.6 ×, 7.4 × 2.9 × over CPU, GPU, a state-of-the-art SmartSSD-only design, and DeepStore, respectively. NDSEARCH also achieves two orders-of-magnitude higher energy efficiency than CPU and GPU. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1258.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
