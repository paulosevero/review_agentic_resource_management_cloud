---
id: "paper-589"
title: "A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling"
authors: ["Fodor, Balazs", "Jakub, Akos", "Szucs, Gabor", "Sonkoly, Balazs"]
year: 2023
venue: "2023 IEEE Virtual Conference on Communications, VCC 2023"
venue_type: "conference"
doi: "10.1109/VCC60689.2023.10474695"
url: "https://www.scopus.com/pages/publications/85190237053?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "139--144"
keywords: ["auto-scaling", "cloud computing", "microservice scaling", "multi-agent reinforcement learning"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-589 — A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling

## Metadata

- **Authors:** Fodor, Balazs and Jakub, Akos and Szucs, Gabor and Sonkoly, Balazs
- **Year:** 2023
- **Venue:** 2023 IEEE Virtual Conference on Communications, VCC 2023
- **DOI:** 10.1109/VCC60689.2023.10474695
- **URL:** https://www.scopus.com/pages/publications/85190237053?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 139--144
- **Language:** English
- **Keywords:** auto-scaling; cloud computing; microservice scaling; multi-agent reinforcement learning

### Abstract

Efficient cloud-based microservice scaling needs to take into account the inter-dependencies between application components to avoid bottlenecks and to swiftly adapt to dynamically changing environments or user demands. Most of today's solutions are not adaptive enough especially to handle large-scale microservices. In this paper, we propose a novel solution leveraging Multi-Agent Deep Reinforcement Learning (MADRL). First, we define our model for horizontal scaling of microservices and formalize the problem. Second, we propose an algorithm based on Multi-Agent Deep Deterministic Policy Gradient (MADDPG) to solve it. Third, a dedicated simulation environment is presented, where arbitrary microservices can be created for testing purposes, and we carry out a comprehensive evaluation. We analyze the performance of the model for microservices of different sizes, investigating its ability to optimize scaling while considering efficient resource utilization and application stability. Results show that our MADDPG-based RL algorithm outperforms the industry standard approach provided by Kubernetes' HPA by at least 14% in terms of resource usage cost.  © 2023 IEEE.

## 04 — Title Screening

**Title:** A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Multi-Agent Deep-Reinforcement Learning Approach for Application-Agnostic Microservice Scaling
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
