---
id: paper-0456
title: A fully distributed optimal control approach for multi-zone dedicated outdoor air systems to be implemented in IoT-enabled building automation networks
authors:
- Li, Wenzhuo
- Wang, Shengwei
venue: Applied Energy
venue_type: journal
year: 2022
doi: 10.1016/j.apenergy.2021.118408
url: https://www.scopus.com/pages/publications/85121988835?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Communication topology
- Distributed optimal control
- Edge computing
- HVAC system
- IoT
- Multi-agent system
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0456 — A fully distributed optimal control approach for multi-zone dedicated outdoor air systems to be implemented in IoT-enabled building automation networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> For heating, ventilation and air-conditioning (HVAC) systems, centralized optimal control approaches are widely investigated, while hierarchical distributed optimal control approaches are of increasing attention. Using both approaches, the central station and the coordinating agent play critical roles, resulting in low robustness. A novel fully distributed approach may offer higher robustness, but has not yet been investigated for HVAC systems. This paper therefore proposes a fully distributed optimal control approach for multi-zone dedicated outdoor air systems (DOASs) to be implemented in IoT-enabled building automation networks. Without the coordinating agent, information is exchanged directly between connected agents. The optimal solutions are found by coordinating these multiple agents. During iterations, the outdoor air volume of individual rooms and the PAU are optimized locally using the Incremental Cost Consensus (ICC) algorithm, and the outdoor air volume mismatch is estimated locally using the average consensus algorithm. Tests are conducted to validate the proposed approach by comparing it with existing approaches. The impacts of communication topology on the performance of the proposed approach are investigated. Results show that the proposed fully distributed optimal control approach with the fully connected topology performs better than the existing hierarchical distributed approach. Among different communication topologies, the proposed approach with the fully connected topology had the highest robustness, lowest computation complexity and highest optimization efficiency. It also guaranteed the best control performance when deployed over physical platforms (e.g. IoT-based smart sensors of limited capacity), which limit the maximum iteration number. © 2021 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0456.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
