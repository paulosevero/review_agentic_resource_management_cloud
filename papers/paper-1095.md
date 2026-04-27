---
id: "paper-1095"
title: "FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network"
authors: ["Nagabushnam, Ganesan", "Choi, Yundo", "Kim, Kyong Hoon"]
year: 2024
venue: "2024 9th International Conference on Fog and Mobile Edge Computing, FMEC 2024"
venue_type: "conference"
doi: "10.1109/FMEC62297.2024.10710250"
url: "https://www.scopus.com/pages/publications/85208137483?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "46--53"
keywords: ["Aperiodic task", "Cloud Computing", "Deadline", "Fog computing", "Heterogeneous", "Multi-Agent Reinforcement Learning", "Proximal Policy Optimization", "Recurrent Neural Network", "Task scheduling"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1095 — FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network

## Metadata

- **Authors:** Nagabushnam, Ganesan and Choi, Yundo and Kim, Kyong Hoon
- **Year:** 2024
- **Venue:** 2024 9th International Conference on Fog and Mobile Edge Computing, FMEC 2024
- **DOI:** 10.1109/FMEC62297.2024.10710250
- **URL:** https://www.scopus.com/pages/publications/85208137483?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 46--53
- **Language:** English
- **Keywords:** Aperiodic task; Cloud Computing; Deadline; Fog computing; Heterogeneous; Multi-Agent Reinforcement Learning; Proximal Policy Optimization; Recurrent Neural Network; Task scheduling

### Abstract

In heterogeneous fog-cloud computing networks, efficiently scheduling aperiodic tasks is an NP-hard problem, particularly when aiming to minimize makespan, adhere to deadlines, and conserve energy. This paper introduces a novel scheduling algorithm, Fog-Optimized Deadline-Adaptive Scheduling (FODAS), which combines Earliest Deadline First (EDF) principles with Deep Multi-Agent Reinforcement Learning, incorporating Proximal Policy Optimization (PPO) and Recurrent Neural Networks (RNN). FODAS is specifically designed to manage aperiodic tasks in heterogeneous fog-cloud environments, prioritizing deadline adherence and energy efficiency. The proposed algorithm begins by collecting tasks into a global scheduling queue, and sorting them by their deadlines. It incorporates three homogeneous schedulers within a heterogeneous framework, ensuring tasks meet their deadlines and achieve notable energy savings. Key performance metrics such as deadline meeting rate, makespan, and energy savings are evaluated, comparing FODAS against single-Agent reinforcement learning algorithms such as PPO and Asynchronous Advantage Actor-Critic (A3C). Our findings reveal that FODAS significantly improves the rate of meeting deadlines by up to 18% compared to the conventional algorithms. Additionally, it delivers substantial energy savings, with improvements of up to 80% in certain setups, and markedly decreases makespan, achieving reductions of up to 57.3% compared to traditional algorithms. The proposed algorithm also demonstrates exceptional operational efficiency, reducing the time required for scheduling tasks, particularly in high-density node networks. These results underscore the effectiveness of FODAS in managing complex task scheduling within fog-cloud computing environments. © 2024 IEEE.

## 04 — Title Screening

**Title:** FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** FODAS: A Novel Reinforcement Learning Approach for Efficient Task Scheduling in Fog Computing Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
