---
id: "paper-2903"
title: "Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge"
authors: ["Zhai, Yu", "Wei, Lili"]
year: 2026
venue: "Electronics (Switzerland)"
venue_type: "journal"
doi: "10.3390/electronics15010230"
url: "https://www.scopus.com/pages/publications/105027026575?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["edge computing", "lightweight semantic segmentation", "point machine inspection", "quantization and deployment", "vision-language model"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2903 — Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge

## Metadata

- **Authors:** Zhai, Yu and Wei, Lili
- **Year:** 2026
- **Venue:** Electronics (Switzerland)
- **DOI:** 10.3390/electronics15010230
- **URL:** https://www.scopus.com/pages/publications/105027026575?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; lightweight semantic segmentation; point machine inspection; quantization and deployment; vision-language model

### Abstract

Existing inspection systems for railway point machines often suffer from high latency and poor interpretability, which impedes the real-time detection of critical mechanical anomalies, thereby increasing the risks of derailment and leading to cascading schedule delays. Addressing these challenges, this study proposes a lightweight computer vision-based detection framework deployed on the RK3588S edge platform. First, to overcome the accuracy degradation of segmentation networks on constrained edge NPUs, a Sensitivity-Aware Mixed-Precision Quantization and Heterogeneous Scheduling (SMPQ-HS) strategy is proposed. Second, a Multimodal Semantic Diagnostic Framework is constructed. By integrating geometric engagement depths—calculated via perspective rectification—with visual features, a Hard-Constrained Knowledge Embedding Paradigm is designed for the Qwen2.5-VL model. This approach constrains the stochastic reasoning of the Qwen2.5-VL model into standardized diagnostic conclusions. Experimental results demonstrate that the optimized model achieves an inference speed of 38.5 FPS and an mIoU of 0.849 on the RK3588S, significantly outperforming standard segmentation models in inference speed while maintaining high precision. Furthermore, the average depth-estimation error remains approximately 3%, and the VLM-based fault identification accuracy reaches 88%. Overall, this work provides a low-cost, deployable, and interpretable solution for intelligent point machine maintenance under edge-computing constraints. © 2026 by the authors.

## 04 — Title Screening

**Title:** Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Real-Time Visual Perception and Explainable Fault Diagnosis for Railway Point Machines at the Edge
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
