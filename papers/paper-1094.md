---
id: "paper-1094"
title: "Understanding Performance Implications of LLM Inference on CPUs"
authors: ["Na, Seonjin", "Jeong, Geonhwa", "Ahn, Byung Hoon", "Young, Jeffrey", "Krishna, Tushar", "Kim, Hyesoon"]
year: 2024
venue: "Proceedings - 2024 IEEE International Symposium on Workload Characterization, IISWC 2024"
venue_type: "conference"
doi: "10.1109/IISWC63097.2024.00024"
url: "https://www.scopus.com/pages/publications/85214571338?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "169--180"
keywords: ["Intel AMX", "Large Language Model (LLM)", "LLM Inference on CPU", "Offloading-based LLM Inference"]
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

# paper-1094 — Understanding Performance Implications of LLM Inference on CPUs

## Metadata

- **Authors:** Na, Seonjin and Jeong, Geonhwa and Ahn, Byung Hoon and Young, Jeffrey and Krishna, Tushar and Kim, Hyesoon
- **Year:** 2024
- **Venue:** Proceedings - 2024 IEEE International Symposium on Workload Characterization, IISWC 2024
- **DOI:** 10.1109/IISWC63097.2024.00024
- **URL:** https://www.scopus.com/pages/publications/85214571338?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 169--180
- **Language:** English
- **Keywords:** Intel AMX; Large Language Model (LLM); LLM Inference on CPU; Offloading-based LLM Inference

### Abstract

The remarkable performance of LLMs has led to their application in a wide range of fields, with data centers utilizing expensive accelerators such as GPUs and TPUs to support LLM inference and training. However, these costly accelerators face challenges with memory capacity due to the large size of LLMs and Key-Value (KV) cache during inference. To address memory capacity issues of accelerators such as GPUs/TPUs, offloading-based LLM inference has been proposed to store model weights, activations, and KV cache in CPU memory. This approach, however, often incurs significant performance degradation in LLM inference in terms of latency and throughput as the offloaded data must be transferred back and forth over the PCIe bus, which has a lower bandwidth compared to memory.This study explores new opportunities for leveraging CPUs in LLM inference. Recent CPUs are equipped with dedicated accelerators for efficient matrix computations and have extended ISAs to support training and inference of new AI models. They support larger memory sizes than most GPUs, allowing for the direct computation of large models and KV caches without offloading. Additionally, recent CPUs are often equipped with DDR and HBM memory, which provides options for optimizing for either memory capacity or bandwidth. This study provides a detailed analysis of LLM inference performance on the latest CPUs equipped with these advanced features. Based on our experimental results, we propose potential optimization strategies tailored to enhance the performance of LLM inference on CPUs.  © 2024 IEEE.

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
