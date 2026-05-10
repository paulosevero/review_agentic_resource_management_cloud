---
id: paper-1807
title: Joint optimization of distributed intelligent computation offloading and service caching for DAG tasks; [面向 DAG 任务的分布式智能计算卸载和服务缓存联合优化]
authors:
- Li, Yun
- Nan, Ziyu
- Yao, Zhixiu
- Xia, Shichao
- Xian, Yongju
venue: Zhongshan Daxue Xuebao/Acta Scientiarum Natralium Universitatis Sunyatseni
venue_type: journal
year: 2025
doi: 10.13471/j.cnki.acta.snus.ZR20240181
url: https://www.scopus.com/pages/publications/85215684545?origin=resultslist
publisher: Journal of Zhongshan University
pages: 71--82
keywords:
- computation offloading
- mobile edge computing
- multi-agent deep reinforcement learning
- resource allocation
- service caching
language: Chinese
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1807 — Joint optimization of distributed intelligent computation offloading and service caching for DAG tasks; [面向 DAG 任务的分布式智能计算卸载和服务缓存联合优化]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A directed acyclic graph（DAG） was developed for task offloading and resource optimization，aiming to minimize system energy consumption under constraints such as maximum tolerable delay. Considering that computing requests are highly dynamic in the network and it is difficult to obtain complete system state information，the multi-agent deep deterministic policy gradient （MADDPG）algorithm is used to explore the optimal strategy. Compared to existing task offloading algorithms，the MADDPG algorithm can reduce the average system power consumption by 14.2% to 40.8%，and improve the local cache hit rate by 3.7% to 4.1%. © 2025 Journal of Zhongshan University. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1807.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
