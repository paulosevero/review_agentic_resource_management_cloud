---
id: "paper-2946"
title: "Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning"
authors: ["Zhu, Bincheng", "Zhu, Shaojun", "Chi, Kaikai", "Mumtaz, Shahid", "Bazzi, Wael"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3637266"
url: "https://www.scopus.com/pages/publications/105023179194?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6596--6613"
keywords: ["convex-based critic", "counterfactual baseline", "mobile edge computing", "multi-agent", "NOMA", "Wireless power transfer"]
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

# paper-2946 — Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Zhu, Bincheng and Zhu, Shaojun and Chi, Kaikai and Mumtaz, Shahid and Bazzi, Wael
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3637266
- **URL:** https://www.scopus.com/pages/publications/105023179194?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6596--6613
- **Language:** English
- **Keywords:** convex-based critic; counterfactual baseline; mobile edge computing; multi-agent; NOMA; Wireless power transfer

### Abstract

Wireless power transfer enhanced mobile edge computing (WPT-MEC) has emerged as a key technology to support low-latency and energy-efficient computation in wireless networks. With increasing network density, multi-base-station architectures emerge where wireless devices (WDs) offload tasks to distributed base stations (BSs), creating challenges in maintaining quality-of-service fairness during complex resource coordination in multi-BS WPT-MEC networks. To address these challenges, we investigate a non-orthogonal multiple access (NOMA)-enhanced WPT-MEC network comprising multiple WDs and BSs with finite computational capacities. For ensuring fairness, we formulate a max-min problem to maximize the minimum task computation amount by jointly optimizing offloading decisions, NOMA decoding orders, offloading powers and time resource allocation, which results in a challenging mixed integer, sequence and nonlinear programming (MISNLP). To tackle this problem, we propose a two-stage distributed multi-agent algorithm. In the first stage, each BS agent generates offloading preferences based on partial observations, guiding WDs' offloading decisions. In the second stage, given these offloading decisions, we develop an efficient convex-based algorithm to solve the per-BS resource allocation subproblem, jointly optimizing NOMA decoding order, offloading powers and time resource allocation. For effective training, we leverage off-policy training and the centralized training with decentralized execution (CTDE) paradigm with two key innovations: (1) a convex-based critic that evaluates the joint action without bias, and (2) a counterfactual baseline that isolates individual agent credit assignment. The proposed C3MA algorithm achieves six times faster convergence and at least 20% performance improvement when serving more than 20 WDs, compared with existing multi-agent schemes, while maintaining a near-optimal Jain's fairness index of 0.97. Moreover, it sustains an ultra-low execution delay below 5 milliseconds even with 40 WDs, confirming its efficiency and scalability.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Max-Min Computation Optimization in Multi-BS WPT-MEC Networks via Multi-Agent Reinforcement Learning
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
