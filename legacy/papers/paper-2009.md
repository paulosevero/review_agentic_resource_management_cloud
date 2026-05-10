---
id: "paper-2009"
title: "InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference"
authors: ["Pan, Xiurui", "Li, Endian", "Li, Qiao", "Liang, Shengwen", "Shan, Yizhou", "Zhou, Ke", "Luo, Yingwei", "Wang, Xiaolin", "Zhang, Jie"]
year: 2025
venue: "Proceedings - International Symposium on High-Performance Computer Architecture"
venue_type: "conference"
doi: "10.1109/HPCA61900.2025.00113"
url: "https://www.scopus.com/pages/publications/105003411754?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1510--1525"
keywords: ["attention", "computational storage", "kv cache", "large language model"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2009 — InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference

## Metadata

- **Authors:** Pan, Xiurui and Li, Endian and Li, Qiao and Liang, Shengwen and Shan, Yizhou and Zhou, Ke and Luo, Yingwei and Wang, Xiaolin and Zhang, Jie
- **Year:** 2025
- **Venue:** Proceedings - International Symposium on High-Performance Computer Architecture
- **DOI:** 10.1109/HPCA61900.2025.00113
- **URL:** https://www.scopus.com/pages/publications/105003411754?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1510--1525
- **Language:** English
- **Keywords:** attention; computational storage; kv cache; large language model

### Abstract

The widespread of Large Language Models (LLMs) marks a significant milestone in generative AI. Nevertheless, the increasing context length and batch size in offline LLM inference escalate the memory requirement of the key-value (KV) cache, which imposes a huge burden on the GPU VRAM, especially for resource-constrained scenarios (e.g., edge computing). Several cost-effective solutions leverage host memory or SSDs to reduce storage costs for offline inference scenarios and improve the throughput. Nevertheless, they suffer from significant performance penalties imposed by intensive KV cache accesses due to limited PCIe bandwidth. To address these issues, we propose InstAttention, a novel LLM inference system that offloads the most performance-critical computation (i.e., attention in decoding phase) and data (i.e., KV cache) parts to Computational Storage Drives (CSDs), which minimize the enormous KV transfer overheads. InstAttention designs a dedicated flashaware in-storage attention engine with KV cache management mechanisms to exploit the high internal bandwidths of CSDs instead of being limited by the PCIe bandwidth. The optimized P2P transmission between GPU and CSDs further reduces data migration overheads. Experimental results demonstrate that for a 13B model using an NVIDIA A6000 GPU, InstAttention improves throughput for long-sequence inference by up to 11.1 ×, compared to existing SSD-based solutions such as FlexGen. © 2025 IEEE.

## 04 — Title Screening

**Title:** InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** InstAttention: In-Storage Attention Offloading for Cost-Effective Long-Context LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
