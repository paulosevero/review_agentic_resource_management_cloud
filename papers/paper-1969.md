---
id: paper-1969
title: Sustainable Carbon-Aware and Water-Efficient LLM Scheduling in Geo-Distributed Cloud Datacenters
authors:
- Moore, Hayden
- Qi, Sirui
- Hogade, Ninad
- Milojicic, Dejan
- Bash, Cullen
- Pasricha, Sudeep
venue: Proceedings of the ACM Great Lakes Symposium on VLSI, GLSVLSI
venue_type: conference
year: 2025
doi: 10.1145/3716368.3735301
url: https://www.scopus.com/pages/publications/105017761029?origin=resultslist
publisher: Association for Computing Machinery
pages: 929--934
keywords:
- Carbon emissions
- Energy cost
- Large language model
- Water
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1969 — Sustainable Carbon-Aware and Water-Efficient LLM Scheduling in Geo-Distributed Cloud Datacenters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In recent years, Large Language Models (LLM) such as ChatGPT, Copilot, and Gemini have been widely adopted in different areas. As the use of LLMs continues to grow, many efforts have focused on reducing the massive training overheads of these models. But it is the environmental impact of handling user requests to LLMs that is increasingly becoming a concern. Recent studies estimate that the costs of operating LLMs in their inference phase can exceed training costs by 25× per year. As LLMs are queried incessantly, the cumulative carbon footprint for the operational phase has been shown to far exceed the footprint during the training phase. Further, estimates indicate that 500 ml of fresh water is expended for every 20-50 requests to LLMs during inference. To address these important sustainability issues with LLMs, we propose a novel framework called SLIT to co-optimize LLM quality of service (time-to-first token), carbon emissions, water usage, and energy costs. The framework utilizes a machine learning (ML) based metaheuristic to enhance the sustainability of LLM hosting across geo-distributed cloud datacenters. Such a framework will become increasingly vital as LLMs proliferate. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1969.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
