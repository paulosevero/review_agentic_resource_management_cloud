---
id: "paper-1615"
title: "Edge-LLM Inference With Cost-Aware Layer Allocation and Adaptive Scheduling"
authors: ["Habibi, Sama", "Ercetin, Ozgur"]
year: 2025
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2025.3592308"
url: "https://www.scopus.com/pages/publications/105011716114?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "131614--131637"
keywords: ["Adaptive scheduling", "distributed AI", "edge computing", "fair incentive mechanism", "large language models", "resource allocation"]
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

# paper-1615 — Edge-LLM Inference With Cost-Aware Layer Allocation and Adaptive Scheduling

## Metadata

- **Authors:** Habibi, Sama and Ercetin, Ozgur
- **Year:** 2025
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2025.3592308
- **URL:** https://www.scopus.com/pages/publications/105011716114?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 131614--131637
- **Language:** English
- **Keywords:** Adaptive scheduling; distributed AI; edge computing; fair incentive mechanism; large language models; resource allocation

### Abstract

This paper addresses two key challenges in distributed Large Language Model (LLM) inference at the edge: 1) cost-efficient and fair task allocation, and 2) dynamic scheduling under deadline constraints. We propose two mechanisms: the Fair Cost-Efficient Incentive Mechanism (FCIM) for task and layer assignment, and the Adaptive Dynamic Scheduling Algorithm (ADSA) for execution scheduling on individual devices. FCIM is an auction-based mechanism that selects cost-effective, memory-feasible devices while minimizing task latency, reward cost, and device usage. Its adaptive reward design ensures positive utility and fairness, even under shifting system priorities. ADSA enables preemption-aware, deadline-driven scheduling by dynamically reordering tasks based on arrival time and workload characteristics. Simulations demonstrate that FCIM reduces communication overhead by 54.7% and task completion time by 36.9% compared to static and performance-driven baselines, while ADSA reduces queueing delay by 39% under strict deadline constraints. © 2013 IEEE.

## 04 — Title Screening

**Title:** Edge-LLM Inference With Cost-Aware Layer Allocation and Adaptive Scheduling

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge-LLM Inference With Cost-Aware Layer Allocation and Adaptive Scheduling
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Edge-LLM Inference With Cost-Aware Layer Allocation and Adaptive Scheduling
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
