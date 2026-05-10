---
id: paper-2535
title: 'LightLoader: Accelerate Python FaaS Cold-Start via Multi-level Source Code Optimization'
authors:
- Chen, Pengyu
- Chen, Wei
- Wu, Guoquan
- Wei, Jun
venue: Lecture Notes in Computer Science
venue_type: conference
year: 2026
doi: 10.1007/978-981-95-5015-9_7
url: https://www.scopus.com/pages/publications/105028365267?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 92--106
keywords:
- cold-start
- FaaS
- Python
- serverless computing
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

# paper-2535 — LightLoader: Accelerate Python FaaS Cold-Start via Multi-level Source Code Optimization

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cold starts are a big challenge in Function-as-a-Service (FaaS). While most solutions focus on optimizing the runtime environment and FaaS scheduling, they often overlook the impact of FaaS implementation on cold-start latency. Dynamic languages like Python, with their extensive dependency imports and dynamic building processes, can particularly suffer from longer startup times. We propose LightLoader, an approach to accelerating Python-based FaaS (i.e., PyFaaS) cold start by debloating them and optimizing their dynamic build. LightLoader rewrites PyFaaS by converting potentially unused functions to on-demand dynamic loading, thereby reducing loading time. It also delays third-party package loading until its first use instead of importing these all at the beginning. Notably, to ensure that these rewrites do not compromise the original PyFaaS’s functionalities, we utilize a large language model (LLM) to test and repair the optimized PyFaaS iteratively. We implemented a prototype on the popular open-source serverless platform OpenFaaS and conducted an extensive evaluation with PyFaaS of various sizes and functionalities. The experimental results show that LightLoader effectively accelerates PyFaaS cold starts, reducing end-to-end latency by 11.44% on average, a 9.32% improvement over the state-of-the-art solution. It also decreases the runtime memory utilization by an average of 9.28% and up to 43.27%. LightLoader is platform-independent and can be a supplement to the optimizations of other layers. © The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2026.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2535.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
