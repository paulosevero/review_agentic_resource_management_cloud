---
id: "paper-858"
title: "Fault Tolerance Oriented SFC Optimization in SDN/NFV-Enabled Cloud Environment Based on Deep Reinforcement Learning"
authors: ["Chen, Jing", "Chen, Jia", "Guo, Kuo", "Hu, Renkun", "Zou, Tao", "Zhu, Jun", "Zhang, Hongke", "Liu, Jingjing"]
year: 2024
venue: "IEEE Transactions on Cloud Computing"
venue_type: "journal"
doi: "10.1109/TCC.2024.3357061"
url: "https://www.scopus.com/pages/publications/85183651963?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "200--218"
keywords: ["deep reinforcement learning", "elastic optimization", "fault-tolerant", "quality of service", "Service function chain"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-858 — Fault Tolerance Oriented SFC Optimization in SDN/NFV-Enabled Cloud Environment Based on Deep Reinforcement Learning

## Metadata

- **Authors:** Chen, Jing and Chen, Jia and Guo, Kuo and Hu, Renkun and Zou, Tao and Zhu, Jun and Zhang, Hongke and Liu, Jingjing
- **Year:** 2024
- **Venue:** IEEE Transactions on Cloud Computing
- **DOI:** 10.1109/TCC.2024.3357061
- **URL:** https://www.scopus.com/pages/publications/85183651963?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 200--218
- **Language:** English
- **Keywords:** deep reinforcement learning; elastic optimization; fault-tolerant; quality of service; Service function chain

### Abstract

In software defined network/network function virtualization (SDN/NFV)-enabled cloud environment, cloud services can be implemented as service function chains (SFCs), which consist of a series of ordered virtual network functions. However, due to fluctuations of cloud traffic and without knowledge of cloud computing network configuration, designing SFC optimization approach to obtain flexible cloud services in dynamic cloud environment is a pivotal challenge. In this paper, we propose a fault tolerance oriented SFC optimization approach based on deep reinforcement learning. We model fault tolerance oriented SFC elastic optimization problem as a Markov decision process, in which the reward is modeled as a weighted function, including minimizing energy consumption and migration cost, maximizing revenue benefit and load balancing. Then, taking binary integer programming model as constraints of quality of cloud services, we design optimization approaches for single-agent double deep Q-network (SADDQN) and multi-agent DDQN (MADDQN). Among them, MADDQN decentralizes training tasks from control plane to data plane to reduce the probability of single point of failure for the centralized controller. Experimental results show that the designed approaches have better performance. MADDQN can almost reach the upper bound of theoretical solution obtained by assuming a prior knowledge of the dynamics of cloud traffic.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Fault Tolerance Oriented SFC Optimization in SDN/NFV-Enabled Cloud Environment Based on Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Fault Tolerance Oriented SFC Optimization in SDN/NFV-Enabled Cloud Environment Based on Deep Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Fault Tolerance Oriented SFC Optimization in SDN/NFV-Enabled Cloud Environment Based on Deep Reinforcement Learning
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
