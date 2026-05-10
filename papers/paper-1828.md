---
id: paper-1828
title: Task Offloading and Resource Allocation in C-V2X based Air-Ground Integrated Vehicular Edge Computing Network
authors:
- Li, Shichao
- Huang, Qiurong
- Chen, Hongbin
- Tan, Fangqing
venue: 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCC65529.2025.11149337
url: https://www.scopus.com/pages/publications/105017645104?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- air-ground integrated vehicular edge computing (AGI-VEC) network
- cellular vehicle-to-everything (C-V2X)
- dual Uu/PC5 interface
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

# paper-1828 — Task Offloading and Resource Allocation in C-V2X based Air-Ground Integrated Vehicular Edge Computing Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In contrast to the traditional vehicular edge computing (VEC) network, the air-ground integrated vehicular edge computing (AGI-VEC) network presents significant benefits characterized by continuous coverage, lower delay, and higher data rates for the Internet of vehicles (IoV). In this paper, considering the vehicles can be connected to the roadside units (RSUs) and unmanned aerial vehicles (UAVs) by using the cellular vehicle-toeverything (C-V2X) links, we investigate a joint task offloading and resource allocation problem in the AGI-VEC network with dual Uu/PC5 interface to minimize the task offloading delay. Due to the non-convexity of the problem, it is difficult to solve by utilizing the traditional methods. We transform it into a Markov decision process (MDP), and then propose a joint task offloading, power allocation, computation resource allocation, and UAV trajectory design (JTPCU) algorithm based on the multi-agent soft actor-critic (MASAC) method. Simulation results demonstrate that, compared to the other benchmark algorithms, the proposed algorithm achieves better performance in reducing task offloading delay.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1828.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
