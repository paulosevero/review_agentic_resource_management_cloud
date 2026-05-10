---
id: paper-1358
title: Priority-Aware Task Offloading and UAV Trajectory Optimization for Aerial Access Network - Assisted Mobile Edge Computing
authors:
- Zhou, Yuqiang
- Sun, Haifeng
venue: Proceedings - 2024 17th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics, CISP-BMEI 2024
venue_type: conference
year: 2024
doi: 10.1109/CISP-BMEI64163.2024.10906132
url: https://www.scopus.com/pages/publications/105000906427?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Aerial Access Networks
- joint optimization
- MAPPO
- Mobile Edge Computing
- task offloading
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

# paper-1358 — Priority-Aware Task Offloading and UAV Trajectory Optimization for Aerial Access Network - Assisted Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the surge in computational data, Mobile Edge Computing (MEC) is set to become a crucial technology for reducing communication latency and congestion. However, the widespread adoption of MEC faces several challenges. Aerial Access Networks (AANs), comprising hierarchical High Altitude Platforms (HAPs) and low-altitude Unmanned Aerial Vehicles (UAVs), offer a groundbreaking framework for MEC task offloading, particularly enhancing the service experience of Internet of Things (IoT) devices in disaster zones, battlefield healthcare, or remote areas. In this paper, we propose an MEC task offloading framework supported by AANs to serve IoT devices distributed on the ground. We define system gain based on the energy consumption and latency of tasks with varying priorities. Our objective is to maximize workload fairness among UAVs and overall system gain by jointly optimizing UAVs' flight trajectories, IoT devices' computational task offloading decisions, and service fairness. We propose a multi-agent proximal policy optimization (MAPPO)-based algorithm to solve this joint optimization problem. Experimental results validate the effectiveness of the proposed approach, and numerical analysis evaluates system performance. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1358.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
