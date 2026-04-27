---
id: "paper-2712"
title: "RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design"
authors: ["Manjunath, T.C.", "Sreerama, M.P.", "Shrivatsa, K.S.", "Khanam, Tanzila", "Modi, Nandini", "Balakrishna, R."]
year: 2026
venue: "7th International Conference on Mobile Computing and Sustainable Informatics, ICMCSI 2026"
venue_type: "conference"
doi: "10.1109/ICMCSI67283.2026.11412692"
url: "https://www.scopus.com/pages/publications/105034864460?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "885--891"
keywords: ["Adaptive Systems", "Deep Reinforcement Learning", "Kernel Scheduling", "Lock-Free Algorithms", "Memory Allocation", "NUMA", "Operating Systems", "Q-Learning", "Rust", "VRRP"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2712 — RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design

## Metadata

- **Authors:** Manjunath, T.C. and Sreerama, M.P. and Shrivatsa, K.S. and Khanam, Tanzila and Modi, Nandini and Balakrishna, R.
- **Year:** 2026
- **Venue:** 7th International Conference on Mobile Computing and Sustainable Informatics, ICMCSI 2026
- **DOI:** 10.1109/ICMCSI67283.2026.11412692
- **URL:** https://www.scopus.com/pages/publications/105034864460?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 885--891
- **Language:** English
- **Keywords:** Adaptive Systems; Deep Reinforcement Learning; Kernel Scheduling; Lock-Free Algorithms; Memory Allocation; NUMA; Operating Systems; Q-Learning; Rust; VRRP

### Abstract

The current OS uses the stationary heuristic methods & are set-up systematically while designing the system for handling of the CPU schedules & allocating of memories. These heuristics fundamentally fail under the different dynamically shifting workloads characteristic of current data centres, where batch processing, real-time analytics, and interactive applications coexist. This paper introduces RATM (Resource-Aware Adaptive Task Manager), an innovative'Authoritative Controller'architecture developed in Rust that substitutes static policies with a Deep Q-Network (DQN) reinforcement learning agent capable of optimising kernel behaviour during runtime. Our system has a rigorous Policy-Mechanism Separation. The model-free DQN agent watches the system state all the time and chooses actions. The VRRP (Varying Response Ratio Priority) Scheduler and NAAT (NUMA-Aware Adaptive Tiered) Allocator, on the other hand, are passive, configurable mechanisms that carry out commands. The RATM controller acts as a middleman between these layers, making sure that safety rules are followed and turning abstract actions into real API calls. The experimental results show that our RL-driven kernel cuts the average wait time in calibration scenarios by more than 70% compared to the static baseline, while still being very fair. The RL agent learns to proactively activate NUMA page migrations during workload phase changes, which 'flattens the curve' of latency spikes that are common in traditional schedulers. Results shows the power of methodology presented here. © 2026 IEEE.

## 04 — Title Screening

**Title:** RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
