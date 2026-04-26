---
id: "paper-1557"
title: "ELLIE: Energy-Efficient LLM Inference at the Edge Via Prefill-Decode Splitting"
authors: ["Fan, Haoyang", "Lin, Yi-Chien", "Prasanna, Viktor"]
year: 2025
venue: "Proceedings of the International Conference on Application-Specific Systems, Architectures and Processors"
venue_type: "conference"
doi: "10.1109/ASAP65064.2025.00031"
url: "https://www.scopus.com/pages/publications/105015603487?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "139--146"
keywords: ["Edge inference", "Heterogeneous computing", "LLM"]
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

# paper-1557 — ELLIE: Energy-Efficient LLM Inference at the Edge Via Prefill-Decode Splitting

## Metadata

- **Authors:** Fan, Haoyang and Lin, Yi-Chien and Prasanna, Viktor
- **Year:** 2025
- **Venue:** Proceedings of the International Conference on Application-Specific Systems, Architectures and Processors
- **DOI:** 10.1109/ASAP65064.2025.00031
- **URL:** https://www.scopus.com/pages/publications/105015603487?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 139--146
- **Language:** English
- **Keywords:** Edge inference; Heterogeneous computing; LLM

### Abstract

As Large Language Models (LLMs) are increasingly deployed for on-device applications, optimizing inference on edge platforms becomes critical. In real-world scenarios, LLM inference must satisfy diverse constraints and user requirements, such as low latency, high energy efficiency, or low Energy-Delay Product (EDP). Most state-of-the-art edge platforms, such as AI PCs and mobile SoCs, integrate heterogeneous processing units, including CPUs, GPUs, and Neural Processing Units (NPUs), each with distinct performance and power characteristics. However, existing approaches often adopt static mapping to a single processing unit (e.g., CPU, GPU, or NPU) and perform optimizations for either latency or energy consumption. This limits their effectiveness in meeting the requirements of diverse application scenarios. Moreover, LLM inference consists of two distinct phases: a highly parallel, compute-intensive Prefill phase, and a sequential, memory-intensive Decode phase. These phases have different computational characteristics, and splitting them across suitable processing units can potentially yield better energy efficiency and EDP than static mapping. However, such improvements may not be realized in all cases, as the actual benefit depends on many factors, including prompt characteristics, the models used, and features of the target hardware. To address these challenges, we propose ellie, a lightweight inference framework for edge heterogeneous platforms that dynamically selects the optimal execution plan based on the usage scenario, LLM, hardware feature, and input prompt. ELLIE builds performance models by regressing latency and power from offline profiling data, and integrates it with a lightweight output token length predictor. At runtime, it estimates the latency and energy of candidate execution plans using the predicted output length and selects an optimized device mapping accordingly. We implement ellie on an Intel AI PC platform with integrated CPU, GPU, and NPU. On average, when optimizing for EDP, ELLIE reduces energy consumption by 1.8×, improves EDP by 1.5×, and achieves latency comparable to GPU-only inference, across diverse LLMs and prompt types. © 2025 IEEE.

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
