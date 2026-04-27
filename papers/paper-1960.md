---
id: "paper-1960"
title: "Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures"
authors: ["Mohan, Jaya Preethi", "Ranganathan, Prakash"]
year: 2025
venue: "Proceedings - 2025 IEEE Cloud Summit, Cloud-Summit 2025"
venue_type: "conference"
doi: "10.1109/Cloud-Summit64795.2025.00027"
url: "https://www.scopus.com/pages/publications/105015510221?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "130--136"
keywords: ["API endpoints", "containers", "deployment", "large language models", "multi-cloud"]
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

# paper-1960 — Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures

## Metadata

- **Authors:** Mohan, Jaya Preethi and Ranganathan, Prakash
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE Cloud Summit, Cloud-Summit 2025
- **DOI:** 10.1109/Cloud-Summit64795.2025.00027
- **URL:** https://www.scopus.com/pages/publications/105015510221?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 130--136
- **Language:** English
- **Keywords:** API endpoints; containers; deployment; large language models; multi-cloud

### Abstract

This paper presents a secure and scalable framework for deploying Large Language Models (LLMs) across multi-cloud platforms using containerization technologies. The framework implements a dual-container architecture comprising a data_service container for Distributed Energy Resource (DER) data processing, aggregation, and the llm_service container that orchestrates multiple LLM providers, including GPT, Claude, Gemini and Llama. Leveraging tools such as Docker, Kubernetes, FASTAPI, and multi-cloud authentication, the framework addresses the key challenges related to security, interoperability and performance in distributed environments. The data_service container processes DER data at a configurable interval and integrates GPT models for energy pattern analysis and optimization recommendations. The llm_service container provides multi-model AI gateway functionality with dynamic load balancing and comprehensive performance monitoring across cloud providers. Security implementation includes container security scan, API security testing, network, and runtime security. Performance results show the GPT model for the analysis achieving 14.21% CPU usage and 1302.16MB memory consumption. Google Cloud Platform provides optimal cost efficiency up to 16.4% per analysis, compared to Amazon Web Services (AWS) and Microsoft Azure. The framework validates successful multi-cloud deployment across AWS, GCP, and Azure while maintaining enterprise-grade security. ©2025 IEEE.

## 04 — Title Screening

**Title:** Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Containerized Deployment of Secure LLM Workflows in Multi-Cloud Infrastructures
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
