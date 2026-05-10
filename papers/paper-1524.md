---
id: paper-1524
title: 'KPAMA: A Kubernetes based tool for Mitigating ML system Aging'
authors:
- Ding, Wenjie
- Liu, Zhihao
- Lu, Xuhui
- Du, Xiaoting
- Zheng, Zheng
venue: Journal of Systems and Software
venue_type: journal
year: 2025
doi: 10.1016/j.jss.2025.112389
url: https://www.scopus.com/pages/publications/85219075919?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- Autoscaling
- Data prediction
- Kubernetes-based machine learning system
- Software aging
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1524 — KPAMA: A Kubernetes based tool for Mitigating ML system Aging

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As machine learning (ML) systems continue to evolve and be applied, their user base and system size also expand. This expansion is particularly evident with the widespread adoption of large language models. Currently, the infrastructure supporting ML systems, such as cloud services and computing hardware, which are increasingly becoming foundational to the ML system environment, is increasingly adopted to support continuous training and inference services. Nevertheless, it has been shown that the increased data volume, complexity of computations, and extended run times challenge the stability of ML systems, efficiency, and availability, precipitating system aging. To address this issue, we develop a novel solution, KPAMA, leveraging Kubernetes, the leading container orchestration platform, to enhance the autoscaling of computing workflows and resources, effectively mitigating system aging. KPAMA employs a hybrid model to predict key aging metrics and uses decision and anti-oscillation algorithms to achieve system resource autoscaling. Our experiments indicate that KPAMA markedly mitigates system aging and enhances task reliability compared to the standard Horizontal Pod Autoscaler and systems without scaling capabilities. © 2025 Elsevier Inc.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1524.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
