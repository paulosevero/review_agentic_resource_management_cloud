---
id: paper-2481
title: 'DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge'
authors:
- Zhu, Changhong
- Zhang, Haitao
- Xu, Xingtao
venue: 'Concurrency and Computation: Practice and Experience'
venue_type: journal
year: 2025
doi: 10.1002/cpe.70174
url: https://www.scopus.com/pages/publications/105009843742?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- dual-stage GPU-CPU task
- edge computing
- quality of service (QoS)
- reinforcement learning
- soft real-time
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

# paper-2481 — DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge cameras are ubiquitous, together with the recent boom in computer vision technology, and a variety of video analytics tasks are being processed at the edge. It is challenging to support more complex video analytics tasks on edge servers with unpredictable request loads and limited resources. However, most of these works use only a single optimization approach, focusing only on the improvement of a certain performance metric in a single processing stage, ignoring the balance of other performance metrics, and the space available for optimization is often very limited. Especially when dealing with video analytics tasks that need to be divided into two GPU-CPU stages for completion, this unidirectional focus may lead to execution performance imbalance or even negative quality of service (QoS) optimization. In addition, to fully utilize the valuable resources on the edge servers, it is often necessary to schedule multiple types of video analytics tasks on the edge servers. However, most of the existing scheduling strategies only focus on how to allocate computational resources for end-to-end tasks. They lack the awareness and consideration of the execution of tasks in different execution stages, as well as the mutual interference among tasks. These scheduling strategies, lacking stage-sensitivity and interference-sensitivity, may cause performance conflicts in environments running multiple tasks involving GPU-CPU dual-stage processing, thus affecting the overall QoS. To address these challenges, we first evaluate the impact of batch processing, frame rate control, resolution selection, and CPU concurrency processing on throughput, latency, and accuracy when running dual-stage tasks on edge platforms. Then, we propose DualRT, a soft real-time video analytics framework for dual-stage tasks, to optimize the QoS of dual-stage tasks while avoiding request stacking on edge platforms. In the scheduling module of DualRT, we design a scheduling method using a multi-agent deep reinforcement learning algorithm and a variable time window approach to schedule multiple dual-stage tasks with joint control of batch size, resolution, frame rate, and CPU concurrency for each task. Our experimental results show that DualRT improves QoS by an average of 13.3% and maximum throughput by an average of 24.6% compared to state-of-the-art solutions. © 2025 John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2481.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
