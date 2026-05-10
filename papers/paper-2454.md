---
id: paper-2454
title: 'Resource Allocation and Trajectory Optimization in Multi-UAV Collaborative Vehicular Networks: An Extended Multiagent DRL Approach'
authors:
- Zhang, Wenqian
- Tan, Lu
- Huang, Tao
- Huang, Xiaowen
- Huang, Mengting
- Zhang, Guanglin
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3492953
url: https://www.scopus.com/pages/publications/105002493287?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9391--9404
keywords:
- Internet of vehicles
- mobile edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- UAVs-assisted vehicular networks
- uncrewed aerial vehicle (UAV)
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

# paper-2454 — Resource Allocation and Trajectory Optimization in Multi-UAV Collaborative Vehicular Networks: An Extended Multiagent DRL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In vehicular networks enhanced by uncrewed aerial vehicles (UAVs), vehicle state information is efficiently collected, and traffic safety is assured. UAVs, serving as aerial base stations, enable vehicle network access and provide edge computing services in the absence of roadside units (RSUs). This study explores a multi-UAV-assisted vehicular network, where multiple UAVs collaboratively offer services to vehicles. The goal is to minimize task completion time by optimizing trajectory planning, spectrum resource allocation, and dynamic data offloading. An enhanced multiagent deep deterministic policy gradient (MADDPG) algorithm is introduced to address the optimization challenge in cooperative multi-UAV scenarios. Within this framework, each UAV, acting as an agent, devises strategies for movement, data offloading, and resource allocation based on the current states of vehicles and fellow UAVs. The simulation results reveal that the proposed algorithm improves task completion efficiency and ensures vehicle Quality of Service (QoS) over existing benchmarks. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2454.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
