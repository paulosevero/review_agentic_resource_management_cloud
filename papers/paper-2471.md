---
id: "paper-2471"
title: "LORA: A Latency-Oriented Recurrent Architecture for Large Language Model on Multi-FPGA Platform with Communication Optimization"
authors: ["Zheng, ZhenDong", "Cheng, Qianyu", "Wang, Teng", "Lou, Wenqi", "Gong, Lei", "Chen, Xianglan", "Wang, Chao", "Zhou, Xuehai"]
year: 2025
venue: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
venue_type: "journal"
doi: "10.1109/TCAD.2025.3629537"
url: "https://www.scopus.com/pages/publications/105021231108?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Data Center", "LLM", "Multi-FPGA Acceleration"]
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

# paper-2471 — LORA: A Latency-Oriented Recurrent Architecture for Large Language Model on Multi-FPGA Platform with Communication Optimization

## Metadata

- **Authors:** Zheng, ZhenDong and Cheng, Qianyu and Wang, Teng and Lou, Wenqi and Gong, Lei and Chen, Xianglan and Wang, Chao and Zhou, Xuehai
- **Year:** 2025
- **Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- **DOI:** 10.1109/TCAD.2025.3629537
- **URL:** https://www.scopus.com/pages/publications/105021231108?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Data Center; LLM; Multi-FPGA Acceleration

### Abstract

The remarkable performance of Large Language Models (LLMs) has driven their widespread deployment in data centers to support diverse user-facing applications. However, the rapidly growing computational and storage demands of these models have made single-device deployment increasingly impractical. Prior research on LLM inference has primarily addressed this challenge through algorithmic optimizations such as quantization or by integrating customized hardware acceleration frameworks. As model parameters continue to scale, multi-device deployment has become a necessary approach for enabling efficient LLM inference. Nevertheless, constructing low-latency multi-device platforms for LLMs inference using available FPGA or GPU accelerators remains constrained by inefficient synchronization schemes or limited compute intensity in current architectures. Furthermore, existing solutions often lack co-optimized designs that effectively integrate communication with computation. To address these limitations, this paper proposes LORA, a low-latency end-to-end LLMs acceleration platform utilizing multiple FPGAs. Firstly, we optimize the synchronization timing within the LLMs to minimize storage, computation, and BRAM overhead. Secondly, we tightly couple communication and computation through techniques such as pipeline overlapping and input data packing. Next, we deploy homogeneous accelerators on each FPGA device, leveraging a recurrent architecture to further reduce inference latency. Finally, we apply FPGA-specific optimizations and conduct performance modeling and analysis of the acceleration framework to select optimal deployment parameters for various computational tasks. Implemented on Xilinx Alveo U280 FPGAs, LORA-F and LORA-Q achieve average speedups of 14.4× and 32.6×, respectively, compared to NVIDIA V100 GPUs when running modern LLMs. Compared with existing multi-FPGA accelerator platforms, LORA-F and LORA-Q demonstrate average performance improvements of up to 2.6× and 4.3×, respectively. © 1982-2012 IEEE.

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
