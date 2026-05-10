---
id: paper-2750
title: 'Space-air-ground integrated network-empowered mobile edge computing: MASAC-based URLLC-aware energy optimization; [空天地协同赋能移动边缘计算: 基于 MASAC 的URLLC 感知能耗优化]'
authors:
- Qin, Peng
- Li, Jinghan
- Fu, Yang
venue: Scientia Sinica Informationis
venue_type: journal
year: 2026
doi: 10.1360/SSI-2025-0368
url: https://www.scopus.com/pages/publications/105034876683?origin=resultslist
publisher: Science Press
pages: 1008--1026
keywords:
- multi-agent soft actor-critic (MASAC)
- resource allocation
- space-air-ground collaborative mobile edge computing
- trajectory optimization
- ultra-reliable and low-latency communication
language: Chinese
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

# paper-2750 — Space-air-ground integrated network-empowered mobile edge computing: MASAC-based URLLC-aware energy optimization; [空天地协同赋能移动边缘计算: 基于 MASAC 的URLLC 感知能耗优化]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To fulfill the flexible, efficient, and random access demands as well as quality of service guarantee requirements of diverse terminals in the new power system, it is imperative to tackle the incomplete communication coverage, weak real-time task response, and device energy limitation issues of the current terrestrial network. In this paper, we propose a space-air-ground integrated network-empowered mobile edge computing system model consisting of low-earth orbit satellites, unmanned aerial vehicles (UAVs), and ground devices. We elaborate on the joint optimization problem of task splitting, task offloading, power control, UAV trajectory planning, and edge computational resource allocation, with the aim of minimizing the long-term terminal energy consumption. However, this problem is intractable due to the coupling between short-term optimization decisions and long-term ultra-reliable and low-latency communication (URLLC) constraints. To this end, we employ Lyapunov optimization to transform the original problem into a series of subproblems that can be solved in a slot-by-slot fashion. We then design a multi-agent soft actor-critic (MASAC)-based URLLC-aware energy optimization algorithm, together with improved reparameterization and activation function configuration tricks, to efficiently solve them. Numerical results verify that the proposed approach outperforms other benchmark methods in reducing system energy consumption whilst guaranteeing URLLC constraints. © 2026 Science Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2750.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
