---
id: paper-0222
title: Multi-agent reinforcement learning for resource allocation in IoT networks with edge computing
authors:
- Liu, Xiaolan
- Yu, Jiadong
- Feng, Zhiyong
- Gao, Yue
venue: China Communications
venue_type: journal
year: 2020
doi: 10.23919/JCC.2020.09.017
url: https://www.scopus.com/pages/publications/85094913898?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 220--236
keywords:
- edge computing
- internet of things
- multi-agent reinforcement learning
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

# paper-0222 — Multi-agent reinforcement learning for resource allocation in IoT networks with edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To support popular Internet of Things (IoT) applications such as virtual reality and mobile games, edge computing provides a front-end distributed computing archetype of centralized cloud computing with low latency and distributed data processing. However, it is challenging for multiple users to offload their computation tasks because they are competing for spectrum and computation as well as Radio Access Technologies (RAT) resources. In this paper, we investigate computation offloading mechanism of multiple selfish users with resource allocation in IoT edge computing networks by formulating it as a stochastic game. Each user is a learning agent observing its local network environment to learn optimal decisions on either local computing or edge computing with a goal of minimizing long term system cost by choosing its transmit power level, RAT and sub-channel without knowing any information of the other users. Since users' decisions are coupling at the gateway, we define the reward function of each user by considering the aggregated effect of other users. Therefore, a multi-agent reinforcement learning framework is developed to solve the game with the proposed Independent Learners based Multi-Agent Q-learning (IL-based MA-Q) algorithm. Simulations demonstrate that the proposed IL-based MA-Q algorithm is feasible to solve the formulated problem and is more energy efficient without extra cost on channel estimation at the centralized gateway. Finally, compared with the other three benchmark algorithms, it has better system cost performance and achieves distributed computation offloading.  © 2013 China Institute of Communications.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0222.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
