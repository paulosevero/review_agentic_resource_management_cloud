---
id: paper-0305
title: Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing
authors:
- Kim, Yohan
- Lim, Hyuk
venue: IEEE Access
venue_type: journal
year: 2021
doi: 10.1109/ACCESS.2021.3072435
url: https://www.scopus.com/pages/publications/85104255617?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 56178--56190
keywords:
- 5G
- multi-access edge computing
- multi-agent reinforcement learning
- network resource management
- network slicing
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0305 — Multi-Agent Reinforcement Learning-Based Resource Management for End-to-End Network Slicing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To meet the explosive growth of mobile traffic, the 5G network is designed to be flexible and support multi-access edge computing (MEC), thereby improving the end-to-end quality of service (QoS). In particular, 5G network slicing, which allows a physical infrastructure to split into multiple logical networks, keeps the balance of network resource allocation among different service types with on-demand resource requests. However, achieving effective resource allocation across the end-to-end network is difficult due to the dynamic characteristics of slicing requests such as uncertain real-time resource demand and heterogeneous requirements. In this paper, we develop a reinforcement learning (RL)-based dynamic resource allocation framework for end-to-end network slicing with heterogeneous requirements in multi-layer MEC environments. We first design a hierarchical MEC architecture and formulate a resource allocation problem for the end-to-end network slicing as an optimization problem using the Markov decision process (MDP). Using proximal policy optimization (PPO), we develop independently-collaborative and jointly-collaborative dynamic resource allocation algorithms to maximize resource efficiency while satisfying the QoS of slices. Experimental results show that the proposed algorithms can recognize the characteristics of slice requests and coming resource demands and efficiently allocate resources with a high QoS satisfaction rate.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0305.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
