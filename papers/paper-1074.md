---
id: paper-1074
title: Collaborative Resource Allocation for Blockchain-Enabled Internet of Things with Multi-Agent Deep Reinforcement Learning
authors:
- Lu, Xinyu
- Wan, Jianxiong
- Li, Leixiao
- Liu, Chuyi
- Si, Xiaowei
venue: Conference Proceedings - IEEE International Conference on Systems, Man and Cybernetics
venue_type: conference
year: 2024
doi: 10.1109/SMC54092.2024.10830981
url: https://www.scopus.com/pages/publications/85217835149?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3583--3588
keywords:
- Deep reinforcement learning
- Markov processes
- Mobile edge computing
- Block-chain
- Collaborative resources
- Edge computing
- Multi agent
- Network edges
- Quality-of-service
- Rapid growth
- Reinforcement learnings
- Resources allocation
- Service latency
- Quality of service
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

# paper-1074 — Collaborative Resource Allocation for Blockchain-Enabled Internet of Things with Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) reduces service latency and enhances Quality of Service (QoS) by offloading tasks to the wireless network edge. However, the rapid growth of task offloading and the associated data transmission security challenges deserve further investigation. This study proposes a blockchain-MEC hybrid solution where mobile devices process tasks and engage in block mining to boost system utility. The objective is to maximize the accumulated reward in the blockchain-MEC system by optimizing off loading decisions, channel selection, transmission power, computing resources, and block intervals. A Markov Decision Process is formulated to model the optimization problem which is solved via a multi-agent deep reinforcement learning (MADRL) algorithm. The results of the simulation demonstrate that our approach is more effective than the baseline method. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1074.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
