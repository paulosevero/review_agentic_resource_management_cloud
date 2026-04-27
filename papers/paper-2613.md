---
id: "paper-2613"
title: "EdgeSD: Efficient Speculative Decoding with Vision-Decoding Disaggregation for MLLM Inference in Edge-Cloud Networks"
authors: ["Huang, Hualong", "Zhan, Wenhan", "Duan, Hancong", "Peng, Kai", "Min, Geyong", "Zhao, Zijia", "Zhao, Zitian", "Ye, Yalan"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3667591"
url: "https://www.scopus.com/pages/publications/105031502323?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["edge-cloud collaborative inference", "mobile edge computing", "Multimodal large language model inference", "task scheduling"]
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
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-2613 — EdgeSD: Efficient Speculative Decoding with Vision-Decoding Disaggregation for MLLM Inference in Edge-Cloud Networks

## Metadata

- **Authors:** Huang, Hualong and Zhan, Wenhan and Duan, Hancong and Peng, Kai and Min, Geyong and Zhao, Zijia and Zhao, Zitian and Ye, Yalan
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3667591
- **URL:** https://www.scopus.com/pages/publications/105031502323?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** edge-cloud collaborative inference; mobile edge computing; Multimodal large language model inference; task scheduling

### Abstract

The deployment of multimodal large language models (MLLMs) in edge-cloud networks faces critical challenges, including computational resource heterogeneity, memory bottlenecks, and bandwidth constraints. To address these issues, we propose EdgeSD, a novel framework that accelerates MLLM inference by integrating speculative decoding (SD) with edge-cloud collaboration. First, EdgeSD decouples the vision encoding and decoding processes of the draft MLLM across heterogeneous edge servers (ESs). This disaggregation architecture overcomes single-node memory constraints, enabling optimized resource utilization and high-resolution input processing. Second, to resolve the communication bottleneck and computational burden inherent in this distributed architecture, EdgeSD integrates a bandwidth-aware dynamic image token merging (ITM) method. Unlike general pruning techniques, this EdgeSD-specific ITM method focuses on minimizing inter-ES transmission latency for vision-decoding disaggregation while maintaining draft quality. Third, to optimize SD efficiency on consumer-grade ESs, EdgeSD employs an adaptive and scalable token tree structure solved using a parallel delta-stepping algorithm. This structure maximizes the number of accepted tokens under strict edge latency constraints. Extensive experiments on six multimodal datasets and five benchmarks with various MLLM pairs demonstrate that EdgeSD achieves substantial acceleration and throughput gains in edge-cloud collaboration scenarios using a lightweight draft MLLM, achieving 3.04-5.12x speedup compared to baseline methods. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** EdgeSD: Efficient Speculative Decoding with Vision-Decoding Disaggregation for MLLM Inference in Edge-Cloud Networks

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeSD: Efficient Speculative Decoding with Vision-Decoding Disaggregation for MLLM Inference in Edge-Cloud Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeSD: Efficient Speculative Decoding with Vision-Decoding Disaggregation for MLLM Inference in Edge-Cloud Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
