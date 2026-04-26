---
id: "paper-2887"
title: "Resource-Efficient Personal Large Language Models Fine-Tuning With Collaborative Edge Computing"
authors: ["Ye, Shengyuan", "Ouyang, Bei", "Qian, Tianyi", "Zeng, Liekang", "Li, Jingyi", "Du, Jiangsu", "Chu, Xiaowen", "Xing, Guoliang", "Chen, Xu"]
year: 2026
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2026.3654957"
url: "https://www.scopus.com/pages/publications/105027963136?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "680--696"
keywords: ["collaborative edge computing", "distributed training", "Edge intelligence", "personal LLM fine-tuning"]
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

# paper-2887 — Resource-Efficient Personal Large Language Models Fine-Tuning With Collaborative Edge Computing

## Metadata

- **Authors:** Ye, Shengyuan and Ouyang, Bei and Qian, Tianyi and Zeng, Liekang and Li, Jingyi and Du, Jiangsu and Chu, Xiaowen and Xing, Guoliang and Chen, Xu
- **Year:** 2026
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2026.3654957
- **URL:** https://www.scopus.com/pages/publications/105027963136?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 680--696
- **Language:** English
- **Keywords:** collaborative edge computing; distributed training; Edge intelligence; personal LLM fine-tuning

### Abstract

Large language models (LLMs) have enabled transformative applications at the network edge, such as intelligent personal assistants. However, data privacy and security concerns necessitate a shift from cloud-centric paradigms to edge-based fine-tuning for personal LLMs. This transition is significantly hindered by intensive computational requirements and inherent resource scarcity, creating a “resource wall” that compromises training efficiency and feasibility. While current parameter-efficient fine-tuning (PEFT) and resource management strategies attempt to mitigate these constraints, they remain insufficient for the limited capacities of individual edge devices. To address these challenges, we propose PAC+, a resourceefficient collaborative edge AI framework for in-situ personal LLM fine-tuning. PAC+ overcomes the resource bottlenecks through a sophisticated algorithm-system codesign: (1) Algorithmically, PAC+ introduces a fine-tuning technique optimized for parameters, time, and memory. It utilizes Parallel Adapters to circumvent the need for a full backward pass through the LLM backbone. Furthermore, an activation cache mechanism streamlines the process by negating redundant forward passes across multiple epochs. (2) Systematically, PAC+ aggregates proximate edge devices into a collective resource pool, employing hybrid data and pipeline parallelism to orchestrate distributed training. By leveraging the activation cache, PAC+ enables the exclusive fine-tuning of Parallel Adapters via data parallelism, effectively bypassing the backbone's constraints. Extensive evaluation of the prototype implementation demonstrates that PAC+ significantly outperforms existing collaborative edge training systems, achieving up to a 9.7× end-to-end speedup. Furthermore, compared to mainstream LLM fine-tuning algorithms, PAC+ reduces memory footprint by up to 88.16%. © 1990-2012 IEEE.

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
