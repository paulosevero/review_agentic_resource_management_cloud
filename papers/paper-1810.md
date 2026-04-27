---
id: "paper-1810"
title: "MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds"
authors: ["Li, Qixin", "Ren, Xiaoxu", "Wang, Zhongyuan", "Yao, Haipeng", "He, Yuan", "Liu, Yunhao"]
year: 2025
venue: "IEEE International Workshop on Quality of Service, IWQoS"
venue_type: "conference"
doi: "10.1109/IWQoS65803.2025.11143291"
url: "https://www.scopus.com/pages/publications/105016996899?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Containerized AI", "Edge Clouds Network", "LLM", "Microservices Deployment"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1810 — MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds

## Metadata

- **Authors:** Li, Qixin and Ren, Xiaoxu and Wang, Zhongyuan and Yao, Haipeng and He, Yuan and Liu, Yunhao
- **Year:** 2025
- **Venue:** IEEE International Workshop on Quality of Service, IWQoS
- **DOI:** 10.1109/IWQoS65803.2025.11143291
- **URL:** https://www.scopus.com/pages/publications/105016996899?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Containerized AI; Edge Clouds Network; LLM; Microservices Deployment

### Abstract

Large language models (LLMs) have emerged as a transformative advancement in artificial intelligence (AI). To fully leverage their potential, Docker containers, serving as a lightweight, portable, and isolated framework, facilitate the seamless deployment of LLM-based applications. However, the deployment of containerized AI microservices faces challenges such as heavy network loads, delayed image loading, and redundancy. In this paper, we introduce MetaPipe, an innovative incremental deployment approach for containerized AI microservices in edge cloud environments. MetaPipe aims to optimize startup times through a dynamic workflow that incorporates proactive layer pre-fetching and reinforcement layer re-scheduling. The proactive pre-fetching reduces service deployment time through layer caching prediction and pre-scheduling before requests arrive, while the reinforcement re-scheduling addresses inaccuracies by dynamically adjusting layer scheduling strategies after requests arrive. Extensive experiments on realworld datasets show that MetaPipe significantly outperforms traditional methods, achieving 83.58% reduction in initialization startup time and 85.58% reduction in cold startup time. These results highlight its effectiveness in enhancing the performance of AI microservices deployment within edge cloud environments. © 2025 IEEE.

## 04 — Title Screening

**Title:** MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MetaPipe: Incremental Deployment of Containerized AI Microservices for Edge Clouds
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
