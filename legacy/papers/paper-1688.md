---
id: "paper-1688"
title: "SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling"
authors: ["Jaiswal, Shashwat", "Jain, Kunal", "Simmhan, Yogesh", "Parayil, Anjaly", "Mallick, Ankur", "Wang, Rujia", "Amant, Renee St", "Bansal, Chetan", "Ruhle, Victor", "Kulkarni, Anoop", "Kofsky, Steve", "Rajmohan, Saravan"]
year: 2025
venue: "Proceedings of the ACM on Measurement and Analysis of Computing Systems"
venue_type: "journal"
doi: "10.1145/3771576"
url: "https://www.scopus.com/pages/publications/105023958367?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: ""
keywords: ["forecast aware auto-scaling", "llm inference serving", "llm inference simulator", "production traces", "resource allocation", "scheduling", "workload analysis"]
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

# paper-1688 — SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling

## Metadata

- **Authors:** Jaiswal, Shashwat and Jain, Kunal and Simmhan, Yogesh and Parayil, Anjaly and Mallick, Ankur and Wang, Rujia and Amant, Renee St and Bansal, Chetan and Ruhle, Victor and Kulkarni, Anoop and Kofsky, Steve and Rajmohan, Saravan
- **Year:** 2025
- **Venue:** Proceedings of the ACM on Measurement and Analysis of Computing Systems
- **DOI:** 10.1145/3771576
- **URL:** https://www.scopus.com/pages/publications/105023958367?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 
- **Language:** English
- **Keywords:** forecast aware auto-scaling; llm inference serving; llm inference simulator; production traces; resource allocation; scheduling; workload analysis

### Abstract

Global cloud service providers handle inference workloads for Large Language Models (LLMs) that span latency-sensitive (e.g., chatbots) and insensitive (e.g., report writing) tasks, resulting in diverse and often conflicting Service Level Agreement (SLA) requirements. Managing such mixed workloads is challenging due to the complexity of the inference serving stack, which encompasses multiple models, GPU hardware, and global data centers. Existing solutions often silo such fast and slow tasks onto separate GPU resource pools with different SLAs, but this leads to significant under-utilization of expensive accelerators due to load mismatch. In this article, we characterize the LLM serving workloads at Microsoft Office 365, one of the largest users of LLMs within Microsoft Azure cloud with over 10 million requests per day, and highlight key observations across workloads in different data center regions and across time. This is one of the first such public studies of Internet-scale LLM workloads. We use these insights to propose SageServe, a comprehensive LLM serving framework that dynamically adapts to workload demands using multi-timescale control knobs. It combines short-term request routing to data centers with long-term scaling of GPU VMs and model placement with higher lead times, and co-optimizes the routing and resource allocation problem using a traffic forecast model and an Integer Linear Programming (ILP) solution. We evaluate SageServe through real runs and realistic simulations on 10 million production requests across three regions and four open-source models. We achieve up to 25% savings in GPU-hours compared to the current baseline deployment and reduce GPU-hour wastage due to inefficient auto-scaling by 80%, resulting in a potential monthly cost savings of up to $2.5 million, while maintaining tail latency and meeting SLAs. © 2025 Association for Computing Machinery. All rights reserved.

## 04 — Title Screening

**Title:** SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** SAGESERVE: Optimizing LLM Serving on Cloud Data Centers with Forecast Aware Auto-Scaling
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
