---
id: "paper-1301"
title: "Efficient Deployment of Large Language Model across Cloud-Device Systems"
authors: ["Yang, Fan", "Wang, Zehao", "Zhang, Haoyu", "Zhu, Zhenhua", "Yang, Xinhao", "Dai, Guohao", "Wang, Yu"]
year: 2024
venue: "International System on Chip Conference"
venue_type: "conference"
doi: "10.1109/SOCC62300.2024.10737825"
url: "https://www.scopus.com/pages/publications/85210582631?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Cloud-Device Collaboration System", "Efficient Inference", "Large Language Models"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-1301 — Efficient Deployment of Large Language Model across Cloud-Device Systems

## Metadata

- **Authors:** Yang, Fan and Wang, Zehao and Zhang, Haoyu and Zhu, Zhenhua and Yang, Xinhao and Dai, Guohao and Wang, Yu
- **Year:** 2024
- **Venue:** International System on Chip Conference
- **DOI:** 10.1109/SOCC62300.2024.10737825
- **URL:** https://www.scopus.com/pages/publications/85210582631?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud-Device Collaboration System; Efficient Inference; Large Language Models

### Abstract

The capabilities of large language models (LLMs) in text comprehension and generation are advancing artificial intelligence. However, the growing number of parameters and computational demands challenge the efficient deployment of inference services. High-performance GPU clusters in the cloud can meet these requirements but incur high service costs and network stability issues, which struggle to meet service-level agreements (SLAs). The 'cloud-device collaboration' approach leverages the heterogeneous hardware on both the cloud and device sides to satisfy SlAs efficiently. However, the varying operational intensity among different LLM operators and their dynamic nature complicate load scheduling for cloud-device systems. To address these challenges, we optimize LLM inference deployment on cloud-device systems through three aspects: scheduling algorithm, hardware modeling, and compilation deployment. For the scheduling algorithm, we analyze the LLM computation network, evaluate the computation-to-memory access ratio under different sequence lengths, and propose a greedy algorithm-based operator-level scheduling strategy. For the hardware modeling, we establish a relationship between operational intensity and GPU resource utilization to estimate operator running time. Finally, we designed a cloud-device LLM compiler framework for quantitative evaluation and efficient deployment across various hardware combinations and inference tasks. In specific inference scenarios, our framework satisfies the need for inference latency and achieves an average cost reduction of 20.7% compared to cloud-side-only inference.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Efficient Deployment of Large Language Model across Cloud-Device Systems

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Efficient Deployment of Large Language Model across Cloud-Device Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Efficient Deployment of Large Language Model across Cloud-Device Systems
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
