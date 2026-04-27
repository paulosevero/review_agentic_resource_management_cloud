---
id: "paper-2707"
title: "Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach"
authors: ["Ma, Lixin", "Zhang, Peiying", "Chen, Ning"]
year: 2026
venue: "Information (Switzerland)"
venue_type: "journal"
doi: "10.3390/info17030278"
url: "https://www.scopus.com/pages/publications/105034105068?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["deep reinforcement learning", "edge computing", "software-defined network", "task offloading", "virtual network embedding"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2707 — Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Ma, Lixin and Zhang, Peiying and Chen, Ning
- **Year:** 2026
- **Venue:** Information (Switzerland)
- **DOI:** 10.3390/info17030278
- **URL:** https://www.scopus.com/pages/publications/105034105068?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning; edge computing; software-defined network; task offloading; virtual network embedding

### Abstract

The advent of 5G/6G technologies and the pervasive deployment of IoT devices are driving the emergence of demanding applications that necessitate ultra-low latency, high bandwidth, and significant computational power. Traditional cloud computing models fall short in meeting these stringent requirements. To address this, Software-Defined Edge Networks (SDENs) have emerged as a promising architecture, yet efficiently managing their heterogeneous and geographically distributed resources poses substantial challenges for optimal application provisioning. In response, this paper proposes a novel framework for intelligent task offloading, which reframes the intricate multi-component application task offloading problem as a Virtual Network Embedding (VNE) challenge within a SDEN environment. We introduce a comprehensive model where complex applications are represented as Virtual Network Requests (VNRs). In this model, each VNR consists of virtual nodes that demand specific computing and storage resources, as well as virtual links that demand specific bandwidth and must adhere to maximum tolerable delay constraints. To dynamically solve this NP-hard VNE problem in the face of stochastic VNR arrivals and dynamic network conditions, we leverage Deep Reinforcement Learning (DRL). Specifically, a Soft Actor-Critic (SAC) agent is employed at the SDN controller. This agent learns a sequential decision-making policy for mapping virtual nodes to physical edge servers and virtual links to network paths. To guide the agent towards efficient resource utilization, we define the reward for each successful embedding as the long-term revenue-to-cost ratio. By learning to maximize this reward, the agent is naturally driven to find economically viable allocation strategies. Comprehensive simulation experiments demonstrate that our SAC-based VNE approach significantly outperforms other baselines across key metrics, affirming its efficacy in dynamic SDEN environments. © 2026 by the authors.

## 04 — Title Screening

**Title:** Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Task Offloading Based on Virtual Network Embedding in Software-Defined Edge Networks: A Deep Reinforcement Learning Approach
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
