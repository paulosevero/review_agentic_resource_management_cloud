---
id: paper-2287
title: 'Optimizing machine learning operations in multi-cloud infrastructure: a framework for unified deployment management and topology discovery'
authors:
- Wei, Hao
- Pañeda, Xabiel García
- Rodriguez, Joaquín Salvachúa
venue: Cluster Computing
venue_type: journal
year: 2025
doi: 10.1007/s10586-025-05584-7
url: https://www.scopus.com/pages/publications/105017671305?origin=resultslist
publisher: Springer
pages: ''
keywords:
- Cloud computing
- DevOps
- MLOps
- Policy-base control
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2287 — Optimizing machine learning operations in multi-cloud infrastructure: a framework for unified deployment management and topology discovery

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Machine learning (ML) transitioned from a purely academic discipline to an applied field, gaining strategic importance in various industries. Meanwhile, Machine Learning Operations (MLOps) has been widely adopted by enterprises as a comprehensive approach for developing and managing machine learning applications. Despite its advantages, challenges remain. The rising demand for flexibility and scalability has led organizations to embrace multi-cloud and hybrid cloud architectures as preferred solutions. However, the autonomous and distributed nature of modern application development, combined with the complexity of training and deploying machine learning models, makes unified operational management impractical, and this will further affect application quality and efficiency. To address these challenges, this paper proposes a framework to manage model training and deployment in a multi-cloud environment. This framework uses a policy-based resource provisioning approach, agent-based application topology reconstruction, and a visualization dashboard. It aims to provide a cloud provider-neutral solution that enhances the quality of application operations. The framework design is introduced, followed by the implementation of a proof-of-concept prototype. Experiments conducted in various empirical scenarios demonstrate that the proposed framework effectively manages deployment resources while providing clear visibility and control across multiple clouds. The results confirm that this framework enhances control over deployment resources and optimizes model deployment efficiency in multi-cloud infrastructure. © The Author(s) 2025.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2287.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
