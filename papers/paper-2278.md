---
id: paper-2278
title: Providing load flexibility by reshaping power profiles of large language model workloads
authors:
- Wang, Yi
- Guo, Qinglai
- Chen, Min
venue: Advances in Applied Energy
venue_type: journal
year: 2025
doi: 10.1016/j.adapen.2025.100232
url: https://www.scopus.com/pages/publications/105010873248?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- Energy efficiency
- Frequency scaling
- Large language model
- Load flexibility
- Renewable energy
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
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

# paper-2278 — Providing load flexibility by reshaping power profiles of large language model workloads

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of large language models (LLM) has driven a significant increase of AI workload in data center power demand. Renewable-powered solutions to decarbonizing LLM workload and reducing electricity costs are faced with the combined volatility of stochastic user requests and renewable energy. The key to removing the barriers in sustainable AI development lies in the adjustable capability of LLM power profiles. Therefore, this paper focuses on exploring the potential load flexibility of LLM workload and proposes a coordinated scheduling framework, notably, without computing performance degradation. Driven by the existence of the energy-optimal core frequency for graphics processing units (GPU), the energy-performance decoupling phenomenon is discovered and proved, where collaborative scaling in GPU quantity and frequency can change power but not computing performance. Motivated by this, the framework slows down the fine-tuning cluster and utilizes idle GPU resources from the inference cluster to maintain the computing performance of fine-tuning tasks. Consequently, the power consumption of the total cluster is reduced, which provides a fresh source of load flexibility. Furthermore, the framework employs dynamic frequency scaling to more flexibly modify the power profile of the expanded fine-tuning cluster. The computing performance is particularly guaranteed through temporal coupling constraints. In a simulated study supported by real-world data, the results prove a 6.8% power-saving ability and 11.3% cost-saving gains on average. © 2025 The Authors

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2278.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
