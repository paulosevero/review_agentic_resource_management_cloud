---
id: paper-1035
title: Offloading Delay Minimization in Air-Ground Integrated Vehicular Edge Computing Network with Energy Harvesting
authors:
- Li, Shichao
- Huang, Qiurong
- Zhang, Ning
- Chen, Hongbin
- Tan, Fangqing
- Dong, Mianxiong
- Ota, Kaoru
venue: 2024 IEEE/CIC International Conference on Communications in China, ICCC 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCC62479.2024.10681792
url: https://www.scopus.com/pages/publications/85206478732?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 467--472
keywords:
- Computation offloading
- Integer linear programming
- Integer programming
- Markov processes
- Mixed-integer linear programming
- Mobile edge computing
- Unmanned aerial vehicles (UAV)
- Aerial vehicle
- Air grounds
- Delay minimization
- Edge computing
- Energy
- Joint resource allocations
- Low-high
- Trajectory designs
- Transmission distances
- Vehicle trajectories
- Resource allocation
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

# paper-1035 — Offloading Delay Minimization in Air-Ground Integrated Vehicular Edge Computing Network with Energy Harvesting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Compared with the traditional vehicular edge computing (VEC), air-ground integrated vehicular edge computing (AGI-VEC) network composed of unmanned aerial vehicles (UAVs) and VEC has significant advantages such as seamless coverage, short transmission distance, low delay, and high throughput, which can provide the high quality-of-service for Internet of vehicles (IoV). In this paper, we investigate a joint resource allocation and UAV trajectory design problem in AGIVEC network with energy harvesting (EH) to minimize the task offloading delay. Since the problem is a mixed integer programming problem, we first reformulate the problem as a Markov decision process (MDP), and then relax discrete variables into continuous variables, after that, a joint resource allocation and UAV trajectory design (JRATD) algorithm based on the multi-agent deep deterministic policy gradient (MADDPG) method is proposed. Simulation results demonstrate that the proposed JRATD algorithm outperforms other algorithms in minimizing the offloading delay. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1035.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
