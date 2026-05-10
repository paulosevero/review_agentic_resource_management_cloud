---
id: paper-2491
title: Cost Optimization and Performance Control in the Hybrid Multi-cloud Environment
authors:
- Zibitsker, Boris
- Lupersolsky, Alexander
venue: ICPE 2025 - Proceedings of the 16th ACM/SPEC International Conference on Performance
venue_type: conference
year: 2025
doi: 10.1145/3676151.3722007
url: https://www.scopus.com/pages/publications/105007304741?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 147--157
keywords:
- closed-loop feedback control
- cost optimization
- finops
- generative ai
- gradient optimization.
- hybrid multi-cloud
- modeling
- observability
- performance control
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

# paper-2491 — Cost Optimization and Performance Control in the Hybrid Multi-cloud Environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Escalating cloud costs and unpredictable performance are major challenges for organizations, particularly when deploying Generative AI (GenAI) applications in hybrid multi-cloud environments-a market projected to reach nearly 20 trillion by 2030. This paper introduces a novel systems approach to cost optimization, performance control, and FinOps decision-making through automated observability, advanced queueing network modeling, and gradient optimization. Observability automation narrows the scope of the tuning efforts by focusing on the most resource-consuming and credit use applications, applications with the highest rate of performance and cost anomalies, applications with the highest frequency of failed queries, and applications with the highest volume of data spilled to local and remote storage. Modeling and optimization determine the minimal configurations, resource allocation, workload management, and budgets needed to meet Service Level Goals (SLGs) for all business applications running on different cloud data platforms in the Hybrid Multi-Cloud environment. Modeling and optimization evaluate options and set cost and performance expectations for proposed changes. By comparing actual performance and costs with expectations, our approach enables closed-loop performance and cost control, mitigating the risks of unexpected financial and operational outcomes. The presented case studies highlight the value of our technology in optimizing application costs and controlling performance across diverse projects, including sizing new applications before cloud deployment, selecting appropriate cloud platforms, optimizing cloud migration strategies, and managing dynamic capacity in hybrid multi-cloud environments. Our predictions demonstrated high accuracy, with the difference between measured and predicted costs within 10%. © 2025 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2491.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
