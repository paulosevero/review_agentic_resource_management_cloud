---
id: paper-2805
title: Energy-Efficient Path Planning and Task Scheduling for UAV-Assisted Wireless Networks via Double Dueling Deep Q-Networks with LSTM
authors:
- Ullah, Amin
- Ul Haq, Qazi Mazhar
- Ali, Sajid
venue: Proceedings - IEEE Consumer Communications and Networking Conference, CCNC
venue_type: conference
year: 2026
doi: 10.1109/CCNC65079.2026.11366608
url: https://www.scopus.com/pages/publications/105034206000?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Double Dueling Deep Q-Network (D3QN)
- Internet of Things (IoT)
- Long Short-Term Memory (LSTM)
- Mobile Edge Computing (MEC)
- unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-2805 — Energy-Efficient Path Planning and Task Scheduling for UAV-Assisted Wireless Networks via Double Dueling Deep Q-Networks with LSTM

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Efficient path planning is crucial to address mission delays, excessive energy consumption, and suboptimal coverage in dynamic Unmanned Aerial Vehicle (UAV) operations. Traditional approaches often overlook temporal patterns in environmental changes and communication demands, leading to inefficient routes and reduced mission performance. To overcome these limitations, this research presents an innovative D3QN-LSTM framework that integrates Double Dueling Deep Q-Networks (D3QN) with Long Short-Term Memory (LSTM) modules for intelligent, temporally-aware UAV path planning. The path planning problem is formulated as a Markov Decision Process (MDP), where the D3QN agent, enhanced with LSTM-based temporal modeling, learns optimal flight trajectories by predicting future changes in mission demands and energy states. Three configurations were evaluated: a baseline D3QN architecture, a D3QN with LSTM integration, and an enhanced D3QN with a deep LSTM architecture. Simulation results demonstrate that incorporating temporal learning reduces mission completion time by up to 14.2%, decreases energy consumption by 12.7%, and improves area coverage efficiency compared to conventional methods. The proposed architecture enables UAVs to perform energy-aware, proactive routing while maintaining operational responsiveness, with promising applications in surveillance, disaster response, and environmental monitoring. © 2026 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2805.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
