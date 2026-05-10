---
id: paper-2631
title: 'LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing'
authors:
- Kaur, Jasmine
- Chana, Inderveer
- Bala, Anju
venue: Simulation Modelling Practice and Theory
venue_type: journal
year: 2026
doi: 10.1016/j.simpat.2025.103227
url: https://www.scopus.com/pages/publications/105023971114?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Auto scaling
- AWS Lambda
- Hybrid reinforcement learning
- Serverless computing
- Simulation modeling
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2631 — LMP-Opt: A simulation-based hybrid model for dynamic job scheduling and energy optimization in serverless computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Serverless computing has revolutionized cloud platforms by enabling developers to deploy applications without the burden of managing infrastructure. However, challenges such as workload unpredictability, inefficient job scheduling, and high energy consumption remain critical concerns. To address these issues, this paper introduces LMP-Opt, a simulation-driven hybrid model that integrates Long Short-Term Memory (LSTM) for workload prediction, Multi-Agent Deep Q-Learning (MADQL) for job scheduling, and Proximal Policy Optimization (PPO) for fine-tuning scheduling decisions. Firstly, LSTM predicts workload patterns by capturing temporal dependencies, enabling efficient resource provisioning, and reducing performance degradation caused by unpredictable workloads. Secondly, MADQL utilizes multiple agents to optimize job scheduling by dynamically adjusting allocation strategies in response to workload fluctuations. Third, PPO refines scheduling policies by balancing exploration and exploitation, improving stability and convergence in decision-making. The proposed approach has been validated using ServerlessSimPro, a specialized simulation environment, and is further tested in AWS Lambda to ensure applicability to real-world serverless platforms. Extensive experiments using an e-commerce transaction processing workload demonstrate that LMP-Opt significantly improves system performance. The simulation results show a reduction in the average response time by 4.79% over MADQL and 6.09% over PPO, in addition to savings in energy consumption of 4.35% and 6.14%, respectively. The model also improves cost efficiency, CPU utilization, and resource scalability by reducing node requirements. These results confirm the value of hybrid learning-based simulation models for optimizing scheduling and energy efficiency in serverless computing environments. © 2025 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2631.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
