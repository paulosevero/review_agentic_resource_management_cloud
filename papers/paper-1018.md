---
id: paper-1018
title: DRL-based Content Caching Strategy With Efficient User Preference Predictions in UAV-assisted VEC
authors:
- Li, Chunlin
- Zhang, Yong
- Yu, Long
- Jiang, Kun
- Luo, Youlong
- Wan, Shaohua
venue: ACM Transactions on Sensor Networks
venue_type: journal
year: 2024
doi: 10.1145/3701234
url: https://www.scopus.com/pages/publications/85210126852?origin=resultslist
publisher: Association for Computing Machinery
pages: ''
keywords:
- cooperative content caching
- I-MADDPG
- UAV-assisted VEC
- user preference predic- tions
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1018 — DRL-based Content Caching Strategy With Efficient User Preference Predictions in UAV-assisted VEC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In vehicular edge computing, Unmanned Aerial Vehicles (UAVs) have become a feasible solution for addressing high deployment costs faced by base stations in congested roads during peak hours. However, UAVs cannot cache all requested content due to limited storage. Hence, we propose a content caching strategy based on user preference predictions. To address resource consumption and user privacy concerns during the training process, we propose a user preference prediction model based on hierarchical federated learning training. Specifically, we employ a hierarchical clustering approach to partition user vehicles and UAVs into multiple clusters and utilize hierarchical federated learning to train prediction models within each cluster. Furthermore, to tackle the joint optimization problem of content caching and bandwidth allocation, we propose I-MADDPG, an improved multi-agent deep deterministic policy gradient algorithm. It determines the next continuous action based on the reward value at the current moment and the average reward value in the iteration period as reference parameters. The experimental results demonstrate that the proposed algorithm has significantly enhanced training efficiency compared to the baselines. Additionally, it has improved cache hit rate and reduced content request delay through effective resource allocation.  © 2024 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1018.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
