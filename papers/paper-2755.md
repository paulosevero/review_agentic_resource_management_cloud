---
id: "paper-2755"
title: "Deploying Efficient LLM Agents on Maritime Autonomous Surface Ships: Fine-Tuning, RAG, and Function Calling in a Mid-Size Model"
authors: ["Ren, Yiling", "Chen, Mozi", "Weng, Junjie", "Zhang, Shengkai", "Xiao, Xuedou", "Liu, Kezhong"]
year: 2026
venue: "Information (Switzerland)"
venue_type: "journal"
doi: "10.3390/info17030284"
url: "https://www.scopus.com/pages/publications/105033859103?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["decision support systems", "edge computing", "large language models", "low-rank adaptation", "maritime autonomous surface ships", "retrieval-augmented generation"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2755 — Deploying Efficient LLM Agents on Maritime Autonomous Surface Ships: Fine-Tuning, RAG, and Function Calling in a Mid-Size Model

## Metadata

- **Authors:** Ren, Yiling and Chen, Mozi and Weng, Junjie and Zhang, Shengkai and Xiao, Xuedou and Liu, Kezhong
- **Year:** 2026
- **Venue:** Information (Switzerland)
- **DOI:** 10.3390/info17030284
- **URL:** https://www.scopus.com/pages/publications/105033859103?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** decision support systems; edge computing; large language models; low-rank adaptation; maritime autonomous surface ships; retrieval-augmented generation

### Abstract

Deploying Large Language Models (LLMs) on Maritime Autonomous Surface Ships (MASS) entails a critical trade-off between reasoning depth, inference latency, and hardware constraints. To fill the existing gap, we introduce MARTIAN (Maritime Agent for Real-time Tactical Inference And Navigation), a 14B-parameter decision support agent engineered for edge deployment on standard vessel hardware (e.g., the NVIDIA Jetson AGX Orin). Central to our approach is the Cognitive Core architecture, which utilizes a verified dataset of 21,800 Chain-of-Thought (CoT) instruction–response pairs to align general linguistic capabilities with maritime procedural logic. Empirical evaluations demonstrate that MARTIAN achieves an overall accuracy of 73.23% (SFT only) and 81.16% (SFT + RAG) on the Bilingual Maritime Multiple-Choice Questionnaire (BM-MCQ), a standardized assessment dataset constructed based on Officer of the Watch (OOW) competencies. Notably, the SFT-only configuration attains 78.53% on pure-logic-intensive COLREG tasks—surpassing the 72B-parameter Qwen-2.5 foundation model in this domain—while maintaining a real-time inference latency of 22.4 ms/token. Crucially, our ablation studies support a nuanced Interference Hypothesis: while RAG significantly enhances factual recall in knowledge-intensive domains (boosting total accuracy from 73.23% to 81.16%), it concurrently introduces semantic noise that degrades performance in pure logic reasoning tasks (e.g., COLREG maneuvering accuracy decreases from 78.53% to 77.36%). On the basis of this finding, we identify and empirically motivate a decoupled cognitive design principle that separates procedural reflexes (via SFT) from declarative knowledge (via RAG). While the full implementation of an adaptive routing mechanism is deferred to future work, the ablation results presented herein offer a validated, cost-effective reference architecture for deploying transparent and regulation-compliant AI on resource-constrained merchant vessels. © 2026 by the authors.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
