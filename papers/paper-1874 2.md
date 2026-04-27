---
id: "paper-1874"
title: "CSGO: Generalized Optimization for Cold Start in Wireless Collaborative Edge LLM Systems"
authors: ["Liu, Xuran", "Xue, Nan", "Bao, Rui", "Sun, Yaping", "Chen, Zhiyong", "Tao, Meixia", "Xu, Xiaodong", "Cui, Shuguang"]
year: 2025
venue: "Journal of Communications and Information Networks"
venue_type: "journal"
doi: "10.23919/JCIN.2025.11357495"
url: "https://www.scopus.com/pages/publications/105029056758?origin=resultslist"
publisher: "Posts and Telecom Press Co Ltd"
pages: "340--351"
keywords: ["cold start latency", "large language models", "mobile edge computing", "pipeline parallelism"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-1874 — CSGO: Generalized Optimization for Cold Start in Wireless Collaborative Edge LLM Systems

## Metadata

- **Authors:** Liu, Xuran and Xue, Nan and Bao, Rui and Sun, Yaping and Chen, Zhiyong and Tao, Meixia and Xu, Xiaodong and Cui, Shuguang
- **Year:** 2025
- **Venue:** Journal of Communications and Information Networks
- **DOI:** 10.23919/JCIN.2025.11357495
- **URL:** https://www.scopus.com/pages/publications/105029056758?origin=resultslist
- **Publisher:** Posts and Telecom Press Co Ltd
- **Pages:** 340--351
- **Language:** English
- **Keywords:** cold start latency; large language models; mobile edge computing; pipeline parallelism

### Abstract

While deploying large language models on edge devices promises low-latency and privacy-preserving artificial intelligence (AI) services, it is hindered by limited device resources. Although pipeline parallelism facilitates distributed inference, existing approaches often ignore the cold-start latency caused by on-demand model loading. In this paper, we propose a latency-aware scheduling framework that overlaps model loading with computation and communication to minimize total inference latency. Based on device and model parameters, the framework dynamically adjusts layer partitioning and allocation to effectively hide loading time, thereby eliminating as many idle periods as possible. We formulate the problem as a mixed-integer non-linear program (MINLP) and design an efficient dynamic programming algorithm to optimize model partitioning and device assignment. Experimental results show that the proposed method significantly reduces cold-start latency compared to baseline strategies. © 2025, Posts and Telecom Press Co Ltd. All rights reserved.

## 04 — Title Screening

**Title:** CSGO: Generalized Optimization for Cold Start in Wireless Collaborative Edge LLM Systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** CSGO: Generalized Optimization for Cold Start in Wireless Collaborative Edge LLM Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** CSGO: Generalized Optimization for Cold Start in Wireless Collaborative Edge LLM Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
