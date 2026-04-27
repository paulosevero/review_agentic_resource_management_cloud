---
id: "paper-1245"
title: "Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning"
authors: ["Wang, Yi-Xiao", "Tao, Wen-Jian", "Zhao, Shao-Peng", "Zhang, Yan-Ping"]
year: 2024
venue: "Computer-Aided Design and Applications"
venue_type: "journal"
doi: "10.14733/cadaps.2024.S9.265-276"
url: "https://www.scopus.com/pages/publications/85173561138?origin=resultslist"
publisher: "CAD Solutions, LLC"
pages: "265--276"
keywords: ["Computer-Aided Medical Systems", "Loading Balance", "MADDPG", "Multi-Agent Reinforcement Learning", "Service Mesh"]
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

# paper-1245 — Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning

## Metadata

- **Authors:** Wang, Yi-Xiao and Tao, Wen-Jian and Zhao, Shao-Peng and Zhang, Yan-Ping
- **Year:** 2024
- **Venue:** Computer-Aided Design and Applications
- **DOI:** 10.14733/cadaps.2024.S9.265-276
- **URL:** https://www.scopus.com/pages/publications/85173561138?origin=resultslist
- **Publisher:** CAD Solutions, LLC
- **Pages:** 265--276
- **Language:** English
- **Keywords:** Computer-Aided Medical Systems; Loading Balance; MADDPG; Multi-Agent Reinforcement Learning; Service Mesh

### Abstract

The service mesh is the most well-known framework for developing network applications because it separates governance and business logic in microservices and achieves unified governance of heterogeneous systems. The Service Mesh has a more complicated topology structure than the typical microservice design, which makes it harder to keep the load balance. The present Service Mesh load balancing technique is rather straightforward, merely taking into account the current load status of each individual node and disregarding the mutual load impact across nodes. This paper proposes a load balancing method based on multi-agent reinforcement learning to address the aforementioned issues. This method turns the Service Mesh load balancing problem into a random game process, builds an Actor-Critic network to simulate the service mesh multi-resource scheduling strategy, and uses the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm to determine the best multi-resource scheduling strategy. The Istio framework is utilized in this study to create a service mesh environment, and the test results demonstrate that the suggested approach can produce faster response times. © 2024, CAD Solutions, LLC. All rights reserved.

## 04 — Title Screening

**Title:** Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Enhancing Load Balancing in Computer-Aided Medical Systems Using Deep Reinforcement Learning
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
