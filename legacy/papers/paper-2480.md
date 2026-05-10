---
id: "paper-2480"
title: "Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment"
authors: ["Zhu, Jiahao", "Zhao, Lu", "Xiao, Fu", "Duan, Lingjie"]
year: 2025
venue: "IEEE International Workshop on Quality of Service, IWQoS"
venue_type: "conference"
doi: "10.1109/IWQoS65803.2025.11143464"
url: "https://www.scopus.com/pages/publications/105016993620?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Approximate Algorithm", "Distributed LLM Inference", "Edge Computing", "Inference Allocation"]
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

# paper-2480 — Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment

## Metadata

- **Authors:** Zhu, Jiahao and Zhao, Lu and Xiao, Fu and Duan, Lingjie
- **Year:** 2025
- **Venue:** IEEE International Workshop on Quality of Service, IWQoS
- **DOI:** 10.1109/IWQoS65803.2025.11143464
- **URL:** https://www.scopus.com/pages/publications/105016993620?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Approximate Algorithm; Distributed LLM Inference; Edge Computing; Inference Allocation

### Abstract

The distributed deployment of Large Language Models (LLM) on edge servers close to users has unlocked the service provider's potential to deliver low-latency inference. To obtain more benefit by serving more resource-demanding inference tasks based on resource-limited edge servers, it is critical for the service provider to allocate inference to suitable edge servers. Three new challenges hinder existing approaches from being implemented: the distributed LLM inference requires edge servers to collaborate following a novel workflow different from other tasks; the generative nature of LLM incurs uncertainty in task resource occupations; considering the heterogeneity in users' latency requirements and service benefit, merely minimizing the total user-perceived latency can not maximize the benefit. In this paper, we make the first attempt to study the edge inference allocation problem for distributed LLM deployment while conquering these challenges. Specifically, we propose a collaborative workflow for edge servers to conduct distributed LLM inferences. Then, we estimate the resource occupations by employing Exact Conic Reformulation (ECR). Based on this, with the objective of maximizing the total service benefit, we formulate the inference allocation problem as a binary integer programming problem which is NP-hard. An approximate algorithm is proposed to find approximate solutions efficiently. Extensive experiments based on a real-world dataset demonstrate the performance of our approach. © 2025 IEEE.

## 04 — Title Screening

**Title:** Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Birds in Cages: Edge Inference Allocation for Distributed LLM Deployment
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
