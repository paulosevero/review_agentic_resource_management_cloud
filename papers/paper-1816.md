---
id: "paper-1816"
title: "Polygon training architecture for foundation models with network- and device-level heterogeneity"
authors: ["Li, Chuantao", "Liu, Fulai", "Wu, Xiaoming", "Huo, Jidong", "Wang, Chunxiao", "Liang, Antian", "Zhao, Zhigang", "Gao, Longxiang"]
year: 2025
venue: "Information Fusion"
venue_type: "journal"
doi: "10.1016/j.inffus.2025.103264"
url: "https://www.scopus.com/pages/publications/105004937680?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Foundation models training", "Fusion system design", "Heterogeneous training", "Parallelism optimization"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1816 — Polygon training architecture for foundation models with network- and device-level heterogeneity

## Metadata

- **Authors:** Li, Chuantao and Liu, Fulai and Wu, Xiaoming and Huo, Jidong and Wang, Chunxiao and Liang, Antian and Zhao, Zhigang and Gao, Longxiang
- **Year:** 2025
- **Venue:** Information Fusion
- **DOI:** 10.1016/j.inffus.2025.103264
- **URL:** https://www.scopus.com/pages/publications/105004937680?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Foundation models training; Fusion system design; Heterogeneous training; Parallelism optimization

### Abstract

Large language models have experienced rapid growth, constrained by the computational limits of training foundation models. With the continuous release of new products, high-end devices are increasingly accessible, eventually transitioning into the mid-range and low-end segments. A pivotal focus in current research is the facilitation of joint training across diverse regions and devices. However, this research encounters dual-heterogeneous challenges in both network and device levels. We introduce a novel polygon training architecture for foundation models, designed to support large-scale training paradigms. Our approach integrates critical factors—including model size, network conditions, and device performance-from both global and local perspectives. Initially, we develop a lightweight polygon initialization algorithm that conceptualizes data centers as the fundamental units on a global scale. This algorithm evaluates computing power, latency, and bandwidth between units to establish an initial training strategy that leverages both pipeline and data parallelism. Following this, we consider the complexities introduced by diverse combinations of heterogeneous devices and network conditions, which give rise to intricate communication scenarios. To tackle this issue, we design a polygon local optimization algorithm-a precise search strategy that accurately assesses communication costs during model training across heterogeneous configurations. This approach identifies an efficient parallel architecture, enabling enhanced collaborative training with fine granularity. Our experimental results indicate that, compared to existing state-of-the-art methods, our algorithm expands the training scale by 1.5 × with the same computational resources, accelerates processing speed by 1.9 ×, and reduces training time by 46% for comparable tasks. © 2025 Elsevier B.V.

## 04 — Title Screening

**Title:** Polygon training architecture for foundation models with network- and device-level heterogeneity

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Polygon training architecture for foundation models with network- and device-level heterogeneity
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Polygon training architecture for foundation models with network- and device-level heterogeneity
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
