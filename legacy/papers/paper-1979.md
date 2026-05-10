---
id: "paper-1979"
title: "Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks"
authors: ["Nagabushnam, Ganesan", "Kim, Kyong Hoon"]
year: 2025
venue: "Cluster Computing"
venue_type: "journal"
doi: "10.1007/s10586-025-05435-5"
url: "https://www.scopus.com/pages/publications/105008077643?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Aperiodic", "Asynchronous advantage actor-critic", "Cloud", "Deadline task", "Deep multi-agent reinforcement learning", "Heterogeneous fog", "IoT", "Task scheduling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1979 — Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks

## Metadata

- **Authors:** Nagabushnam, Ganesan and Kim, Kyong Hoon
- **Year:** 2025
- **Venue:** Cluster Computing
- **DOI:** 10.1007/s10586-025-05435-5
- **URL:** https://www.scopus.com/pages/publications/105008077643?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Aperiodic; Asynchronous advantage actor-critic; Cloud; Deadline task; Deep multi-agent reinforcement learning; Heterogeneous fog; IoT; Task scheduling

### Abstract

Fog computing has become essential for real-time applications in domains such as autonomous driving, smart cities, Industry 4.0, and large-scale IoT ecosystems, where low latency and efficient resource utilization are critical. However, scheduling aperiodic tasks in fog environments remains a significant challenge, particularly when ensuring strict deadline adherence, energy efficiency, and optimized use of heterogeneous low-power devices. This challenge is further intensified by the dynamic and unpredictable nature of fog networks, making the problem NP-hard. To address these issues, we propose FADDEER (fog adaptive deadline-driven energy efficient reinforcement), a novel deep multi-agent reinforcement learning (Deep MARL)-based scheduling algorithm that integrates earliest deadline first (EDF) and asynchronous advantage actor-critic (A3C) to enable adaptive, scalable, and deadline-aware task scheduling. FADDEER intelligently allocates aperiodic tasks to distributed fog nodes, dynamically balancing task makespan, energy consumption, and resource utilization. Experiments were conducted using the COSCO simulation framework with workloads ranging from 100 to 1,000 aperiodic tasks distributed across fog networks of 10 to 100 nodes, respectively. The results demonstrate that FADDEER consistently outperforms state-of-the-art algorithms, including A3C, multi-agent deep deterministic policy gradient (MADDPG), genetic algorithm, particle swarm optimization (PSO), EDF achieving up to 4% higher deadline adherence and up to 55% lower energy consumption compared to the next best alternatives. Moreover, FADDEER achieved up to 19.4% lower makespan under high task loads and significantly reduced scheduling time, validating its efficiency and responsiveness in dynamic fog environments. These outcomes highlight FADDEER’s robustness, scalability, and effectiveness for real-time IoT task scheduling in fog computing frameworks. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

## 04 — Title Screening

**Title:** Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Faddeer: a deep multi-agent reinforcement learning-based scheduling algorithm for aperiodic tasks in heterogeneous fog computing networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
