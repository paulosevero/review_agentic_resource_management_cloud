---
id: paper-0793
title: Multiagent Reinforcement Learning-Based Orbital Edge Offloading in SAGIN Supporting Internet of Remote Things
authors:
- Zhang, Senbai
- Liu, Aijun
- Han, Chen
- Liang, Xiaohu
- Xu, Xin
- Wang, Guangyu
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3287737
url: https://www.scopus.com/pages/publications/85162905708?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 20472--20483
keywords:
- Multiagent reinforcement learning (MARL)
- orbital edge computing (OEC)
- space-air-ground integrated network (SAGIN)
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

# paper-0793 — Multiagent Reinforcement Learning-Based Orbital Edge Offloading in SAGIN Supporting Internet of Remote Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We investigate a computing task scheduling problem in space-air-ground integrated network (SAGIN) for Internet of Remote Things (IoRT). In the considered scenario, the unmanned aerial vehicles (UAVs) collect computing tasks from IoRT devices and make offloading decisions, in which the tasks can be computed at the UAVs or offloaded to the low Earth orbital (LEO) satellite. The optimization objective is to design offloading strategies for each UAV that maximum the number of tasks satisfies delay constraint and reduces the energy consumption of UAVs. We formulate this problem as a nonlinear integer optimization problem, and remodel it as a stochastic game to solve it. To copy with the dynamic and complexity environment, we propose a learning-based orbital edge offloading (LOEF) approach which can coordinate all UAVs to learn the optimal offloading strategies. This method is based on the actor-critic framework of multiagent reinforcement learning, the Actor observes the environment and output the current offloading decision, the Critic evaluates the action of the Actor and coordinate the actions of all UAV to increase the reward of system. The simulation results show that the proposed offloading strategy converges fast, increases the number of satisfying the delay constraints tasks and the energy utilization of UAVs compared with the baseline strategies.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0793.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
