---
id: "paper-2874"
title: "DynaAdaFL: A GNN-Assisted MARL Framework for Client Hyperparameter Adaptive Optimization in Edge Federated Learning for Carbon Emission Prediction"
authors: ["Yan, Haotian", "Pan, Li", "Liu, Shijun", "Li, Weiping"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3661240"
url: "https://www.scopus.com/pages/publications/105029430557?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "17151--17168"
keywords: ["Carbon emission prediction", "edge computing", "federated learning (FL)", "graph neural networks (GNNs)", "hyperparameter optimization", "multiagent reinforcement learning (MARL)"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2874 — DynaAdaFL: A GNN-Assisted MARL Framework for Client Hyperparameter Adaptive Optimization in Edge Federated Learning for Carbon Emission Prediction

## Metadata

- **Authors:** Yan, Haotian and Pan, Li and Liu, Shijun and Li, Weiping
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3661240
- **URL:** https://www.scopus.com/pages/publications/105029430557?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 17151--17168
- **Language:** English
- **Keywords:** Carbon emission prediction; edge computing; federated learning (FL); graph neural networks (GNNs); hyperparameter optimization; multiagent reinforcement learning (MARL)

### Abstract

Accurate prediction of carbon emissions is crucial for formulating effective climate policies. However, building powerful prediction models requires large-scale data, which are often distributed across different regions and entities, leading to data silos and privacy concerns. Federated learning (FL) offers a promising privacy-preserving solution, yet its performance in edge environments is severely hampered by resource heterogeneity, which causes slow convergence and inefficiency when using fixed local training hyperparameters. To address this challenge, we propose DynaAdaFL, a graph neural network (GNN)-assisted multiagent reinforcement learning (MARL) framework for adaptive optimization of client hyperparameters in edge FL, specifically tailored for carbon emission prediction. DynaAdaFL leverages a GNN to model client relationships as a preprocessing layer for MARL, enabling each client to perceive neighboring states and adaptively adjust its local hyperparameters (learning rate and epochs). This approach optimizes the tradeoff between global model performance and training efficiency. Extensive experiments on carbon emission data from multiple regions demonstrate that DynaAdaFL not only achieves superior prediction accuracy but also significantly reduces the overall training time compared to various baselines and state-of-the-art methods, providing an efficient and practical solution for cross-regional collaborative carbon emission forecasting.  © 2014 IEEE.

## 04 — Title Screening

**Title:** DynaAdaFL: A GNN-Assisted MARL Framework for Client Hyperparameter Adaptive Optimization in Edge Federated Learning for Carbon Emission Prediction

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** DynaAdaFL: A GNN-Assisted MARL Framework for Client Hyperparameter Adaptive Optimization in Edge Federated Learning for Carbon Emission Prediction
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** DynaAdaFL: A GNN-Assisted MARL Framework for Client Hyperparameter Adaptive Optimization in Edge Federated Learning for Carbon Emission Prediction
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
