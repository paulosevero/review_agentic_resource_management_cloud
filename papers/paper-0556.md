---
id: paper-0556
title: A smart palletising planning and control model in Logistics 4.0 framework
authors:
- Borangiu, Theodor
- Răileanu, Silviu
venue: International Journal of Production Research
venue_type: journal
year: 2023
doi: 10.1080/00207543.2022.2154405
url: https://www.scopus.com/pages/publications/85145322697?origin=resultslist
publisher: Taylor and Francis Ltd.
pages: 8580--8597
keywords:
- advanced planning and scheduling systems
- combinatorial optimisation
- distributed MAS
- Integrated logistics engineering
- palletising
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0556 — A smart palletising planning and control model in Logistics 4.0 framework

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The paper describes a smart model for palletising as main intra-logistics task for product-on-pallet distribution, and its development in Logistics 4.0 framework aligned to Industry 4.0. The model is developed in holonic paradigm as a 2-layer Holonic Logistics Execution System (HLES) in semi-heterarchical topology. Scheduling of logistics activities and allocation to resources are optimised for global efficiency on compact time periods. The logistics model virtualises physical entities: resources, pallets and orders as holons implemented with digital twin software, and categories of task workloads: resource health monitoring, dispatching and tracking pallet orders, re-assigning jobs at resource failure, which grants reality-awareness and robustness. Global workload optimisation uses Constraint Programming as decision making technology with ILOG optimiser engine as situation-specific solver tool in SaaS cloud model, and delegate multi-agent system (MAS) technology for intelligence distribution. The optimised objective function is a combination of palletising cost weighted by robot speed limits and pallet storage cost in payable stocks. The main constructs are exemplified and validated on a real-life structure with multiple palletising resources in which programmable logic controllers (PLC) coordinate locally the parallel execution of order holons according to their globally optimised sequence. © 2022 Informa UK Limited, trading as Taylor & Francis Group.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0556.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
