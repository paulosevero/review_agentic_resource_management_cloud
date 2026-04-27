---
id: "paper-318"
title: "Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach"
authors: ["Munir, Md. Shirajum", "Abedin, Sarder Fakhrul", "Tran, Nguyen H.", "Han, Zhu", "Huh, Eui-Nam", "Hong, Choong Seon"]
year: 2021
venue: "IEEE Transactions on Network and Service Management"
venue_type: "journal"
doi: "10.1109/TNSM.2021.3049381"
url: "https://www.scopus.com/pages/publications/85099423791?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3476--3497"
keywords: ["conditional value-at-risk (CVaR)", "demand-response (DR)", "microgrid", "Multi-access edge computing (MEC)", "multi-agent deep reinforcement learning", "stochastic game"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-318 — Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Munir, Md. Shirajum and Abedin, Sarder Fakhrul and Tran, Nguyen H. and Han, Zhu and Huh, Eui-Nam and Hong, Choong Seon
- **Year:** 2021
- **Venue:** IEEE Transactions on Network and Service Management
- **DOI:** 10.1109/TNSM.2021.3049381
- **URL:** https://www.scopus.com/pages/publications/85099423791?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3476--3497
- **Language:** English
- **Keywords:** conditional value-at-risk (CVaR); demand-response (DR); microgrid; Multi-access edge computing (MEC); multi-agent deep reinforcement learning; stochastic game

### Abstract

In recent years, multi-access edge computing (MEC) is a key enabler for handling the massive expansion of Internet of Things (IoT) applications and services. However, energy consumption of a MEC network depends on volatile tasks that induces risk for energy demand estimations. As an energy supplier, a microgrid can facilitate seamless energy supply. However, the risk associated with energy supply is also increased due to unpredictable energy generation from renewable and non-renewable sources. Especially, the risk of energy shortfall is involved with uncertainties in both energy consumption and generation. In this article, we study a risk-aware energy scheduling problem for a microgrid-powered MEC network. First, we formulate an optimization problem considering the conditional value-at-risk (CVaR) measurement for both energy consumption and generation, where the objective is to minimize the expected residual of scheduled energy for the MEC networks and we show this problem is an NP-hard problem. Second, we analyze our formulated problem using a multi-agent stochastic game that ensures the joint policy Nash equilibrium, and show the convergence of the proposed model. Third, we derive the solution by applying a multi-agent deep reinforcement learning (MADRL)-based asynchronous advantage actor-critic (A3C) algorithm with shared neural networks. This method mitigates the curse of dimensionality of the state space and chooses the best policy among the agents for the proposed problem. Finally, the experimental results establish a significant performance gain by considering CVaR for high accuracy energy scheduling of the proposed model than both the single and random agent models.  © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Risk-Aware Energy Scheduling for Edge Computing with Microgrid: A Multi-Agent Deep Reinforcement Learning Approach
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
