---
id: "paper-2262"
title: "Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks"
authors: ["Wang, Zixin", "Zhou, Yong", "Shi, Yuanming", "Letaief, Khaled B."]
year: 2025
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2025.3531128"
url: "https://www.scopus.com/pages/publications/105002494727?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3450--3464"
keywords: ["Federated learning", "parameter-efficient fine-tuning", "pre-trained foundation model", "resource allocation"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2262 — Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks

## Metadata

- **Authors:** Wang, Zixin and Zhou, Yong and Shi, Yuanming and Letaief, Khaled B.
- **Year:** 2025
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2025.3531128
- **URL:** https://www.scopus.com/pages/publications/105002494727?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3450--3464
- **Language:** English
- **Keywords:** Federated learning; parameter-efficient fine-tuning; pre-trained foundation model; resource allocation

### Abstract

Pre-trained foundation models (FMs), with extensive number of neurons, are key to advancing next-generation intelligence services, where personalizing these models requires massive amount of task-specific data and computational resources. The prevalent solution involves centralized processing at the edge server, which, however, raises privacy concerns due to the transmission of raw data. Instead, federated fine-tuning (FedFT) is an emerging privacy-preserving fine-tuning (FT) paradigm for personalized pre-trained foundation models. In particular, by integrating low-rank adaptation (LoRA) with federated learning (FL), federated LoRA enables the collaborative FT of a global model with edge devices, achieving comparable learning performance to full FT while training fewer parameters over distributed data and preserving raw data privacy. However, the limited radio resources and computation capabilities of edge devices pose significant challenges for deploying 3 LoRA over wireless networks. To this paper, we propose a split federated LoRA framework, which deploys the computationally-intensive encoder of a pre-trained model at the edge server, while keeping the embedding and task modules at the edge devices. The information exchanges between these modules occur over wireless networks. Building on this split framework, the paper provides a rigorous analysis of the upper bound of the convergence gap for the wireless federated LoRA system. This analysis reveals the weighted impact of the number of edge devices participating in FedFT over all rounds, motivating the formulation of a long-term upper bound minimization problem. To address the long-term constraint, we decompose the formulated long-term mixed-integer programming (MIP) problem into sequential sub-problems using the Lyapunov technique. We then develop an online algorithm for effective device scheduling and bandwidth allocation. Simulation results demonstrate the effectiveness of the proposed online algorithm in enhancing learning performance. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Federated Fine-Tuning for Pre-Trained Foundation Models over Wireless Networks
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
