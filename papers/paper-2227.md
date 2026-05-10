---
id: paper-2227
title: Adaptive Q-Learning-Based Event-Prioritized QoS and incentive optimization for enhancing safety in vehicular fog networks
authors:
- Tripura, Sajib
- Lu, Qing-Chang
- Tripura, Dhonita
- Kholilullah, Md Ibrahim
- Avi, Arunav Mallik
- Ahamed, Mostak
- Hussain, Adil
venue: Egyptian Informatics Journal
venue_type: journal
year: 2025
doi: 10.1016/j.eij.2025.100821
url: https://www.scopus.com/pages/publications/105022492762?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Emergency priority
- Incentive
- Message dissemination
- Reinforcement learning
- Reliability
- Vehicular fog computing (VFC)
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2227 — Adaptive Q-Learning-Based Event-Prioritized QoS and incentive optimization for enhancing safety in vehicular fog networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the rapidly changing world of Intelligent Transportation Systems (ITS), achieving fast, reliable, and energy-efficient communication in vehicle fog computing (VFC) networks is crucial for safety–critical applications. Current VFC approaches are not apt for safety–critical applications as they are based on static heuristics, QoS focus design which neglects trust, energy and reliability; slow convergence and does not support fairness and responsiveness. Moreover, they do not adaptively prioritize concurrent emergencies, which motivates the development of mobility and criticality-aware adaptive approaches. This study proposes a novel reinforcement learning framework named Q-APERF based on tabular Q-learning agent improved by the Augmented Priority-Entropy Reward Function (APERF). Our approach dynamically adjusts multiple QoS metrics, including latency, reliability, trustworthiness, and energy consumption, while prioritizing overlapping emergencies such as ambulances, crash alerts, and road hazards exponentially. The agent achieves adaptive QoS weighting and discrete vehicular state, and therefore, the message forwarding performance can be enhanced in a highly dynamic environment (i.e., the IoV). Extensive simulations show that it outperforms some of the existing state-of-the-art approaches. The Q-APERF achieves 95.5% of message prioritization accuracy, 75.4% of transmission efficacy in packet loss situation, and 83% of energy efficiency and 80% faster response to emergency events, which illustrates its dynamic resilience adaptability balance QoS and energy consumption perspective. Moreover, we introduce a novel metric, Survival-Weighted Data Integrity (SWDI), to evaluate incentive mechanisms that promote the sustained participation of vehicles and encourage them to share their resources. This holistic view will enable safer and more fault-tolerant smart transportation systems through offering a secure, scalable, and context-aware vehicular communication solution. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2227.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
