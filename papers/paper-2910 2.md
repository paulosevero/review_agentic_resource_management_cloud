---
id: "paper-2910"
title: "EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices"
authors: ["Zhang, Yutao", "Zhong, Wentao", "Liu, Xuerui", "Huang, Fengyi", "Wang, Wenhua", "Wang, Tian", "Jia, Weijia"]
year: 2026
venue: "Lecture Notes in Computer Science"
venue_type: "conference"
doi: "10.1007/978-981-95-5012-8_34"
url: "https://www.scopus.com/pages/publications/105028311673?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "457--465"
keywords: ["Edge LLM inference", "Heterogeneous", "KV cache", "Tensor parallelism"]
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

# paper-2910 — EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices

## Metadata

- **Authors:** Zhang, Yutao and Zhong, Wentao and Liu, Xuerui and Huang, Fengyi and Wang, Wenhua and Wang, Tian and Jia, Weijia
- **Year:** 2026
- **Venue:** Lecture Notes in Computer Science
- **DOI:** 10.1007/978-981-95-5012-8_34
- **URL:** https://www.scopus.com/pages/publications/105028311673?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 457--465
- **Language:** English
- **Keywords:** Edge LLM inference; Heterogeneous; KV cache; Tensor parallelism

### Abstract

Large Language Model (LLM) inference heavily relies on cloud systems, resulting in inherent limitations such as prolonged delays, escalated bandwidth expenditure, and potential data security risks. Edge computing emerges as a solution by enabling LLM execution on edge devices, closer to data sources. However, challenges such as device heterogeneity and limited memory capacity pose significant barriers to conventional tensor parallelism of LLM. Therefore, we propose EdgeInfer-TP, a resource-aware collaborative tensor parallelism inference system tailored for heterogeneous edge devices. It integrates MILP-based model allocation optimization and multi-level dynamic offloading of KV cache to enable efficient and stable collaborative inference on resource-constrained devices. The experimental results across multiple real-world heterogeneous devices and diverse network environments demonstrate that our approach achieves up to 22.23% latency reduction and 27.87% throughput improvement over baseline approaches. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

## 04 — Title Screening

**Title:** EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** EdgeInfer-TP: A Collaborative Tensor Parallelism Inference System for Heterogeneous Edge Devices
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
