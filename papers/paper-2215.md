---
id: paper-2215
title: Multi-user multi-exit DNN inference partitioning and task scheduling strategy
authors:
- Tian, Xianzhong
- Li, Yucheng
- Mao, Xuhua
- Zhang, Luoming
- Lin, Ziyi
venue: Journal of Supercomputing
venue_type: journal
year: 2025
doi: 10.1007/s11227-025-07508-z
url: https://www.scopus.com/pages/publications/105007770502?origin=resultslist
publisher: Springer
pages: ''
keywords:
- DNN inference
- Double greedy algorithm
- Edge intelligence
- Reinforcement learning
- Task scheduling
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2215 — Multi-user multi-exit DNN inference partitioning and task scheduling strategy

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge intelligence, combining artificial intelligence with edge computing, is a promising emerging technology. However, its efficient operation inevitably faces the challenge of handling massive data. To address this challenge, multi-exit models and partitioning models have been developed. Notably, existing research on multi-exit deep neural networks (DNN) inference partitioning models predominantly focuses on optimizing the model itself, with less attention to the task scheduling complexity in multi-user scenarios. In view of this, this paper delves into the issues of DNN inference partitioning and task scheduling within a multi-user environment, proposing a multi-user multi-exit DNN inference partitioning and task scheduling strategy. This strategy takes into account factors such as task urgency and deadlines, optimizing DNN exit and partition points while enabling rational task scheduling to maximize task completion rates and inference accuracy. We design a double greedy algorithm-based inference task scheduling mechanism that efficiently schedules inference tasks for multiple users on edge servers, achieving optimal utilization of system resources. Additionally, we introduce the multi-agent proximal policy optimization method to further optimize the performance of multi-exit and partition models. Simulation experiments, compared to other mainstream scheduling algorithms, demonstrate that the proposed algorithm effectively improves task completion rates. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2215.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
