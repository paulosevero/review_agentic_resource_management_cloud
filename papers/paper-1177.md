---
id: "paper-1177"
title: "IANUS: Integrated Accelerator based on NPU-PIM Unified Memory System"
authors: ["Seo, Minseok", "Nguyen, Xuan Truong", "Hwang, Seok Joong", "Kwon, Yongkee", "Kim, Guhyun", "Park, Chanwook", "Kim, Ilkon", "Park, Jaehan", "Kim, Jeongbin", "Shin, Woojae", "Won, Jongsoon", "Choi, Haerang", "Kim, Kyuyoung", "Kwon, Daehan", "Jeong, Chunseok", "Lee, Sangheon", "Choi, Yongseok", "Byun, Wooseok", "Baek, Seungcheol", "Lee, Hyuk-Jae", "Kim, John"]
year: 2024
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3620666.3651324"
url: "https://www.scopus.com/pages/publications/85192190910?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "545--560"
keywords: ["Critical component", "End to end", "Language model", "Main-memory", "Memory access", "Memory computations", "Memory systems", "Neural-processing", "Processing units", "Processing-in-memory", "Memory architecture"]
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

# paper-1177 — IANUS: Integrated Accelerator based on NPU-PIM Unified Memory System

## Metadata

- **Authors:** Seo, Minseok and Nguyen, Xuan Truong and Hwang, Seok Joong and Kwon, Yongkee and Kim, Guhyun and Park, Chanwook and Kim, Ilkon and Park, Jaehan and Kim, Jeongbin and Shin, Woojae and Won, Jongsoon and Choi, Haerang and Kim, Kyuyoung and Kwon, Daehan and Jeong, Chunseok and Lee, Sangheon and Choi, Yongseok and Byun, Wooseok and Baek, Seungcheol and Lee, Hyuk-Jae and Kim, John
- **Year:** 2024
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3620666.3651324
- **URL:** https://www.scopus.com/pages/publications/85192190910?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 545--560
- **Language:** English
- **Keywords:** Critical component; End to end; Language model; Main-memory; Memory access; Memory computations; Memory systems; Neural-processing; Processing units; Processing-in-memory; Memory architecture

### Abstract

Accelerating end-to-end inference of transformer-based large language models (LLMs) is a critical component of AI services in datacenters. However, the diverse compute characteristics of LLMs’ end-to-end inference present challenges as previously proposed accelerators only address certain operations or stages (e.g., self-attention, generation stage, etc.). To address the unique challenges of accelerating end-to-end inference, we propose IANUS – Integrated Accelerator based on NPU-PIM Unified Memory System. IANUS is a domain-specific system architecture that combines a Neural Processing Unit (NPU) with a Processing-in-Memory (PIM) to leverage both the NPU’s high computation throughput and the PIM’s high effective memory bandwidth. In particular, IANUS employs a unified main memory system where the PIM memory is used both for PIM operations and for NPU’s main memory. The unified main memory system ensures that memory capacity is efficiently utilized and the movement of shared data between NPU and PIM is minimized. However, it introduces new challenges since normal memory accesses and PIM computations cannot be performed simultaneously. Thus, we propose novel PIM Access Scheduling that manages not only the scheduling of normal memory accesses and PIM computations but also workload mapping across the PIM and the NPU. Our detailed simulation evaluations show that IANUS improves the performance of GPT-2 by 6.2× and 3.2×, on average, compared to the NVIDIA A100 GPU and the state-of-the-art accelerator. As a proof-of-concept, we develop a prototype of IANUS with a commercial PIM, NPU, and an FPGA-based PIM controller to demonstrate the feasibility of IANUS. © 2024 Copyright held by the owner/author(s).

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
