---
id: paper-0459
title: 'Cooperative Multiagent Deep Reinforcement Learning for Computation Offloading: A Mobile Network Operator Perspective'
authors:
- Li, Kexin
- Wang, Xingwei
- He, Qiang
- Yi, Bo
- Morichetta, Andrea
- Huang, Min
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3189445
url: https://www.scopus.com/pages/publications/85135220830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 24161--24173
keywords:
- Computational offloading
- deep reinforcement learning (DRL)
- delay bounds
- mobile-edge computing (MEC)
- task revenue
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

# paper-0459 — Cooperative Multiagent Deep Reinforcement Learning for Computation Offloading: A Mobile Network Operator Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Computation offloading decisions play a crucial role in implementing mobile-edge computing (MEC) technology in the Internet of Things (IoT) services. Mobile network operators (MNOs) can employ computation offloading techniques to reduce task completion delay and improve the Quality of Service (QoS) for users by optimizing the system's processing delay and energy consumption. However, different IoT applications (e.g., entertainment and autonomous driving) generate different delay tolerances and benefits for computational tasks from the MNO perspective. Therefore, simply minimizing the delay of all tasks does not satisfy the QoS of each user. The system architecture design should consider the significance of users and the heterogeneity of tasks. Unfortunately, rare work has been done to discuss this practical issue. In this article, from the perspective of MNO, we investigate the computation offloading optimization problem of multiuser delay-sensitive tasks. First, we propose a new optimization model, which designs different optimization objectives for the cost and revenue of tasks. Then, we transform the problem into a Markov decision processes problem, which leads to designing a multiagent iterative optimization framework. For the strategic optimization of each agent, we further propose a cooperative multiagent deep reinforcement learning (CMDRL) algorithm to optimize two different objectives at the same time. Two agents are integrated into the CMDRL framework to enable agents to collaborate and converge to the global optimum in a distributed manner. At the same time, the priority experience replay method is introduced to improve the utilization rate of effective samples and the learning efficiency of the algorithm. The experimental results show that our proposed method can effectively achieve a significantly higher profit than the alternative state-of-the-art method and exhibit a more favorable computational performance than benchmark deep reinforcement learning methods.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0459.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
