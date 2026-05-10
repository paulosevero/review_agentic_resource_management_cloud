---
id: paper-2338
title: 'Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach'
authors:
- Xu, Bo
- Zhao, Haitao
- Cao, Haotong
- Zhu, Chun
- Sun, Jinlong
- Zhang, Linghao
- Zhu, Hongbo
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3514095
url: https://www.scopus.com/pages/publications/105002486644?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10795--10807
keywords:
- Fog computing
- Industrial Internet of Things (IIoT)
- multiagent reinforcement learning (MARL)
- submodular optimization
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

# paper-2338 — Mobility-Aware Task Offloading in Industrial Fog Networks: A Submodular-Based MARL Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The development of Industrial Internet of Things (IIoT) applications presents a critical challenge in terms of latency limitation, particularly considering the limited availability of resources that prevent a single fog device from fully executing large-scale computing tasks. In such scenarios, enabling distributed computing across multiple fog servers or collaborating with cloud servers holds promising potential. To improve the efficiency of task offloading while accounting for the crucial role of movable fog devices (e.g., robots and unmanned cars), we formulate a joint optimization problem as a partially observable Markov decision process (POMDP), incorporating offloading decisions, computing resource allocation, and trajectory optimization under constraints related to available resources and collision avoidance. Due to the nondeterministic polynomial-time hardness (NP-hardness) in the problems of task offloading and resource allocation, we reformulate a matroid-constrained submodular maximization problem and propose an iterative low-complexity algorithm to find solutions. Subsequently, extracting better solutions from submodular optimization, we propose a multiagent reinforcement learning (MARL)-based algorithm to solve the trajectory optimization problem for the movable fog devices acting as agents, making decisions based on their local observations. Finally, simulation results have validated that the proposed scheme has a superior performance compared to the baselines. © 2014 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2338.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
