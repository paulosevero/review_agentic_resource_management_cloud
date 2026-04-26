---
id: "paper-2136"
title: "InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers"
authors: ["Shou, Chenchen", "Liu, Guyue", "Nie, Hao", "Meng, Huaiyu", "Zhou, Yu", "Jiang, Yimin", "Lv, Wenqing", "Xu, Yelong", "Lu, Yuanwei", "Chen, Zhang", "Yu, Yanbo", "Shen, Yichen", "Zhu, Yibo", "Jiang, Daxin"]
year: 2025
venue: "SIGCOMM 2025 - ACM SIGCOMM 2025 Conference"
venue_type: "conference"
doi: "10.1145/3718958.3750468"
url: "https://www.scopus.com/pages/publications/105016246660?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "1--23"
keywords: ["High-Bandwidth Domain", "Large Language Model", "Optical Circuit Switching"]
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

# paper-2136 — InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers

## Metadata

- **Authors:** Shou, Chenchen and Liu, Guyue and Nie, Hao and Meng, Huaiyu and Zhou, Yu and Jiang, Yimin and Lv, Wenqing and Xu, Yelong and Lu, Yuanwei and Chen, Zhang and Yu, Yanbo and Shen, Yichen and Zhu, Yibo and Jiang, Daxin
- **Year:** 2025
- **Venue:** SIGCOMM 2025 - ACM SIGCOMM 2025 Conference
- **DOI:** 10.1145/3718958.3750468
- **URL:** https://www.scopus.com/pages/publications/105016246660?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 1--23
- **Language:** English
- **Keywords:** High-Bandwidth Domain; Large Language Model; Optical Circuit Switching

### Abstract

Scaling Large Language Model (LLM) training relies on multidimensional parallelism, where High-Bandwidth Domains (HBDs) are critical for communication-intensive parallelism like Tensor Parallelism. However, existing HBD architectures face fundamental limitations in scalability, cost, and fault resiliency: switch-centric HBDs (e.g., NVL-72) incur prohibitive scaling costs, while GPU-centric HBDs (e.g., TPUv3/Dojo) suffer from severe fault propagation. Switch-GPU hybrid HBDs (e.g., TPUv4) take a middle-ground approach, but the fault explosion radius remains large. We propose InfiniteHBD, a transceiver-centric HBD architecture that integrates connectivity and dynamic switching at the transceiver level by embedding Optical Circuit Switching (OCS) within each transceiver. It enables reconfigurable point-to-multipoint communication and scalable variable-size ring topologies. InfiniteHBD achieves datacenter-scale scalability without cost explosion, fault isolation at the node level, and full bandwidth utilization for healthy GPUs. Key innovations include a Silicon Photonic-based OCS transceiver (OCSTrx), a reconfigurable k-hop ring topology, and an HBD-DCN orchestration algorithm. The evaluation demonstrates that InfiniteHBD reduces cost to 31% of NVL-72, achieves a near-zero GPU waste ratio (over 10x lower than NVL-72 and TPUv4), maintains near-zero cross-ToR traffic under 7% node fault ratio, and improves Model FLOPs Utilization by 3.37× compared to NVIDIA DGX (8 GPUs/node). © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** InfiniteHBD: Building Datacenter-Scale High-Bandwidth Domain for LLM with Optical Circuit Switching Transceivers
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
