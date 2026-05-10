---
id: paper-1641
title: Task Optimization Allocation in Vehicle Based Edge Computing Systems With Deep Reinforcement Learning
authors:
- He, Qiang
- Li, Quanwei
- Zhang, Chuangchuang
- Wang, Xingwei
- Bi, Yuanguo
- Zhao, Liang
- Hawbani, Ammar
- Yu, Keping
venue: IEEE Transactions on Computers
venue_type: journal
year: 2025
doi: 10.1109/TC.2025.3585630
url: https://www.scopus.com/pages/publications/105010303537?origin=resultslist
publisher: IEEE Computer Society
pages: 3156--3167
keywords:
- deep reinforcement learning
- resource allocation
- task offloading
- Vehicle based medical edge computing
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

# paper-1641 — Task Optimization Allocation in Vehicle Based Edge Computing Systems With Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the recent advancement in network technologies, the vehicle based medical networks extend medical services to mobile vehicles, thereby offering flexible and efficient healthcare services for vehicle users in need. The integration of vehicle based medical network and edge computing enables computation intensive medical service tasks to be offloaded on edge servers, to provide fast service response for vehicle users. An efficient task offloading and resource allocation strategy is critical for Vehicle based Medical Edge Computing System (VMECS) to satisfy real-time and reliability requirements while ensuring service performance. To this end, in this paper, we investigate the problem of task computation allocation in VMECS networks. By introducing deep reinforcement learning, we first present a novel VMECS architecture to automatically achieve the optimal task offloading and resource allocation through the multi-agent collaboration, thereby improving service performance. Then, we formulate the problem of task offloading and resource allocation in VMECS networks as an optimization model with the aim of maximizing task success rate by jointly considering communication interferences, resource allocation and delay requirements. To solve it, we further devise a Distributed distributional deterministic policy gradients based Task offloading and Resource allocation (DTR) algorithm. Final simulation results demonstrate that compared with benchmark algorithms, DTR algorithm can obtain higher task success rate, smaller service time, and less task processing time. © 1968-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1641.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
