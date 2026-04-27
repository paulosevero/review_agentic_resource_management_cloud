---
id: "paper-2410"
title: "Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning"
authors: ["Zaki, Amr M.", "Elsayed, Sara A.", "Elgazzar, Khalid", "Hassanein, Hossam S."]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3559928"
url: "https://www.scopus.com/pages/publications/105002690010?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "26169--26185"
keywords: ["Autonomous vehicles (AVs)", "cooperative perception", "task offloading", "vehicular edge computing (VEC)"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2410 — Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning

## Metadata

- **Authors:** Zaki, Amr M. and Elsayed, Sara A. and Elgazzar, Khalid and Hassanein, Hossam S.
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3559928
- **URL:** https://www.scopus.com/pages/publications/105002690010?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 26169--26185
- **Language:** English
- **Keywords:** Autonomous vehicles (AVs); cooperative perception; task offloading; vehicular edge computing (VEC)

### Abstract

Task offloading in Vehicular Edge Computing (VEC) is crucial for enhancing cooperative perception (CP) in Autonomous Vehicles (AVs), thereby improving traffic situational awareness. However, existing approaches often neglect the balance between high-quality execution of interdependent tasks and conserving AVs’ limited budget, including communication and financial resources. To address this, we propose the Quality and Budget-Aware Task Offloading (QBATO) framework. QBATO is the first framework to balance the quality of CP with budget conservation. QBATO models the budget as a queue to ensure stability, balancing resource use while prioritizing situational awareness in CP. Additionally, QBATO enhances CP quality by predicting vehicles’ movements and estimating their regions of interest, thereby improving the Value of Information (VOI). The task offloading problem is modeled as a Quadratic Multiple Knapsack Problem (QMKP), an NP-hard problem that optimizes vehicle allocation by evaluating the quality of assigning multiple vehicles to the same worker through a quadratic objective function. To manage resources effectively, we apply the queue stability Lyapunov drift-minus-bonus approach. We also introduce the QBATO-Heuristic (QBATO-H), which solves the problem in a decentralized, time-efficient manner using a multiagent deep reinforcement learning technique that leverages the Q-Mixing Network (QMIX) method, which employs monotonic value decomposition to coordinate the actions of multiple agents. Extensive evaluations show that QBATO outperforms prominent quality and budget-oblivious schemes by up to 49%, 15%, and 35% in terms of budget conservation, situational awareness, and efficiency, respectively. QBATO-H also yields a small gap of up to 7% and 11% with QBATO in terms of budget conservation and efficiency, respectively. © 2014 IEEE.

## 04 — Title Screening

**Title:** Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
