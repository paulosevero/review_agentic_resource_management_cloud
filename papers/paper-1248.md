---
id: "paper-1248"
title: "Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks"
authors: ["Wang, Zixin", "Zhou, Yong", "Shi, Yuanming", "Letaief, Khaled. B."]
year: 2024
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM52923.2024.10901572"
url: "https://www.scopus.com/pages/publications/105000834215?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3063--3068"
keywords: ["Edge computing", "Frequency allocation", "Integer programming", "Learning to rank", "Mixed-integer linear programming", "Problem oriented languages", "Resource allocation", "Critical challenges", "Device scheduling", "Distributed data", "Fine tuning", "Fine-tuning methods", "Global models", "Language model", "Learning performance", "On-line algorithms", "Radio resources", "Bandwidth"]
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
    human_justification: "LLM as workload"

---

# paper-1248 — Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks

## Metadata

- **Authors:** Wang, Zixin and Zhou, Yong and Shi, Yuanming and Letaief, Khaled. B.
- **Year:** 2024
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM52923.2024.10901572
- **URL:** https://www.scopus.com/pages/publications/105000834215?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3063--3068
- **Language:** English
- **Keywords:** Edge computing; Frequency allocation; Integer programming; Learning to rank; Mixed-integer linear programming; Problem oriented languages; Resource allocation; Critical challenges; Device scheduling; Distributed data; Fine tuning; Fine-tuning methods; Global models; Language model; Learning performance; On-line algorithms; Radio resources; Bandwidth

### Abstract

Low-rank adaptation (LoRA) is an emerging fine-tuning method for personalized large language models (LLMs) due to its capability of achieving comparable learning performance to full fine-tuning by training a much smaller number of parameters. Federated fine-tuning (FedFT) combines LoRA with federated learning (FL) to enable collaborative fine-tuning of a global model with edge devices, leveraging distributed data while ensuring privacy. However, limited radio resources and computation capabilities of edge devices pose critical challenges on deploying FedFT over wireless networks. In this paper, we propose a split FedFT framework to separately deploy the computationally-intensive encoder of a pre-trained model at the edge server while reserving the embedding and the task modules at the edge devices, where the information exchanges between these modules are carried out over wireless networks. By exploiting the low-rank property of LoRA, the proposed FedFT framework reduces communication overhead by aggregating the gradient of the task module with respect to the output of a low-rank matrix. To enhance learning performance under stringent resource constraints, we formulate a joint device scheduling and bandwidth allocation problem while considering average transmission delay. By applying the Lyapunov technique, we decompose the formulated long-term mixed-integer programming (MIP) problem into sequential subproblems, followed by developing an online algorithm for effective device scheduling and bandwidth allocation. Simulation results demonstrate the effectiveness of our proposed online algorithm in enhancing learning performance. © 2024 IEEE.

## 04 — Title Screening

**Title:** Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Federated Low-Rank Adaptation for Large Language Model Fine-Tuning Over Wireless Networks
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
