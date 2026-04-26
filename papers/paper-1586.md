---
id: "paper-1586"
title: "Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]"
authors: ["Ge, Xuran", "Ou, Yang", "Wang, Bo", "Zhao, Yu", "Wu, Lizhou", "Wang, Zicong", "Chen, Zhiguang", "Xiao, Nong"]
year: 2025
venue: "Jisuanji Yanjiu yu Fazhan/Computer Research and Development"
venue_type: "journal"
doi: "10.7544/issn1000-1239.202440628"
url: "https://www.scopus.com/pages/publications/105001257497?origin=resultslist"
publisher: "Science Press"
pages: "545--562"
keywords: ["distributed storage", "fault recovery", "heterogeneous storage", "LLM inference system", "memory management", "serverless LLM inference"]
language: "Chinese"
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1586 — Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]

## Metadata

- **Authors:** Ge, Xuran and Ou, Yang and Wang, Bo and Zhao, Yu and Wu, Lizhou and Wang, Zicong and Chen, Zhiguang and Xiao, Nong
- **Year:** 2025
- **Venue:** Jisuanji Yanjiu yu Fazhan/Computer Research and Development
- **DOI:** 10.7544/issn1000-1239.202440628
- **URL:** https://www.scopus.com/pages/publications/105001257497?origin=resultslist
- **Publisher:** Science Press
- **Pages:** 545--562
- **Language:** Chinese
- **Keywords:** distributed storage; fault recovery; heterogeneous storage; LLM inference system; memory management; serverless LLM inference

### Abstract

In recent years, LLM (large language model) has exhibited remarkable performance, profoundly transforming various aspects of human life. As these models grow in size and user demand for long-context inference increases, LLM inference systems face significant storage challenges. These challenges stem primarily from the vast number of model parameters and the key value cache required for efficient inference, both of which strain GPU memory resources. Additionally, inefficiencies in storage usage in distributed systems often result in over-provisioning and fault tolerance issues, further complicating resource management. Researchers explore memory optimization, heterogeneous storage, and distributed storage, synthesizing various research efforts to address GPU memory constraints and enhance resource utilization. Memory-optimized LLM inference systems improve GPU memory efficiency and reduce memory footprint through techniques like efficient key value cache management, compression, and attention operator optimization. Heterogeneous storage based LLM inference systems expand storage capacity by integrating various storage resources, thereby minimizing I/O overhead via tensor placement strategies, asynchronous data transfer, and intelligent memory allocation and prefetching methods. Distributed LLM systems enhance the utilization of multi-machine resources, boosting execution efficiency and fault tolerance in LLM inference tasks through batching, multi-level scheduling, and redundant replication. Finally, we review existing research and outline future research directions to further optimize storage solutions for LLM inference systems. © 2025 Science Press. All rights reserved.

## 04 — Title Screening

**Title:** Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Survey of Storage Optimization Techniques in Large Language Model Inference; [大语言模型推理中的存储优化技术综述]
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
