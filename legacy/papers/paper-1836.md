---
id: "paper-1836"
title: "GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks"
authors: ["Liang, Ruihuai", "Yang, Bo", "Chen, Pengyu", "Cao, Xuelin", "Yu, Zhiwen", "Debbah, Merouane", "Niyato, Dusit", "Poor, H. Vincent", "Yuen, Chau"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3568248"
url: "https://www.scopus.com/pages/publications/105005424986?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10264--10277"
keywords: ["computation offloading", "generative AI", "graph diffusion", "Multi-access edge computing", "network optimization"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1836 — GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks

## Metadata

- **Authors:** Liang, Ruihuai and Yang, Bo and Chen, Pengyu and Cao, Xuelin and Yu, Zhiwen and Debbah, Merouane and Niyato, Dusit and Poor, H. Vincent and Yuen, Chau
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3568248
- **URL:** https://www.scopus.com/pages/publications/105005424986?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10264--10277
- **Language:** English
- **Keywords:** computation offloading; generative AI; graph diffusion; Multi-access edge computing; network optimization

### Abstract

Optimization is crucial for the efficiency and reliability of multi-access edge computing (MEC) networks. Many optimization problems in this field are NP-hard and do not have effective approximation algorithms. Consequently, there is often a lack of optimal (ground-truth) data, which limits the effectiveness of traditional deep learning approaches. Most existing learning-based methods require a large amount of optimal data and do not leverage the potential advantages of using suboptimal data, which can be obtained more efficiently. To illustrate this point, we focus on the multi-server multi-user computation offloading (MSCO) problem, a common issue in MEC networks that lacks efficient optimal solution methods. In this paper, we introduce the graph diffusion-based solution generator (GDSG), designed to work with suboptimal datasets while still achieving convergence to the optimal solution with high probability. We reformulate the network optimization challenge as a distribution-learning problem and provide a clear explanation of how to learn from suboptimal training datasets. We develop GDSG, a multi-task diffusion generative model that employs a graph neural network (GNN) to capture the distribution of high-quality solutions. Our approach includes a straightforward and efficient heuristic method to generate a sufficient amount of training data composed entirely of suboptimal solutions. In our implementation, we enhance the GNN architecture to achieve better generalization. Moreover, the proposed GDSG can achieve nearly 100% task orthogonality, which helps prevent negative interference between the discrete and continuous solution generation training objectives. We demonstrate that this orthogonality arises from the diffusion-related training loss in GDSG, rather than from the GNN architecture itself. Finally, our experiments show that the proposed GDSG outperforms other benchmark methods on both optimal and suboptimal training datasets. Regarding the minimization of computation offloading costs, GDSG achieves savings of up to 56.62% on the ground-truth training set and 41.06% on the suboptimal training set compared to existing discriminative methods. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** GDSG: Graph Diffusion-Based Solution Generator for Optimization Problems in MEC Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
