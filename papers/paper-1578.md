---
id: paper-1578
title: 'End-Edge-Cloud Collaborative Offloading of Splittable Tasks in Internet of Vehicles: A Multi-Agent Reinforcement Learning Approach with Group Updating'
authors:
- Gao, Zhenguo
- Fan, Weiwei
- Zhang, Jiahui
- Ye, Wenhui
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3619438
url: https://www.scopus.com/pages/publications/105018521630?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Internet of vehicles
- Multi-agent deep reinforcement learning
- Stackelberg game
- Task splitting
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

# paper-1578 — End-Edge-Cloud Collaborative Offloading of Splittable Tasks in Internet of Vehicles: A Multi-Agent Reinforcement Learning Approach with Group Updating

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of intelligent transportation and the exponential growth of data traffic drive the emerging of more computation-intensive latency-critical tasks in vehicles, bring challenges to the task offloading research in the Internet of vehicles, which provides vehicles with ultralow-latency task processing services via offloading tasks to Edge Servers (ESs) and Cloud Servers (CSs). Focusing on offloading splittable tasks, an end-edge-cloud cooperative splittable task offloading framework is presented for IoV, where vehicles with idle resources are regarded as temporary edge servers for complementing the computing services of CSs and ESs. Then, we propose a multiagent deep deterministic policy gradient algorithm to minimize task completion latency by making comprehensive decisions jointly involving task splitting, communication, and computation resource allocation. Furthermore, we propose a group-based random updating strategy for multi-agent deep reinforcement model training to promote training efficiency. To incentivize Highperformance Vehicles (HVs) to offer edge computing services via sharing their spare computation resources, we construct a Multi-Leader Multi-Follower Stackelberg incentive game model where CSs act as leaders and HVs act as followers. We prove the existence of a Stackelberg equilibrium point, and propose an optimal dynamic response algorithm to drive the CSs' resource renting price decisions and the HVs' resource sharing amount decisions to arrive at the SE point via multi-round negotiations. Simulation results demonstrate the superiority of the proposed algorithm over some selected benchmark algorithms.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1578.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
