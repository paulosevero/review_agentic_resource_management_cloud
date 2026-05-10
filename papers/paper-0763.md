---
id: paper-0763
title: Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning
authors:
- Xu, Chi
- Tang, Zixuan
- Yu, Haibin
- Zeng, Peng
- Kong, Linghe
venue: IEEE Journal on Selected Areas in Communications
venue_type: journal
year: 2023
doi: 10.1109/JSAC.2023.3310066
url: https://www.scopus.com/pages/publications/85169672081?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3056--3069
keywords:
- collaborative scheduling
- Digital twin
- edge computing
- multi-Agent deep reinforcement learning
- task offloading
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

# paper-0763 — Digital Twin-Driven Collaborative Scheduling for Heterogeneous Task and Edge-End Resource via Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the interdisciplinary advances of mobile communication and edge computing, massive heterogeneous tasks are accessing wireless networks and competing for the edge-end computing and communication resources. Digital twin (DT), which establishes the digital models of physical objects for simulation, analysis and optimization, provides a promising method for network scheduling and management. This paper proposes a DT-driven edge-end collaborative scheduling algorithm for heterogeneous tasks and heterogeneous computing/communication resources. Specifically, multiple end devices (EDs) cooperate with each other to accomplish a complex job, where each ED can offload individual task to multiple edge servers (ESs) for parallel computing. By fully considering deadline requirements of heterogeneous tasks, maximum computing capabilities of ESs and EDs, computing resource estimation deviations of DT, maximum transmit powers of EDs and tolerable peak interference powers to coexisting EDs, we formulate a job completion time minimization problem to jointly optimize the edge-end task division, transmit power control, computing resource type matching and allocation. To solve this non-convex problem, we first reformulate it by multi-Agent Markov decision process, where a compound reward leveraging latency reward and deadline reward according to the task criticality is designed. Then, we propose a multi-Agent deep reinforcement learning-based scheduling algorithm, where Actor-Critic framework with estimation and target networks is designed for policy and value iterations. Meanwhile, a step-by-step-greedy algorithm is proposed to balance exploration and exploitation, avoiding local optimal trap. Through offline centralized training by DT and online distributed execution by EDs, we realize edge-end collaborative computing for heterogeneous tasks. Experimental results demonstrate that, comparing with typical benchmark algorithms, the proposed algorithm converges with the highest reward and achieves the smallest job completion time, where the deadlines of heterogeneous tasks can be well satisfied respectively.  © 1983-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0763.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
