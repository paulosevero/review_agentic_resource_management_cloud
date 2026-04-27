---
id: "paper-1538"
title: "Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data"
authors: ["Doostmohammadian, Mohammadreza", "Qureshi, Muhammad I.", "Hossein Khalesi, Mohammad", "Rabiee, Hamid R.", "Khan, Usman A."]
year: 2025
venue: "IEEE Transactions on Automation Science and Engineering"
venue_type: "journal"
doi: "10.1109/TASE.2025.3526967"
url: "https://www.scopus.com/pages/publications/105003042085?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "10948--10959"
keywords: ["data classification", "Distributed algorithm", "graph theory", "optimization", "quantization"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1538 — Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data

## Metadata

- **Authors:** Doostmohammadian, Mohammadreza and Qureshi, Muhammad I. and Hossein Khalesi, Mohammad and Rabiee, Hamid R. and Khan, Usman A.
- **Year:** 2025
- **Venue:** IEEE Transactions on Automation Science and Engineering
- **DOI:** 10.1109/TASE.2025.3526967
- **URL:** https://www.scopus.com/pages/publications/105003042085?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 10948--10959
- **Language:** English
- **Keywords:** data classification; Distributed algorithm; graph theory; optimization; quantization

### Abstract

Decentralized strategies are of interest for learning from large-scale data over networks. This paper studies learning over a network of geographically distributed nodes/agents subject to quantization. Each node possesses a private local cost function, collectively contributing to a global cost function, which the considered methodology aims to minimize. In contrast to many existing papers, the information exchange among nodes is log-quantized to address limited network-bandwidth in practical situations. We consider a first-order computationally efficient distributed optimization algorithm (with no extra inner consensus loop) that leverages node-level gradient correction based on local data and network-level gradient aggregation only over nearby nodes. This method only requires balanced networks with no need for stochastic weight design. It can handle log-scale quantized data exchange over possibly time-varying and switching network setups. We study convergence over both structured networks (for example, training over data-centers) and ad-hoc multi-agent networks (for example, training over dynamic robotic networks). Through experimental validation, we show that (i) structured networks generally result in a smaller optimality gap, and (ii) log-scale quantization leads to a smaller optimality gap compared to uniform quantization. © 2004-2012 IEEE.

## 04 — Title Screening

**Title:** Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Log-Scale Quantization in Distributed First-Order Methods: Gradient-Based Learning From Distributed Data
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
