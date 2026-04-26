---
id: "paper-216"
title: "Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning"
authors: ["Li, Shilu", "Li, Baogang", "Zhao, Wei"]
year: 2020
venue: "IEEE Access"
venue_type: "journal"
doi: "10.1109/ACCESS.2020.3002895"
url: "https://www.scopus.com/pages/publications/85087627827?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "112762--112771"
keywords: ["caching", "Mobile edge computing (MEC)", "multi-agent Deep-Q-network (MADQN)", "non-orthogonal multiple access (NOMA)"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-216 — Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning

## Metadata

- **Authors:** Li, Shilu and Li, Baogang and Zhao, Wei
- **Year:** 2020
- **Venue:** IEEE Access
- **DOI:** 10.1109/ACCESS.2020.3002895
- **URL:** https://www.scopus.com/pages/publications/85087627827?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 112762--112771
- **Language:** English
- **Keywords:** caching; Mobile edge computing (MEC); multi-agent Deep-Q-network (MADQN); non-orthogonal multiple access (NOMA)

### Abstract

With the development of emerging applications such as augmented reality, more and more computing tasks are sensitive to delay. Caching popular task computation results on the mobile edge computing (MEC) server is an effective solution to meet the latency requirements. When multiple users request the same task, if the computation result is cached on the MEC server, it will return the computation result directly to the user to reduce the delay for repeated computation. In this paper, we use the caching to assist the calculation. Non-orthogonal multiple access (NOMA) is used to further reduce the delay for computation offloading. The optimization problem is formulated as how to make caching and offloading decision to minimize the delay of whole system. In the case of unknown popularity, we use Gated Recurrent Unit (GRU) algorithm to predict the task popularity in time-varying system, and place the computing results of tasks with high popularity on the corresponding server. Based on the predicted popularity, a multi-agent Deep-Q-network (MADQN) algorithm is used to solve the caching and offloading problem. The simulation results show that the prediction error of GRU algorithm can be reduced by increasing the learning rate. Meanwhile, the proposed MADQN can effectively reduce the delay compared with other methods. © 2013 IEEE.

## 04 — Title Screening

**Title:** Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Optimization of Caching and Computation in Multi-Server NOMA-MEC System via Reinforcement Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
