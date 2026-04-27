---
id: "paper-2348"
title: "Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach"
authors: ["Yahya, Widhi", "Lai, Yuan-Cheng", "Lin, Ying-Dar", "Rohmatillah, Mahdin", "Kar, Binayak"]
year: 2025
venue: "Journal of Network and Computer Applications"
venue_type: "journal"
doi: "10.1016/j.jnca.2025.104277"
url: "https://www.scopus.com/pages/publications/105012613745?origin=resultslist"
publisher: "Academic Press"
pages: ""
keywords: ["Central Office Re-Architected as a Data Center (CORD)", "Edge computing", "Offloading", "Optimization", "Reinforcement learning"]
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

# paper-2348 — Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach

## Metadata

- **Authors:** Yahya, Widhi and Lai, Yuan-Cheng and Lin, Ying-Dar and Rohmatillah, Mahdin and Kar, Binayak
- **Year:** 2025
- **Venue:** Journal of Network and Computer Applications
- **DOI:** 10.1016/j.jnca.2025.104277
- **URL:** https://www.scopus.com/pages/publications/105012613745?origin=resultslist
- **Publisher:** Academic Press
- **Pages:** 
- **Language:** English
- **Keywords:** Central Office Re-Architected as a Data Center (CORD); Edge computing; Offloading; Optimization; Reinforcement learning

### Abstract

In a distributed edge system, such as the Central Office Re-architected as a Datacenter (CORD), traffic offloading is crucial for minimizing latency by redistributing traffic from overloaded edge sites to less congested sites. The control plane must make rapid decisions to accommodate fluctuating traffic rates. Traditional optimization methods, such as Simulated Annealing (SA), often require significant time to converge in this complex environment. This study proposes the Weighted Action Twin Delayed Deep Deterministic Policy Gradient (WA-TD3), a weighted action approach that optimizes the exploration stage to reduce the exploration space of the original TD3 algorithm in continuous action spaces, resulting in faster convergence. WA-TD3 enhances decision-making in edge offloading by effectively addressing the continuous search space problem and enabling quicker decision-making compared to traditional optimization methods. Evaluation results indicate that WA-TD3 achieves decision times measured in milliseconds, making it five orders of magnitude faster than SA, which has decision times ranging from minutes to hours, despite WA-TD3 exhibiting slightly higher average packet latency. In addition to its performance advantages, the offloading agent can be implemented in a centralized cloud (single agent) or across multiple core networks (multi-agent) with varying coverage. In CORD with 50 sites, the convergence times for SA, single-agent WA-TD3, and multi-agent WA-TD3 are 47,813 s, 1,302 s, and 929 s, respectively. © 2025 Elsevier Ltd

## 04 — Title Screening

**Title:** Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Optimizing ratio-based task offloading in two-tier edge computing: Multi-agent weighted action TD3 approach
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
