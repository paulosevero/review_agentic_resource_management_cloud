---
id: "paper-1671"
title: "Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence"
authors: ["Huang, Hebin", "Liang, Junbin", "Min, Geyong"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3586793"
url: "https://www.scopus.com/pages/publications/105010316243?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12726--12741"
keywords: ["DNN inference", "Edge intelligence", "mobile edge computing", "reinforcement learning", "service deployment"]
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

# paper-1671 — Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence

## Metadata

- **Authors:** Huang, Hebin and Liang, Junbin and Min, Geyong
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3586793
- **URL:** https://www.scopus.com/pages/publications/105010316243?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12726--12741
- **Language:** English
- **Keywords:** DNN inference; Edge intelligence; mobile edge computing; reinforcement learning; service deployment

### Abstract

Edge intelligence is an emerging paradigm in edge computing that deploys Deep Neural Network (DNN) models on edge servers with limited storage and computation capacities to provide inference services for high mobility and real-time applications, such as autonomous driving or smart surveillance, with varying accuracy and delay requirements. Adapting application configurations (e.g., image resolution or video frame rate) while selecting different DNN models and deployment locations can provide high-accuracy, low-delay inference services that meet user requirements. However, the configurations and DNN models of various inference services are highly heterogeneous. As balancing inference accuracy, resource cost, and delay is a multi-objective programming problem, it is a great challenge to obtain the optimal solution. To address this challenge, we propose a novel online framework to jointly optimize the configuration adaption, DNN model selection, and deployment for heterogeneous inference services. Specifically, we first formulate this joint optimization problem as an integer linear programming problem and prove it is NP-hard. Then, we further model the problem as a Partial Observable Markov Decision Process (POMDP) and solve it by developing a Heterogeneous-Agent Reinforcement Learning (HARL) based algorithm, named Heterogeneous Inference Service ProvidER (HISPER). It allows agents to have different action spaces corresponding to different types of configurations and DNN models. Finally, extensive experiments demonstrate that the proposed algorithm outperforms other state-of-the-art counterparts. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint DNN Model Deployment, Selection, and Configuration for Heterogeneous Inference Services Toward Edge Intelligence
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
