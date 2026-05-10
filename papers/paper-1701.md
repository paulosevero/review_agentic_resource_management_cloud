---
id: paper-1701
title: Co-allocation and operational optimization for green power-direct-supply data center clusters with shared energy storage
authors:
- Jiang, Zeming
- Tang, Yingzhao
- Ding, Shixing
- Yang, Yu
- Zhao, Jingyi
- Tao, Sicheng
- Xu, Yijun
venue: International Journal of Electrical Power and Energy Systems
venue_type: journal
year: 2025
doi: 10.1016/j.ijepes.2025.111403
url: https://www.scopus.com/pages/publications/105022215318?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Asymmetric Nash bargaining
- Data center cluster
- Robust optimization
- Shared energy storage
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

# paper-1701 — Co-allocation and operational optimization for green power-direct-supply data center clusters with shared energy storage

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of data center cluster (DCC) presents significant challenges to power system flexibility and renewable energy integration. This paper proposes a two-stage, bi-level collaborative framework to optimize the joint operation and capacity planning of DCC in Green Power Direct Supply (GPDS) mode and a Shared Energy Storage system. To manage uncertainties in renewable generation and workloads, a data-driven sample-based robust (DSRO) optimization approach is employed to mitigate the conservatism of traditional methods. In the first stage, a robust configuration model determines the optimal capacities of the SES and gas turbines, while linearizing the M/M/1 queuing model to guarantee a service violation rate below 5%. The second stage focuses on distributed operation. The complex, non-convex problem is decoupled into cost minimization and benefit allocation subproblems, solved efficiently using the alternating direction method of multipliers. Cooperative benefits are then distributed via an asymmetric Nash bargaining game, where a novel logarithmic function quantifies each participant's bargaining power based on their net energy contribution, ensuring fair allocation. Simulation results validate that the proposed framework significantly enhances system economy, renewable accommodation, and resource allocation flexibility, offering a robust foundation for multi-agent collaborative energy systems. © 2025 The Author(s)

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1701.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
