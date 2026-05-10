---
id: "paper-827"
title: "Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G"
authors: ["Ayepah-Mensah, Daniel", "Sun, Guolin", "Boateng, Gordon Owusu", "Anokye, Stephen", "Liu, Guisong"]
year: 2024
venue: "IEEE/ACM Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TNET.2023.3297390"
url: "https://www.scopus.com/pages/publications/85166743615?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "654--669"
keywords: ["5G", "Blockchain", "federated learning", "network slicing", "peer-to-peer resource trading", "privacy-preserving", "resource trading", "Stackelberg game"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-827 — Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G

## Metadata

- **Authors:** Ayepah-Mensah, Daniel and Sun, Guolin and Boateng, Gordon Owusu and Anokye, Stephen and Liu, Guisong
- **Year:** 2024
- **Venue:** IEEE/ACM Transactions on Networking
- **DOI:** 10.1109/TNET.2023.3297390
- **URL:** https://www.scopus.com/pages/publications/85166743615?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 654--669
- **Language:** English
- **Keywords:** 5G; Blockchain; federated learning; network slicing; peer-to-peer resource trading; privacy-preserving; resource trading; Stackelberg game

### Abstract

Radio Access Network (RAN) slicing enables resource sharing among multiple tenants and is an essential feature for next-generation mobile networks. Usually, a centralized controller aggregates available resource pools from multiple tenants to increase spectrum availability. In dynamic resource allocation, a tenant could behave strategically by adjusting its preferences based on perceived conditions to maximize its utility. Slice tenants may lie about the resources needed to gain greater utility. Such behavior could lead to poor resource utilization due to excess resources acquired by lying tenants and resource shortages because slice tenants choose not to purchase high-priced resources to save costs. Furthermore, in a scenario with many slice tenants, the centralized controller can become overwhelmed by the number of requests. This, in turn, can lead to slower response times and higher latency, resulting in poor resource utilization and QoS performance of slice tenants. Therefore, this paper proposes a peer-to-peer (P2P) approach to resource trading, where slice tenants communicate directly instead of relying on a centralized orchestrator. This design is motivated by the need for slice tenants to collaborate effectively. We model the interaction between tenants in a Stackelberg multi-leader and multi-follower game and solve the game with multi-agent deep reinforcement learning with an incentive-reward model to achieve the Stackelberg equilibrium. Furthermore, we propose a decentralized resource trading framework by integrating blockchain technology and federated deep reinforcement learning, enabling network tenants to perform inter-slice resource sharing securely. The simulation results show that the proposed mechanism has significant performance improvements over existing implementations.  © 1993-2012 IEEE.

## 04 — Title Screening

**Title:** Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.5
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Blockchain-Enabled Federated Learning-Based Resource Allocation and Trading for Network Slicing in 5G
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
