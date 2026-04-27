---
id: "paper-1853"
title: "Large Language Model Inference over Edge-assisted IoT: An Cost-efficient Optimization Method"
authors: ["Lin, Yiying", "Yao, Su", "Wang, Mu", "Wei, Shenghui", "Chen, Xingyan", "Zhang, Hongke"]
year: 2025
venue: "2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025"
venue_type: "conference"
doi: "10.1109/ICCC65529.2025.11148968"
url: "https://www.scopus.com/pages/publications/105017552508?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["computing offloading", "IoT", "large language model"]
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
    human_justification: "LLM as workload"

---

# paper-1853 — Large Language Model Inference over Edge-assisted IoT: An Cost-efficient Optimization Method

## Metadata

- **Authors:** Lin, Yiying and Yao, Su and Wang, Mu and Wei, Shenghui and Chen, Xingyan and Zhang, Hongke
- **Year:** 2025
- **Venue:** 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
- **DOI:** 10.1109/ICCC65529.2025.11148968
- **URL:** https://www.scopus.com/pages/publications/105017552508?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** computing offloading; IoT; large language model

### Abstract

With the widespread adoption of Internet of Things (IoT) devices and the rapid advancement of edge computing technologies, there is a growing demand for the application of Large Language Models (LLMs) in IoT environments assisted by edge computing. However, unlike the batch processing inference mode of traditional artificial intelligence tasks, the inference process of large language models exhibits significant iterative characteristics. This results in the processing time of a single request not only depending on its task complexity but also being influenced by other requests within the same batch. Therefore, when designing scheduling strategies, it is essential to comprehensively consider the overall processing situation of each batch of tasks. Based on this, this study proposes an innovative finegrained scheduling method. This method first intelligently selects requests that need to be offloaded based on the real-time load status of computing nodes and network conditions. Secondly, by predicting the length of received requests, it dynamically adjusts the number of requests per batch to maximize the alignment of request processing times, thereby optimizing the overall system performance.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Large Language Model Inference over Edge-assisted IoT: An Cost-efficient Optimization Method

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Large Language Model Inference over Edge-assisted IoT: An Cost-efficient Optimization Method
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Large Language Model Inference over Edge-assisted IoT: An Cost-efficient Optimization Method
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
