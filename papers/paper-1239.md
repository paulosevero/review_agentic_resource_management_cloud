---
id: paper-1239
title: Adaptive personalized federated reinforcement learning for multiple-ESS optimal market dispatch strategy with electric vehicles and photovoltaic power generations
authors:
- Wang, Tianjing
- Dong, Zhao Yang
venue: Applied Energy
venue_type: journal
year: 2024
doi: 10.1016/j.apenergy.2024.123107
url: https://www.scopus.com/pages/publications/85191154105?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Electricity market
- Energy storage
- Federated reinforcement learning
- Personalization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1239 — Adaptive personalized federated reinforcement learning for multiple-ESS optimal market dispatch strategy with electric vehicles and photovoltaic power generations

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The state-of-the-art centralized computing framework applied to the optimal market dispatch of energy storage systems (ESS) aggregates data from local ESS units for training on the cloud server due to the limited computing resources on edge. However, this approach poses several challenges, including the lack of joint optimization for multiple ESS units, susceptibility to single point of failure and attacks, and inadequate data privacy protection for ESS owners. This study proposes an adaptive personalized federated reinforcement learning (FRL) for multiple-ESS optimal dispatch in various electricity markets with electric vehicle and renewable energy, achieving both the joint optimization of multiple ESSs and avoiding the degraded performance of FRL's local model. Under an adaptively ESS-related differential privacy protection, local devices and the cloud server are specialized to form multiagent deep reinforcement learning (DRL) model for bidding energy, regulation, and third-party services and update the global models, respectively. Given the adaptability of personalization layer to different agents and clients, an adaptive personalization method is developed by calculating the number of personalization layers with the relative loss of each agent and client in the iteration process. The case study shows that the adaptive personalized FRL outperforms conventional FRL, DRL and optimization algorithms. © 2024 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1239.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
