---
id: paper-1120
title: Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application
authors:
- Park, Jinhyuk
- Shim, Junki
- Lee, Gwonyeol
- Choi, Seongim
venue: AIAA SciTech Forum and Exposition, 2024
venue_type: conference
year: 2024
doi: 10.2514/6.2024-1711
url: https://www.scopus.com/pages/publications/85196214190?origin=resultslist
publisher: American Institute of Aeronautics and Astronautics Inc, AIAA
pages: ''
keywords:
- Aircraft detection
- Convolution
- Flight simulators
- Long short-term memory
- Motion planning
- Multi agent systems
- Real time systems
- Reinforcement learning
- Robot programming
- Software design
- Software testing
- Collisions avoidance
- Flight test
- Flight validation
- In-flight tests
- Non-blocking
- Path planners
- Real time path planning
- Reinforcement learnings
- Route planning
- Small UAS
- Unmanned aerial vehicles (UAV)
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
    proposed_decision: Exclude
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
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

# paper-1120 — Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This study focused on the application and verification of real-time path planning and execution in flight test of UAVs using the deep neural network (DRL). The real-time path planner that have been developed takes into the input the ego UAV's current position, the position of obstacles, and destination information, then determines the UAV's next position. This path planner utilizes the deep reinforcement learning techniques, such as Proximal Policy Optimization (PPO) and Twin Delayed Deep Deterministic Policy Gradient (TD3). It also uses the Long Short-Term Memory (LSTM) network to predict the other UAVs trajectories for more stable route planning. Different types of data communication are developed and tested in flight test: blocking vs. non-blocking, and synchronous vs. asynchronous. It was demonstrated that the flexibility to unexpected changes in environment is greater with the non-blocking and asynchronous communication. In addition, distinctively different operation methods of the central vs. distributed approaches are developed, which have different authority in who makes a decision on the collision detection and the optimal route planning. The distributed operation value a preference of an individual UAV, but requires the powerful edge computing capability in timely data communication and efficient optimization algorithm to minimize flight time. The deep reinforcement learning methods were employed for the optimal path planning with collision avoidance, and validated through software simulation as well as outdoor flight tests. The multi-agent tests were implemented using two UAVs with a communication system with Robot Operating System2 (ROS2). Flight test results validate a series of operation concepts introduced in the present study by performance metric of accuracy in target tracking and collision avoidance. © 2024 by the American Institute of Aeronautics and Astronautics, Inc. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1120.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
