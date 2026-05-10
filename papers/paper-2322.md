---
id: paper-2322
title: 'AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference'
authors:
- Xiong, Yi
- Zhang, Rui
- Zu, Yulong
- Liu, Weihong
- Zhu, Zongwei
- Geng, Jiawei
- Li, Boyu
- Cao, Qianyue
- Zhou, Xuehai
venue: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
venue_type: journal
year: 2025
doi: 10.1109/TCAD.2025.3624135
url: https://www.scopus.com/pages/publications/105020985176?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- edge computing
- LLM inference
- model parallelism
- response latency
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2322 — AsyncGrid: An Intra- and Inter-Layer Asynchronous Hybrid Parallelism System for Responsive Edge LLM Inference

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge deployment of large language models (LLMs) is increasingly attractive due to its advantages in privacy, customization, and availability. However, edge environments face significant challenges in reducing Time-to-First-Token (TTFT). TTFT consists of (1) queuing delay and (2) prefill latency, both of which are exacerbated by edge‑resource constraints: the substantial computational demands of LLM inference grow superlinearly with prompt length, causing high prefill latency; and limited edge resources restrict prefill throughput, preventing the timely handling of incoming requests, thereby exacerbating queuing delays. Model parallelism is a commonly used solution in cloud-based systems, but directly applying it to edge environments proves ineffective. Intra-layer parallelism (e.g., tensor/sequence parallelism) can reduce prefill latency but suffers from frequent global synchronization, which bottlenecks prefill throughput due to edge-limited interconnection bandwidth. Inter-layer parallelism (e.g., pipeline parallelism) improves prefill throughput via fully asynchronous execution but retains high prefill latency due to stage-wise serialized computation. To address this dilemma, this paper leverages the properties of the causal attention mechanism in LLMs and proposes Intra-layer Asynchronous Parallelism (IAP), which performs intra-layer parallel computations to reduce prefill latency while avoiding global synchronization to mitigate prefill throughput bottlenecks. Moreover, considering communication sensitivity in intra-layer parallelism, this paper integrate IAP with inter-layer asynchronous parallelism into a unified plan space. This hybrid parallelism adapts to diverse hardware and request loads, enabling more effective TTFT optimization. To enable the end-to-end implementation of this hybrid parallelism, this paper propose AsyncGrid, an LLM inference system tailored for responsive edge LLM inference. AsyncGrid (1) models runtime overheads through a performance profiler, (2) employs an integer programming (IP) formulation to optimize execution plan, with the objective of minimizing latency while meeting throughput requirements, and (3) implements fine-grained communication optimization during runtime. A comprehensive evaluation on an edge testbed demonstrates AsyncGrid’s significant advantages over existing methods, achieving substantial improvements in both homogeneous and heterogeneous settings. © 1982-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2322.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
