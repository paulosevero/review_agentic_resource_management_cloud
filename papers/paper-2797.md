---
id: paper-2797
title: QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads
authors:
- Tao, Xi
- Lu, Dongji
- Cao, Weipeng
- Gu, Jiongjiong
- Cai, Zhiyuan
- Xu, Chuanfei
- Zhang, Liang-Jie
- Ming, Zhong
venue: IEEE Transactions on Services Computing
venue_type: journal
year: 2026
doi: 10.1109/TSC.2026.3676714
url: https://www.scopus.com/pages/publications/105034077540?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- cloud workload
- CPU pinning
- Deep reinforcement learning
- quality of service
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2797 — QoS-Aware Deep Reinforcement Learning for Dynamic CPU Pinning of Co-located Cloud Workloads

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In cloud computing, static resource configurations create a trade-off: tenants overprovision to avoid resource starvation, causing inefficiency and cost, while providers suffer low utilization despite high allocations. To improve efficiency, providers often use overcommitted environments where multiple workloads share hosts, but this leads to interference and potential Quality-of-Service (QoS) violations. This paper introduces a realtime dynamic control framework that mitigates interference by adaptively pinning workloads to CPU groups. Using deep reinforcement learning (DRL) with the Proximal Policy Optimization (PPO) algorithm, an intelligent agent continuously adjusts CPU pinning based on real-time feedback to maintain Service- Level-Agreement (SLA) compliance. Experiments under two optimization objectives—overall-performance-first and priorityperformance- first—show that the proposed approach improves overall QoS by ≈25% compared with static pinning. When prioritization is enabled, high-priority workloads gain significant performance improvements while lower-priority ones remain within SLA limits. These results demonstrate that a DRL-based CPU-pinning strategy effectively manages resource contention in overcommitted clouds, enhancing utilization while upholding tenant SLAs. © 2008-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2797.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
