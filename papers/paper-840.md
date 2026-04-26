---
id: "paper-840"
title: "A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum"
authors: ["Cai, Binlei", "Wang, Xiaoli", "Wang, Bin", "Yang, Meihong", "Guo, Ying", "Guo, Qin"]
year: 2024
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2024.110279"
url: "https://www.scopus.com/pages/publications/85186415484?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Edge-cloud continuum", "Microservice deployment", "Reinforcement learning", "Resource management", "Tail latency"]
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

# paper-840 — A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum

## Metadata

- **Authors:** Cai, Binlei and Wang, Xiaoli and Wang, Bin and Yang, Meihong and Guo, Ying and Guo, Qin
- **Year:** 2024
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2024.110279
- **URL:** https://www.scopus.com/pages/publications/85186415484?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge-cloud continuum; Microservice deployment; Reinforcement learning; Resource management; Tail latency

### Abstract

Modern user-facing services are progressively evolving from large monolithic applications to complex graphs of loosely-coupled microservices. While this shift provides opportunities to offload some microservices of a user-facing service to edge devices that are close to the end users, it also complicates the application deployment and resource provisioning in the edge-cloud continuum, due to complex relationships across microservices and unstable public networks. To reduce resource wastage and improve user experience, this paper presents SMO, a self-managed orchestration system for microservices. SMO leverages a self-stabilizing placement mechanism to optimally deploy microservices through perceiving both interferences and communication overheads. During runtime, it further tailors a multi-agent deep deterministic policy gradient (MADDPG)-based model in combination with attention and prioritized replay, which automatically provisions appropriate resources for each microservice subject to the differentiated tail latency Service Level Objectives (SLOs) of multiple user workloads. Experimental results demonstrate that SMO saves up to 39% of CPU cores and 47% of memory footprint while providing guarantees for heterogeneous tail latency SLOs. © 2024 Elsevier B.V.

## 04 — Title Screening

**Title:** A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A self-stabilizing and auto-provisioning orchestration for microservices in edge-cloud continuum
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
