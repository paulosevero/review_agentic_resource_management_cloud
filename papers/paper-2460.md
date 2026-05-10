---
id: paper-2460
title: 'IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks'
authors:
- Zhao, Taiyin
- Chen, Tian
- Sun, Yudong
- Xu, Yi
venue: Symmetry
venue_type: journal
year: 2025
doi: 10.3390/sym17040525
url: https://www.scopus.com/pages/publications/105003677061?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- graph neural networks
- interface matching
- microservice dependency graph
- recommendation system
- workflow orchestration
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-2460 — IM-GNN: Microservice Orchestration Recommendation via Interface-Matched Dependency Graphs and Graph Neural Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Microservice workflow orchestration recommendation aims to streamline business process construction by suggesting relevant microservices, yet existing methods relying on functional similarity in dependency graphs prove inadequate. Traditional graphs cluster functionally analogous microservices, neglecting execution-order dependencies critical for orchestration. This paper introduces a novel interface-matching-based approach to construct microservice dependency graphs, addressing the incompatibility of current methods with orchestration scenarios. The proposed method leverages a TF-WF-IDF algorithm and language models to extract input–output representations from microservice documentation, followed by interface-matching algorithms to establish call dependencies. By capturing the inherent structural symmetry in microservice interactions, where balanced and reciprocal relationships between inputs and outputs guide service connectivity, our approach enhances the fidelity of dependency graphs. Building on this graph, we present IM-GNN, a graph neural network-based recommendation model that generates microservice embeddings and computes node similarities to recommend orchestration candidates. Experiments on Amazon’s SageMaker and Comprehend datasets validate the model’s effectiveness, demonstrating superior recommendation accuracy compared to traditional methods. Key contributions include the interface-driven graph construction framework, the IM-GNN model, and empirical insights into hyperparameter impacts. This work bridges the gap between dependency graph quality and orchestration needs, offering a foundation for integrating deep learning with microservice workflow design while highlighting the role of symmetry in structuring service dependencies and optimizing orchestration patterns. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2460.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
