---
id: paper-2410
title: Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning
authors:
- Zaki, Amr M.
- Elsayed, Sara A.
- Elgazzar, Khalid
- Hassanein, Hossam S.
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3559928
url: https://www.scopus.com/pages/publications/105002690010?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 26169--26185
keywords:
- Autonomous vehicles (AVs)
- cooperative perception
- task offloading
- vehicular edge computing (VEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2410 — Quality and Budget-Oriented Task Offloading for Vehicular Cooperative Perception Using Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Task offloading in Vehicular Edge Computing (VEC) is crucial for enhancing cooperative perception (CP) in Autonomous Vehicles (AVs), thereby improving traffic situational awareness. However, existing approaches often neglect the balance between high-quality execution of interdependent tasks and conserving AVs’ limited budget, including communication and financial resources. To address this, we propose the Quality and Budget-Aware Task Offloading (QBATO) framework. QBATO is the first framework to balance the quality of CP with budget conservation. QBATO models the budget as a queue to ensure stability, balancing resource use while prioritizing situational awareness in CP. Additionally, QBATO enhances CP quality by predicting vehicles’ movements and estimating their regions of interest, thereby improving the Value of Information (VOI). The task offloading problem is modeled as a Quadratic Multiple Knapsack Problem (QMKP), an NP-hard problem that optimizes vehicle allocation by evaluating the quality of assigning multiple vehicles to the same worker through a quadratic objective function. To manage resources effectively, we apply the queue stability Lyapunov drift-minus-bonus approach. We also introduce the QBATO-Heuristic (QBATO-H), which solves the problem in a decentralized, time-efficient manner using a multiagent deep reinforcement learning technique that leverages the Q-Mixing Network (QMIX) method, which employs monotonic value decomposition to coordinate the actions of multiple agents. Extensive evaluations show that QBATO outperforms prominent quality and budget-oblivious schemes by up to 49%, 15%, and 35% in terms of budget conservation, situational awareness, and efficiency, respectively. QBATO-H also yields a small gap of up to 7% and 11% with QBATO in terms of budget conservation and efficiency, respectively. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2410.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
