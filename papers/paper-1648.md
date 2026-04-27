---
id: "paper-1648"
title: "CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing"
authors: ["Hong, Guihang", "Ouyang, Tao", "Zhao, Kongyange", "Zhou, Zhi", "Chen, Xu"]
year: 2025
venue: "Proceedings - Real-Time Systems Symposium"
venue_type: "conference"
doi: "10.1109/RTSS66672.2025.00022"
url: "https://www.scopus.com/pages/publications/105032423508?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "162--174"
keywords: ["Edge Computing", "LLM", "RAG"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1648 — CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing

## Metadata

- **Authors:** Hong, Guihang and Ouyang, Tao and Zhao, Kongyange and Zhou, Zhi and Chen, Xu
- **Year:** 2025
- **Venue:** Proceedings - Real-Time Systems Symposium
- **DOI:** 10.1109/RTSS66672.2025.00022
- **URL:** https://www.scopus.com/pages/publications/105032423508?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 162--174
- **Language:** English
- **Keywords:** Edge Computing; LLM; RAG

### Abstract

Motivated by the imperative for real-time responsiveness and data privacy preservation, large language models (LLMs) are increasingly deployed on resource-constrained edge devices to enable localized inference. To improve output quality, retrieval-augmented generation (RAG) is an efficient technique that seamlessly integrates local data into LLMs. However, existing edge computing paradigms primarily focus on single-node optimization, neglecting opportunities to holistically exploit distributed data and heterogeneous resources through cross-node collaboration. To bridge this gap, we propose CoEdge-RAG, a hierarchical scheduling framework for retrieval-augmented LLMs in collaborative edge computing. In general, privacy constraints preclude accurate a priori acquisition of heterogeneous data distributions across edge nodes, directly impeding RAG performance optimization. Thus, we first design an online query identification mechanism using proximal policy optimization (PPO), which autonomously infers query semantics and establishes cross-domain knowledge associations in an online manner. Second, we devise a dynamic inter-node scheduling strategy that balances workloads across heterogeneous edge nodes by synergizing historical performance analytics with real-time resource thresholds. Third, we develop an intra-node scheduler based on online convex optimization, adaptively allocating query processing ratios and memory resources to optimize the latency-quality trade-off under fluctuating assigned loads. Comprehensive evaluations across diverse QA benchmarks demonstrate that our proposed method significantly boosts the performance of collaborative retrieval-augmented LLMs, achieving performance gains of 4.23% to 91.39% over baseline methods across all tasks. © 2025 IEEE.

## 04 — Title Screening

**Title:** CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** CoEdge-RAG: Optimizing Hierarchical Scheduling for Retrieval-Augmented LLMs in Collaborative Edge Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
