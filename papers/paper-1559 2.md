---
id: "paper-1559"
title: "MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning"
authors: ["Fan, Wenhao", "Chen, Penghui", "Chun, Xiongfei", "Liu, Yuan'an"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3530482"
url: "https://www.scopus.com/pages/publications/85215382734?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5324--5341"
keywords: ["Edge computing", "machine learning", "multi-agent reinforcement learning", "resource management", "split federated learning"]
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

# paper-1559 — MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning

## Metadata

- **Authors:** Fan, Wenhao and Chen, Penghui and Chun, Xiongfei and Liu, Yuan'an
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3530482
- **URL:** https://www.scopus.com/pages/publications/85215382734?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5324--5341
- **Language:** English
- **Keywords:** Edge computing; machine learning; multi-agent reinforcement learning; resource management; split federated learning

### Abstract

Split Federated Learning (SFL) has emerged as a promising paradigm to enhance FL by partitioning the Machine Learning (ML) model into parts and deploying them across clients and servers, effectively mitigating the workload on resource-constrained devices and preserving privacy. Compared to cloud-device-based and edge-device-based SFL, cloud-edge-device collaborative SFL offers both lower communication latency and wider network coverage. However, existing works adopt a uniform model partitioning strategy for different devices, ignoring the heterogeneous nature of device resources. This oversight leads to severe straggler problems, making the training process inefficient. Moreover, they do not consider joint optimization of model aggregation control and computing and communication resource allocation, and lack distributed algorithm design. To address these issues, we propose a joint resource management scheme for cloud-edge-device collaborative SFL to optimize the training latency and energy consumption of all devices. In our scheme, the partitioning strategy is optimized for each device based on resource heterogeneity. Meanwhile, we jointly optimize the aggregation frequency of ML models, computing resource allocation for all devices and edge servers, and transmit power allocation for all devices. We formulate a coordination game among all edge servers and then design a distributed optimization algorithm employing partially observable Multi-Agent Deep Reinforcement Learning (MADRL) with integrated numerical methods. Extensive experiments are conducted to validate the convergence of our algorithm and demonstrate the superiority of our scheme via evaluations under multiple scenarios and in comparison with four reference schemes. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MADRL-Based Model Partitioning, Aggregation Control, and Resource Allocation for Cloud-Edge-Device Collaborative Split Federated Learning
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
