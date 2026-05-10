---
id: "paper-688"
title: "Multi-Agent Task Assignment in Vehicular Edge Computing: A Regret-Matching Learning-Based Approach"
authors: ["Nguyen, Bach Long", "Nguyen, Duong D.", "Nguyen, Hung X.", "Ngo, Duy T.", "Wagner, Markus"]
year: 2023
venue: "IEEE Transactions on Emerging Topics in Computational Intelligence"
venue_type: "journal"
doi: "10.1109/TETCI.2023.3339540"
url: "https://www.scopus.com/pages/publications/85179383323?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1527--1539"
keywords: ["Correlated equilibrium", "intelligent transportation systems", "multi-agent learning", "regret matching", "task assignment", "vehicular edge computing"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-688 — Multi-Agent Task Assignment in Vehicular Edge Computing: A Regret-Matching Learning-Based Approach

## Metadata

- **Authors:** Nguyen, Bach Long and Nguyen, Duong D. and Nguyen, Hung X. and Ngo, Duy T. and Wagner, Markus
- **Year:** 2023
- **Venue:** IEEE Transactions on Emerging Topics in Computational Intelligence
- **DOI:** 10.1109/TETCI.2023.3339540
- **URL:** https://www.scopus.com/pages/publications/85179383323?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1527--1539
- **Language:** English
- **Keywords:** Correlated equilibrium; intelligent transportation systems; multi-agent learning; regret matching; task assignment; vehicular edge computing

### Abstract

Vehicular edge computing has emerged as a solution for enabling computation-intensive applications within Intelligent Transportation Systems (ITS), encompassing domains like autonomous driving and augmented reality. Despite notable progress in this domain, the efficient allocation of constrained computational resources to a spectrum of time-critical ITS tasks remains a substantial challenge. We address this challenge by devising an innovative task assignment scheme tailored for vehicles navigating a highway. Given the high speed of vehicles and the limited communication radius of roadside units (RSUs), the dynamic migration of computation tasks among multiple servers becomes imperative. We present a novel approach that formulates the task assignment challenge as a binary nonlinear programming (BNLP) problem, managing the allocation of computation tasks from vehicles to RSUs and a macrocell base station. To tackle the potentially large dimensionality of this optimization problem, we develop a distributed multi-agent regret-matching learning algorithm. Incorporating the method of regret minimization, our proposed algorithm employs a forgetting mechanism that enables a continuous learning process, thereby accommodating the high mobility of vehicle networks. We prove that this algorithm converges towards correlated equilibrium solutions for our BNLP formulation. Extensive simulations, grounded in practical parameter settings, underscore the algorithm’s ability to minimize total delay and task processing costs, while ensuring equitable utility distribution among agents. © 2023 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Task Assignment in Vehicular Edge Computing: A Regret-Matching Learning-Based Approach

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Task Assignment in Vehicular Edge Computing: A Regret-Matching Learning-Based Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Task Assignment in Vehicular Edge Computing: A Regret-Matching Learning-Based Approach
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
