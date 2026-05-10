---
id: paper-1000
title: Multiagent Reinforcement Learning in Controlling Offloading Ratio and Trajectory for Multi-UAV Mobile-Edge Computing
authors:
- Lee, Wonseok
- Kim, Taejoon
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2023.3296774
url: https://www.scopus.com/pages/publications/85165254042?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3417--3429
keywords:
- Deep reinforcement learning (DRL)
- mobile-edge computing (MEC)
- task offloading
- trajectory design
- unmanned aerial vehicles (UAVs)
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

# paper-1000 — Multiagent Reinforcement Learning in Controlling Offloading Ratio and Trajectory for Multi-UAV Mobile-Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this article, a multiunmanned aerial vehicle-mobile-edge computing (UAV-MEC) network is proposed for mobile devices (MDs) located far from a terrestrial base station (BS)-MEC. In the UAV-MEC network, the MDs offload tasks to the UAV-MECs, followed by task offloading from the UAV-MECs to the BS-MEC. Each UAV-MEC aims to jointly optimize its energy consumption, queue stability, and the energy consumption of the MDs by controlling its trajectory and offloading ratio. Specifically, the trajectories of the UAV-MECs are controlled to locate themselves at the optimal positions where the transmission energy of the MDs is minimized. Additionally, the UAV-MECs consider the constraints of task processing time and queue stability in determining the amount of task to be offloaded. Thus, an independent proximal policy optimization (IPPO)-based offloading and trajectory control learning model (IM) is proposed to solve these problems, and a convex optimization model (CM) is also presented to show the optimality of the proposed IM. Specifically, in IM, a near-optimal trajectory control for the randomly located MDs is enabled by exploiting channel gain information only without resorting to accurate location information of the MDs. Furthermore, a dynamic offloading ratio control of each UAV-MEC is achieved by considering its queue dynamics. The simulation results show that the proposed IM jointly optimizes energy consumption and queue stability. Consequently, it outperforms other deep reinforcement learning (DRL)-based algorithms by achieving low energy consumption and long service duration. Moreover, it achieves similar performance to CM while requiring remarkably less time on action decision.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1000.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
