---
id: paper-0897
title: 'Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach'
authors:
- Ejaz, Muhammad Asim
- Wu, Guowei
- Ahmed, Adeel
- Iftikhar, Saman
- Bawazeer, Shaikhan
venue: Sensors
venue_type: journal
year: 2024
doi: 10.3390/s24175558
url: https://www.scopus.com/pages/publications/85203879202?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- deep reinforcement learning (DRL)
- end-to-end network slicing
- Internet of Things (IoT)
- mobile edge computing (MEC)
- multi-agent
- utility optimization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0897 — Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) is crucial for reducing latency by bringing computational resources closer to the network edge, thereby enhancing the quality of services (QoS). However, the broad deployment of cloudlets poses challenges in efficient network slicing, particularly when traffic distribution is uneven. Therefore, these challenges include managing diverse resource requirements across widely distributed cloudlets, minimizing resource conflicts and delays, and maintaining service quality amid fluctuating request rates. Addressing this requires intelligent strategies to predict request types (common or urgent), assess resource needs, and allocate resources efficiently. Emerging technologies like edge computing and 5G with network slicing can handle delay-sensitive IoT requests rapidly, but a robust mechanism for real-time resource and utility optimization remains necessary. To address these challenges, we designed an end-to-end network slicing approach that predicts common and urgent user requests through T distribution. We formulated our problem as a multi-agent Markov decision process (MDP) and introduced a multi-agent soft actor–critic (MAgSAC) algorithm. This algorithm prevents the wastage of scarce resources by intelligently activating and deactivating virtual network function (VNF) instances, thereby balancing the allocation process. Our approach aims to optimize overall utility, balancing trade-offs between revenue, energy consumption costs, and latency. We evaluated our method, MAgSAC, through simulations, comparing it with the following six benchmark schemes: MAA3C, SACT, DDPG, S2Vec, Random, and Greedy. The results demonstrate that our approach, MAgSAC, optimizes utility by 30%, minimizes energy consumption costs by 12.4%, and reduces execution time by 21.7% compared to the closest related multi-agent approach named MAA3C. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0897.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
