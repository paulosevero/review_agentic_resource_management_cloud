---
id: paper-0665
title: Multi-agent Deep Reinforcement Learning-based Trajectory Design for UAV-aided Edge Computing System
authors:
- Lu, Gengyuan
- Chang, Zheng
venue: IEEE Wireless Communications and Networking Conference, WCNC
venue_type: conference
year: 2023
doi: 10.1109/WCNC55385.2023.10118895
url: https://www.scopus.com/pages/publications/85159790269?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Mobile edge computing
- multi-agent deep reinforcement learning
- trajectory design.
- unmanned aerial vehicle
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0665 — Multi-agent Deep Reinforcement Learning-based Trajectory Design for UAV-aided Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The unmanned aerial vehicle (UAV)-aided communication system is able to extend the coverage of the cellular network and provide flexible connectivity to the ground users. Recently, in order to achieve the ambitious goal of ubiquitous computing and intelligence, UAV-aided mobile edge computing (MEC) system also attracts significant research interests. In this work, we investigate the trajectory design for a multi-UAV-aided MEC system to maximize the defined quality of experience (QoE) and service fairness of multiple ground user equipments (UEs). Since the practical communication environment is complex and time-varying, it is challenging for the multiple UAVs to dynamically make autonomous decisions. Meanwhile, the centralized decision-making scheme may also have a certain degree of transmission delay and affect efficiency of the considered system. Therefore, bearing in mind these challenges, in order to solve the formulated problem, we propose a multi-agent deep reinforcement learning algorithm using Multi-Agent Deep Deterministic Policy Gradient (MADDPG) to design UAV's trajectory via optimizing the flying angle and distance. The simulation results show that our proposed solution outperforms the traditional algorithms.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0665.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
