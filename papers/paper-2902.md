---
id: paper-2902
title: 'Multiple Reconfigurable Intelligent Surfaces Aided V2X Offloading Networks: A Federated Reinforcement Learning-Based Approach'
authors:
- Zeng, Ming
- Zhao, Yanbin
- Wang, Jing
- Fei, Zesong
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2025.3592718
url: https://www.scopus.com/pages/publications/105012156418?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1281--1294
keywords:
- deep reinforcement learning
- Internet of vehicles
- task offload
- vehicular edge computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2902 — Multiple Reconfigurable Intelligent Surfaces Aided V2X Offloading Networks: A Federated Reinforcement Learning-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of a large number of computation intensive and delay sensitive on-vehicle applications, vehicle edge computing (VEC), as an emerging computing paradigm, aims to enhance computing performance by offloading computation tasks to vehicles and edge servers. However, the mobility of vehicles and obstacles which hamper the propagation of electromagnetic signals may result in poor vehicle-to-everything (V2X) channel quality. In this paper, we consider improving the wireless propagation environment by deploying reconfigurable intelligent surface (RIS) devices and study a task offloading strategy in VEC networks assisted by RIS. Under the constraints of vehicle-to-vehicle link reliability and minimum transmission rate requirement, we jointly optimize the RIS reflection coefficient matrix, task vehicle offloading mode and beamforming vector to minimize the average offloading delay of the entire system. Considering the non-convexity of the optimization problem and the isomorphism of task vehicle agents, we propose a feasible joint optimization algorithm based on multi-agent proximal policy optimization with federated learning framework (F-MAPPO). Additionally, this paper further develops a low-complexity F-MAPPO algorithm (LF-MAPPO) to address the large multidimensional state space problem in F-MAPPO algorithm. Numerical simulation results show that compared with centralized and decentralized MAPPO algorithms, the proposed algorithm achieves performance boost in convergence. Moreover, the proposed LF-MAPPO algorithm reduces the average task processing latency by 44.05% and 48.91% compared to the schemes without RIS devices and without vehicle-to-vehicle (V2V) link, which indicate the crucial role of introducing RIS and V2V task offloading in improving the system performance. © 1967-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2902.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
