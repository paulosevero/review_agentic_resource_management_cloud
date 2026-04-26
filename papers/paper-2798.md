---
id: "paper-2798"
title: "Strategies for computational efficiency in small language models"
authors: ["Taylar, Jonathan"]
year: 2026
venue: "Autonomous Intelligent Systems"
venue_type: "journal"
doi: "10.1007/s43684-026-00130-7"
url: "https://www.scopus.com/pages/publications/105036043172?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Generative AI", "Large Language Models (LLMs)", "Natural Language Processing (NLP)", "Small Language Models (SLMs)"]
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

# paper-2798 — Strategies for computational efficiency in small language models

## Metadata

- **Authors:** Taylar, Jonathan
- **Year:** 2026
- **Venue:** Autonomous Intelligent Systems
- **DOI:** 10.1007/s43684-026-00130-7
- **URL:** https://www.scopus.com/pages/publications/105036043172?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Generative AI; Large Language Models (LLMs); Natural Language Processing (NLP); Small Language Models (SLMs)

### Abstract

The proliferation of Large Language Models (LLMs) is often constrained by their significant computational and memory requirements, limiting their deployment to large data centers. Small Language Models (SLMs) offer a feasible solution for on-device applications; yet their efficiency requires optimization to operate well on resource-constrained hardware. This study looks at ways to make SLMs more efficient at using computers. The effects of two primary methods were compared: post-training optimization and architectural innovation through quantitative and observational study. Using a standardized suite of benchmarks measuring accuracy, reasoning, and inference performance, a baseline is established with state-of-the-art SLMs like Phi-3 and Llama 3. Post-training techniques were evaluated, including 4-bit quantization (GPTQ) and knowledge distillation from a superior teacher model. Finally, these optimized Transformers were compared against a custom-trained, non-Transformer model based on the Mamba (State-Space Model) architecture. Results show that 4-bit quantization is the most effective compression strategy among those evaluated. It reduces peak inference memory footprint by 71%, increases throughput by 83%, and does so with minimal accuracy degradation. Within the controlled experimental space evaluated in this study, the 4-bit quantized Phi-3-mini model occupies a Pareto-optimal position in memory-normalized accuracy. Focused skill growth works best with knowledge distillation. However, new designs like Mamba offer a different trade-off by being the best at streaming jobs’ raw output. It was found that improving current Transformer-based SLMs through quantization is the best way to use them for general purposes. However, customized designs and distillation work better for specific, high-performance uses. This research offers a definitive framework and pragmatic recommendations for advancing the next generation of robust, efficient, and accessible language models. © The Author(s) 2026.

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
