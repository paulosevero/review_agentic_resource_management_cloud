---
id: "paper-231"
title: "Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation"
authors: ["Obermeier, Sandra", "Berrendorf, Max", "Kroger, Peer"]
year: 2020
venue: "Proceedings - 2020 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology, WI-IAT 2020"
venue_type: "conference"
doi: "10.1109/WIIAT50758.2020.00056"
url: "https://www.scopus.com/pages/publications/85114440496?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "387--390"
keywords: ["Edge computing", "Index compression", "Reverse k-nearest neighbor"]
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
    human_decision: ""
    human_justification: ""

---

# paper-231 — Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation

## Metadata

- **Authors:** Obermeier, Sandra and Berrendorf, Max and Kroger, Peer
- **Year:** 2020
- **Venue:** Proceedings - 2020 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology, WI-IAT 2020
- **DOI:** 10.1109/WIIAT50758.2020.00056
- **URL:** https://www.scopus.com/pages/publications/85114440496?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 387--390
- **Language:** English
- **Keywords:** Edge computing; Index compression; Reverse k-nearest neighbor

### Abstract

The reverse k-nearest neighbor (RkNN) query is an established query type with various applications reaching from identifying highly influential objects over incrementally updating kNN graphs to optimizing sensor communication and outlier detection. State-of-the-art solutions exploit that the k-distances in real-world datasets often follow the power-law distribution, and bound them with linear lines in log-log space. In this work, we investigate this assumption and uncover that it is violated in regions of changing density, which we show are typical for real-life datasets. Towards a generic solution, we pose the estimation of k-distances as a regression problem. Thereby, we enable harnessing the power of the abundance of available Machine Learning models and profiting from their advancement. We propose a flexible approach which allows steering the performance-memory consumption trade-off, and in particular to find good solutions with a fixed memory budget crucial in the context of edge computing. Moreover, we show how to obtain and improve guaranteed bounds essential to exact query processing. In experiments on real-world datasets, we demonstrate how this framework can significantly reduce the index memory consumption, and strongly reduce the candidate set size. We publish our code at https://github.com/sobermeier/nonlinear-kdist, and a detailed technical report at https://arxiv.org/abs/2011.01773. © 2020 IEEE.

## 04 — Title Screening

**Title:** Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation

### Machine Screening

- **Final Score:** 0.0 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Memory-Efficient RkNN Retrieval by Nonlinear k-Distance Approximation
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
