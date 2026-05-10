---
id: paper-2313
title: Carbon-Aware LLM Inference Instance Deployment and Workload Assignment Across Geo-distributed Data Centers
authors:
- Xiao, Yanran
- Wang, Wei
- Hu, Qiaojun
- Wang, Yibo
- Li, Yajie
- Zhao, Yongli
- Zhang, Jie
venue: Asia Communications and Photonics Conference, ACP
venue_type: conference
year: 2025
doi: 10.1109/ACP66871.2025.11350985
url: https://www.scopus.com/pages/publications/105034211322?origin=resultslist
publisher: Optica Publishing Group (formerly OSA)
pages: ''
keywords:
- Carbon-Aware
- Inference Deployment
- Large Language Models (LLMs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2313 — Carbon-Aware LLM Inference Instance Deployment and Workload Assignment Across Geo-distributed Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid proliferation of large language models (LLMs) has led to an increase in energy consumption and greenhouse gas (GHG) emissions. While prior research has addressed energy efficiency and carbon-aware scheduling in single data center (DC) environments, limited attention has been paid to inference deployment and workload assignment across geo-distributed DCs, where regional disparities in carbon emission intensity and user demand are significant. In this work, we study the problem of LLM inference deployment and workload assignment in geo-distributed DCs. We show that carbon intensity, latency latency, and regional demand heterogeneity interact in complex ways that critically affect the sustainability of LLM inference services. A mixed integer linear programming (MILP) model is proposed to jointly optimize the placement of inference instances and the allocation of request flows, with the objective of minimizing total GHG emissions while satisfying diverse latency requirements. Numerical results based on realistic carbon intensity data, hardware configurations, and user demand demonstrate that strategic workload distribution across regions with lower carbon intensity can substantially reduce the carbon footprint of LLM inference services. This study provides actionable insights for sustainable LLM serving in globally infrastructures. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2313.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
