---
id: paper-0606
title: Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System
authors:
- He, Yejun
- Gan, Youhui
- Cui, Haixia
- Guizani, Mohsen
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3241087
url: https://www.scopus.com/pages/publications/85148425093?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11383--11395
keywords:
- Computing offloading
- fairness
- mobile-edge computing (MEC)
- multiagent deep deterministic policy gradient (MADDPG)
- selectivity
- trajectory optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0606 — Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs)-assisted mobile-edge computing (MEC) communication system has recently gained increasing attention. In this article, we investigate a 3-D multi-UAV trajectory optimization based on ground devices (GDs) selecting the target UAV for task computing. Specifically, we first design a 3-D dynamic multi-UAV-assisted MEC system in which GDs have real-time mobility and task update. Next, we formulate the system communication, computation, and flight energy consumption as objective functions based on fairness among UAVs. Then, to pursue fairness among UAVs, we theoretically deduce and mathematically prove the optimal GDs' selectivity and offloading strategy, that is, how GDs select the optimal UAV for task offloading and how much to offload. While ensuring the optimal offloading strategy and GDs' selectivity between UAVs and GDs at each step, we model UAV trajectories as a sequence of location updates of all UAVs and apply a multiagent deep deterministic policy gradient (MADDPG) algorithm to find the optimal solution. Simulation results demonstrate that we achieve the minimum energy consumption under the premise of fairness and the efficiency of model processing tasks.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0606.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
