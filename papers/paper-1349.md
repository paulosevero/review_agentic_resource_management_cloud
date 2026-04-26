---
id: "paper-1349"
title: "LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization"
authors: ["Zheng, ZhenDong", "Cheng, Qianyu", "Wang, Teng", "Gong, Lei", "Chen, Xianglan", "Tang, Cheng", "Wang, Chao", "Zhou, Xuehai"]
year: 2024
venue: "Proceedings - 2024 34th International Conference on Field-Programmable Logic and Applications, FPL 2024"
venue_type: "conference"
doi: "10.1109/FPL64840.2024.00053"
url: "https://www.scopus.com/pages/publications/85207830144?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "332--338"
keywords: ["Data Center", "GPT", "Multi-FPGA Acceleration"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-1349 — LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization

## Metadata

- **Authors:** Zheng, ZhenDong and Cheng, Qianyu and Wang, Teng and Gong, Lei and Chen, Xianglan and Tang, Cheng and Wang, Chao and Zhou, Xuehai
- **Year:** 2024
- **Venue:** Proceedings - 2024 34th International Conference on Field-Programmable Logic and Applications, FPL 2024
- **DOI:** 10.1109/FPL64840.2024.00053
- **URL:** https://www.scopus.com/pages/publications/85207830144?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 332--338
- **Language:** English
- **Keywords:** Data Center; GPT; Multi-FPGA Acceleration

### Abstract

Large Language Models (LLMs) have been widely deployed in data centers to provide various services, among which the most representative is the Generative Pre-trained Transformer (GPT). The GPT model has heavy memory and computing overhead, and its inference process has two stages with distinct computing characteristics: Prefill and Decode. Utilizing existing GPUs and FPGA accelerators to construct a platform for deploying GPT in data centers faces the challenges of needing more effective synchronization schemes or structures with higher computational intensity. This paper proposes LORA, a low latency end-to-end GPT acceleration platform utilizing multiple FPGAs. Firstly, we optimize the synchronization timing of the GPT model to reduce the computation and communication overhead. Secondly, we devise some efficient synchronization steps for specific layers of the GPT model that overlap part of the computation and communication delay to improve the latency of our platform. Finally, we deploy recurrent structures on each FPGA to accelerate the different stages of the GPT model. Implemented on the Xilinx Alveo U280 FPGAs, LORA achieves an average 11.1 × speedup over NVIDIA V100 GPUs on the modern GPT-2 model. Compared to the existing multi-FPGA accelerator appliance, LORA shows performance improvements of up to 4 × and 2.7 × in the Prefill and Decode stages.  © 2024 IEEE.

## 04 — Title Screening

**Title:** LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LORA: A Latency-Oriented Recurrent Architecture for GPT Model on Multi-FPGA Platform with Communication Optimization
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
