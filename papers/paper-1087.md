---
id: paper-1087
title: A Multi-Agent RL Algorithm for Dynamic Task Offloading in D2D-MEC Network with Energy Harvesting †
authors:
- Mi, Xin
- He, Huaiwen
- Shen, Hong
venue: Sensors
venue_type: journal
year: 2024
doi: 10.3390/s24092779
url: https://www.scopus.com/pages/publications/85192785108?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- D2D communication
- dynamic task offloading
- energy harvesting
- MEC
- multi-agent reinforcement learning
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1087 — A Multi-Agent RL Algorithm for Dynamic Task Offloading in D2D-MEC Network with Energy Harvesting †

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Delay-sensitive task offloading in a device-to-device assisted mobile edge computing (D2D-MEC) system with energy harvesting devices is a critical challenge due to the dynamic load level at edge nodes and the variability in harvested energy. In this paper, we propose a joint dynamic task offloading and CPU frequency control scheme for delay-sensitive tasks in a D2D-MEC system, taking into account the intricacies of multi-slot tasks, characterized by diverse processing speeds and data transmission rates. Our methodology involves meticulous modeling of task arrival and service processes using queuing systems, coupled with the strategic utilization of D2D communication to alleviate edge server load and prevent network congestion effectively. Central to our solution is the formulation of average task delay optimization as a challenging nonlinear integer programming problem, requiring intelligent decision making regarding task offloading for each generated task at active mobile devices and CPU frequency adjustments at discrete time slots. To navigate the intricate landscape of the extensive discrete action space, we design an efficient multi-agent DRL learning algorithm named MAOC, which is based on MAPPO, to minimize the average task delay by dynamically determining task-offloading decisions and CPU frequencies. MAOC operates within a centralized training with decentralized execution (CTDE) framework, empowering individual mobile devices to make decisions autonomously based on their unique system states. Experimental results demonstrate its swift convergence and operational efficiency, and it outperforms other baseline algorithms. © 2024 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1087.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
