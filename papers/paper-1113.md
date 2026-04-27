---
id: "paper-1113"
title: "Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]"
authors: ["Pan, Xi'an", "Ai, Xin", "Hu, Junjie", "Wang, Kunyu", "Wang, Haoyang"]
year: 2024
venue: "Diangong Jishu Xuebao/Transactions of China Electrotechnical Society"
venue_type: "journal"
doi: "10.19595/j.cnki.1000-6753.tces.231352"
url: "https://www.scopus.com/pages/publications/85211429124?origin=resultslist"
publisher: "China Machine Press"
pages: "6104--6118"
keywords: ["deep reinforcement learning", "Distributed smart grid", "edge-cloud collaboration", "flexible resources", "network safety constrain"]
language: "Chinese"
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1113 — Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]

## Metadata

- **Authors:** Pan, Xi'an and Ai, Xin and Hu, Junjie and Wang, Kunyu and Wang, Haoyang
- **Year:** 2024
- **Venue:** Diangong Jishu Xuebao/Transactions of China Electrotechnical Society
- **DOI:** 10.19595/j.cnki.1000-6753.tces.231352
- **URL:** https://www.scopus.com/pages/publications/85211429124?origin=resultslist
- **Publisher:** China Machine Press
- **Pages:** 6104--6118
- **Language:** Chinese
- **Keywords:** deep reinforcement learning; Distributed smart grid; edge-cloud collaboration; flexible resources; network safety constrain

### Abstract

With the increasing penetration of distributed generation and the growing demand for power system flexibility, issues like voltage rise at the edge of distribution networks and network congestion under bidirectional power flow are becoming more prominent. Integrating and coordinating flexible resources at the user side through Distributed Smart Grids (DSG) is significant for enhancing the accommodation of distributed generation and the real-time supply-demand balancing capability of distribution systems. Considering the large quantity and high dispersion of flexible resource devices and the distinct characteristics of different prosumers, traditional centralized optimization and dispatch schemes as well as distributed computing methods will face greater challenges in solving efficiency and decision delivery timeliness. Against this background, this paper aims to develop a DSG system collaborative optimization and dispatch method that takes into account operational economy, energy network security, and decision timeliness concurrently. Firstly, mapping real-world prosumers who control and own flexible resources to intelligent agents in reinforcement learning, the optimization and dispatch of flexible resources in DSG is formulated as a multi-agent collaborative optimization model. The existing edge-cloud collaborative framework is extended to the optimization of flexible resources considering energy network security constraints, and a hierarchical optimization and dispatch framework of flexible resource-prosumer-DSG is established. Secondly, considering the differentiated characteristics of prosumers in aspects like types of flexible resource devices, photovoltaics (PV) is taken as distributed generation, and electric vehicles (EV), heating, ventilation and air conditioning (HVAC) of buildings, and energy storage systems (ESS) are taken as demand-side flexible resources. A heterogeneous intelligent agent interactive environment model is built based on the operational characteristics of different flexible resources. Meanwhile, to balance flexible resource operational requirements, overall economic efficiency and energy network security of the DSG system, user satisfaction evaluation of EV and HVAC operation and ESS operation cost are considered as local rewards, while system energy cost and energy network security evaluation are taken as global rewards, and a combined global-local reward mechanism for heterogeneous intelligent agents is proposed. Finally, to adapt to the collaborative training task of the heterogeneous intelligent agent system, an improved multi-agent proximal policy optimization (MAPPO) algorithm is proposed based on asynchronous update of agent policies in random order. Case studies on the IEEE 33-node system are conducted for analysis. Firstly, the proposed improved MAPPO algorithm is compared with existing multi-agent collaborative training schemes in the offline training stage. Secondly, the differences in flexible resource prosumers' power decisions with and without considering energy network constraints are analyzed in the online dispatch stage. Finally, the proposed method is compared with traditional mathematical programming and particle swarm optimization methods regarding optimization performance in real-time dispatch. The main conclusions are: (1) The edge-cloud collaborative hierarchical optimization and dispatch framework for DSG systems is established, which can obtain dispatch decisions faster in real-time dispatch compared to traditional centralized optimization and thus improve the timeliness of DSG power dispatch decisions. (2) The combined global-local reward mechanism for heterogeneous intelligent agents can achieve overall DSG system optimization and collaborative training objectives of balancing user comfort, economic efficiency and energy network security. (3) The proposed improved MAPPO algorithm adapted for heterogeneous intelligent agent training can maintain independent decision spaces for each agent while ensuring environment state stability in collaborative training through asynchronous policy updates in random order. © 2024 China Machine Press. All rights reserved.

## 04 — Title Screening

**Title:** Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Network Security Constrained Distributed Smart Grid Edge-Cloud Collaborative Optimization Scheduling; [考虑网络安全约束的分布式智能电网边云协同优化调度方法]
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
