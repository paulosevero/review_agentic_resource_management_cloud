---
id: "paper-1042"
title: "Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks"
authors: ["Liang, Yuxin", "Yang, Peng", "He, Yuanyuan", "Lyu, Feng"]
year: 2024
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM52923.2024.10901571"
url: "https://www.scopus.com/pages/publications/105000832164?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2647--2652"
keywords: ["Mobile edge computing", "Backhaul traffics", "Content creation", "Content production", "Content services", "Edge modeling", "EDGE Networks", "Edge server", "Resource-efficient", "Service delays", "Traffic loads", "Generative adversarial networks"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "LLM as workload"

---

# paper-1042 — Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks

## Metadata

- **Authors:** Liang, Yuxin and Yang, Peng and He, Yuanyuan and Lyu, Feng
- **Year:** 2024
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM52923.2024.10901571
- **URL:** https://www.scopus.com/pages/publications/105000832164?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2647--2652
- **Language:** English
- **Keywords:** Mobile edge computing; Backhaul traffics; Content creation; Content production; Content services; Edge modeling; EDGE Networks; Edge server; Resource-efficient; Service delays; Traffic loads; Generative adversarial networks

### Abstract

The surging development of Artificial Intelligence-Generated Content (AIGC) marks a transformative era of the content creation and production. Edge servers promise attractive benefits, e.g., reduced service delay and backhaul traffic load, for hosting AIGC services compared to cloud-based solutions. However, the scarcity of available resources on the edge pose significant challenges in deploying generative AI models. In this paper, by characterizing the resource and delay demands of typical generative AI models, we find that the consumption of storage and GPU memory, as well as the model switching delay represented by I/O delay during the preloading phase, are significant and vary across models. These multidimensional coupling factors render it difficult to make efficient edge model deployment decisions. Hence, we present a collaborative edge-cloud framework aiming to properly manage generative AI model deployment on the edge. Specifically, we formulate edge model deployment problem considering heterogeneous features of models as an optimization problem, and propose a model-level decision selection algorithm to solve it. It enables pooled resource sharing and optimizes the trade-off between resource consumption and delay in edge generative AI model deployment. Simulation results validate the efficacy of the proposed algorithm compared with baselines, demonstrating its potential to reduce overall costs by providing feature-aware model deployment decisions. © 2024 IEEE.

## 04 — Title Screening

**Title:** Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Resource-Efficient Generative AI Model Deployment in Mobile Edge Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
