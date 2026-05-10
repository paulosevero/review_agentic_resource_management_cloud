---
id: "paper-1922"
title: "Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity"
authors: ["Lv, Cunchi", "Shi, Xiao", "Lei, Zhengyu", "Huang, Jinyue", "Tan, Wenting", "Zheng, Xiaohui", "Zhao, Xiaofang"]
year: 2025
venue: "International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS"
venue_type: "conference"
doi: "10.1145/3669940.3707251"
url: "https://www.scopus.com/pages/publications/105002373103?origin=resultslist"
publisher: "Association for Computing Machinery"
pages: "311--325"
keywords: ["co-scaling", "gpu resourcing-on-demand", "introspective elasticity", "serverless deep learning"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1922 — Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity

## Metadata

- **Authors:** Lv, Cunchi and Shi, Xiao and Lei, Zhengyu and Huang, Jinyue and Tan, Wenting and Zheng, Xiaohui and Zhao, Xiaofang
- **Year:** 2025
- **Venue:** International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
- **DOI:** 10.1145/3669940.3707251
- **URL:** https://www.scopus.com/pages/publications/105002373103?origin=resultslist
- **Publisher:** Association for Computing Machinery
- **Pages:** 311--325
- **Language:** English
- **Keywords:** co-scaling; gpu resourcing-on-demand; introspective elasticity; serverless deep learning

### Abstract

Serverless computing, with its ease of management, auto-scaling, and cost-effectiveness, is widely adopted by deep learning (DL) applications. DL workloads, especially with large language models, require substantial GPU resources to ensure QoS. However, it is prone to produce GPU fragments (e.g., 15%-94%) in serverless DL systems due to the dynamicity of workloads and coarse-grained static GPU allocation mechanisms, gradually eroding the profits offered by serverless elasticity. Different from classical serverless systems that only scale horizontally, we present introspective elasticity (IE), a fine-grained and adaptive two-dimensional co-scaling mechanism to support GPU resourcing-on-demand for serverless DL tasks. Based on this insight, we build Dilu, a cross-layer and GPU-based serverless DL system with IE support. First, Dilu provides multi-factor profiling for DL tasks with efficient pruning search methods. Second, Dilu adheres to the resourcing-complementary principles in scheduling to improve GPU utilization with QoS guarantees. Third, Dilu adopts an adaptive 2D co-scaling method to enhance the elasticity of GPU provisioning in real time. Evaluations show that it can dynamically adjust the resourcing of various DL functions with low GPU fragmentation (10%-46% GPU defragmentation), high throughput (up to 1.8× inference and 1.1× training throughput increment) and QoS guarantees (11%-71% violation rate reduction), compared to the SOTA baselines.  © 2025 ACM.

## 04 — Title Screening

**Title:** Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
