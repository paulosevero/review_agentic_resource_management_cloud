---
id: "paper-912"
title: "ServerlessLLM: Low-Latency Serverless Inference for Large Language Models"
authors: ["Fu, Yao", "Xue, Leyang", "Huang, Yeqi", "Brabete, Andrei-Octavian", "Ustiugov, Dmitrii", "Patel, Yuvraj", "Mai, Luo"]
year: 2024
venue: "Proceedings of the 18th USENIX Symposium on Operating Systems Design and Implementation, OSDI 2024"
venue_type: "conference"
doi: ""
url: "https://www.scopus.com/pages/publications/85196227125?origin=resultslist"
publisher: "USENIX Association"
pages: "135--153"
keywords: ["Associative storage", "Computer graphics equipment", "Problem oriented languages", "Virtual storage", "Checkpoint storages", "Distributed systems", "Language model", "Loading system", "Low latency", "Memory capacity", "Model inference", "Multi-tier", "Storage capacity", "Storage hierarchy", "Graphics processing unit"]
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

# paper-912 — ServerlessLLM: Low-Latency Serverless Inference for Large Language Models

## Metadata

- **Authors:** Fu, Yao and Xue, Leyang and Huang, Yeqi and Brabete, Andrei-Octavian and Ustiugov, Dmitrii and Patel, Yuvraj and Mai, Luo
- **Year:** 2024
- **Venue:** Proceedings of the 18th USENIX Symposium on Operating Systems Design and Implementation, OSDI 2024
- **DOI:** N/A
- **URL:** https://www.scopus.com/pages/publications/85196227125?origin=resultslist
- **Publisher:** USENIX Association
- **Pages:** 135--153
- **Language:** English
- **Keywords:** Associative storage; Computer graphics equipment; Problem oriented languages; Virtual storage; Checkpoint storages; Distributed systems; Language model; Loading system; Low latency; Memory capacity; Model inference; Multi-tier; Storage capacity; Storage hierarchy; Graphics processing unit

### Abstract

This paper presents ServerlessLLM, a distributed system designed to support low-latency serverless inference for Large Language Models (LLMs). By harnessing the substantial near-GPU storage and memory capacities of inference servers, ServerlessLLM achieves effective local checkpoint storage, minimizing the need for remote checkpoint downloads and ensuring efficient checkpoint loading. The design of ServerlessLLM features three core contributions: (i) fast multi-tier checkpoint loading, featuring a new loading-optimized checkpoint format and a multi-tier loading system, fully utilizing the bandwidth of complex storage hierarchies on GPU servers; (ii) efficient live migration of LLM inference, which enables newly initiated inferences to capitalize on local checkpoint storage while ensuring minimal user interruption; and (iii) startup-time-optimized model scheduling, which assesses the locality statuses of checkpoints on each server and schedules the model onto servers that minimize the time to start the inference. Comprehensive evaluations, including microbenchmarks and real-world scenarios, demonstrate that ServerlessLLM dramatically outperforms state-of-the-art serverless systems, reducing latency by 10 - 200X across various LLM inference workloads. © OSDI 2024.All rights reserved.

## 04 — Title Screening

**Title:** ServerlessLLM: Low-Latency Serverless Inference for Large Language Models

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** ServerlessLLM: Low-Latency Serverless Inference for Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** ServerlessLLM: Low-Latency Serverless Inference for Large Language Models
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
