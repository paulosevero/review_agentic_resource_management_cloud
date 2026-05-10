---
id: "paper-2863"
title: "Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach"
authors: ["Xu, Yueqiang", "Wang, Lei", "Gao, Qiang", "Zhao, Wei", "Zhang, Heli", "Lin, Fuhong", "Lu, Lu", "He, Jianhua"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3631071"
url: "https://www.scopus.com/pages/publications/105021405510?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3726--3742"
keywords: ["Edge collaboration", "Lyapunov theory", "multiagent deep reinforcement learning (MADRL)", "nonterrestrial networks (NTNs)"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2863 — Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach

## Metadata

- **Authors:** Xu, Yueqiang and Wang, Lei and Gao, Qiang and Zhao, Wei and Zhang, Heli and Lin, Fuhong and Lu, Lu and He, Jianhua
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3631071
- **URL:** https://www.scopus.com/pages/publications/105021405510?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3726--3742
- **Language:** English
- **Keywords:** Edge collaboration; Lyapunov theory; multiagent deep reinforcement learning (MADRL); nonterrestrial networks (NTNs)

### Abstract

Satellite-edge computing offers promising solutions for extending the coverage of terrestrial networks, particularly in remote and harsh environments. By offloading ground data to satellites for processing, this paradigm enables real-time data handling in nonterrestrial networks (NTNs). However, due to limited onboard resources and dynamic task requirements from the Internet of Things (IoT) devices, online energy management becomes a critical challenge that hinders the scalability and deployment of satellite-edge computing systems. In this article, we propose an online energy management framework based on satellite-edge collaboration. A queue-based collaboration scheme is designed to coordinate satellites in handling tasks with random arrival patterns. Building upon this scheme, we formulate a joint optimization problem that integrates transmission resource allocation, computational resource assignment, power control, routing strategies, and collaboration policies, aiming to minimize the energy consumption of the satellite network. Given the dynamic, complex, and distributed nature of the problem, we present a Lyapunov-based multiagent deep reinforcement learning (MADRL) algorithm. Specifically, we first transform the long-term stochastic optimization problem into a sequence of deterministic subproblems using the Lyapunov theory. Subsequently, each subproblem is decomposed into a resource allocation subproblem and an edge collaboration subproblem. Correspondingly, we devise a MADRL-based algorithm for edge collaboration and a Lagrangian multiplier iteration (LMI)-based algorithm for resource allocation. Finally, the overall problem is iteratively optimized using the block coordinate descent (BCD) framework. Simulation results demonstrate that the proposed approach achieves significant performance improvements over both baseline methods and several state-of-the-art pure deep reinforcement learning (DRL) approaches. © 2014 IEEE.

## 04 — Title Screening

**Title:** Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Edge Collaboration-Enabled Online Energy Optimization for Satellite-Assisted Internet of Things: A Lyapunov-Based Learning Approach
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
