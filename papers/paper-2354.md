---
id: "paper-2354"
title: "From ATOP to ZCube: Automated Topology Optimization Pipeline and A Highly Cost-Effective Network Topology for Large Model Training"
authors: ["Yan, Zihan", "Li, Dan", "Chen, Li", "Xiong, Dian", "Gao, Kaihui", "Zhang, Yiwei", "Yan, Rui", "Zhang, Menglei", "Zhang, Bochun", "Jiang, Zhuo", "Ye, Jianxi", "Lin, Haibin"]
year: 2025
venue: "SIGCOMM 2025 - ACM SIGCOMM 2025 Conference"
venue_type: "conference"
doi: "10.1145/3718958.3750503"
url: "https://www.scopus.com/pages/publications/105016234831?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "861--881"
keywords: ["AI infrastructure", "Data center networks", "Network topology"]
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

# paper-2354 — From ATOP to ZCube: Automated Topology Optimization Pipeline and A Highly Cost-Effective Network Topology for Large Model Training

## Metadata

- **Authors:** Yan, Zihan and Li, Dan and Chen, Li and Xiong, Dian and Gao, Kaihui and Zhang, Yiwei and Yan, Rui and Zhang, Menglei and Zhang, Bochun and Jiang, Zhuo and Ye, Jianxi and Lin, Haibin
- **Year:** 2025
- **Venue:** SIGCOMM 2025 - ACM SIGCOMM 2025 Conference
- **DOI:** 10.1145/3718958.3750503
- **URL:** https://www.scopus.com/pages/publications/105016234831?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 861--881
- **Language:** English
- **Keywords:** AI infrastructure; Data center networks; Network topology

### Abstract

The development of large language models (LLMs) poses new challenges in data center network topology design. To assist in exploring topology design, we propose ATOP, an Automated Topology Optimization Pipeline, which models network topology as a set of hyperparameters, enabling the discovery of potential topologies. With various optimization algorithms and customizable optimization objectives, ATOP achieves automated topology optimization on a scale of tens of thousands of GPUs. We apply ATOP on network topologies for 256, 1024, 4096, and 16384 GPUs, optimizing performance under LLMs training traffic patterns, collective communication performance, fault tolerance, and network cost. We also evaluate ATOP in different scenarios: building, optimizing, and expanding a data center. From ATOP’s results, we discover a new topology - ZCube, which reaches the highest cost-effectiveness across various GPU scales. Simulation results show that ZCube, compared to the previous state-of-the-art topologies, including Rail-optimized Fat-tree (ROFT), Rail-only, and HPN, improves end-to-end LLM training speed by 3% to 7% and reduces network hardware costs by 26% to 46%. We also construct ZCube on a real-world testbed. Results show that ZCube reduces hardware costs by 25% compared to Rail-Optimized Topology while maintaining the same all-reduce and all-to-all performance. © 2025 Copyright held by the owner/author(s).

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
