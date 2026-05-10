---
id: "paper-1328"
title: "Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning"
authors: ["Zhang, Fan", "Han, Guangjie", "Liu, Li", "Zhang, Yu", "Peng, Yan", "Li, Chao"]
year: 2024
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2023.3306803"
url: "https://www.scopus.com/pages/publications/85168749751?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5526--5544"
keywords: ["Cooperative task offloading (TO)", "improved soft actor-critic (SAC)", "Industrial Internet of Things (IIoT)", "multiagent deep reinforcement learning (MADRL)", "resource allocation (RA)"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1328 — Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning

## Metadata

- **Authors:** Zhang, Fan and Han, Guangjie and Liu, Li and Zhang, Yu and Peng, Yan and Li, Chao
- **Year:** 2024
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2023.3306803
- **URL:** https://www.scopus.com/pages/publications/85168749751?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5526--5544
- **Language:** English
- **Keywords:** Cooperative task offloading (TO); improved soft actor-critic (SAC); Industrial Internet of Things (IIoT); multiagent deep reinforcement learning (MADRL); resource allocation (RA)

### Abstract

Edge computing has become increasingly important to fulfill the diversified Quality-of-Service (QoS) or Quality-of-Experience (QoE) demands for Industrial Internet of Things (IIoT) applications, such as machine condition monitoring, fault diagnosis, intelligent production scheduling, and production quality control. Due to the heterogeneity of IIoT systems, it is of urgent necessity to concentrate on the cloud-edge-end cooperative partial task offloading and resource allocation (CPTORA) problem for realizing workload balancing, efficient resource utilization, and better QoS/QoE of IIoT applications. However, the challenge lies in how to make real-time, accurate, decentralized task offloading (TO) and resource allocation (RA) decisions for dynamic and device-intensive IIoT. Therefore, this work examines the CPTORA problem for IIoT, aiming at minimizing its long-run overall delay and energy costs. To lower the problem complexity, this problem is decomposed into the TO subproblem and the RA subproblem. Then, an improved soft actor-critic-based decentralized multiagent deep reinforcement learning (MADRL) algorithm is proposed to address the TO subproblem, where each IIoT device can learn its globally optimal policy and make its decisions independently. This algorithm innovatively combines the divergence regularization, the distributional reinforcement learning, and the value function decomposition methods to improve convergence speed and accuracy of the existing MADRL methods. After receiving the TO decisions of every IIoT device, every edge server employs the Lagrange multiplier method and Karush-Kuhn-Tucker condition to solve its RA subproblem. The experimental results show that the proposed algorithm decreases the overall delay and energy costs more effectively, compared to the other state-of-the-art MADRL approaches.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Cooperative Partial Task Offloading and Resource Allocation for IIoT Based on Decentralized Multiagent Deep Reinforcement Learning
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
