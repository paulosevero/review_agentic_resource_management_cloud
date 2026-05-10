---
id: "paper-1886"
title: "GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum"
authors: ["Liu, Peini", "Santos, Jos\u00e9", "De Turck, Filip", "Guitart, Jordi"]
year: 2025
venue: "Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025"
venue_type: "conference"
doi: "10.1145/3773274.3774275"
url: "https://www.scopus.com/pages/publications/105027132697?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: ""
keywords: ["Computing Continuum", "Intelligent Service Migration", "Kubernetes", "Power-Performance Aware", "Reinforcement Learning"]
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

# paper-1886 — GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum

## Metadata

- **Authors:** Liu, Peini and Santos, José and De Turck, Filip and Guitart, Jordi
- **Year:** 2025
- **Venue:** Proceedings of the 18th IEEE/ACM International Conference on Utility and Cloud Computing, UCC 2025
- **DOI:** 10.1145/3773274.3774275
- **URL:** https://www.scopus.com/pages/publications/105027132697?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 
- **Language:** English
- **Keywords:** Computing Continuum; Intelligent Service Migration; Kubernetes; Power-Performance Aware; Reinforcement Learning

### Abstract

Machine Learning (ML) services require both responsiveness and efficiency. In the dynamic Computing Continuum (CC), service migration has emerged as an important strategy to optimize service performance, improve power efficiency, or reduce operational costs. A basis enabler of the service migration in the CC is containerization and container orchestration, however, dynamically moving the service among Cloud and Edge servers based on several uncertainties is still challenging. In this paper, we present GreenWise, a framework for intelligent service migration for containerized ML services in the heterogeneous CC. GreenWise extends the monitoring agents to continuously monitor power consumption and performance metrics across diverse layers and sources in real-time, providing a holistic view of states. Leveraging Reinforcement Learning (RL), it enables Power-Performance aware strategies to achieve near-optimal online migration decisions under dynamic conditions. We perform GreenWise on top of a Kubernetes-based CC platform, implementing agents for intelligent migration for containerized ML services. Experimental results demonstrate that GreenWise achieves effective trade-offs between performance and power efficiency. Our proposed Power-Latency-Aware (MaskPPO) migration strategy outperforms Random and Round-Robin baselines 159.2% and 13.8% in a real cluster. These results highlight GreenWise's potential for sustainable and intelligent ML service migration in the dynamic CC. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** GreenWise: Intelligent Application Migration for Containerized Machine Learning Services in the Computing Continuum
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
