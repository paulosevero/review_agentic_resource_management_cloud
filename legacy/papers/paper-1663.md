---
id: "paper-1663"
title: "QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems"
authors: ["Hu, Miao", "He, Qi", "Wu, Di"]
year: 2025
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM55648.2025.11044591"
url: "https://www.scopus.com/pages/publications/105011046553?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["heterogeneous edge servers", "LLM", "partially in-formed", "Quantization", "scheduling"]
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

# paper-1663 — QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems

## Metadata

- **Authors:** Hu, Miao and He, Qi and Wu, Di
- **Year:** 2025
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM55648.2025.11044591
- **URL:** https://www.scopus.com/pages/publications/105011046553?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** heterogeneous edge servers; LLM; partially in-formed; Quantization; scheduling

### Abstract

The quantization technologies have enabled the practical deployment of large language models (LLMs) at the edge, however, current edge scheduling and quantization selection are separately designed. Furthermore, partially informed edge processing performance further exacerbates these challenges. To address these issues, we introduce QLLMS, a joint quantization-adaptive scheduling scheme for large language models tailored to partially informed edge serving systems. The primary objective of our approach is to reduce GPU rental costs by strategically orchestrating both quantization options and heterogeneous resources. The QLLMS algorithm first determines the available quantization set (AQS) to optimize the LLM inference performance within limited edge resources. To address the unpredictable nature of edge computing performance, we present a low-rank property-driven recovery approach, which can reconstruct complete AQS matrices using only partial samples. Subsequently, we devise a novel many-to-one matching algorithm that aims to strike a balance between efficient utilization of edge resources and optimal model inference performance, factoring in the available quantization options. We prove that QLLMS yields a stable matching without blocking pairs that could lead to inefficiencies. Experiment results show that QLLMS achieves a reduction of up to 22.36% in rental costs compared to state-of-the-art baselines in partially informed edge serving systems while simultaneously improving the task completion rate on edge servers.  © 2025 IEEE.

## 04 — Title Screening

**Title:** QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** QLLMS: Quantization-Adaptive LLM Scheduling for Partially Informed Edge Serving Systems
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
