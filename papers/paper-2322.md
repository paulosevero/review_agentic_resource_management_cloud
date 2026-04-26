---
id: "paper-2322"
title: "AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference"
authors: ["Xiong, Yi", "Zhang, Rui", "Zu, Yulong", "Liu, Weihong", "Zhu, Zongwei", "Geng, Jiawei", "Li, Boyu", "Cao, Qianyue", "Zhou, Xuehai"]
year: 2025
venue: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
venue_type: "journal"
doi: "10.1109/TCAD.2025.3624135"
url: "https://www.scopus.com/pages/publications/105020985176?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["edge computing", "LLM inference", "model parallelism", "response latency"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2322 — AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference

## Metadata

- **Authors:** Xiong, Yi and Zhang, Rui and Zu, Yulong and Liu, Weihong and Zhu, Zongwei and Geng, Jiawei and Li, Boyu and Cao, Qianyue and Zhou, Xuehai
- **Year:** 2025
- **Venue:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
- **DOI:** 10.1109/TCAD.2025.3624135
- **URL:** https://www.scopus.com/pages/publications/105020985176?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** edge computing; LLM inference; model parallelism; response latency

### Abstract

Edge deployment of large language models (LLMs) is increasingly attractive due to its advantages in privacy, customization, and availability. However, edge environments face significant challenges in reducing Time-to-First-Token (TTFT). TTFT consists of (1) queuing delay and (2) prefill latency, both of which are exacerbated by edge‑resource constraints: the substantial computational demands of LLM inference grow superlinearly with prompt length, causing high prefill latency; and limited edge resources restrict prefill throughput, preventing the timely handling of incoming requests, thereby exacerbating queuing delays. Model parallelism is a commonly used solution in cloud-based systems, but directly applying it to edge environments proves ineffective. Intra-layer parallelism (e.g., tensor/sequence parallelism) can reduce prefill latency but suffers from frequent global synchronization, which bottlenecks prefill throughput due to edge-limited interconnection bandwidth. Inter-layer parallelism (e.g., pipeline parallelism) improves prefill throughput via fully asynchronous execution but retains high prefill latency due to stage-wise serialized computation. To address this dilemma, this paper leverages the properties of the causal attention mechanism in LLMs and proposes Intra-layer Asynchronous Parallelism (IAP), which performs intra-layer parallel computations to reduce prefill latency while avoiding global synchronization to mitigate prefill throughput bottlenecks. Moreover, considering communication sensitivity in intra-layer parallelism, this paper integrate IAP with inter-layer asynchronous parallelism into a unified plan space. This hybrid parallelism adapts to diverse hardware and request loads, enabling more effective TTFT optimization. To enable the end-to-end implementation of this hybrid parallelism, this paper propose AsyncGrid, an LLM inference system tailored for responsive edge LLM inference. AsyncGrid (1) models runtime overheads through a performance profiler, (2) employs an integer programming (IP) formulation to optimize execution plan, with the objective of minimizing latency while meeting throughput requirements, and (3) implements fine-grained communication optimization during runtime. A comprehensive evaluation on an edge testbed demonstrates AsyncGrid’s significant advantages over existing methods, achieving substantial improvements in both homogeneous and heterogeneous settings. © 1982-2012 IEEE.

## 04 — Title Screening

**Title:** AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
