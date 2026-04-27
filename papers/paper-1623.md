---
id: "paper-1623"
title: "Research on the Construction and Resource Optimization of a UAV Command Information System Based on Large Language Models"
authors: ["Han, Songyue", "Wan, Pengfei", "Lian, Zhixuan", "Wang, Mingyu", "Li, Dongdong", "Fan, Chengli"]
year: 2025
venue: "Drones"
venue_type: "journal"
doi: "10.3390/drones9090639"
url: "https://www.scopus.com/pages/publications/105017432221?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["command and control system", "edge computing", "intelligent optimization algorithm", "large language model", "multi-objective optimization", "UAV"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-1623 — Research on the Construction and Resource Optimization of a UAV Command Information System Based on Large Language Models

## Metadata

- **Authors:** Han, Songyue and Wan, Pengfei and Lian, Zhixuan and Wang, Mingyu and Li, Dongdong and Fan, Chengli
- **Year:** 2025
- **Venue:** Drones
- **DOI:** 10.3390/drones9090639
- **URL:** https://www.scopus.com/pages/publications/105017432221?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** command and control system; edge computing; intelligent optimization algorithm; large language model; multi-objective optimization; UAV

### Abstract

Highlights: What are the main findings? A three-layer “cloud-edge-terminal” UAV command information system has been developed, deploying LLMs of different scales (cloud 175B, edge 70B, terminal 7B) to achieve optimal resource allocation and support elastic expansion from 10 to over 1000 UAVs. An improved Grey Wolf Optimization Algorithm (ILGWO) integrating Lévy flight, adaptive weighting, elite learning, and chaotic initialization strategies has been proposed to enhance system performance. The system achieves remarkable improvements compared to traditional methods: 34.2% reduction in task latency, 29.6% optimization in energy consumption, and 31.8% improvement in resource utilization. In urban rescue scenarios, response latency decreased by 44.7% and coordination efficiency increased by 39.5%, while LLM integration enhanced decision-making accuracy across multiple dimensions—task priority adjustment (76.3% to 94.7%), dynamic resource allocation (68.9% to 91.2%), and anomaly handling (71.5% to 93.8%). What is the implication of the main finding? System Performance and Generalization Capabilities. Integrating large language models into unmanned aerial vehicle command information systems enables autonomous decision-making and intelligent planning without relying on preset rules, effectively addressing the shortcomings of existing information systems in handling dynamic scenarios and complex environments. The system demonstrates superior generalization ability with 82.5% performance retention in new scenarios, significantly outperforming the reinforcement learning method’s 56.7%, enabling rapid deployment in rescue, emergency response, inspection, and reconnaissance scenarios. Technical Specifications and Practical Implementation. The proposed system architecture and optimization algorithm provide a scalable and robust solution for large-scale UAV swarm operations. With fault tolerance capabilities maintaining an 88.4% task completion rate even under 20% node failure conditions and a real-time inference delay of only 156 ms for edge-deployed 7B models, the system meets practical requirements for emergency rescue, environmental monitoring, and intelligent surveillance applications. This work establishes a theoretical and practical foundation for integrating cutting-edge AI technologies into unmanned aerial vehicle systems, promoting the development of intelligent, adaptive, and resilient autonomous systems for critical mission scenarios. As UAVs are increasingly deployed in complex scenarios such as disaster monitoring, emergency rescue, and power-line inspection, traditional command and control systems face severe challenges in intelligent decision-making, resource allocation, and elastic scalability. To address these issues, we first propose a distributed UAV command and control system based on large language models of the LLaMA2 family. The system adopts a “cloud–edge–terminal” architecture, using 5G as the backbone network and the Internet of Things as a supplement, with edge computing serving as the computing platform. LLMs of various parameter scales are deployed on demand at different hierarchical levels to support both training and inference, enabling intelligent decision-making and optimal resource allocation. Second, we establish a multidimensional system model that integrates computation, communication, and energy consumption, providing a theoretical analysis of network dynamics, resource constraints, and task heterogeneity. Furthermore, we develop an improved Grey Wolf Optimizer (ILGWO) that incorporates adaptive weights, an elite learning strategy, and Lévy flights to solve the multi-objective optimization problem posed by the system. Experimental results show that the proposed system improves task latency, energy efficiency, and resource utilization by 34.2%, 29.6%, and 31.8%, respectively, compared with conventional methods. Real-world field tests demonstrate that, in urban rescue scenarios, the system reduces response latency by 44.7% and increases coordination efficiency by 39.5%. This work offers a reference for the optimized design and practical deployment of UAV command and control systems in complex environments. © 2025 by the authors.

## 04 — Title Screening

**Title:** Research on the Construction and Resource Optimization of a UAV Command Information System Based on Large Language Models

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Research on the Construction and Resource Optimization of a UAV Command Information System Based on Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Research on the Construction and Resource Optimization of a UAV Command Information System Based on Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
