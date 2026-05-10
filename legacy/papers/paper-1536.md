---
id: "paper-1536"
title: "Discretized Distributed Optimization over Dynamic Digraphs"
authors: ["Doostmohammadian, Mohammadreza", "Jiang, Wei", "Liaquat, Muwahida", "Aghasi, Alireza", "Zarrabi, Houman"]
year: 2025
venue: "IEEE Transactions on Automation Science and Engineering"
venue_type: "journal"
doi: "10.1109/TASE.2024.3383894"
url: "https://www.scopus.com/pages/publications/85190169910?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2758--2767"
keywords: ["consensus constraint", "Distributed optimization", "dynamic digraphs", "matrix perturbation theory"]
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
    final_score: 0.1666
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-1536 — Discretized Distributed Optimization over Dynamic Digraphs

## Metadata

- **Authors:** Doostmohammadian, Mohammadreza and Jiang, Wei and Liaquat, Muwahida and Aghasi, Alireza and Zarrabi, Houman
- **Year:** 2025
- **Venue:** IEEE Transactions on Automation Science and Engineering
- **DOI:** 10.1109/TASE.2024.3383894
- **URL:** https://www.scopus.com/pages/publications/85190169910?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2758--2767
- **Language:** English
- **Keywords:** consensus constraint; Distributed optimization; dynamic digraphs; matrix perturbation theory

### Abstract

We consider a discrete-time model of continuous-time distributed optimization over dynamic directed-graphs (digraphs) with applications to distributed learning. Our optimization algorithm works over general strongly connected dynamic networks under switching topologies, e.g., in mobile multi-agent systems and volatile networks due to link failures. Compared to many existing lines of work, there is no need for bi-stochastic weight designs on the links. The existing literature mostly needs the link weights to be stochastic using specific weight-design algorithms needed both at the initialization and at all times when the topology of the network changes. This paper eliminates the need for such algorithms and paves the way for distributed optimization over time-varying digraphs. We derive the bound on the gradient-tracking step-size and discrete time-step for convergence and prove dynamic stability using arguments from consensus algorithms, matrix perturbation theory, and Lyapunov theory. This work, particularly, is an improvement over existing stochastic-weight undirected networks in case of link removal or packet drops. This is because the existing literature may need to rerun time-consuming and computationally complex algorithms for stochastic design, while the proposed strategy works as long as the underlying network is weight-symmetric and balanced. The proposed optimization framework finds applications to distributed classification and learning. Note to Practitioners - Inspired by recent advances in cloud-computing and distributed and parallel processing along with embedded low-cost CPUs and wireless communications, this paper considers distributed algorithms for optimization and machine learning over wireless-connected autonomous multi-agent systems (MASs). In contrast to the classical centralized learning methods, which are prone to single-point-of-failure and centralized processing, in cooperative optimization the learning is distributed among a group of data-processing agents (e.g. robots) with communication units. This article provides an efficient algorithm to enable MASs to collaboratively optimize a cost function, e.g., for binary classification and distributed support vector machine (D-SVM). Sampled data systems related to MASs and robotic networks, due to digital communications and discretized control models, use discrete-time algorithms that need to account for intermittent communications and dynamic networking. This requires discretized algorithms over dynamic digraphs, practical in the presence of packet drops (or lost communication channels). Most existing distributed algorithms either are susceptible to change in the communication network or impose computationally inefficient stochastic design. These algorithms need to be rerun, for example, whenever the mobile robotic network changes due to limited communication range. This makes most existing algorithms infeasible in real-time applications. Our proposed method outperforms similar algorithms over dynamic robotic networks and in the presence of link removal (packet drops). We show this efficiency of our distributed optimization method by simulation.  © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Discretized Distributed Optimization over Dynamic Digraphs

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.5
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Discretized Distributed Optimization over Dynamic Digraphs
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Discretized Distributed Optimization over Dynamic Digraphs
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
