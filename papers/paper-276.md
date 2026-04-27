---
id: "paper-276"
title: "Seek Common while Shelving Differences: Orchestrating Deep Neural Networks for Edge Service Provisioning"
authors: ["Chen, Lixing", "Xu, Jie"]
year: 2021
venue: "IEEE Journal on Selected Areas in Communications"
venue_type: "journal"
doi: "10.1109/JSAC.2020.3036953"
url: "https://www.scopus.com/pages/publications/85096392010?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "251--264"
keywords: ["deep reinforcement learning", "distributed optimization", "Edge computing", "multi-agent learning"]
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

# paper-276 — Seek Common while Shelving Differences: Orchestrating Deep Neural Networks for Edge Service Provisioning

## Metadata

- **Authors:** Chen, Lixing and Xu, Jie
- **Year:** 2021
- **Venue:** IEEE Journal on Selected Areas in Communications
- **DOI:** 10.1109/JSAC.2020.3036953
- **URL:** https://www.scopus.com/pages/publications/85096392010?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 251--264
- **Language:** English
- **Keywords:** deep reinforcement learning; distributed optimization; Edge computing; multi-agent learning

### Abstract

Edge computing (EC) platforms, which enable Application Service Providers (ASPs) to deploy applications in close proximity to users, are providing ultra-low latency and location-awareness to a rich portfolio of services. As monetary costs are incurred for renting computing resources on edge servers to enable service provisioning, ASP has to cautiously decide where to deploy the application and how much resources would be needed to deliver satisfactory performance. However, the service provisioning problem exhibits complex correlations with multifarious factors in EC systems, ranging from user behavior to computation offloading, which are difficult to be fully captured by mathematical modeling and also put off traditional machine learning techniques due to the induction of high-dimension state space. The recent success of deep learning (DL) underpins new tools for addressing our problem. While previous works provide valuable insights on applying DL techniques, e.g., distributed DL, deep reinforcement learning (DRL), and multi-agent DL, in EC systems, these techniques cannot solely handle the distributed and heterogeneous nature of EC systems. To address these limitations, we propose a novel framework based on multi-agent DRL, distributed neural network orchestration (N2O), and knowledge distilling. The multi-agent DRL enables edge servers to learn deep neural networks that shelve distinct features learned from local edge sites and hence caters to the heterogeneity of EC systems. N2O coordinates edge servers in a fully distributed manner toward a common goal of maximizing ASP's reward. It requires only local communications during execution and provides provable performance guarantees. The knowledge distilling is further utilized to distill the N2O policy for reducing the communication overhead and stabilizing the decision-making. We also carry out systematic experiments to show the advantages of our method over state-of-the-art alternatives. © 1983-2012 IEEE.

## 04 — Title Screening

**Title:** Seek Common while Shelving Differences: Orchestrating Deep Neural Networks for Edge Service Provisioning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Seek Common while Shelving Differences: Orchestrating Deep Neural Networks for Edge Service Provisioning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Seek Common while Shelving Differences: Orchestrating Deep Neural Networks for Edge Service Provisioning
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
