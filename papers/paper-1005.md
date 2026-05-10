---
id: paper-1005
title: A fully distributed robust optimal control approach for air-conditioning systems considering uncertainties of communication link in IoT-enabled building automation systems
authors:
- Li, Wenzhuo
- Tang, Rui
- Wang, Shengwei
venue: Energy and Built Environment
venue_type: journal
year: 2024
doi: 10.1016/j.enbenv.2023.02.001
url: https://www.scopus.com/pages/publications/85148735538?origin=resultslist
publisher: KeAi Communications Co.
pages: 446--454
keywords:
- Air-conditioning system
- Communication link failure
- Edge computing
- Internet of Things (IoT)
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

# paper-1005 — A fully distributed robust optimal control approach for air-conditioning systems considering uncertainties of communication link in IoT-enabled building automation systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Internet of Things (IoT) technologies are increasingly implemented in buildings as the cost-effective smart sensing infrastructure of building automation systems (BASs). They are also dispersed computing resources for novel distributed optimal control approaches. However, wireless communication networks are critical to fulfill these tasks with the performance influenced by inherent uncertainties in networks, e.g., unpredictable occurrence of link failures. Centralized and hierarchical distributed approaches are vulnerable against link failure, while the robustness of fully distributed approaches depends on the algorithms adopted. This study therefore proposes a fully distributed robust optimal control approach for air-conditioning systems considering uncertainties of communication link in IoT-enabled BASs. The distributed algorithm is adopted that agents know their out-neighbors only. Agents directly coordinate with the connected neighbors for global optimization. Tests are conducted to test and validate the proposed approach by comparing with existing approaches, i.e., the centralized, the hierarchical distributed and the fully distributed approaches. Results show that different approaches are vulnerable against to uncertainties of communication link to different extents. The proposed approach always guarantees the optimal control performance under normal conditions and conditions with link failures, verifying its high robustness. It also has low computation complexity and high optimization efficiency, thus applicable on IoT-enabled BASs. © 2023

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1005.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
