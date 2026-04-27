---
id: "paper-1120"
title: "Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application"
authors: ["Park, Jinhyuk", "Shim, Junki", "Lee, Gwonyeol", "Choi, Seongim"]
year: 2024
venue: "AIAA SciTech Forum and Exposition, 2024"
venue_type: "conference"
doi: "10.2514/6.2024-1711"
url: "https://www.scopus.com/pages/publications/85196214190?origin=resultslist"
publisher: "American Institute of Aeronautics and Astronautics Inc, AIAA"
pages: ""
keywords: ["Aircraft detection", "Convolution", "Flight simulators", "Long short-term memory", "Motion planning", "Multi agent systems", "Real time systems", "Reinforcement learning", "Robot programming", "Software design", "Software testing", "Collisions avoidance", "Flight test", "Flight validation", "In-flight tests", "Non-blocking", "Path planners", "Real time path planning", "Reinforcement learnings", "Route planning", "Small UAS", "Unmanned aerial vehicles (UAV)"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1120 — Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application

## Metadata

- **Authors:** Park, Jinhyuk and Shim, Junki and Lee, Gwonyeol and Choi, Seongim
- **Year:** 2024
- **Venue:** AIAA SciTech Forum and Exposition, 2024
- **DOI:** 10.2514/6.2024-1711
- **URL:** https://www.scopus.com/pages/publications/85196214190?origin=resultslist
- **Publisher:** American Institute of Aeronautics and Astronautics Inc, AIAA
- **Pages:** 
- **Language:** English
- **Keywords:** Aircraft detection; Convolution; Flight simulators; Long short-term memory; Motion planning; Multi agent systems; Real time systems; Reinforcement learning; Robot programming; Software design; Software testing; Collisions avoidance; Flight test; Flight validation; In-flight tests; Non-blocking; Path planners; Real time path planning; Reinforcement learnings; Route planning; Small UAS; Unmanned aerial vehicles (UAV)

### Abstract

This study focused on the application and verification of real-time path planning and execution in flight test of UAVs using the deep neural network (DRL). The real-time path planner that have been developed takes into the input the ego UAV's current position, the position of obstacles, and destination information, then determines the UAV's next position. This path planner utilizes the deep reinforcement learning techniques, such as Proximal Policy Optimization (PPO) and Twin Delayed Deep Deterministic Policy Gradient (TD3). It also uses the Long Short-Term Memory (LSTM) network to predict the other UAVs trajectories for more stable route planning. Different types of data communication are developed and tested in flight test: blocking vs. non-blocking, and synchronous vs. asynchronous. It was demonstrated that the flexibility to unexpected changes in environment is greater with the non-blocking and asynchronous communication. In addition, distinctively different operation methods of the central vs. distributed approaches are developed, which have different authority in who makes a decision on the collision detection and the optimal route planning. The distributed operation value a preference of an individual UAV, but requires the powerful edge computing capability in timely data communication and efficient optimization algorithm to minimize flight time. The deep reinforcement learning methods were employed for the optimal path planning with collision avoidance, and validated through software simulation as well as outdoor flight tests. The multi-agent tests were implemented using two UAVs with a communication system with Robot Operating System2 (ROS2). Flight test results validate a series of operation concepts introduced in the present study by performance metric of accuracy in target tracking and collision avoidance. © 2024 by the American Institute of Aeronautics and Astronautics, Inc. All rights reserved.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning based Real-Time Path Planning and Flight Validation of small UAS Application
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
