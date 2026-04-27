---
id: "paper-1206"
title: "Vexless: A Serverless Vector Data Management System Using Cloud Functions"
authors: ["Su, Yongye", "Sun, Yinqi", "Zhang, Minjia", "Wang, Jianguo"]
year: 2024
venue: "Annals of the Entomological Society of America"
venue_type: "journal"
doi: "10.1145/3654990"
url: "https://www.scopus.com/pages/publications/105018840957?origin=resultslist"
publisher: "Entomological Society of America"
pages: ""
keywords: ["cloud functions", "serverless computing", "serverless databases", "vector databases"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1206 — Vexless: A Serverless Vector Data Management System Using Cloud Functions

## Metadata

- **Authors:** Su, Yongye and Sun, Yinqi and Zhang, Minjia and Wang, Jianguo
- **Year:** 2024
- **Venue:** Annals of the Entomological Society of America
- **DOI:** 10.1145/3654990
- **URL:** https://www.scopus.com/pages/publications/105018840957?origin=resultslist
- **Publisher:** Entomological Society of America
- **Pages:** 
- **Language:** English
- **Keywords:** cloud functions; serverless computing; serverless databases; vector databases

### Abstract

Cloud functions, exemplified by AWS Lambda and Azure Functions, are emerging as a new computing paradigm in the cloud. They provide elastic, serverless, and low-cost cloud computing, making them highly suitable for bursty and sparse workloads, which are quite common in practice. Thus, there is a new trend in designing data systems that leverage cloud functions. In this paper, we focus on vector databases, which have recently gained significant attention partly due to large language models. In particular, we investigate how to use cloud functions to build high-performance and cost-efficient vector databases. This presents significant challenges in terms of how to perform sharding, how to reduce communication overhead, and how to minimize cold-start times. In this paper, we introduce Vexless, the first vector database system optimized for cloud functions. We present three optimizations to address the challenges. To perform sharding, we propose a global coordinator (orchestrator) that assigns workloads to Cloud function instances based on their available hardware resources. To overcome communication overhead, we propose the use of stateful cloud functions, eliminating the need for costly communications during synchronization. To minimize cold-start overhead, we introduce a workload-aware Cloud function lifetime management strategy. Vexless has been implemented using Azure Functions. Experimental results demonstrate that Vexless can significantly reduce costs, especially on bursty and sparse workloads, compared to cloud VM instances, while achieving similar or higher query performance and accuracy. © 2024 ACM.

## 04 — Title Screening

**Title:** Vexless: A Serverless Vector Data Management System Using Cloud Functions

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Vexless: A Serverless Vector Data Management System Using Cloud Functions
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Vexless: A Serverless Vector Data Management System Using Cloud Functions
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
