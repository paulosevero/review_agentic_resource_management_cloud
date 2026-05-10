---
id: paper-0551
title: UAV Assisted Cooperative Caching on Network Edge Using Multi-Agent Actor-Critic Reinforcement Learning
authors:
- Araf, Sadman
- Saha, Adittya Soukarjya
- Kazi, Sadia Hamid
- Tran, Nguyen H.
- Alam, Md. Golam Rabiul
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2023
doi: 10.1109/TVT.2022.3209079
url: https://www.scopus.com/pages/publications/85139421253?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2322--2337
keywords:
- Cooperative edge caching
- multi-acccess edge computing
- multi-agent actor-critic
- reinforcement learning
- unmanned aerial vehicle (UAV)
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

# paper-0551 — UAV Assisted Cooperative Caching on Network Edge Using Multi-Agent Actor-Critic Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent times, caching at edge nodes is a well-known technique to overcome the limitation of strict latency, which simultaneously improves users' Quality of Experience (QoE). However, choosing an appropriate caching policy and content placement poses another significant issue that has been acknowledged in this research. Conventional caching policies that are experimented with at the edge do not consider the dynamic and stochastic characteristics of edge caching. As a result, we have proposed a cooperative deep reinforcement learning algorithm that deals with the dynamic nature of content demand. It also ensures efficient use of storage through the cooperation between nodes. In addition, previous works on cooperative caching have assumed the users to be static and didn't consider the mobile nature of users. Therefore, we have proposed UAVs as aerial Base Stations (UAV-BS) to assist in peak hours where a ground base station is insufficient to support the surge in user requests. In this novel research, we have demonstrated the cooperation between aerial and Ground Base Stations (GBS) and aimed at maximizing the global cache hit ratio. Simulations have shown that our proposed Cooperative Multi-Agent Actor-Critic algorithm outperforms conventional and reinforcement learning based caching methods and achieves a state-of-the-art global cache hit ratio when there is a surge in user requests. Thus, it opens the door for further research on cooperative caching in joint air and ground architecture.  © 1967-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0551.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
