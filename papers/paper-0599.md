---
id: paper-0599
title: Blockchain-Based Collaborative Caching for Multi-edge Server Video Streaming; [区 块 链 辅 助 的 多 边 缘 服 务 器 协 作 视 频 流 缓 存 优 化 策 略]
authors:
- Guo, Yongan
- Zhou, Yi
- Wang, Quan
- Wang, Yuao
- Cheng, Yao
- Zhu, Hao
venue: Shuju Caiji Yu Chuli/Journal of Data Acquisition and Processing
venue_type: journal
year: 2023
doi: 10.16337/j.1004-9037.2023.06.011
url: https://www.scopus.com/pages/publications/85179742524?origin=resultslist
publisher: Nanjing University of Aeronautics an Astronautics
pages: 1353--1368
keywords:
- blockchain
- collaborative caching
- edge computing
- multi-agent deep reinforcement learning
- video streaming
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0599 — Blockchain-Based Collaborative Caching for Multi-edge Server Video Streaming; [区 块 链 辅 助 的 多 边 缘 服 务 器 协 作 视 频 流 缓 存 优 化 策 略]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the growth of Internet video traffic and the improvement of user requirements for experience quality， the traditional backbone network is facing great pressure. Moving edge cache technology can reduce latency，reduce backhaul link load，and improve video user experience quality. However，the finiteness of edge server cache resources，the dynamic nature of video requests，and the attention of users to the security of cached data pose new challenges to the research of edge cache strategy. To solve the above problems，this paper proposes a blockchain-assisted multi-edge server collaborative video stream cache optimization scheme. This paper constructs a four-layer network architecture composed of content delivery network（CDN）server，edge server，user device，and blockchain. We introduce the blockchain consensus mechanism to protect the charging video with insensitive request delay and ensure the data security of users. Based on the three-layer cache mechanism of local hit，proximity hit and CDN hit，the collaborative cache among edge servers is further strengthened by defining proximity hit reward factors，and the cache hit ratio of edge servers is improved. In this paper，we jointly consider the state of edge servers，the change in content popularity，and the resource allocation of cooperative cache among multi-edge servers. By establishing the minimum access latency，traffic cost，and system energy consumption optimization problem. The cooperative cache optimization algorithm of multi-agent proximal policy optimization（MAPPO）is used to solve the problem. The simulation results show that compared with the existing caching strategies，the proposed scheme can effectively improve the cache hit rate of video streaming and reduce energy consumption and delay. 2023 by Journal of Data Acquisition and Processing.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0599.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
