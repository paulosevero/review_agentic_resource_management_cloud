---
id: "paper-1168"
title: "Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios"
authors: ["Sang, Ziyi", "Cai, Mingjun", "Shen, Shihao", "Zhang, Cheng", "Wang, Xiaofei", "Qiu, Chao"]
year: 2024
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM52923.2024.10901331"
url: "https://www.scopus.com/pages/publications/105000819313?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4618--4623"
keywords: ["diffusion model", "imitation learning", "Kubernetes", "Service migration"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1168 — Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios

## Metadata

- **Authors:** Sang, Ziyi and Cai, Mingjun and Shen, Shihao and Zhang, Cheng and Wang, Xiaofei and Qiu, Chao
- **Year:** 2024
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM52923.2024.10901331
- **URL:** https://www.scopus.com/pages/publications/105000819313?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4618--4623
- **Language:** English
- **Keywords:** diffusion model; imitation learning; Kubernetes; Service migration

### Abstract

With the rapid increase in user scale and the explosive rise of emerging applications, the contradiction between heavy load pressure and excellent network performance is becoming increasingly prominent, and task processing is gradually shifting towards the edge of the network. However, the resources of edge networks are limited, making it difficult to meet the huge computing and storage needs, and managing and allocating edge nodes is also a huge challenge. The Kubernetes (K8S) framework for deploying and orchestrating containerized applications provides a solution for this. How to improve the adaptability of K8S in edge networks, meet the demand of services for heterogeneous resources, and train decision models with better performance using limited datasets has become an urgent problem to be solved. Based on the above issues, we propose a distributed service migration architecture for multi-user access, and design a service migration algorithm based on imitation learning to achieve resource combination optimization and reduce the impact of insufficient data on model training. Design agent models based on diffusion models to accelerate model convergence and avoid the increase in training costs caused by constantly updating agent models. Our results show that the efficiency of the expert model is 92.0%, and the learning process of the agent model can converge within 100 training cycles with an accuracy of 97.89%. The service processing delay, throughput rate, and model convergence are all significantly better than those of classical algorithms. © 2024 IEEE.

## 04 — Title Screening

**Title:** Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Kubernetes Scheduling Design Based on Imitation Learning in Edge Cloud Scenarios
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
