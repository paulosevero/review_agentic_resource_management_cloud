---
id: "paper-110"
title: "BARISTA: Efficient and scalable serverless serving system for deep learning prediction services"
authors: ["Bhattacharjee, Anirban", "Chhokra, Ajay Dev", "Kang, Zhuangwei", "Sun, Hongyang", "Gokhale, Aniruddha", "Karsai, Gabor"]
year: 2019
venue: "Proceedings - 2019 IEEE International Conference on Cloud Engineering, IC2E 2019"
venue_type: "conference"
doi: "10.1109/IC2E.2019.00-10"
url: "https://www.scopus.com/pages/publications/85071468472?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "23--33"
keywords: ["Containers", "Machine Learning Models", "Predictive Analytics", "Resource Management", "Serverless Computing"]
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

# paper-110 — BARISTA: Efficient and scalable serverless serving system for deep learning prediction services

## Metadata

- **Authors:** Bhattacharjee, Anirban and Chhokra, Ajay Dev and Kang, Zhuangwei and Sun, Hongyang and Gokhale, Aniruddha and Karsai, Gabor
- **Year:** 2019
- **Venue:** Proceedings - 2019 IEEE International Conference on Cloud Engineering, IC2E 2019
- **DOI:** 10.1109/IC2E.2019.00-10
- **URL:** https://www.scopus.com/pages/publications/85071468472?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 23--33
- **Language:** English
- **Keywords:** Containers; Machine Learning Models; Predictive Analytics; Resource Management; Serverless Computing

### Abstract

Pre-trained deep learning models are increasingly being used to offer a variety of compute-intensive predictive analytics services such as fitness tracking, speech, and image recognition. The stateless and highly parallelizable nature of deep learning models makes them well-suited for serverless computing paradigm. However, making effective resource management decisions for these services is a hard problem due to the dynamic workloads and diverse set of available resource configurations that have different deployment and management costs. To address these challenges, we present a distributed and scalable deep-learning prediction serving system called Barista and make the following contributions. First, we present a fast and effective methodology for forecasting workloads by identifying various trends. Second, we formulate an optimization problem to minimize the total cost incurred while ensuring bounded prediction latency with reasonable accuracy. Third, we propose an efficient heuristic to identify suitable compute resource configurations. Fourth, we propose an intelligent agent to allocate and manage the compute resources by horizontal and vertical scaling to maintain the required prediction latency. Finally, using representative real-world workloads for an urban transportation service, we demonstrate and validate the capabilities of Barista. © 2019 IEEE.

## 04 — Title Screening

**Title:** BARISTA: Efficient and scalable serverless serving system for deep learning prediction services

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** BARISTA: Efficient and scalable serverless serving system for deep learning prediction services
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** BARISTA: Efficient and scalable serverless serving system for deep learning prediction services
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
