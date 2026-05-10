---
id: "paper-1258"
title: "NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing"
authors: ["Wang, Yitu", "Li, Shiyu", "Zheng, Qilin", "Song, Linghao", "Li, Zongwang", "Chang, Andrew", "Li, Hai lHelenr", "Chen, Yiran"]
year: 2024
venue: "Proceedings - International Symposium on Computer Architecture"
venue_type: "conference"
doi: "10.1109/ISCA59077.2024.00035"
url: "https://www.scopus.com/pages/publications/85201143773?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "368--381"
keywords: ["Approximate Nearest Neighbor Search", "Hardware/Software Co-Design", "Near Data Processing"]
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
    final_score: 0.0
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1258 — NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing

## Metadata

- **Authors:** Wang, Yitu and Li, Shiyu and Zheng, Qilin and Song, Linghao and Li, Zongwang and Chang, Andrew and Li, Hai lHelenr and Chen, Yiran
- **Year:** 2024
- **Venue:** Proceedings - International Symposium on Computer Architecture
- **DOI:** 10.1109/ISCA59077.2024.00035
- **URL:** https://www.scopus.com/pages/publications/85201143773?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 368--381
- **Language:** English
- **Keywords:** Approximate Nearest Neighbor Search; Hardware/Software Co-Design; Near Data Processing

### Abstract

Approximate nearest neighbor search (ANNS) is a key retrieval technique for vector database and many data center applications, such as person re-identification and recommendation systems. It is also fundamental to retrieval augmented generation (RAG) for large language models (LLM) now. Among all the ANNS algorithms, graph-traversal-based ANNS achieves the highest recall rate. However, as the size of dataset increases, the graph may require hundreds of gigabytes of memory, exceeding the main memory capacity of a single workstation node. Although we can do partitioning and use solid-state drive (SSD) as the backing storage, the limited SSD I/O bandwidth severely degrades the performance of the system. To address this challenge, we present NDSEARCh, a hardware-software co-designed near-data processing (NDP) solution for ANNS processing. NDSeARCH consists of a novel in-storage computing architecture, namely, SEARSSD, that supports the ANNS kernels and leverages logic unit (LUN)-level parallelism inside the NAND flash chips. NDSEARCH also includes a processing model that is customized for NDP and cooperates with SearSSD. The processing model enables us to apply a two-level scheduling to improve the data locality and exploit the internal bandwidth in NDSearch, and a speculative searching mechanism to further accelerate the ANNS workload. Our results show that NDSEARCH improves the throughput by up to 31.7 ×, 14.6 ×, 7.4 × 2.9 × over CPU, GPU, a state-of-the-art SmartSSD-only design, and DeepStore, respectively. NDSEARCH also achieves two orders-of-magnitude higher energy efficiency than CPU and GPU. © 2024 IEEE.

## 04 — Title Screening

**Title:** NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** NDSEARCH: Accelerating Graph-Traversal-Based Approximate Nearest Neighbor Search through Near Data Processing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
