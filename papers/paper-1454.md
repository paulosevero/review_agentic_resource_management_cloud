---
id: "paper-1454"
title: "SEAL: Secure and Efficient Adaptive Layering for On-Device Language Models with TEE"
authors: ["Chang, Wen-Tzu", "Fang, Rui", "Chen, Ming-Syan"]
year: 2025
venue: "Proceedings - 2025 IEEE 11th International Conference on Edge Computing and Scalable Cloud, EdgeCom 2025"
venue_type: "conference"
doi: "10.1109/EdgeCom66327.2025.00030"
url: "https://www.scopus.com/pages/publications/105033584304?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "138--143"
keywords: ["Edge Computing", "Energy Efficiency", "Model Stealing", "On-Device AI", "Security and Privacy", "Small Language Models", "Trusted Execution Environment (TEE)"]
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

# paper-1454 — SEAL: Secure and Efficient Adaptive Layering for On-Device Language Models with TEE

## Metadata

- **Authors:** Chang, Wen-Tzu and Fang, Rui and Chen, Ming-Syan
- **Year:** 2025
- **Venue:** Proceedings - 2025 IEEE 11th International Conference on Edge Computing and Scalable Cloud, EdgeCom 2025
- **DOI:** 10.1109/EdgeCom66327.2025.00030
- **URL:** https://www.scopus.com/pages/publications/105033584304?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 138--143
- **Language:** English
- **Keywords:** Edge Computing; Energy Efficiency; Model Stealing; On-Device AI; Security and Privacy; Small Language Models; Trusted Execution Environment (TEE)

### Abstract

The deployment of Small Language Models (SLMs) on edge devices presents a fundamental trade-off between performance and security: executing in the untrusted Rich Execution Environment (REE) risks model theft, while running entirely within a Trusted Execution Environment (TEE) incurs significant overhead. Existing approaches often sacrifice one for the other. To address this, we propose SEAL (Secure and Efficient Adaptive Layering), a framework that enables informed, quantitative trade-offs between security and efficiency for on-device inference. SEAL introduces two key components: Confidential Layer Analysis (CLA), which quantitatively assesses the confidentiality of each model layer, and the Layer Importance-Guided Adaptive Partition (LIAP) algorithm, which maps the most sensitive, low-overhead layers into the TEE based on device constraints, while retaining others in the REE to preserve performance. To evaluate security, we develop the Model Parameter Reconstruction Success Rate (MPRSR), a metric that measures behavioral, parametric, and functional similarity under model extraction attacks. Experiments using the INT4-quantized Qwen3-0.6B model on WikiQA demonstrate that SEAL reduces model theft risk by 65.8%—with only a 22% increase in latency and memory—by protecting a single critical layer. When securing the top five layers, SEAL reduces MPRSR to 7.9%, while reducing time and energy consumption by roughly 50% compared to full-TEE deployment. SEAL reframes security as an optimization problem, enabling practical and trustworthy secure inference for edge AI. ©2025 IEEE.

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
