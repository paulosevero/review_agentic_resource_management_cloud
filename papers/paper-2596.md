---
id: paper-2596
title: 'BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure'
authors:
- He, Yiyuan
- Xu, Minxian
- Wu, Jingfeng
- Hu, Jianmin
- Ma, Chong
- Shen, Min
- Chen, Le
- Xu, Chengzhong
- Qu, Lin
- Ye, Kejiang
venue: Software - Practice and Experience
venue_type: journal
year: 2026
doi: 10.1002/spe.70054
url: https://www.scopus.com/pages/publications/105028129774?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: 424--444
keywords:
- AI infrastructure
- cloud computing
- disaggregated LLM serving
- large language models
- resource management
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
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

# paper-2596 — BanaServe: Unified KV Cache and Dynamic Module Migration for Balancing Disaggregated LLM Serving in AI Infrastructure

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Objective: Large Language Models (LLMs) are increasingly deployed in modern AI infrastructure, creating a strong demand for high-throughput and resource-efficient serving systems. Disaggregated LLM serving, which decouples prompt prefill from auto-regressive decode to accommodate their heterogeneous compute and memory characteristics, has emerged as a promising architecture. However, existing disaggregated serving systems suffer from three fundamental limitations: static resource allocation that fails to adapt to highly dynamic workloads, severe load imbalance between compute-bound prefill and memory-bound decode stages, and prefix-cache-aware routing that skews load distribution and creates performance hotspots. These issues collectively limit resource utilization, scalability, and the ability to meet service level objectives (SLOs) under real-world workloads. Methods: To address these challenges, we propose BanaServe, a dynamic orchestration framework for disaggregated LLM serving that continuously rebalances both computational and memory resources across prefill and decode instances. BanaServe introduces three key mechanisms: (i) layer-level weight migration to enable coarse-grained redistribution of computation, (ii) attention-level Key–Value (KV) cache migration for fine-grained memory load balancing, and (iii) a Global KV Cache Store with layer-wise overlapped transmission to decouple routing decisions from cache placement. Together, these mechanisms eliminate cache-induced hotspots and allow routers to perform purely load-aware scheduling with minimal latency overhead. BanaServe is implemented on top of state-of-the-art LLM serving frameworks, including vLLM and DistServe. Results: We evaluate BanaServe under diverse and challenging workloads, including long-context inference, bursty request arrivals, and mixed prompt–generation patterns. Experimental results show that, compared to vLLM, BanaServe improves throughput by 1.2–3.9× and reduces total processing time by 3.9%–78.4%. In comparison with DistServe, BanaServe achieves 1.1–2.8× higher throughput while reducing latency by 1.4%–70.1%. These gains are consistent across workload variations, demonstrating BanaServe's robustness under highly dynamic serving conditions. Conclusion: BanaServe demonstrates that dynamic, multi-granularity resource rebalancing and cache-decoupled routing are essential for efficient disaggregated LLM serving. By jointly addressing resource elasticity, stage imbalance, and cache-induced load skew, BanaServe substantially improves throughput, latency, and resource utilization in real-world deployments. This work provides a practical and scalable foundation for next-generation LLM serving systems operating under dynamic and heterogeneous workloads. © 2026 John Wiley & Sons Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2596.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
