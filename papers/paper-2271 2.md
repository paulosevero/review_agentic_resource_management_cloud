---
id: "paper-2271"
title: "lm-Meter: Unveiling Runtime Inference Latency for On-Device Language Models"
authors: ["Wang, Haoxin", "Tu, Xiaolong", "Ke, Hongyu", "Chai, Huirong", "Chen, Dawei", "Han, Kyungtae"]
year: 2025
venue: "SEC 2025 - Proceedings of the 2025 10th ACM/IEEE Symposium on Edge Computing"
venue_type: "conference"
doi: "10.1145/3769102.3770614"
url: "https://www.scopus.com/pages/publications/105024937778?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: ""
keywords: ["Edge Computing", "Large Language Models", "On-Device AI"]
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

# paper-2271 — lm-Meter: Unveiling Runtime Inference Latency for On-Device Language Models

## Metadata

- **Authors:** Wang, Haoxin and Tu, Xiaolong and Ke, Hongyu and Chai, Huirong and Chen, Dawei and Han, Kyungtae
- **Year:** 2025
- **Venue:** SEC 2025 - Proceedings of the 2025 10th ACM/IEEE Symposium on Edge Computing
- **DOI:** 10.1145/3769102.3770614
- **URL:** https://www.scopus.com/pages/publications/105024937778?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 
- **Language:** English
- **Keywords:** Edge Computing; Large Language Models; On-Device AI

### Abstract

Large Language Models (LLMs) are increasingly integrated into everyday applications, but their prevalent cloud-based deployment raises growing concerns around data privacy and long-term sustainability. Running LLMs locally on mobile and edge devices (on-device LLMs) offers the promise of enhanced privacy, reliability, and reduced communication costs. However, realizing this vision remains challenging due to substantial memory and compute demands, as well as limited visibility into performance-efficiency trade-offs on resource-constrained hardware. We propose lm-Meter, the first lightweight, online latency profiler tailored for on-device LLM inference. lm-Meter captures fine-grained, real-time latency at both phase (e.g., embedding, prefill, decode, softmax, sampling) and kernel levels without auxiliary devices. We implement lm-Meter on commercial mobile platforms and demonstrate its high profiling accuracy with minimal system overhead, e.g., only 2.58% throughput reduction in prefill and 0.99% in decode under the most constrained Powersave governor. Leveraging lm-Meter, we conduct comprehensive empirical studies revealing phase- and kernel-level bottlenecks in on-device LLM inference, quantifying accuracy-efficiency trade-offs, and identifying systematic optimization opportunities. lm-Meter provides unprecedented visibility into the runtime behavior of LLMs on constrained platforms, laying the foundation for informed optimization and accelerating the democratization of on-device LLM systems. Code and tutorials are available at github.com/amai-gsu/LM-Meter. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** lm-Meter: Unveiling Runtime Inference Latency for On-Device Language Models

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** lm-Meter: Unveiling Runtime Inference Latency for On-Device Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** lm-Meter: Unveiling Runtime Inference Latency for On-Device Language Models
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
