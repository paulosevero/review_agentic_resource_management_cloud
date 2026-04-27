---
id: "paper-2596"
title: "BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure"
authors: ["He, Yiyuan", "Xu, Minxian", "Wu, Jingfeng", "Hu, Jianmin", "Ma, Chong", "Shen, Min", "Chen, Le", "Xu, Chengzhong", "Qu, Lin", "Ye, Kejiang"]
year: 2026
venue: "Software - Practice and Experience"
venue_type: "journal"
doi: "10.1002/spe.70054"
url: "https://www.scopus.com/pages/publications/105028129774?origin=resultslist"
publisher: "John Wiley and Sons Ltd"
pages: "424--444"
keywords: ["AI infrastructure", "cloud computing", "disaggregated LLM serving", "large language models", "resource management"]
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

# paper-2596 — BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure

## Metadata

- **Authors:** He, Yiyuan and Xu, Minxian and Wu, Jingfeng and Hu, Jianmin and Ma, Chong and Shen, Min and Chen, Le and Xu, Chengzhong and Qu, Lin and Ye, Kejiang
- **Year:** 2026
- **Venue:** Software - Practice and Experience
- **DOI:** 10.1002/spe.70054
- **URL:** https://www.scopus.com/pages/publications/105028129774?origin=resultslist
- **Publisher:** John Wiley and Sons Ltd
- **Pages:** 424--444
- **Language:** English
- **Keywords:** AI infrastructure; cloud computing; disaggregated LLM serving; large language models; resource management

### Abstract

Objective: Large Language Models (LLMs) are increasingly deployed in modern AI infrastructure, creating a strong demand for high-throughput and resource-efficient serving systems. Disaggregated LLM serving, which decouples prompt prefill from auto-regressive decode to accommodate their heterogeneous compute and memory characteristics, has emerged as a promising architecture. However, existing disaggregated serving systems suffer from three fundamental limitations: static resource allocation that fails to adapt to highly dynamic workloads, severe load imbalance between compute-bound prefill and memory-bound decode stages, and prefix-cache-aware routing that skews load distribution and creates performance hotspots. These issues collectively limit resource utilization, scalability, and the ability to meet service level objectives (SLOs) under real-world workloads. Methods: To address these challenges, we propose BanaServe, a dynamic orchestration framework for disaggregated LLM serving that continuously rebalances both computational and memory resources across prefill and decode instances. BanaServe introduces three key mechanisms: (i) layer-level weight migration to enable coarse-grained redistribution of computation, (ii) attention-level Key–Value (KV) cache migration for fine-grained memory load balancing, and (iii) a Global KV Cache Store with layer-wise overlapped transmission to decouple routing decisions from cache placement. Together, these mechanisms eliminate cache-induced hotspots and allow routers to perform purely load-aware scheduling with minimal latency overhead. BanaServe is implemented on top of state-of-the-art LLM serving frameworks, including vLLM and DistServe. Results: We evaluate BanaServe under diverse and challenging workloads, including long-context inference, bursty request arrivals, and mixed prompt–generation patterns. Experimental results show that, compared to vLLM, BanaServe improves throughput by 1.2–3.9× and reduces total processing time by 3.9%–78.4%. In comparison with DistServe, BanaServe achieves 1.1–2.8× higher throughput while reducing latency by 1.4%–70.1%. These gains are consistent across workload variations, demonstrating BanaServe's robustness under highly dynamic serving conditions. Conclusion: BanaServe demonstrates that dynamic, multi-granularity resource rebalancing and cache-decoupled routing are essential for efficient disaggregated LLM serving. By jointly addressing resource elasticity, stage imbalance, and cache-induced load skew, BanaServe substantially improves throughput, latency, and resource utilization in real-world deployments. This work provides a practical and scalable foundation for next-generation LLM serving systems operating under dynamic and heterogeneous workloads. © 2026 John Wiley & Sons Ltd.

## 04 — Title Screening

**Title:** BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure
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
