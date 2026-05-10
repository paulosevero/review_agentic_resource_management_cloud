---
id: paper-1703
title: Efficient On-Orbit Remote Sensing Imagery Processing via Satellite Edge Computing Resource Scheduling Optimization
authors:
- Jiang, Qiangqiang
- Zheng, Lujie
- Zhou, Yu
- Liu, Hao
- Kong, Qinglei
- Zhang, Yamin
- Chen, Bo
venue: IEEE Transactions on Geoscience and Remote Sensing
venue_type: journal
year: 2025
doi: 10.1109/TGRS.2025.3528015
url: https://www.scopus.com/pages/publications/85215929434?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Multiagent deep reinforcement learning (MADRL)
- on-orbit computation
- remote sensing imagery processing
- resource scheduling model
- satellite edge computing (SEC)
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

# paper-1703 — Efficient On-Orbit Remote Sensing Imagery Processing via Satellite Edge Computing Resource Scheduling Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the enormous scale of remote sensing imagery generation, on-orbit computing has become a crucial paradigm to enable near-real-time processing. Due to the limited onboard resources and on-orbit power supply, satellite edge computing (SEC) is developed for satellite-ground collaboration, aiding on-orbit computation. However, the intermittent satellite-to-ground transmission link poses an efficiency challenge when collaborating SEC resources. Therefore, this article proposes a satellite edge computing resource scheduling technique for on-orbit remote sensing imagery processing (SECORS). First, we design a remote sensing mission-specific SEC architecture, which involves an offline-online satellite working mode. Subsequently, a computational resource scheduling model (SEC-RSM) is established, including the directed acyclic graph (DAG) model and mathematical problem formulation. Next, to obtain effective scheduling solutions, we develop an end-to-end algorithm leveraging the multiagent proximal policy optimization and heuristic rule of the earliest finish time (SEC-MPH). Finally, we build a simulation SEC platform to carry out experiments and implement several methods as the comparison including multiobjective evolutionary algorithms, deep reinforcement learning approaches, and the scheme without optimization (baseline). Simulation results show that SECORS achieves 68.87% and 66.60% reductions in time and energy for on-orbit computation. Moreover, our method improves the energy efficiency ratio (EER) by three times and achieves high processing capacity with 548 pixels per unit of power (W) and time (ms). © 1980-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1703.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
