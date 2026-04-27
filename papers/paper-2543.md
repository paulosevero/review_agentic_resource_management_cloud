---
id: "paper-2543"
title: "Mico: efficient query scheduling for multi-cloud deployed LLM inference service"
authors: ["Cong, Peizhuang", "Yang, Tong", "Zhang, Yuchao", "Wang, Wendong", "Xu, Ke"]
year: 2026
venue: "Science China Information Sciences"
venue_type: "journal"
doi: "10.1007/s11432-024-4487-8"
url: "https://www.scopus.com/pages/publications/105027455232?origin=resultslist"
publisher: "Science China Press"
pages: ""
keywords: ["cloud computing", "cloud service optimization", "LLM inference", "prediction", "query scheduling"]
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

# paper-2543 — Mico: efficient query scheduling for multi-cloud deployed LLM inference service

## Metadata

- **Authors:** Cong, Peizhuang and Yang, Tong and Zhang, Yuchao and Wang, Wendong and Xu, Ke
- **Year:** 2026
- **Venue:** Science China Information Sciences
- **DOI:** 10.1007/s11432-024-4487-8
- **URL:** https://www.scopus.com/pages/publications/105027455232?origin=resultslist
- **Publisher:** Science China Press
- **Pages:** 
- **Language:** English
- **Keywords:** cloud computing; cloud service optimization; LLM inference; prediction; query scheduling

### Abstract

Given the powerful capabilities of large language models (LLMs), many tech companies make LLM inference a service for users, which may be deployed in multiple clouds to provide better service. Computational overhead and cloud workload are crucial metrics in cloud computing task scheduling. However, the autoregressive nature of LLMs makes these metrics difficult to measure. Specifically, LLMs require multiple iterations of computation to process a single query, and there is significant differentiation in the number of iterations needed for different queries. Moreover, batch-wise model inference exacerbates the gap between allocated and actual computational loads for each cloud due to these variations, ultimately affecting computational resource utilization and the throughput of inference service query processing. To this end, we propose Mico, which includes a query scheduling strategy based on response length prediction to achieve token-granularity workload distribution across clouds, and an inference framework that supports the flexible insertion of queries into the processing batch, eliminating unnecessary computation introduced by the iteration differentiation of queries in batch-wise inference. We conducted experiments based on two GPT series models, and the results show that Mico can reduce KV-Cache resource consumption by 44.89% during inference and increase the query processing throughput of the service system by up to 2.2×. © Science China Press 2026.

## 04 — Title Screening

**Title:** Mico: efficient query scheduling for multi-cloud deployed LLM inference service

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Mico: efficient query scheduling for multi-cloud deployed LLM inference service
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Mico: efficient query scheduling for multi-cloud deployed LLM inference service
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
