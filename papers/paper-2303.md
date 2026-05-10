---
id: paper-2303
title: Swarm Intelligence-Based Algorithm for Workload Placement in Edge-Fog-Cloud Continuum
authors:
- Wu, Kefan
- Ghasemi, Abdorasoul
- Schranz, Melanie
venue: International Conference on Agents and Artificial Intelligence
venue_type: conference
year: 2025
doi: 10.5220/0013140800003890
url: https://www.scopus.com/pages/publications/105001735120?origin=resultslist
publisher: Science and Technology Publications, Lda
pages: 310--317
keywords:
- Ant Colony Optimization
- Edge-Fog-Cloud Continuum
- Swarm Intelligence
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

# paper-2303 — Swarm Intelligence-Based Algorithm for Workload Placement in Edge-Fog-Cloud Continuum

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper addresses the workload placement problem in the edge-fog-cloud continuum. We model the edge fog-cloud computing continuum as a multi-agent framework consisting of networked resource supply and demand agents. Inspired by the swarm intelligence behavior of the ant colony optimization, we propose a workload scheduler for the arriving demand agents to increase local resource utilization and reduce com munication costs without relying on a centralized scheduler. Like the ants, the demand agents will release pheromones on the resource agent to indicate the available resources. The next arriving demand agent will most probably choose a neighbor, following the pheromone value and communication cost. The framework’s performance is evaluated in terms of local resource utilization, dependency on fog and cloud, and commu nication cost. We compare these metrics for the ant-inspired algorithm with random and greedy algorithms. The simulation results reveal that the proposed algorithm inspired by swarm intelligence can increase resource utilization at the edge and reduce the dependency on higher layers, while also decreasing the communication cost for the task of resource allocation. © 2025 by SCITEPRESS– Science and Technology Publications, Lda.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2303.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
