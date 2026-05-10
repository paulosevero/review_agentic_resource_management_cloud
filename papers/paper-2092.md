---
id: paper-2092
title: Network Traffic Reduction Through AI-Assisted Local Data Optimization of Synthetic Data
authors:
- Rüb, Matthias
- Grüber, Jens
- Schotten, Hans D.
venue: International Conference on Information and Communications Technology, ICOIACT
venue_type: conference
year: 2025
doi: 10.1109/ICOIACT67584.2025.11344995
url: https://www.scopus.com/pages/publications/105033352531?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 310--315
keywords:
- AI
- Edge computing
- Sustainability
- Synthetic data
- Wireless networks
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2092 — Network Traffic Reduction Through AI-Assisted Local Data Optimization of Synthetic Data

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In future wireless networks, AI instances are expected to take on autonomous tasks increasingly. In this context, the availability of high-quality synthetic data is becoming more important, as AI-agents in different domains, such as healthcare and natural language processing (NLP) will be expected to run safety and stability tests without the need for real data. Synthetic data is also useful for clinical practitioners to address imbalances in datasets or to augment existing data. However, this increased demand for datasets places an additional burden on the communication infrastructure, adding to the existing traffic. T his n ot o nly impacts t he performance o f t he network but also negatively affects sustainability. In this work addresses these issues by introducing a new paradigm, which shifts away from transmitting entire datasets and focuses on local data generation and optimization instead. While this approach has been desirable for a long time, recent developments in artificial intelligence (AI), particularly in NLP, have made it now feasible by empowering end-users without technical expertise to perform data optimization. As an exemplary use case, this work demonstrates a large language model (LLM) curated data optimization using synthetic smart insole gait data. Several low-weight LLMs are tasked to assist the curation. It is shown that local light-weight models, which can be deployed even with low-cost clinical IT infrastructure, can support non-experts with the local optimization process of otherwise insufficient synthetic data. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2092.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
