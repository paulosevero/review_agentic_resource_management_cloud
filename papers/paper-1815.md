---
id: paper-1815
title: 'Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach'
authors:
- Li, Zixin
- Liang, Xin
- Liu, Juan
- He, Xiaofan
- Xie, Lingfu
- Qu, Long
- Feng, Guinian
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3580468
url: https://www.scopus.com/pages/publications/105009599205?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 35756--35772
keywords:
- Mobile-edge computing (MEC)
- multiagent deep reinforcement learning (MARL)
- uncrewed aerial vehicle (UAV)
- virtual reality (VR)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1815 — Optimizing Mobile-Edge Computing for Virtual Reality Rendering via UAVs: A Multiagent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Virtual reality (VR) demands extensive computation while imposing strict requirements for ultralow latency, placing a significant burden on wireless communication systems. In recent years, there has been a growing interest in leveraging uncrewed aerial vehicle (UAV)-assisted mobile-edge computing (MEC) as a promising technology to provide flexible computing resources at the edge of wireless networks. To meet the computational demands of VR, we propose a collaborative three-layer edge computing framework assisted by multiple UAVs. This framework enables VR rendering tasks to be executed locally on user devices or offloaded to UAVs and base station (BS) for execution. By jointly optimizing the flight trajectories of UAVs and the rendering modes of users, we aim to maximize the average rendering completion rate, defined as the ratio of successfully completed VR rendering tasks within the specified delay constraints, while minimizing the average energy consumption of UAVs. To enhance adaptability, we adopt a multiagent twin delayed deep deterministic policy gradient (MATD3) approach that provides an efficient strategy for multi-UAV-assisted VR rendering, even in partially observable scenarios. Simulation results validate our proposed approach and demonstrate that the MATD3 algorithm surpasses the classical multiagent deep deterministic policy gradient (MADDPG) algorithm in terms of convergence speed and the average rendering completion rate. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1815.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
