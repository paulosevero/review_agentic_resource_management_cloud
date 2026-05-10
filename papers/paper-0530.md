---
id: paper-0530
title: Standards-based modeling and deployment of serverless function orchestrations using BPMN and TOSCA
authors:
- Yussupov, Vladimir
- Soldani, Jacopo
- Breitenbücher, Uwe
- Leymann, Frank
venue: Software - Practice and Experience
venue_type: journal
year: 2022
doi: 10.1002/spe.3073
url: https://www.scopus.com/pages/publications/85123751822?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: 1454--1495
keywords:
- BPMN
- FaaS
- function orchestrations
- function-as-a-service
- serverless
- TOSCA
- workflows
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

# paper-0530 — Standards-based modeling and deployment of serverless function orchestrations using BPMN and TOSCA

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Function-as-a-Service (FaaS) is a cloud service model enabling to implement serverless applications for a variety of use cases. These range from scheduled calls of single functions to complex function orchestrations executed using orchestration services such as AWS step functions. However, since the available function orchestration technologies vary in functionalities, supported modeling languages, and APIs, modeling such function orchestrations and their deployment require significant technology-specific expertise. Moreover, the resulting models are typically not portable due to provider- and technology-specific details, and major efforts are required when exchanging an orchestrator or provider due to such lock-ins. To tackle this issue, we introduce a vendor- and technology-agnostic method for the modeling and deployment of serverless function orchestrations, which relies on the business process model and notation (BPMN) and topology and orchestration specification for cloud applications (TOSCA) standards for modeling function orchestrations and their deployment, respectively. We also present a toolchain for modeling serverless function orchestrations in BPMN, generating proprietary models supported by different function orchestration technologies from BPMN models, specifying their actual deployment in TOSCA, and then enacting such deployment. Finally, we illustrate a case study applying our method and toolchain in practice. © 2022 The Authors. Software: Practice and Experience published by John Wiley & Sons Ltd.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0530.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
