---
id: paper-0942
title: 'EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning'
authors:
- Hao, Yijun
- Yang, Shusen
- Li, Fang
- Zhang, Yifan
- Wang, Shibo
- Ren, Xuebin
venue: Proceedings - IEEE INFOCOM
venue_type: conference
year: 2024
doi: 10.1109/INFOCOM52122.2024.10621305
url: https://www.scopus.com/pages/publications/85201792059?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 671--680
keywords:
- adaptive timescales
- Mobile edge computing
- reinforcement learning
- resource scheduling
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

# paper-0942 — EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC), resource scheduling is crucial to task requests' performance and service providers' cost, involving multi-layer heterogeneous scheduling decisions. Existing schedulers typically adopt static timescales to regularly update scheduling decisions of each layer, without adaptive adjustment of timescales for different layers, resulting in potentially poor performance in practice.We notice that the adaptive timescales would significantly improve the trade-off between the operation cost and delay performance. Based on this insight, we propose EdgeTimer, the first work to automatically generate adaptive timescales to update multi-layer scheduling decisions using deep reinforcement learning (DRL). First, EdgeTimer uses a three-layer hierarchical DRL framework to decouple the multi-layer decision-making task into a hierarchy of independent sub-tasks for improving learning efficiency. Second, to cope with each sub-task, EdgeTimer adopts a safe multi-agent DRL algorithm for decentralized scheduling while ensuring system reliability. We apply EdgeTimer to a wide range of Kubernetes scheduling rules, and evaluate it using production traces with different workload patterns. Extensive trace-driven experiments demonstrate that EdgeTimer can learn adaptive timescales, irrespective of workload patterns and built-in scheduling rules. It obtains up to 9:1 more profit than existing approaches without sacrificing the delay performance. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0942.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
