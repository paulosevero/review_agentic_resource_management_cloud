---
id: "paper-1122"
title: "Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism"
authors: ["Park, Yu Min", "Hassan, Sheikh Salman", "Tun, Yan Kyaw", "Han, Zhu", "Hong, Choong Seon"]
year: 2024
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2023.3311537"
url: "https://www.scopus.com/pages/publications/85171526953?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2003--2016"
keywords: ["attention mechanism", "mobile-edge computing", "multi-agent proximal policy optimization", "resource allocation", "sub-terahertz communication", "Unmanned aerial vehicles (UAVs)"]
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

# paper-1122 — Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism

## Metadata

- **Authors:** Park, Yu Min and Hassan, Sheikh Salman and Tun, Yan Kyaw and Han, Zhu and Hong, Choong Seon
- **Year:** 2024
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2023.3311537
- **URL:** https://www.scopus.com/pages/publications/85171526953?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2003--2016
- **Language:** English
- **Keywords:** attention mechanism; mobile-edge computing; multi-agent proximal policy optimization; resource allocation; sub-terahertz communication; Unmanned aerial vehicles (UAVs)

### Abstract

The use of Terahertz (THz) technology in sixth-generation (6G) networks will bring high-speed and capacity data services. But limitations like molecular absorption, rain attenuation, and limited coverage range cause communication losses. To overcome these losses and improve coverage in rural areas, a high number of base stations are required. Hence, an aerial communication platform, which uses line-of-sight (LoS) communication to avoid losses, is needed. To address this, we study the deployment and optimization of multi-access edge computing (MEC)-powered unmanned aerial vehicle (UAV) for sub-THz communication in remote areas. To this end, we solve an optimization problem to minimize energy consumption and delay for MEC-UAV and mobile users. The formulated problem is a mixed-integer non-linear programming (MINLP) problem. As the problem is an MINLP, we decompose the main problem into two subproblems. Due to its convex nature, we solve the first subproblem with a standard optimization solver, i.e., CVXPY. To solve the second subproblem, we design a resources-based multi-agent proximal policy optimization (RMAPPO) deep reinforcement learning (DRL) algorithm with an attention mechanism. The considered attention mechanism is utilized for encoding a diverse number of observations. This is designed by the network coordinator to provide a differentiated fit reward to each agent in the network. The simulation results show that the proposed algorithm outperforms the benchmark and yields a network utility that is 2.22%, 15.55%, and 17.77% more than the benchmarks.  © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Joint Trajectory and Resource Optimization of MEC-Assisted UAVs in Sub-THz Networks: A Resources-Based Multi-Agent Proximal Policy Optimization DRL With Attention Mechanism
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
