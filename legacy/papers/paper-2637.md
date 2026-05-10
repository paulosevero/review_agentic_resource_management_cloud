---
id: "paper-2637"
title: "Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems"
authors: ["Khater, Heba M.", "Sallabi, Farag", "Serhani, Mohamed Adel", "Barka, Ezedin", "Khayat, Mohamad"]
year: 2026
venue: "Computers and Operations Research"
venue_type: "journal"
doi: "10.1016/j.cor.2026.107454"
url: "https://www.scopus.com/pages/publications/105034613612?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Actor-critic", "Collaborative decision-making", "Deep reinforcement learning", "Mobile Edge Computing", "Multi-agent systems", "Offloading optimization"]
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

# paper-2637 — Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems

## Metadata

- **Authors:** Khater, Heba M. and Sallabi, Farag and Serhani, Mohamed Adel and Barka, Ezedin and Khayat, Mohamad
- **Year:** 2026
- **Venue:** Computers and Operations Research
- **DOI:** 10.1016/j.cor.2026.107454
- **URL:** https://www.scopus.com/pages/publications/105034613612?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Actor-critic; Collaborative decision-making; Deep reinforcement learning; Mobile Edge Computing; Multi-agent systems; Offloading optimization

### Abstract

With the rise of the Internet of Medical Things (IoMT), healthcare systems increasingly rely on Wireless Body Area Networks (WBANs) for continuous, real-time patient monitoring and clinical decision-making. These applications require ultra-low latency, high reliability, and energy efficiency. Typically, they operate via mobile devices, such as smartphones, wearables, or WBAN coordinators, which collect, process, and transmit medical data. However, the limited processing capabilities and energy constraints of these devices often lead to increased delays and degraded system performance. To address these challenges, Mobile Edge Computing (MEC) has emerged as a promising solution that brings computation closer to the network edge. This paper addresses the optimization problem of task offloading and resource allocation in WBAN-MEC systems, where each task can be executed locally on the mobile device, offloaded to the MEC server, or to the cloud. The problem is formulated as a Mixed-Integer Nonlinear Programming (MINLP) model involving offloading decisions and the allocation of communication and computational resources. Our objective is to maximize task completion subject to time constraints, minimize mobile energy consumption, and ensure efficient use of MEC resources. We propose a Collaborative Multi-Agent Task Offloading and Resource Allocation (CoMA-TORA) framework, which decomposes the complex optimization problem into two coordinated components: a decentralized offloading decision component and a centralized resource allocation component. The framework is implemented using an actor-critic reinforcement learning architecture, with a global critic that evaluates a shared reward for coordinated decision-making. Simulation results show that CoMA-TORA outperforms both traditional and DRL-based approaches in delay-sensitive healthcare environments. © 2026 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license. http://creativecommons.org/licenses/by/4.0/

## 04 — Title Screening

**Title:** Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Collaborative multi-agent DRL for energy-efficient task offloading and resource allocation in WBAN-MEC systems
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
