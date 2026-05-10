---
id: "paper-548"
title: "Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT"
authors: ["Al-Maslamani, Noora Mohammed", "Abdallah, Mohamed", "Ciftler, Bekir Sait"]
year: 2023
venue: "IEEE Open Journal of the Communications Society"
venue_type: "journal"
doi: "10.1109/OJCOMS.2023.3280359"
url: "https://www.scopus.com/pages/publications/85161555519?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1274--1284"
keywords: ["Deep reinforcement learning", "hierarchical federated learning", "neural networks", "poisoning attack", "reputation management"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-548 — Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT

## Metadata

- **Authors:** Al-Maslamani, Noora Mohammed and Abdallah, Mohamed and Ciftler, Bekir Sait
- **Year:** 2023
- **Venue:** IEEE Open Journal of the Communications Society
- **DOI:** 10.1109/OJCOMS.2023.3280359
- **URL:** https://www.scopus.com/pages/publications/85161555519?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1274--1284
- **Language:** English
- **Keywords:** Deep reinforcement learning; hierarchical federated learning; neural networks; poisoning attack; reputation management

### Abstract

Aiming at protecting device data privacy, Federated Learning (FL) is a framework of distributed machine learning in which devices' local model parameters are exchanged with a centralized server without revealing the actual data. Hierarchical Federated Learning (HFL) framework was introduced to improve FL communication efficiency where devices are clustered and seek model consensus with the support of edge servers (e.g., base stations). Devices in a cluster submit their local model updates to their assigned local edge server for aggregation at each iteration. The edge servers transmit the aggregated models to a centralized server and establish a global consensus. However, similar to FL, adversaries may threaten the security and privacy of HFL. The client devices within a cluster may deliberately provide unreliable local model updates through poisoning attacks or poor-quality model updates due to inconsistent communication channels, increased device mobility, or inadequate device resources. To address the above challenges, this paper investigates the client selection problem in the HFL framework to eliminate the impact of unreliable clients while maximizing the global model accuracy of HFL. Each FL edge server is equipped with a Deep Reinforcement Learning (DRL)-based reputation model to optimally measure the reliability and trustworthiness of FL workers within its cluster. A Multi-Agent Deep Deterministic Policy Gradient (MADDPG) is utilized to enhance the accuracy and stability of the HFL global model, given the workers' dynamic behaviors in the HFL environment. The experimental results indicate that our proposed MADDPG improves the accuracy and stability of HFL compared with the conventional reputation model and single-agent DDPG-based reputation model.  © 2020 IEEE.

## 04 — Title Screening

**Title:** Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Reputation-Aware Multi-Agent DRL for Secure Hierarchical Federated Learning in IoT
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
