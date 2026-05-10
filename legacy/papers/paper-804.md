---
id: "paper-804"
title: "Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing"
authors: ["Zhou, Ao", "Li, Sisi", "Ma, Xiao", "Zhang, Yiran", "Wang, Shangguang"]
year: 2023
venue: "Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023"
venue_type: "conference"
doi: "10.1109/ICWS60048.2023.00047"
url: "https://www.scopus.com/pages/publications/85173880801?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "278--288"
keywords: ["Container image", "Edge computing", "Instance deployment.", "Offloading", "Resource provisioning"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-804 — Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing

## Metadata

- **Authors:** Zhou, Ao and Li, Sisi and Ma, Xiao and Zhang, Yiran and Wang, Shangguang
- **Year:** 2023
- **Venue:** Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023
- **DOI:** 10.1109/ICWS60048.2023.00047
- **URL:** https://www.scopus.com/pages/publications/85173880801?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 278--288
- **Language:** English
- **Keywords:** Container image; Edge computing; Instance deployment.; Offloading; Resource provisioning

### Abstract

Container-enabled serverless computing has become a widely adopted approach for resource provisioning in the edge cloud. However, traffic incurred by container image pulling heavily burdens the already congested back-haul network. To relieve the problem, we do an analysis on Docker Hub, and find that instance deployment strategy has a significant impact on the back-haul traffic due to the varying similarity levels of different images. We incorporate this feature into task offloading decision and resource provisioning, and formulate the problem with a mixed integer non-linear programming (MINLP) problem. To address the challenges arising from the coupling and contradiction of instance deployment, image pulling, offloading decision, and resource allocation, we employ multi-agent deep reinforcement learning to decompose the problem into several simpler sub-problems, and design an algorithm for each sub-problem individually by exploiting convex optimization and fractional programming techniques. Simulations are conducted to validate the effectiveness of the proposed algorithm. The experiment results illustrate that our algorithm outperforms current notable solutions and improves the global utility by 13%-74%. © 2023 IEEE.

## 04 — Title Screening

**Title:** Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Container Image Similarity-Aware Resource Provisioning for Serverless Edge Computing
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
