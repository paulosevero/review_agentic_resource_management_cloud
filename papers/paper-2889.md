---
id: paper-2889
title: Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks
authors:
- Yin, Fangfang
- Liu, Qihong
- Liu, Danpu
- Jin, Libiao
- Li, Shufeng
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3628965
url: https://www.scopus.com/pages/publications/105020879353?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1440--1459
keywords:
- Multiaccess edge computing (MEC)
- multiagent deep reinforcement learning (MADRL)
- resource allocation
- satellite–terrestrial integrated networks (STINs)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2889 — Deep-Reinforcement-Learning-Based Resource Allocation for MEC-Assisted Satellite–Terrestrial Integrated Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article investigates the mixed-timescale resource allocation problem in satellite–terrestrial integrated networks (STINs). Moreover, the multiaccess edge computing (MEC) technology and millimeter wave (mmWave) with rich spectrum resource are merged into the STIN to improve the network performance. A network utility maximization problem characterized by the achievable rate and backhaul reduction is formulated under the constraints of the maximum caching capacity, transmission power of mmWave small-cell base stations (SBSs) and quality of service (QoS) for Internet of Things (IoT) devices, where the caching placement, power allocation, and user-SBS association are jointly optimized. In order to tackle this mixed-integer nonlinear programming (MINLP) problem, we decompose the original problem into the long-term caching placement subproblem, and short-term power allocation and user-SBS association subproblems. Then, a multiagent deep reinforcement learning (MADRL)-based independent proximal policy optimization (IPPO) algorithm is proposed to solve the short-term user-SBS association subproblem. Meanwhile, the linear programming (LP) is used to solve the long-term caching placement subproblem. Furthermore, we derive the closed-form solution of the short-term power allocation subproblem through the Karush–Kuhn–Tucker (KKT) conditions. Simulation results are carried out to validate the effectiveness and scalability of the proposed joint approach. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2889.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
