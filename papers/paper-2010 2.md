---
id: "paper-2010"
title: "RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models"
authors: ["Pan, Xiaojian", "Zeng, Chuxuan", "Liang, Du", "Cheng, Ma", "Huang, Dan"]
year: 2025
venue: "2025 5th International Conference on Communication Technology and Information Technology, ICCTIT 2025"
venue_type: "conference"
doi: "10.1109/ICCTIT68197.2025.11406447"
url: "https://www.scopus.com/pages/publications/105036197843?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "119--123"
keywords: ["Inference", "LLM", "Model Loading", "RDMA", "Serverless"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2010 — RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models

## Metadata

- **Authors:** Pan, Xiaojian and Zeng, Chuxuan and Liang, Du and Cheng, Ma and Huang, Dan
- **Year:** 2025
- **Venue:** 2025 5th International Conference on Communication Technology and Information Technology, ICCTIT 2025
- **DOI:** 10.1109/ICCTIT68197.2025.11406447
- **URL:** https://www.scopus.com/pages/publications/105036197843?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 119--123
- **Language:** English
- **Keywords:** Inference; LLM; Model Loading; RDMA; Serverless

### Abstract

Serverless computing facilitates elastic scaling for large language model (LLM) inference, but cold start latency - caused by inefficient loading of massive model parameters - limits its real-world applicability. Traditional TCP/IP-based remote loading suffers from high latency and CPU overhead, while local SSD caching solutions incur severe storage redundancy and underutilize distributed caches. To address these challenges, this paper proposes rtLoad, an efficient and scalable LLM parameter loading system based on RDMA (Remote Direct Memory Access) mechanism, integrating a client-server (CS) architecture with client-to-client (C2C) data sharing. rtLoad partitions models into 32MB fine-grained blocks, leverages GPUDirect RDMA to bypass the OS kernel call, and overlaps SSD I/O with RDMA transmission asynchronously. Clients holding model caches can act as data providers to enable C2C transmission, and a dynamic scheduling algorithm optimizes block distribution based on node load and network proximity. Experimental results on DeepSeek-R1-Distill-Qwen-7B and 14B models show that rtLoad outperforms existing methods significantly: compared with ServerlessLLM, rtLoad reduces loading time by up to 67% in warm start scenarios and 46% in dual-server cold start scenarios. For 4 concurrent clients loading the 14B model, rtLoad achieves a loading time of 3.16s, which is 20× faster than NFS-based loading. rtLoad effectively addresses the scalability and efficiency bottlenecks of LLM loading in serverless environments.  © 2025 IEEE.

## 04 — Title Screening

**Title:** RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** RtLoad: RDMA-Based Fast Scalable Loading for Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
