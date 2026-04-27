---
id: "paper-975"
title: "Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native"
authors: ["Joshi, Suyash", "Hasan, Basit", "Brindha, R."]
year: 2024
venue: "Proceedings of the 3rd International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2024"
venue_type: "conference"
doi: "10.1109/ICAAIC60222.2024.10575306"
url: "https://www.scopus.com/pages/publications/85198731134?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "578--582"
keywords: ["API", "Kubernetes", "Operator", "Orchestration"]
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

# paper-975 — Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native

## Metadata

- **Authors:** Joshi, Suyash and Hasan, Basit and Brindha, R.
- **Year:** 2024
- **Venue:** Proceedings of the 3rd International Conference on Applied Artificial Intelligence and Computing, ICAAIC 2024
- **DOI:** 10.1109/ICAAIC60222.2024.10575306
- **URL:** https://www.scopus.com/pages/publications/85198731134?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 578--582
- **Language:** English
- **Keywords:** API; Kubernetes; Operator; Orchestration

### Abstract

The widespread use of Large Language Models (LLMs) in natural language processing tasks has become increasingly common. LLMs have the ability to produce content that is both coherent and contextually relevant. Notwithstanding, there exist notable obstacles in effectively implementing and overseeing these models within operational settings, especially in infrastructures that are cloud native. A cloud-native system for optimizing and delivering live learning modules on Kubernetes clusters is presented in this study. There are many obstacles in the way of effectively deploying inference services on the cloud. After obtaining a trained model, cloud operators need to specify hardware configurations for every model-serving container. These settings cover a wide range of topics, including CPU core counts, GPU specs, GPU RAM, possible setups for GPU sharing, and runtime parameters like batch size. When combined, these factors provide a vast and intricate configuration space. By utilizing the declarative resource management that Kubernetes provides, the suggested approach leverages declarative resource management capabilities of Kubernetes and allows users to easily train and serve LLMs on those clusters. Kubernetes clusters from a variety of cloud providers, including KIND (provisioned on bare metal), Google Kubernetes Engine (GKE), and Amazon Elastic Kubernetes Service (EKS), are specifically supported by the framework. This Kubernetes custom resource enables users to maximize the performance and cost-effectiveness of LLM deployments by utilizing Kubernetes' scalability, flexibility, and resource allocation properties and allows to maintain the stable state with use of operators and watch pattern. © 2024 IEEE.

## 04 — Title Screening

**Title:** Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Optimal Declarative Orchestration of Full Lifecycle of Machine Learning Models for Cloud Native
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
