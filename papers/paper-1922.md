---
id: paper-1922
title: 'Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity'
authors:
- Lv, Cunchi
- Shi, Xiao
- Lei, Zhengyu
- Huang, Jinyue
- Tan, Wenting
- Zheng, Xiaohui
- Zhao, Xiaofang
venue: International Conference on Architectural Support for Programming Languages and Operating Systems - ASPLOS
venue_type: conference
year: 2025
doi: 10.1145/3669940.3707251
url: https://www.scopus.com/pages/publications/105002373103?origin=resultslist
publisher: Association for Computing Machinery
pages: 311--325
keywords:
- co-scaling
- gpu resourcing-on-demand
- introspective elasticity
- serverless deep learning
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1922 — Dilu: Enabling GPU Resourcing-on-Demand for Serverless DL Serving via Introspective Elasticity

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing, with its ease of management, auto-scaling, and cost-effectiveness, is widely adopted by deep learning (DL) applications. DL workloads, especially with large language models, require substantial GPU resources to ensure QoS. However, it is prone to produce GPU fragments (e.g., 15%-94%) in serverless DL systems due to the dynamicity of workloads and coarse-grained static GPU allocation mechanisms, gradually eroding the profits offered by serverless elasticity. Different from classical serverless systems that only scale horizontally, we present introspective elasticity (IE), a fine-grained and adaptive two-dimensional co-scaling mechanism to support GPU resourcing-on-demand for serverless DL tasks. Based on this insight, we build Dilu, a cross-layer and GPU-based serverless DL system with IE support. First, Dilu provides multi-factor profiling for DL tasks with efficient pruning search methods. Second, Dilu adheres to the resourcing-complementary principles in scheduling to improve GPU utilization with QoS guarantees. Third, Dilu adopts an adaptive 2D co-scaling method to enhance the elasticity of GPU provisioning in real time. Evaluations show that it can dynamically adjust the resourcing of various DL functions with low GPU fragmentation (10%-46% GPU defragmentation), high throughput (up to 1.8× inference and 1.1× training throughput increment) and QoS guarantees (11%-71% violation rate reduction), compared to the SOTA baselines.  © 2025 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1922.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
