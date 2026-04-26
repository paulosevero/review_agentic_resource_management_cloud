---
id: "paper-2631"
title: "LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing"
authors: ["Kaur, Jasmine", "Chana, Inderveer", "Bala, Anju"]
year: 2026
venue: "Simulation Modelling Practice and Theory"
venue_type: "journal"
doi: "10.1016/j.simpat.2025.103227"
url: "https://www.scopus.com/pages/publications/105023971114?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Auto scaling", "AWS Lambda", "Hybrid reinforcement learning", "Serverless computing", "Simulation modeling"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2631 — LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing

## Metadata

- **Authors:** Kaur, Jasmine and Chana, Inderveer and Bala, Anju
- **Year:** 2026
- **Venue:** Simulation Modelling Practice and Theory
- **DOI:** 10.1016/j.simpat.2025.103227
- **URL:** https://www.scopus.com/pages/publications/105023971114?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Auto scaling; AWS Lambda; Hybrid reinforcement learning; Serverless computing; Simulation modeling

### Abstract

Serverless computing has revolutionized cloud platforms by enabling developers to deploy applications without the burden of managing infrastructure. However, challenges such as workload unpredictability, inefficient job scheduling, and high energy consumption remain critical concerns. To address these issues, this paper introduces LMP-Opt, a simulation-driven hybrid model that integrates Long Short-Term Memory (LSTM) for workload prediction, Multi-Agent Deep Q-Learning (MADQL) for job scheduling, and Proximal Policy Optimization (PPO) for fine-tuning scheduling decisions. Firstly, LSTM predicts workload patterns by capturing temporal dependencies, enabling efficient resource provisioning, and reducing performance degradation caused by unpredictable workloads. Secondly, MADQL utilizes multiple agents to optimize job scheduling by dynamically adjusting allocation strategies in response to workload fluctuations. Third, PPO refines scheduling policies by balancing exploration and exploitation, improving stability and convergence in decision-making. The proposed approach has been validated using ServerlessSimPro, a specialized simulation environment, and is further tested in AWS Lambda to ensure applicability to real-world serverless platforms. Extensive experiments using an e-commerce transaction processing workload demonstrate that LMP-Opt significantly improves system performance. The simulation results show a reduction in the average response time by 4.79% over MADQL and 6.09% over PPO, in addition to savings in energy consumption of 4.35% and 6.14%, respectively. The model also improves cost efficiency, CPU utilization, and resource scalability by reducing node requirements. These results confirm the value of hybrid learning-based simulation models for optimizing scheduling and energy efficiency in serverless computing environments. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 04 — Title Screening

**Title:** LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing
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
