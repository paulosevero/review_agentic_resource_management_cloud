---
id: "paper-1151"
title: "Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing"
authors: ["Rafiq, Ahsan", "Wei, Min", "Wang, Ping", "Jain, Deepak Kumar"]
year: 2024
venue: "IEEE Transactions on Consumer Electronics"
venue_type: "journal"
doi: "10.1109/TCE.2024.3414324"
url: "https://www.scopus.com/pages/publications/85196510264?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5911--5928"
keywords: ["6TiSCH", "and migration", "artificial intelligence (AI)", "edge computing", "federated learning (FL)", "hybrid scheduling", "Industrial Internet of Things (IIoT)"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-1151 — Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing

## Metadata

- **Authors:** Rafiq, Ahsan and Wei, Min and Wang, Ping and Jain, Deepak Kumar
- **Year:** 2024
- **Venue:** IEEE Transactions on Consumer Electronics
- **DOI:** 10.1109/TCE.2024.3414324
- **URL:** https://www.scopus.com/pages/publications/85196510264?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5911--5928
- **Language:** English
- **Keywords:** 6TiSCH; and migration; artificial intelligence (AI); edge computing; federated learning (FL); hybrid scheduling; Industrial Internet of Things (IIoT)

### Abstract

Standardizing the Industrial Internet of Things (IIoT) with 6TiSCH enables the IIoT nodes to utilize low power with high reliability. It ensures the allocation of resources for IIoT nodes with minimal power consumption. The existing work focused on various issues in the 6TiSCH-based IIoT in terms of network formation, and scheduling. However, security, energy efficiency, and latency remain challenging issues. The aforementioned issues are resolved by adopting different technologies in the 6TiSCH IIoT environment such as edge computing and federated learning named AIFed-6TiSCH IIoT. In the 6TiSCH layer, all IIoT nodes are authenticated to the Trusted Authority (TA) to reduce unwanted malicious traffic using Hybrid Authentication Algorithm (HAS) named Mchacha-poly 1305 algorithm based on several credentials. The authenticated nodes are allowed to form the network, for that we utilized a multicast CORONA-based DODAG structure using the Dijkstra algorithm. Eventually, new node joining is initiated by an already joined node which transmits Enhanced Beacons (EBs) in adaptive time intervals for synchronizing the new node. The synchronized nodes aim to select the optimal parent for transmitting data to the root node using an Enhanced Sea Gull (ESG) optimization algorithm based on mobility and several information. After that, optimal channel selection and scheduling are done using a Multi Criteria Decision Making (MCDM) algorithm named TOPSIS and a hybrid scheduling algorithm (i.e., Autonomous, and centralized scheduling) based on federated learning. By Performing channel selection, the congestion rate is reduced and federated learning ensures privacy and communication reliability. In the edge layer, data from the root are forwarded via a smart gateway to the edge servers for local processing. The security and latency issues in the edge layer are mitigated by performing Deep Reinforcement Learning (DRL) based migration named Enhanced Multi-Agent Deep Deterministic Policy Gradient (EMADDPG) that runs based on three policies. In addition, a virtual edge server is deployed in case of excess search time and overloading. The simulation of the proposed work is carried out using Cooja simulation based on Contiki 3x OS, and the simulation results are validated with existing works in terms of several validation metrics. The validation results show that the proposed work outperforms the existing works.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Delay Aware 6TiSCH IIoT Networks for Energy Efficient Data Transmission by Adopting Federated Learning and Edge Computing
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
