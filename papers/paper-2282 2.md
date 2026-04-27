---
id: "paper-2282"
title: "WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving"
authors: ["Wang, Tianyu", "Rattihalli, Gourav", "Dhakal, Aditya", "Tang, Xulong", "Milojicic, Dejan"]
year: 2025
venue: "Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops"
venue_type: "conference"
doi: "10.1145/3731599.3767396"
url: "https://www.scopus.com/pages/publications/105023404126?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "508--515"
keywords: ["energy efficiency", "LLM serving", "serverless"]
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

# paper-2282 — WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving

## Metadata

- **Authors:** Wang, Tianyu and Rattihalli, Gourav and Dhakal, Aditya and Tang, Xulong and Milojicic, Dejan
- **Year:** 2025
- **Venue:** Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops
- **DOI:** 10.1145/3731599.3767396
- **URL:** https://www.scopus.com/pages/publications/105023404126?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 508--515
- **Language:** English
- **Keywords:** energy efficiency; LLM serving; serverless

### Abstract

Serverless LLM serving reduces operational costs by elastically provisioning GPUs and charging users only for actual usage. However, existing systems mainly optimize cold-start latency while overlooking two inefficiencies: (i) static, exclusive GPU allocation that over-provisions compute resources, lowering utilization and inflating hardware costs, and (ii) reliance on hardware-controlled clock frequencies, wasting energy. Our measurements show that many LLM workloads can meet SLOs with partial SM allocations and reduced clock speeds, enabling opportunities for GPU multiplexing and dynamic clock scaling to reduce energy consumption. We propose WAGES, a workload-aware GPU-sharing system for energy-efficient serverless LLM serving. WAGES uses NVIDIA MPS to co-locate multiple LLMs on a single GPU, dynamically tuning SM partitions and clock speeds to match workload demands while preserving SLOs. A two-tier scheduling framework coordinates global GPU consolidation and local SLO-aware scheduling with on-the-fly tuning. It also overlaps model/KV migration with execution to reduce reconfiguration overheads. On real-world LLM traces, WAGES improves SLO attainment by up to 4% over state-of-the-art GPU sharing while cutting energy use by up to 26%, showing that fine-grained, workload-aware sharing can improve SLO attainment and reduce energy consumption simultaneously. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** WAGES: Workload-Aware GPU Sharing System for Energy-Efficient Serverless LLM Serving
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
