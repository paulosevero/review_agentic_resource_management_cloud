---
id: paper-2254
title: Data prioritization aware resource allocation in internet of vehicles using multi-agent deep reinforcement learning
authors:
- Wang, Cong
- Guan, Yingshan
- Peng, Sancheng
- Chen, Hao
- Li, Guorui
venue: Neural Networks
venue_type: journal
year: 2025
doi: 10.1016/j.neunet.2025.107671
url: https://www.scopus.com/pages/publications/105007889228?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Data prioritization
- Internet of vehicles
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Spectrum resource allocation
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2254 — Data prioritization aware resource allocation in internet of vehicles using multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent transportation systems (ITS) are facing the limitation of spectral resources and stringent real time communication requirements. How to effectively allocate system resources for maximizing the performance in Internet of Vehicles (IoV) is still a substantial challenge, particularly the priority and urgency of different types of data need to be focused. To improve the allocation spectrum resources and optimize transmission power while taking into the dynamic characteristics of vehicles and data priorities account, we design a time-series-based multi-agent deep reinforcement learning framework (NL-MAPPO for short), in this paper. First, we formulate the joint optimization problem as a multi-agent Markov decision process to ensure the minimization of transmission delays and energy consumption when the total vehicle-to-vehicle (V2V) link capacity is maximized. Here, V2V link capacity refers to the maximum achievable data rate for direct communication between vehicles, which depends on factors such as signal strength, interference, and available bandwidth. Then, we design a multi-agent resource allocation algorithm based on a shared-critic mechanism to realize the global sharing of channel information and solve the optimization problem. Finally, to improve efficiency, we also introduce a time series-based channel information extraction mechanism to capture the temporal characteristics of channel information. The simulation experiments were conducted and the results demonstrated that our proposed NL-MAPPO can demonstrate superiority in multiple metrics. © 2025

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2254.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
