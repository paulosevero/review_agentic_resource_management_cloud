---
id: paper-0973
title: 'Multilayer Satellite Network Collaborative Mobile Edge Caching: A GCN-Based Multi-Agent Approach'
authors:
- Jie, Yang
- Jingchao, He
- Nan, Cheng
- Zhisheng, Yin
- Dairu, Han
- Conghao, Zhou
- Ruijin, Sun
venue: China Communications
venue_type: journal
year: 2024
doi: 10.23919/JCC.fa.2024-0216.202411
url: https://www.scopus.com/pages/publications/105024920716?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 56--74
keywords:
- cache placement
- coded caching
- graph convolutional network (GCN)
- mobile edge caching (MEC)
- multilayer satellite network
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
    my_justification: Out of scope (GCN, not Agents / LLM)
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

# paper-0973 — Multilayer Satellite Network Collaborative Mobile Edge Caching: A GCN-Based Multi-Agent Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the explosive growth of high-definition video streaming data, a substantial increase in network traffic has ensued. The emergency of mobile edge caching (MEC) can not only alleviate the burden on core network, but also significantly improve user experience. Integrating with the MEC and satellite networks, the network is empowered popular content ubiquitously and seamlessly. Addressing the research gap between multilayer satellite networks and MEC, we study the caching placement problem in this paper. Initially, we introduce a three-layer distributed network caching management architecture designed for efficient and flexible handling of large-scale networks. Considering the constraint on satellite capacity and content propagation delay, the cache placement problem is then formulated and transformed into a markov decision process (MDP), where the content coded caching mechanism is utilized to promote the efficiency of content delivery. Furthermore, a new generic metric, content delivery cost, is proposed to elaborate the performance of caching decision in large-scale networks. Then, we introduce a graph convolutional network (GCN)-based multi-agent advantage actor-critic (A2C) algorithm to optimize the caching decision. Finally, extensive simulations are conducted to evaluate the proposed algorithm in terms of content delivery cost and transferability. © China Communications Magazine Co., Ltd.

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
- **my_justification:** "Out of scope (GCN, not Agents / LLM)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0973.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
