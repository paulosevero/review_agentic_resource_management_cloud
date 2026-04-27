---
id: "paper-1787"
title: "CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network"
authors: ["Li, Zhuotong", "Xu, Liang", "Huang, Ziqi", "Qian, Shuyun", "Bu, Hongwei", "Yang, Ming", "Luan, Mengyun", "Chen, Weiguo", "Wen, Xu"]
year: 2025
venue: "Proceedings of the International Conference on Supercomputing"
venue_type: "conference"
doi: "10.1145/3721145.3725772"
url: "https://www.scopus.com/pages/publications/105021481260?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "355--367"
keywords: ["Collective Communication Library", "LLMs", "Load Balancing", "RoCE"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-1787 — CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network

## Metadata

- **Authors:** Li, Zhuotong and Xu, Liang and Huang, Ziqi and Qian, Shuyun and Bu, Hongwei and Yang, Ming and Luan, Mengyun and Chen, Weiguo and Wen, Xu
- **Year:** 2025
- **Venue:** Proceedings of the International Conference on Supercomputing
- **DOI:** 10.1145/3721145.3725772
- **URL:** https://www.scopus.com/pages/publications/105021481260?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 355--367
- **Language:** English
- **Keywords:** Collective Communication Library; LLMs; Load Balancing; RoCE

### Abstract

Pre-training large language models (LLMs) in data centers (DCs) is a complex yet essential task that requires vast computational resources and carefully designed infrastructures to enable efficient, large-scale distributed learning. However, without effective load balancing in RDMA over Converged Ethernet (RoCE) networks, network congestion and latency can create significant bottlenecks, disrupting data transmission, reducing resource utilization, and prolonging training times, ultimately compromising the scalability and performance of LLM training. To address these challenges, we propose and develop an innovative and cost-effective joint Device-Network Load Balancing (DNLB) approach. Built on our custom collective communication library, CTCCL, DNLB coordinates device-side flow optimization with network-side switch configuration to mitigate hash collisions and alleviate congestion. By managing UDP source port numbers and distributing traffic uniformly across multiple paths, DNLB achieves efficient load balancing without requiring hardware modifications. Moreover, DNLB demonstrates exceptional adaptability and fault tolerance, ensuring compatibility with diverse network architectures, task modes, and device deployments. Even in the event of uplink failures, it maintains robust network load balancing. Experiments conducted in real-world intelligent computing DCs demonstrate that DNLB improves communication efficiency by up to 40% and enhances overall pre-training efficiency of LLMs by 7%, offering a practical, scalable solution for modern LLM training. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.

## 04 — Title Screening

**Title:** CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** CTCCL: Cost-Efficient Joint Device-Network Load Balancing for LLM Training in RoCE-based Intelligent Computing Network
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
