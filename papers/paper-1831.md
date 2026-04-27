---
id: "paper-1831"
title: "Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method"
authors: ["Li, Shichao", "Lu, Bingji", "Ale, Laha", "Chen, Hongbin", "Tan, Fangqing", "Huang, Jingyue"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3548088"
url: "https://www.scopus.com/pages/publications/86000448616?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "21443--21456"
keywords: ["Independent proximal policy optimization (IPPO)", "mobile edge computing (MEC)", "multiagent deep deterministic policy gradient (MADDPG)", "partial task offloading", "uncrewed aerial vehicles (UAVs) trajectory design"]
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

# paper-1831 — Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method

## Metadata

- **Authors:** Li, Shichao and Lu, Bingji and Ale, Laha and Chen, Hongbin and Tan, Fangqing and Huang, Jingyue
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3548088
- **URL:** https://www.scopus.com/pages/publications/86000448616?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 21443--21456
- **Language:** English
- **Keywords:** Independent proximal policy optimization (IPPO); mobile edge computing (MEC); multiagent deep deterministic policy gradient (MADDPG); partial task offloading; uncrewed aerial vehicles (UAVs) trajectory design

### Abstract

The integration of mobile edge computing (MEC) and air-ground integrated network is viewed as a crucial technology for Internet of Remote Things (IoRT) devices. It provides widespread service coverage and allows the tasks of IoRT devices to be executed by the uncrewed aerial vehicles (UAVs) and the high altitude platforms (HAPs). In this article, we investigate a joint partial task offloading, resource allocation, and UAV trajectory design problem to minimize the total task offloading delay of all IoRT devices in the air-ground integrated MEC network. Given that the problem is nonconvex and hard to solve by the traditional methods, we convert it into a Markov decision process (MDP) and leverage the deep reinforcement learning method to address it. Considering the complexity of the MDP grows with the number of the IoRT devices and the UAVs increasing, the primal problem is decomposed into two subproblems: 1) the UAV trajectory design and IoRT device power control subproblem, and 2) the partial task offloading and resource allocation subproblem. To address these two subproblems, we apply the basic concepts of the multiagent deep deterministic policy gradient (MADDPG) and the independent proximal policy optimization (IPPO) methods, respectively. Additionally, we introduce the enhanced prioritized experience replay and noise value to improve both the convergence performance and rate. This leads to the development of the MADDPG-improved prioritized experience replay (MADDPG-IPER) algorithm and noise value-IPPO (NV-IPPO) algorithm. Based on the solution of these two subproblems, a joint partial task offloading, resource allocation, and UAV trajectory design (JPTORAUTD) algorithm is proposed. Simulation results present that the proposed JPTORAUTD algorithm outperforms other benchmark algorithms in terms of reducing the total task offloading delay. © 2014 IEEE.

## 04 — Title Screening

**Title:** Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Two-Hop Partial Task Offloading and Resource Allocation in Air–Ground Integrated Mobile Edge Computing Network: A DRL-Based Method
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
