---
id: paper-2185
title: Multi-Agent Q-Net Enhanced Coevolutionary Algorithm for Resource Allocation in Emergency Human-Machine Fusion UAV-MEC System
authors:
- Sun, Lu
- Liu, Ziqian
- Ning, Zhaolong
- Wang, Jie
- Fu, Xianping
venue: IEEE Transactions on Automation Science and Engineering
venue_type: journal
year: 2025
doi: 10.1109/TASE.2024.3409551
url: https://www.scopus.com/pages/publications/85197656594?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4473--4489
keywords:
- cooperative genetic algorithm
- emergency environment
- Human-machine fusion UAV-MEC
- reinforcement learning
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

# paper-2185 — Multi-Agent Q-Net Enhanced Coevolutionary Algorithm for Resource Allocation in Emergency Human-Machine Fusion UAV-MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV) assisted communication has emerged as a powerful technology for reliable and flexible emergency communications (e.g., earthquakes, hurricanes and floods), especially when the mobile infrastructure is seriously damaged. UAV assisted mobile edge computing (UAV-MEC) system can be deployed in the natural disaster area as communication relay or air mobile base stations to resume communication and provide computing resources for the users in disaster areas. However, the optimized resource allocation performance of UAV-MEC system can be further guaranteed with the human-fusion decision making. In this paper, we construct an emergency human-machine fusion UAV-MEC system consisting of multiple UAVs equipped with computing resources, and the human-machine decision makings are fused for UAV deployment. In order to solve the resource allocation problem of human-machine fusion UAV-MEC system, we establish an human-machine deep integration model for UAV-MEC system, and the UAVs are dispatched reasonably through human-machine fusion decision makings to maintain efficient communication in emergency communication areas. To minimize task latency and improve the computation efficiency in emergency human-machine fusion UAV-MEC system, we consider the number of dispatched UAVs, deployment plans, flight plans, and simultaneously optimize the task allocation scheme, priority order, and task offloading ratio. We propose a reinforcement learning framework combined with evolutionary algorithms, which is named as multi-agent Q-net enhanced cooperative genetic algorithm (MQCGA), for resource allocation of UAV. Based on neural network forecasts, the greedy rate during training processing can be dynamically controlled, and the learning ability of different agents can be strengthened. Simulation experiments are conducted to evaluate the proposed framework, and the results show that our proposed MQCGA algorithm is significantly superior to other algorithms in terms of latency and energy consumption. Note to Practitioners - With the development of MEC and the popularity of UAVs, the potential of UAV-assisted MEC draw much attention from industrial field. Considering the lack of communication capabilities in a certain area in an unexpected situation, UAVs can be quickly deployed to corresponding locations and provide computing services. In this paper, an UAV-MEC system that integrates human-machine decision-making for emergency communication situations, named human-machine fusion UAV-MEC system, is considered. The system divides the scene into regions, models users and UAVs, and provides detailed deployment schemes, maximizing the practicality and applicability of the scene. In order to improve the communication efficiency in the case of emergency communication, this paper proposes a new resource scheduling algorithm and adds human-machine decision-making to enable UAVs to continuously provide efficient services for a certain area. The experimental results provide practitioners with a theoretical basis, such as the task completion time, UAV energy consumption and computing resource scheduling. Applying the system to actual scenarios also requires two preconditions of the system, one is the information collected by the large UAV, and the other is the communication among the UAVs. These two preconditions facilitate the human-machine fusion UAV-MEC system deployment in practical applications.  © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2185.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
