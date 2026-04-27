---
id: "paper-2338"
title: "Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach"
authors: ["Xu, Bo", "Zhao, Haitao", "Cao, Haotong", "Zhu, Chun", "Sun, Jinlong", "Zhang, Linghao", "Zhu, Hongbo"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2024.3514095"
url: "https://www.scopus.com/pages/publications/105002486644?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10795--10807"
keywords: ["Fog computing", "Industrial Internet of Things (IIoT)", "multiagent reinforcement learning (MARL)", "submodular optimization"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2338 — Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach

## Metadata

- **Authors:** Xu, Bo and Zhao, Haitao and Cao, Haotong and Zhu, Chun and Sun, Jinlong and Zhang, Linghao and Zhu, Hongbo
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2024.3514095
- **URL:** https://www.scopus.com/pages/publications/105002486644?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10795--10807
- **Language:** English
- **Keywords:** Fog computing; Industrial Internet of Things (IIoT); multiagent reinforcement learning (MARL); submodular optimization

### Abstract

The development of Industrial Internet of Things (IIoT) applications presents a critical challenge in terms of latency limitation, particularly considering the limited availability of resources that prevent a single fog device from fully executing large-scale computing tasks. In such scenarios, enabling distributed computing across multiple fog servers or collaborating with cloud servers holds promising potential. To improve the efficiency of task offloading while accounting for the crucial role of movable fog devices (e.g., robots and unmanned cars), we formulate a joint optimization problem as a partially observable Markov decision process (POMDP), incorporating offloading decisions, computing resource allocation, and trajectory optimization under constraints related to available resources and collision avoidance. Due to the nondeterministic polynomial-time hardness (NP-hardness) in the problems of task offloading and resource allocation, we reformulate a matroid-constrained submodular maximization problem and propose an iterative low-complexity algorithm to find solutions. Subsequently, extracting better solutions from submodular optimization, we propose a multiagent reinforcement learning (MARL)-based algorithm to solve the trajectory optimization problem for the movable fog devices acting as agents, making decisions based on their local observations. Finally, simulation results have validated that the proposed scheme has a superior performance compared to the baselines. © 2014 IEEE.

## 04 — Title Screening

**Title:** Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
