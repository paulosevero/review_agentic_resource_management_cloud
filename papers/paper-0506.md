---
id: paper-0506
title: Joint Optimization for MEC Computation Offloading and Resource Allocation in IoV Based on Deep Reinforcement Learning
authors:
- Wang, Jian
- Wang, Yancong
- Ke, Hongchang
venue: Mobile Information Systems
venue_type: journal
year: 2022
doi: 10.1155/2022/9230521
url: https://www.scopus.com/pages/publications/85136580700?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- computation offloading
- Deep learning
- Multi agent systems
- Reinforcement learning
- Resource allocation
- Stochastic systems
- Computation offloading
- Computation resources
- Computation tasks
- Computing capacity
- Computing resource
- Edge computing
- Joint optimization
- Multiaccess
- Reinforcement learnings
- Resources allocation
- Vehicles
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0506 — Joint Optimization for MEC Computation Offloading and Resource Allocation in IoV Based on Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the Internet of Vehicle (IoV), the limited computing capacity of vehicles hardly processes the intensive computation tasks locally. The computation tasks can be offloaded to multiaccess edge computing (MEC) servers for processing, where MEC provides the required computing capacity to the nearby vehicles. In this paper, we consider a scenario where there are cooperation and competition between vehicles, the offloading decision of any vehicle will affect the decisions of the others, and the computing resource allocation strategies by MEC will dynamically change. Therefore, we propose a joint optimization scheme for computation offloading decisions and computing resource allocation based on decentralized multiagent deep reinforcement learning. The proposed scheme learns the optimal actions to minimize the total weighted cost which is designed as the vehicles' satisfaction based on the type of stochastic arrival tasks and dynamic interaction between MEC server and vehicles within different RSUs coverages. The numerical results show that the proposed algorithms based on decentralized multiagent deep deterministic policy gradient (DDPG) which is named De-DDPG can autonomously learn the optimal computation offloading and resource allocation policy without a priori knowledge and outperform the other three baseline algorithms in terms of the rewards.  © 2022 Jian Wang et al.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0506.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
