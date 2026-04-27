---
id: "paper-2112"
title: "Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems"
authors: ["Seisa, Achilleas Santi", "Kotpalliwar, Shruti", "Satpute, Sumeet Gajanan", "Nikolakopoulos, George"]
year: 2025
venue: "European Control Conference (Piscataway, N.J. Online), ECC"
venue_type: "conference"
doi: "10.23919/ECC65951.2025.11187111"
url: "https://www.scopus.com/pages/publications/105030960225?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2907--2913"
keywords: ["Closed loop control systems", "Control theory", "Controllers", "Covariance matrix", "Curve fitting", "Memory architecture", "Parameter estimation", "Regression analysis", "Resource allocation", "Collision-free trajectory", "Computational resources", "Covariance matrices", "Edge-based", "Least square minimization techniques", "Multiagent systems (MASs)", "Parameters estimates", "Polynomial regression models", "Resources allocation", "Second-order polynomial", "Multi agent systems"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-2112 — Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems

## Metadata

- **Authors:** Seisa, Achilleas Santi and Kotpalliwar, Shruti and Satpute, Sumeet Gajanan and Nikolakopoulos, George
- **Year:** 2025
- **Venue:** European Control Conference (Piscataway, N.J. Online), ECC
- **DOI:** 10.23919/ECC65951.2025.11187111
- **URL:** https://www.scopus.com/pages/publications/105030960225?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2907--2913
- **Language:** English
- **Keywords:** Closed loop control systems; Control theory; Controllers; Covariance matrix; Curve fitting; Memory architecture; Parameter estimation; Regression analysis; Resource allocation; Collision-free trajectory; Computational resources; Covariance matrices; Edge-based; Least square minimization techniques; Multiagent systems (MASs); Parameters estimates; Polynomial regression models; Resources allocation; Second-order polynomial; Multi agent systems

### Abstract

This article presents a novel edge-based architecture to dynamically allocate resources to edge-offloaded controllers for multi-agent systems. The proposed controllers are designed to generate collision-free trajectories to track the desired reference positions. The computational complexity of the controllers' problem is estimated by a second-order polynomial regression model, while the Least Squares (LS) minimization technique is employed for the coefficients' estimation. The covariance matrix plays an essential role in assessing the confidence in the parameter estimates and in investigating correlations among parameters. Through this curve fitting process, we can dynamically estimate the complexity of the controllers' problem as conditions change, enabling effective and responsive resource allocation. Furthermore, a novel control law is designed to control the dynamic resource allocation, based on the measured communication and processing time delays. This approach allows us to control the controllers' response time, thereby ensuring the closed-loop system's stability. The overall architecture is enabled through a Kubernetes (k8s) cluster and is experimentally evaluated.  © 2025 EUCA.

## 04 — Title Screening

**Title:** Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic Computational Resource Allocation for Ensuring Stability of Remote Edge-based Controlled Multi-agent Systems
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
