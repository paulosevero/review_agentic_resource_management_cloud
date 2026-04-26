---
id: "paper-068"
title: "Cloud-Enabled Differentially Private Multiagent Optimization with Constraints"
authors: ["Hale, Matthew T.", "Egerstedt, Magnus"]
year: 2018
venue: "IEEE Transactions on Control of Network Systems"
venue_type: "journal"
doi: "10.1109/TCNS.2017.2751458"
url: "https://www.scopus.com/pages/publications/85030330215?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1693--1706"
keywords: ["Data privacy", "decentralized control", "networked control systems", "optimization"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-068 — Cloud-Enabled Differentially Private Multiagent Optimization with Constraints

## Metadata

- **Authors:** Hale, Matthew T. and Egerstedt, Magnus
- **Year:** 2018
- **Venue:** IEEE Transactions on Control of Network Systems
- **DOI:** 10.1109/TCNS.2017.2751458
- **URL:** https://www.scopus.com/pages/publications/85030330215?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1693--1706
- **Language:** English
- **Keywords:** Data privacy; decentralized control; networked control systems; optimization

### Abstract

We present an optimization framework for solving multiagent convex programs subject to inequality constraints while keeping the agents' state trajectories private. Each agent has an objective function depending only upon its own state and the agents are collectively subject to global constraints. The agents do not directly communicate with each other but instead route messages through a trusted cloud computer. The cloud adds noise to data being sent to the agents in accordance with the framework of differential privacy and, thus, keeps each agent's state trajectory private from all other agents and any eavesdroppers. This private problem can be viewed as a stochastic variational inequality, and it is solved using a projection-based method for solving variational inequalities that resemble a noisy primal-dual gradient algorithm. Convergence of the optimization algorithm in the presence of noise is proven, and a quantifiable tradeoff between privacy and convergence is extracted from this proof. Simulation results are provided that demonstrate numerical convergence for both ϵ-differential privacy and (ϵ, δ)-differential privacy. © 2017 IEEE.

## 04 — Title Screening

**Title:** Cloud-Enabled Differentially Private Multiagent Optimization with Constraints

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Cloud-Enabled Differentially Private Multiagent Optimization with Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cloud-Enabled Differentially Private Multiagent Optimization with Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
