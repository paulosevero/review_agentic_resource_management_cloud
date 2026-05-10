---
id: "paper-2379"
title: "Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices"
authors: ["Ye, Shengyuan", "Ouyang, Bei", "Zeng, Liekang", "Qian, Tianyi", "Chu, Xiaowen", "Tang, Jian", "Chen, Xu"]
year: 2025
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM55648.2025.11044734"
url: "https://www.scopus.com/pages/publications/105011060003?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Artificial intelligence", "Computer architecture", "Data privacy", "Decoding", "Mobile edge computing", "Computational resources", "Datacenter", "Decoding phasis", "Edge computing", "Jupiters", "Language model", "Memory usage", "Privacy preservation", "Resource-efficient", "User data", "Pipelines"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2379 — Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices

## Metadata

- **Authors:** Ye, Shengyuan and Ouyang, Bei and Zeng, Liekang and Qian, Tianyi and Chu, Xiaowen and Tang, Jian and Chen, Xu
- **Year:** 2025
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM55648.2025.11044734
- **URL:** https://www.scopus.com/pages/publications/105011060003?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Artificial intelligence; Computer architecture; Data privacy; Decoding; Mobile edge computing; Computational resources; Datacenter; Decoding phasis; Edge computing; Jupiters; Language model; Memory usage; Privacy preservation; Resource-efficient; User data; Pipelines

### Abstract

Generative large language models (LLMs) have garnered significant attention due to their exceptional capabilities in various AI tasks. Traditionally deployed in cloud datacenters, LLMs are now increasingly moving towards more accessible edge platforms to protect sensitive user data and ensure privacy preservation. The limited computational resources of individual edge devices, however, can result in excessively prolonged in-ference latency and overwhelmed memory usage. While existing research has explored collaborative edge computing to break the resource wall of individual devices, these solutions yet suffer from massive communication overhead and under-utilization of edge resources. Furthermore, they focus exclusively on optimizing the prefill phase, neglecting the crucial autoregressive decoding phase for generative LLMs. To address that, we propose Jupiter, a fast, scalable, and resource-efficient collaborative edge AI system for generative LLM inference. Jupiter introduces a flexible pipelined architecture as a principle and differentiates its system design according to the differentiated characteristics of the prefill and decoding phases. For prefill phase, Jupiter submits a novel intra-sequence pipeline parallelism and develops a meticulous parallelism planning strategy to maximize resource efficiency; For decoding, Jupiter devises an effective outline-based pipeline parallel decoding mechanism combined with speculative decoding, which further magnifies inference acceleration. Extensive evaluation based on realistic implementation demon-strates that Jupiter remarkably outperforms state-of-the-art approaches under various edge environment setups, achieving up to 26.1 × end-to-end latency reduction while rendering on-par generation quality.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Jupiter: Fast and Resource-Efficient Collaborative Inference of Generative LLMs on Edge Devices
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
