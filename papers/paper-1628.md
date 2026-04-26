---
id: "paper-1628"
title: "WiP: From Wasted Compute to Quality Gains: LLM Test-Time Scaling on Mobile NPUs"
authors: ["Hao, Zixu", "Ren, Ju", "Cao, Ting"]
year: 2025
venue: "EdgeFM 2025 - Proceedings of the 2025 2nd International Workshop on Edge and Mobile Foundation Models"
venue_type: "conference"
doi: "10.1145/3737902.3768361"
url: "https://www.scopus.com/pages/publications/105022089329?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "56--58"
keywords: ["Mathematical operators", "Mobile edge computing", "Neural networks", "Program processors", "Programmable logic controllers", "System-on-chip", "Acceleration capabilities", "Low-power consumption", "Lower-power consumption", "Neural-networks", "Neural-processing", "Performance", "Processing units", "Quantisation", "Test time", "Time-scaling", "Economic and social effects"]
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

# paper-1628 — WiP: From Wasted Compute to Quality Gains: LLM Test-Time Scaling on Mobile NPUs

## Metadata

- **Authors:** Hao, Zixu and Ren, Ju and Cao, Ting
- **Year:** 2025
- **Venue:** EdgeFM 2025 - Proceedings of the 2025 2nd International Workshop on Edge and Mobile Foundation Models
- **DOI:** 10.1145/3737902.3768361
- **URL:** https://www.scopus.com/pages/publications/105022089329?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 56--58
- **Language:** English
- **Keywords:** Mathematical operators; Mobile edge computing; Neural networks; Program processors; Programmable logic controllers; System-on-chip; Acceleration capabilities; Low-power consumption; Lower-power consumption; Neural-networks; Neural-processing; Performance; Processing units; Quantisation; Test time; Time-scaling; Economic and social effects

### Abstract

With advancements in the performance of small-sized LLMs and Mobile SoCs, deploying LLMs on edge devices such as mobile phones is becoming a reality. The emerging NPU (Neural Processing Unit) units on mobile SoCs, with their specialized neural network acceleration capabilities and lower power consumption, have become ideal processors for running LLM workloads. We identify that the NPU's core matrix multiplication units perform computations at a large tile granularity, leading to significant underutilization of computational resources during the autoregressive decoding phase of LLMs. Therefore, we propose leveraging test-time scaling techniques to fully utilize this wasted NPU compute capacity to enhance the performance of small on-device models. To address accuracy degradation associated with NPU-native coarse-grained quantization, we implement mixed-precision operators that support fine-grained group quantization to strike a balance between memory footprint and accuracy. Preliminary results show that a 1B model with test-time scaling can achieve a better accuracy-latency trade-off on complex reasoning tasks like MATH than a 3B model without scaling.  © 2025 Copyright held by the owner/author(s).

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
