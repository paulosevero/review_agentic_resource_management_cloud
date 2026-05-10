---
id: paper-2672
title: Enhancing reliability of integrated electricity-water systems with data centers via decentralized robust planning considering decision-dependent uncertainties
authors:
- Liang, Chen
- Zeng, Bo
- Lei, Yueyi
- Wen, Zhu
- Zhang, Jiayi
venue: Applied Energy
venue_type: journal
year: 2026
doi: 10.1016/j.apenergy.2026.127574
url: https://www.scopus.com/pages/publications/105031616394?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Coordination
- Decision-dependent uncertainty
- Integrated electricity-water system
- Internet data center
- Reliability enhancement
- Robust optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2672 — Enhancing reliability of integrated electricity-water systems with data centers via decentralized robust planning considering decision-dependent uncertainties

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid expansion of Internet Data Centers (IDCs) has significantly intensified the operational pressure on urban electricity and water infrastructures, necessitating the development of cross-system collaborative planning mechanisms to enhance overall system reliability. This paper proposes a tri-level robust planning framework for the coordinated optimization of IDCs and the integrated electricity-water system (IEWS) under multiple uncertainties. The upper-level model optimizes IDC resource deployment and IEWS infrastructure reinforcement investments. The middle-level model constructs decision-dependent uncertainty (DDU) and decision-independent uncertainty (DIU) sets to jointly capture the endogenous and exogenous coupling mechanisms among load fluctuations, power grid failure scenarios, and renewable energy outputs. The lower-level model addresses system operation scheduling under worst-case disturbances to ensure operational safety and cost-effectiveness. To enhance tractability and convergence efficiency, a hybrid solution approach is developed by integrating Parametric Column-and-Constraint Generation (PC&CG), Analytical Target Cascading (ATC), and Alternating Optimization Process (AOP), enabling synchronized decentralized solving across heterogeneous stakeholders. Case studies demonstrate that the proposed framework significantly improves system reliability under multiple disturbance scenarios, reducing electricity and water load shedding rates from 4.31% to 1.29% and from 6.33% to 2.15%, respectively, while enhancing system adaptability and robustness. This work provides a scalable and privacy-preserving theoretical foundation and methodological tool for robust multi-agent co-planning in integrated IDC-IEWS environments. © 2024

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2672.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
