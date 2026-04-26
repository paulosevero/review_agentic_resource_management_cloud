---
id: "paper-660"
title: "SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization"
authors: ["Liu, Pengtao", "An, Kang", "Lei, Jing", "Liu, Wei", "Sun, Yifu", "Zheng, Gan", "Chatzinotas, Symeon"]
year: 2023
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2023.3242422"
url: "https://www.scopus.com/pages/publications/85148425842?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "7987--8003"
keywords: ["binary offloading", "Internet of things", "multi-access edge computing (MEC)", "partial offloading", "resource management", "sparse code multiple access (SCMA)"]
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

# paper-660 — SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization

## Metadata

- **Authors:** Liu, Pengtao and An, Kang and Lei, Jing and Liu, Wei and Sun, Yifu and Zheng, Gan and Chatzinotas, Symeon
- **Year:** 2023
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2023.3242422
- **URL:** https://www.scopus.com/pages/publications/85148425842?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 7987--8003
- **Language:** English
- **Keywords:** binary offloading; Internet of things; multi-access edge computing (MEC); partial offloading; resource management; sparse code multiple access (SCMA)

### Abstract

Multi-access edge computing (MEC) is regarded as a promising approach for providing resource-constrained mobile devices with computing resources through task offloading. Sparse code multiple access (SCMA) is a code-domain non-orthogonal multiple access (NOMA) scheme that can meet the demands of multi-cell MEC networks for high data transmission rates and massive connections. In this paper, we propose an optimization framework for SCMA-enabled multi-cell MEC networks. The joint resource allocation and computation offloading problem is formulated to minimize the system cost, which is defined as the weighted energy cost and latency. Due to the nonconvexity of the proposed optimization problem induced by the coupled optimization variables, we first propose an algorithm based on the block coordinate descent (BCD) method to iteratively optimize the transmit power and edge computing resources allocation by deriving closed-form solutions, and further develop an improved low-complexity simulated annealing (SA) algorithm to solve the computation offloading and multi-cell SCMA codebook allocation problem. To solve the problem of partial state observation and timely decision-making in long-term optimization environment, we put forward a multiagent deep deterministic policy gradient (MADDPG) algorithm with centralized training and distributed execution. Furthermore, we extend the framework to the partial offloading case and propose an algorithm based on alternating convex search for solving the task offloading ratio. Numerical results show that the proposed multi-cell SCMA-MEC scheme achieves lower energy consumption and system latency in comparison to the orthogonal frequency division multiple access (OFDMA) and power-domain (PD) NOMA techniques.  © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** SCMA-Enabled Multi-Cell Edge Computing Networks: Design and Optimization
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
