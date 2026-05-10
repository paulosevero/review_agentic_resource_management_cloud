---
id: paper-1389
title: Enhancing wireless sensor network lifespan and efficiency through improved cluster head selection using improved squirrel search algorithm
authors:
- Alshammri, Ghalib H.
venue: Artificial Intelligence Review
venue_type: journal
year: 2025
doi: 10.1007/s10462-024-11088-4
url: https://www.scopus.com/pages/publications/85214240567?origin=resultslist
publisher: Springer Nature
pages: ''
keywords:
- Clustering
- Routing protocol
- Squirrel search algorithm
- Wireless Sensor Networks
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1389 — Enhancing wireless sensor network lifespan and efficiency through improved cluster head selection using improved squirrel search algorithm

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A Wireless Sensor Network (WSN) is a significant technological advancement that might contribute to the industrial revolution. The sensor nodes that are part of WSNs are battery-powered. Energy is the most crucial resource for WSNs since batteries cannot be changed or refilled. Since WSNs are a finite resource, several techniques have been devised and used throughout time to preserve them. To extend the lifespan of WSNs, this study will provide an effective method for Cluster Head (CH) selections. Many researches are employing the Swarm-based optimization algorithm to Select the optimal CH. In this study, the Squirrel Search Algorithm (SSA) is utilized to select the optimal CH Selection in WSN. The general SSA has been modified in this study to address the exact need for CH choice in WSNs. The Improved Squirrel Search Algorithm (I-SSA) integrates a series of enhancements aimed at accelerating convergence and elevating solution quality. Notably, we’ve implemented Adaptive Population Initialization, Dynamic Step Size Control, and a Local Search Algorithm to augment the exploration and exploitation capabilities of the SSA. These enhancements collectively refine the algorithm’s ability to navigate the search space effectively, resulting in more efficient convergence towards optimal solutions. The suggested formulation’s goal function takes into account the CH balance average, factor, sink distance residual energy and intra-cluster distance. The simulations are run under a variety of circumstances. The MATLAB 2021a working setting is utilised for simulation. The proposed code of conduct SSA-C is compared with the existing protocols Grey Wolf Optimization (GWO), SSA, Chernobyl Disaster Optimizer (CDO), Sperm Swarm Optimization (SSO), A Metaheuristic Optimized Cluster head selection-based Routing Algorithm for WSNs (MOCRAW), Energy-Efficient Weighted Clustering (EEWC), and Multi-agent pathfinding using Ant Colony Optimization (MAP-ACO). The ISSA-C method achieved a Packet Delivery Ratio (PDR) of 88%, outperforming GWO, SSA, and MAP-ACO. It reduced energy consumption to 210 mJ, which is lower than other methods, and showed improved bit error rates. Cluster formation and head selection times were also reduced to 82 s and 67 s, respectively. © The Author(s) 2024.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1389.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
