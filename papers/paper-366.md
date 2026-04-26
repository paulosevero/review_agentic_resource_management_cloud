---
id: "paper-366"
title: "Cooperative multi-agent actor–critic control of traffic network flow based on edge computing"
authors: ["Zhang, Yongnan", "Zhou, Yonghua", "Lu, Huapu", "Fujita, Hamido"]
year: 2021
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2021.04.018"
url: "https://www.scopus.com/pages/publications/85105361041?origin=resultslist"
publisher: "Elsevier B.V."
pages: "128--141"
keywords: ["Cooperative multi-agent actor\u2013critic framework", "Distributed deep reinforcement learning", "Edge computing", "Traffic network flow control"]
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
    human_decision: ""
    human_justification: ""

---

# paper-366 — Cooperative multi-agent actor–critic control of traffic network flow based on edge computing

## Metadata

- **Authors:** Zhang, Yongnan and Zhou, Yonghua and Lu, Huapu and Fujita, Hamido
- **Year:** 2021
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2021.04.018
- **URL:** https://www.scopus.com/pages/publications/85105361041?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 128--141
- **Language:** English
- **Keywords:** Cooperative multi-agent actor–critic framework; Distributed deep reinforcement learning; Edge computing; Traffic network flow control

### Abstract

Most of the existing traffic signal control strategies are hard to satisfy the real-time requirements of traffic big data analysis, knowledge reasoning and decision making for sophisticated traffic dynamics and heterogeneous intersection structures in the context of Internet of Vehicles (IoV). In this paper, we attempt to propose a cooperative multi-agent actor–critic (CMAC) deep reinforcement learning (DRL) approach with value decomposition based on edge computing architecture. The intuition behind CMAC is to decompose the global actor–critic learning tasks into several local actor–critic​ sub-problems with respect to each intersection. Each agent searches the local optimal decision by actor–critic network that takes the discrete state encoding about several consecutive frames of image-like traffic states as the inputs of the network. Among them, the green ratio output strategy considering multiple constraints is formulated in the output layer of the actor network, so that the continuous control of traffic signals using multi-agent DRL (MADRL) can be realized. Furthermore, a cooperative mechanism that considers contribution weight distributions of local agents to the global traffic pattern is proposed to coordinate multiple local agents to evolve toward global optimization. Especially, some parallel training tasks of CMAC with a large number of computing loads are deployed on the cloud side in the edge computing architecture to accelerate learning and reconstructing knowledge. The well-trained multi-agent model is downloaded from the cloud side into the edge side for real-time decision making of traffic network flow adaptive control. Simulation results with regard to a realistic traffic network demonstrate that the proposed CMAC approach under edge computing architecture outperforms the value-decomposition based multi-agent actor–critic (VMAC), independent multi-agent actor–critic (IMAC), and the fixed timing control (FTC) in terms of alleviating traffic congestion. © 2021

## 04 — Title Screening

**Title:** Cooperative multi-agent actor–critic control of traffic network flow based on edge computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cooperative multi-agent actor–critic control of traffic network flow based on edge computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cooperative multi-agent actor–critic control of traffic network flow based on edge computing
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
