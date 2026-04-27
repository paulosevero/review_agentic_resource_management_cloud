---
id: "paper-2678"
title: "AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach"
authors: ["Liu, Xiaoying", "Zheng, Junhao", "Zheng, Kechen", "Liu, Jia", "Taleb, Tarik", "Shiratori, Norio"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3674155"
url: "https://www.scopus.com/pages/publications/105033470100?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Age of information", "federated learning", "heterogeneous network", "mobile edge computing", "multi-agent deep reinforcement learning"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2678 — AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach

## Metadata

- **Authors:** Liu, Xiaoying and Zheng, Junhao and Zheng, Kechen and Liu, Jia and Taleb, Tarik and Shiratori, Norio
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3674155
- **URL:** https://www.scopus.com/pages/publications/105033470100?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Age of information; federated learning; heterogeneous network; mobile edge computing; multi-agent deep reinforcement learning

### Abstract

This paper investigates a dynamic heterogeneous mobile edge computing network (HMECN), where mobile devices (MDs) could offload their full tasks to a small base station (SBS) directly or the macro base station (MBS) in direct or relay mode. As age of information (AoI) is a comprehensive and accurate metric to capture the freshness of computation results, we formulate a long-term weighted sum AoI (LWSA) minimization problem in the HMECN by jointly optimizing the offloading decisions of MDs as well as the bandwidth and computation resource allocation of all base stations, subject to energy, delay and peak AoI constraints. To address the formulated non-convex mixed integer nonlinear programming problem, we decompose it into the offloading decision optimization (ODO) top-problem and the resource allocation optimization (RAO) sub-problem. Based on the decomposition, we propose a federated learning (FL)-assisted hybrid DRL and convex approach that is comprised of a safe multi-agent DRL algorithm, convex optimization and FL. The ODO top-problem is solved by the safe multi-agent DRL algorithm, which strictly ensures that the actions of each agent do not exceed its energy constraint and then paves the way for using convex optimization to solve the RAO sub-problem. FL is used to alleviate the training instability problem aggravated by multi agent settings via breaking the limitation of partial knowledge for each individual agent. Simulation results demonstrate the superiority of the proposed approach in terms of the LWSA, convergence, scalability and robustness in dynamic environments. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** AoI Minimization in Heterogeneous MEC Networks: a Federated Learning-Assisted Hybrid DRL and Convex Approach
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
