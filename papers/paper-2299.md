---
id: "paper-2299"
title: "Recursive Offloading for LLM Serving in Multi-tier Networks"
authors: ["Wu, Zhiyuan", "Sun, Sheng", "Wang, Yuwei", "Liu, Min", "Gao, Bo", "Lu, Jinda", "Wu, Tingting", "Yang, Zheming", "Wen, Tian"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3642580"
url: "https://www.scopus.com/pages/publications/105024591245?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["communication efficiency", "edge-cloud collaboration", "Large language models", "services computing", "task offloading"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": pending
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
---

# paper-2299 — Recursive Offloading for LLM Serving in Multi-tier Networks

## Metadata

- **Authors:** Wu, Zhiyuan and Sun, Sheng and Wang, Yuwei and Liu, Min and Gao, Bo and Lu, Jinda and Wu, Tingting and Yang, Zheming and Wen, Tian
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3642580
- **URL:** https://www.scopus.com/pages/publications/105024591245?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** communication efficiency; edge-cloud collaboration; Large language models; services computing; task offloading

### Abstract

Heterogeneous device-edge-cloud computing infrastructures have become the backbone of modern telecommunication operators and Wide Area Networks (WANs), providing multi-tier computational support for emerging intelligent applications. With the rapid proliferation of Large Language Model (LLM) services, efficiently coordinating inference tasks and reducing communication burden within these multi-tier network architectures becomes a critical deployment challenge. Current LLM serving paradigms exhibit significant limitations: on-device deployment restricts service to lightweight LLMs due to hardware constraints, while cloud-centric deployment encounters resource congestion and considerable prompt communication overhead during peak periods. Model-cascading inference, though better suited for multi-tier networks, depends on static, manually-tuned thresholds that cannot adapt to dynamic network conditions or varying task complexities. To address these challenges, we propose RecServe, a recursive offloading framework tailored for LLM serving in multi-tier networks. RecServe introduces a task-specific hierarchical confidence evaluation mechanism that guides offloading decisions based on inferred task complexity in progressively scaled LLMs across device, edge, and cloud tiers. To further enable intelligent task routing across tiers, RecServe employs a sliding-window-based dynamic offloading strategy with quantile interpolation, enabling real-time tracking of historical confidence distributions and adaptive offloading threshold adjustments. This design allows inference tasks to be recursively offloaded to higher tiers only when necessary, optimizing heterogeneous resource utilization while reducing cross-tier communication with little compromise on service quality. Theoretical analysis provides distinct conditions under which RecServe is expected to achieve reduced communication burden and computational costs. Experiments on eight datasets demonstrate that RecServe outperforms CasServe in both service quality and communication efficiency, and reduces the communication burden by over 50% compared to centralized cloud-based serving.  © 2002-2012 IEEE.

## 04 — Title Screening

<!-- Populated by /04-title-screening -->

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
