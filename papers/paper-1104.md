---
id: paper-1104
title: 'FootPrinter: Quantifying Data Center Carbon Footprint'
authors:
- Niewenhuis, Dante
- Talluri, Sacheendra
- Iosup, Alexandru
- De Matteis, Tiziano
venue: ICPE 2024 - Companion of the 15th ACM/SPEC International Conference on Performance Engineering
venue_type: conference
year: 2024
doi: 10.1145/3629527.3651419
url: https://www.scopus.com/pages/publications/85193922877?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 189--195
keywords:
- carbon emission
- carbon footprint
- data center
- simulation
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

# paper-1104 — FootPrinter: Quantifying Data Center Carbon Footprint

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Data centers have become an increasingly significant contributor to the global carbon footprint. In 2021, the global data center industry was responsible for around 1% of the worldwide greenhouse gas emissions. With more resource-intensive workloads, such as Large Language Models, gaining popularity, this percentage is expected to increase further. Therefore, it is crucial for data center service providers to become aware of and accountable for the sustainability impact of their design and operational choices. However, reducing the carbon footprint of data centers has been a challenging process due to the lack of comprehensive metrics, carbon-aware design tools, and guidelines for carbon-aware optimization. In this work, we propose FootPrinter, a first-of-its-kind tool that supports data center designers and operators in assessing the environmental impact of their data center. FootPrinter uses coarse-grained operational data, grid energy mix information, and discrete event simulation to determine the data center's operational carbon footprint and evaluate the impact of infrastructural or operational changes. FootPrinter can simulate days of operations of a regional data center on a commodity laptop in a few seconds, returning the estimated footprint with marginal error. By making this project open source, we hope to engage the community in the development of methodologies and tools for systematically assessing and exploring the sustainability of data centers.  © 2024 Copyright held by the owner/author(s).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1104.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
