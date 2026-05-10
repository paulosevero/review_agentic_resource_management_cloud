---
id: paper-1275
title: Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks
authors:
- Wu, Yingying
- Zhang, Zhifei
- Ge, Yiyang
- Mao, Jin
- Chu, Zhipeng
- Xiong, Ke
- Fan, Pingyi
venue: 2024 9th International Conference on Computer and Communication Systems, ICCCS 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCCS61882.2024.10603138
url: https://www.scopus.com/pages/publications/85201318830?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 718--724
keywords:
- Age of Information (AoI)
- High-Speed Railway Networks (HSRNs)
- Mobile Edge Computing (MEC)
- Multiple Agent
- Reinforcement Learning
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

# paper-1275 — Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper investigates mobile edge computing (MEC) assisted high-speed railway networks (HSRNs), where a MEC server positioned at the ground base station (GBS) assists train users in task computing. When the computing capacity of users' equipment is insufficient, the users are allowed to offload their tasks to the MEC server. To well measure the timeliness of users' task computation, we extend the traditional age of information (AoI) to the concept of age of computing (AoC), which is defined as the time elapsed since the last completed task was generated. To pursue the green HSRN design, this paper formulates an energy minimization problem by jointly optimizing task offloading vectors and power allocation vectors. To ensure the timeliness of task execution, AoC is taken as constraints into account. Besides, the maximum available power constraints are also considered. To tackle this non-convex mixed integer nonlinear programming (MINLP) problem, we firstly reformulate it as a Markov Decision Process (MDP) and then propose a Multi-Agent Twin Delayed Deep Deterministic Policy Gradient based resource allocation (MATD3-RA) framework. To characterize the energy consumption of user equipment under the constraints of AoC, we define a utility function as the negative linear combination of the violation of AoC constraints and the energy consumption. Simulation results show that the utility function value of the proposed MATD3-RA is increased by about 14% and about 39% respectively compared to the resource allocation with only MEC and local computing, about 23% compared to the Multi-agent Deep Deterministic Policy Gradient based resource allocation (MADDPG-RA) method, and about 28% compared to the random power allocation method. We also observe that there is a trade-off between energy consumption and AoC. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1275.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
