---
id: "paper-2239"
title: "Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures"
authors: ["Vellaisamy, Prabhu", "Labonte, Thomas", "Chakraborty, Sourav", "Turner, Matt", "Sury, Samantika", "Shen, John Paul"]
year: 2025
venue: "IEEE International Symposium on Performance Analysis of Systems and Software/ISPASS"
venue_type: "conference"
doi: "10.1109/ISPASS64960.2025.00015"
url: "https://www.scopus.com/pages/publications/105029905852?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "49--61"
keywords: ["Accelerators", "AI", "benchmarking", "coupling"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2239 — Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures

## Metadata

- **Authors:** Vellaisamy, Prabhu and Labonte, Thomas and Chakraborty, Sourav and Turner, Matt and Sury, Samantika and Shen, John Paul
- **Year:** 2025
- **Venue:** IEEE International Symposium on Performance Analysis of Systems and Software/ISPASS
- **DOI:** 10.1109/ISPASS64960.2025.00015
- **URL:** https://www.scopus.com/pages/publications/105029905852?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 49--61
- **Language:** English
- **Keywords:** Accelerators; AI; benchmarking; coupling

### Abstract

Large language model (LLM)-based inference workloads increasingly dominate data center costs and resource utilization. Therefore, understanding the inference workload characteristics on evolving CPU-GPU coupled architectures is crucial for optimization. This paper presents an in-depth analysis of LLM inference behavior on loosely-coupled (PCIe A100/H100) and closely-coupled (GH200) systems. We analyze performance dynamics using fine-grained operator-to-kernel trace analysis, facilitated by our novel profiler SKIP and metrics like Total Kernel Launch and Queuing Time (TKLQT). Results show that closely-coupled (CC) GH200 significantly outperforms loosely-coupled (LC) systems at large batch sizes, achieving 1.9x-2.7x faster prefill latency for Llama-3.2-1B. However, our analysis also reveals that GH200 remains CPU-bound up to 4x larger batch sizes than LC systems. In this extended CPU-bound region, we identify the performance characteristics of the Grace CPU as a key factor contributing to higher inference latency at low batch sizes on GH200. We demonstrate that TKLQT accurately identifies this CPU/GPU-bound transition point. Based on this analysis, we further show that kernel fusion offers significant potential to mitigate GH200's low-batch latency bottleneck by reducing kernel launch overhead. This detailed kernel-level characterization provides critical insights for optimizing diverse CPU-GPU coupling strategies. This work is an initial effort, and we plan to explore other major AI/DL workloads that demand different degrees of CPU-GPU heterogeneous architectures.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Characterizing and Optimizing LLM Inference Workloads on CPU-GPU Coupled Architectures
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
