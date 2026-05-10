---
id: "paper-2441"
title: "Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks"
authors: ["Zhang, Zhenyu", "Lu, Lu", "Li, Qin", "Chai, Yuhao", "Wu, Di", "Zhang, Yong"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3587979"
url: "https://www.scopus.com/pages/publications/105010344392?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "39042--39060"
keywords: ["artificial intelligence (AI) service placement", "digital twin", "Internet of Things (IoT)", "mean-field multiagent reinforcement learning (MARL)", "task scheduling"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2441 — Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks

## Metadata

- **Authors:** Zhang, Zhenyu and Lu, Lu and Li, Qin and Chai, Yuhao and Wu, Di and Zhang, Yong
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3587979
- **URL:** https://www.scopus.com/pages/publications/105010344392?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 39042--39060
- **Language:** English
- **Keywords:** artificial intelligence (AI) service placement; digital twin; Internet of Things (IoT); mean-field multiagent reinforcement learning (MARL); task scheduling

### Abstract

As Internet of Things (IoT)-based artificial intelligence (AI) applications grow, the surge in computational and communication demands has raised concerns about energy consumption, making it critical for 6G networks to address this challenge. This article examines the joint optimization of AI service placement, task scheduling, and computing resource allocation in an edge-network-cloud system to minimize long-term energy consumption. These problems are interdependent: AI service placement determines service locations, influencing task scheduling, which in turn dictates computing resource allocation. The key challenge lies in the coupling of these variables and the two time-scale nature of the problem, involving long-term (AI service placement) and short-term (task scheduling and computing resource allocation) strategies. To address this, a hierarchical Markov decision process (HMDP) framework is proposed for efficient and coordinated optimization across time scales. A hierarchical mean-field dueling double deep Q-network (HMFD3QN) algorithm is developed within this framework, where the upper layer optimizes AI service placement, and the lower layer manages task scheduling and computing resource allocation. By integrating mean-field theory, the algorithm reduces the complexity of multiagent interactions. The computing resource allocation problem is shown to be convex when other variables are fixed, and an optimal strategy is derived using Karush–Kuhn–Tucker (KKT) conditions to simplify the action space for reinforcement learning. Experimental results demonstrate that the proposed method can reduce energy consumption by up to 34% compared to baseline methods, significantly improve queue stability, and increase the proportion of tasks meeting QoS requirements. © 2014 IEEE.

## 04 — Title Screening

**Title:** Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.5
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint AI Service Placement, Task Scheduling, and Resource Allocation for IoT in 6G Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
