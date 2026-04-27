---
id: "paper-2460"
title: "IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks"
authors: ["Zhao, Taiyin", "Chen, Tian", "Sun, Yudong", "Xu, Yi"]
year: 2025
venue: "Symmetry"
venue_type: "journal"
doi: "10.3390/sym17040525"
url: "https://www.scopus.com/pages/publications/105003677061?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["graph neural networks", "interface matching", "microservice dependency graph", "recommendation system", "workflow orchestration"]
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

# paper-2460 — IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks

## Metadata

- **Authors:** Zhao, Taiyin and Chen, Tian and Sun, Yudong and Xu, Yi
- **Year:** 2025
- **Venue:** Symmetry
- **DOI:** 10.3390/sym17040525
- **URL:** https://www.scopus.com/pages/publications/105003677061?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** graph neural networks; interface matching; microservice dependency graph; recommendation system; workflow orchestration

### Abstract

Microservice workflow orchestration recommendation aims to streamline business process construction by suggesting relevant microservices, yet existing methods relying on functional similarity in dependency graphs prove inadequate. Traditional graphs cluster functionally analogous microservices, neglecting execution-order dependencies critical for orchestration. This paper introduces a novel interface-matching-based approach to construct microservice dependency graphs, addressing the incompatibility of current methods with orchestration scenarios. The proposed method leverages a TF-WF-IDF algorithm and language models to extract input–output representations from microservice documentation, followed by interface-matching algorithms to establish call dependencies. By capturing the inherent structural symmetry in microservice interactions, where balanced and reciprocal relationships between inputs and outputs guide service connectivity, our approach enhances the fidelity of dependency graphs. Building on this graph, we present IM-GNN, a graph neural network-based recommendation model that generates microservice embeddings and computes node similarities to recommend orchestration candidates. Experiments on Amazon’s SageMaker and Comprehend datasets validate the model’s effectiveness, demonstrating superior recommendation accuracy compared to traditional methods. Key contributions include the interface-driven graph construction framework, the IM-GNN model, and empirical insights into hyperparameter impacts. This work bridges the gap between dependency graph quality and orchestration needs, offering a foundation for integrating deep learning with microservice workflow design while highlighting the role of symmetry in structuring service dependencies and optimizing orchestration patterns. © 2025 by the authors.

## 04 — Title Screening

**Title:** IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks
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
