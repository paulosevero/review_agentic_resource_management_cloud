---
id: paper-0931
title: I’ve Got 99 Problems But FLOPS Ain’t One
authors:
- Gherghescu, Alexandru M.
- Bădoiu, Vlad-Andrei
- Agache, Alexandru
- Dumitru, Mihai-Valentin
- Vasilescu, Iuliu
- Mantu, Radu
- Raiciu, Costin
venue: HOTNETS 2024 - Proceedings of the 2024 3rd ACM Workshop on Hot Topics in Networks
venue_type: conference
year: 2024
doi: 10.1145/3696348.3696893
url: https://www.scopus.com/pages/publications/85215670507?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 195--204
keywords:
- Datacenter Networking
- Large Language Models Training
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-0931 — I’ve Got 99 Problems But FLOPS Ain’t One

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Hyperscalers dominate the landscape of large network deployments, yet they rarely share data or insights about the challenges they face. In light of this supremacy, what problems can we find to solve in this space? We take an unconventional approach to find relevant research directions, starting from public plans to build a $100 billion datacenter for machine learning applications [53]. Leveraging the language models scaling laws, we discover what workloads such a datacenter might carry and explore the challenges one may encounter in doing so, with a focus on networking research. We conclude that building the datacenter and training such models is technically possible, but this requires novel wide-area transports for inter-DC communication, a multipath transport and novel datacenter topologies for intra-datacenter communication, high speed scale-up networks and transports, outlining a rich research agenda for the networking community. © 2024 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0931.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
