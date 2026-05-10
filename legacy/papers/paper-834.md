---
id: "paper-834"
title: "Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints"
authors: ["Ben Sada, Abdelkarim", "Khelloufi, Amar", "Naouri, Abdenacer", "Ning, Huansheng", "Aung, Nyothiri", "Dhelim, Sahraoui"]
year: 2024
venue: "Electronics (Switzerland)"
venue_type: "journal"
doi: "10.3390/electronics13132580"
url: "https://www.scopus.com/pages/publications/85198348261?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["deep reinforcement learning", "edge AI", "Internet of Things", "task offloading"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-834 — Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints

## Metadata

- **Authors:** Ben Sada, Abdelkarim and Khelloufi, Amar and Naouri, Abdenacer and Ning, Huansheng and Aung, Nyothiri and Dhelim, Sahraoui
- **Year:** 2024
- **Venue:** Electronics (Switzerland)
- **DOI:** 10.3390/electronics13132580
- **URL:** https://www.scopus.com/pages/publications/85198348261?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning; edge AI; Internet of Things; task offloading

### Abstract

The journey towards realizing real-time AI-driven IoT applications is facing a significant hurdle caused by the limited resources of IoT devices. Particularly for battery-powered edge devices, the decision between performing task inference locally or by offloading to edge servers, all while ensuring timely results and conserving energy, is a critical issue. This problem is further complicated when an edge device houses multiple local inference models. The challenge of effectively allocating inference models to tasks between local models and edge server models under strict time and energy constraints while maximizing overall accuracy is recognized as a strongly NP-hard problem and has not been addressed in the literature. Therefore, in this work we propose MASITO, a novel multi-agent deep reinforcement learning framework designed to address this intricate problem. By dividing the problem into two sub-problems namely task scheduling and edge server selection we propose a cooperative multi-agent system for addressing each sub-problem. MASITO’s design allows for faster training and more robust schedules using cooperative behavior where agents compensate for each other’s sub-optimal actions. Moreover, MASITO dynamically adapts to different network configurations which allows for high-mobility edge computing applications. Experiments on the ImageNet-mini dataset demonstrate the framework’s efficacy, outperforming genetic algorithms (GAs), simulated annealing (SA), and particle swarm optimization (PSO) in scheduling times by providing lower times ranging from 60% up to 90% while maintaining comparable average accuracy in worst-case scenarios and superior accuracy in best-case scenarios. © 2024 by the authors.

## 04 — Title Screening

**Title:** Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Deep Reinforcement Learning-Based Inference Task Scheduling and Offloading for Maximum Inference Accuracy under Time and Energy Constraints
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
