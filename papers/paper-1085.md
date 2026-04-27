---
id: "paper-1085"
title: "Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks"
authors: ["Men, Rui", "Fan, Xiumei", "Yau, Kok-Lim Alvin", "Shan, Axida", "Yuan, Gang"]
year: 2024
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2024.3391382"
url: "https://www.scopus.com/pages/publications/85193244954?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3891--3904"
keywords: ["aerial computing", "lyapunov optimization", "MARL", "resource allocation", "Task offloading"]
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

# paper-1085 — Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks

## Metadata

- **Authors:** Men, Rui and Fan, Xiumei and Yau, Kok-Lim Alvin and Shan, Axida and Yuan, Gang
- **Year:** 2024
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2024.3391382
- **URL:** https://www.scopus.com/pages/publications/85193244954?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3891--3904
- **Language:** English
- **Keywords:** aerial computing; lyapunov optimization; MARL; resource allocation; Task offloading

### Abstract

The upsurge of mobile service demands underscores the inevitability of the emergence of 6G technology. Amidst the challenges that accompany the 6G networks, the exponential growth of computation-intensive and delay-sensitive applications in vehicular networks poses a significant hurdle. Vehicular edge computing relying solely on terrestrial infrastructures cannot meet the performance requirements due to insufficient resources in edge servers. To address this challenge, we introduce a novel three-layer hierarchical architecture called the air-ground-end aerial computing (AGEAC) architecture, which consists of three types of resource providers, namely high-altitude platform stations, roadside units, and volunteer vehicles willing to share their underutilized resources. We select service vehicles based on the utilization rate of their underutilized resources to ensure fairness. Our objective is to minimize the average latency of all tasks in the long term, and it is formulated as a mixed-integer nonlinear programming problem for task offloading and resource allocation. The complicated intertwined problem is decomposed into four sub-problems by leveraging Lyapunov optimization method. A multi-agent reinforcement learning-based algorithm is designed to make offloading decisions, and convex optimization is introduced to allocate resources iteratively. Extensive simulations have been conducted to demonstrate the superiority of AGEAC in terms of convergence speed, average latency, and resource utilization.  © 2013 IEEE.

## 04 — Title Screening

**Title:** Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Hierarchical Aerial Computing for Task Offloading and Resource Allocation in 6G-Enabled Vehicular Networks
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
