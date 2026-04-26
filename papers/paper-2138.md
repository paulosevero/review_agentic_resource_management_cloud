---
id: "paper-2138"
title: "Proactive Concurrency Tuning for Inference Serving in Serverless Platform"
authors: ["Shwe, Thanda", "Muhammad-Bello, Bilkisu Larai", "Aritsugi, Masayoshi"]
year: 2025
venue: "Proceedings - 2025 IEEE Conference on Cloud and Big Data Computing, CBDCom 2025"
venue_type: "conference"
doi: "10.1109/CBDCOM68404.2025.00011"
url: "https://www.scopus.com/pages/publications/105033527802?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "23--32"
keywords: ["Cloud Computing", "Cold Start", "Image Inference", "LLM"]
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

# paper-2138 — Proactive Concurrency Tuning for Inference Serving in Serverless Platform

## Metadata

- **Authors:** Shwe, Thanda and Muhammad-Bello, Bilkisu Larai and Aritsugi, Masayoshi
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE Conference on Cloud and Big Data Computing, CBDCom 2025
- **DOI:** 10.1109/CBDCOM68404.2025.00011
- **URL:** https://www.scopus.com/pages/publications/105033527802?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 23--32
- **Language:** English
- **Keywords:** Cloud Computing; Cold Start; Image Inference; LLM

### Abstract

Serverless platforms are increasingly being adopted for deploying machine learning (ML) and deep learning (DL) inference workloads, due to their scalability, isolation, and ease of deployment. These benefits are challenged by cold start latency, a well-known issue in serverless platforms, which significantly affects the performance of inference workloads. Provisioned concurrency is used to prepare resources in advance to reduce cold starts, but it can be costly if it is not managed well. Determining the appropriate level of concurrency is particularly challenging for dynamic request patterns. Static, threshold-based approaches lack the responsiveness needed to adapt to changing workloads, often resulting in over-provisioning or under-provisioning. In this paper, we introduce proactive concurrency tuning for setting up the concurrency level dynamically and automatically based on the workload access pattern. Unlike prior works that focus on pre-warming of functions during periods of inactivity and infrastructure-level optimizations to mitigate cold starts, our approach proactively predicts concurrency demands for bursty and high-intensity workloads at the user level without requiring any modifications to the underlying infrastructure. This makes it broadly applicable across a wide range of serverless platforms, both public and private. Our evaluation on the public serverless platform AWS Lambda demonstrates that our approach reduces cold starts more effectively than both fixed concurrency and reactive methods, while also minimizing costs. ©2025 IEEE.

## 04 — Title Screening

**Title:** Proactive Concurrency Tuning for Inference Serving in Serverless Platform

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Concurrency Tuning for Inference Serving in Serverless Platform
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Proactive Concurrency Tuning for Inference Serving in Serverless Platform
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
