---
id: paper-0083
title: A negotiation-based service selection approach using swarm intelligence and kernel density estimation
authors:
- Mezni, Haithem
- Sellami, Mokhtar
venue: Software - Practice and Experience
venue_type: journal
year: 2018
doi: 10.1002/spe.2575
url: https://www.scopus.com/pages/publications/85046729866?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: 1285--1311
keywords:
- kernel density estimation
- negotiation
- particle swarm optimization
- self-* Web service
- service selection
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
    my_justification: Swarm intelligence + KDE
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

# paper-0083 — A negotiation-based service selection approach using swarm intelligence and kernel density estimation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Nowadays, the cloud computing environment is becoming a natural choice to deploy and provide Web services that meet user needs. However, many services provide the same functionality and high quality of service (QoS) but different self-adaptive behaviors. In this case, providers' adaptation policies are useful to select services with high QoS and high quality of adaptation (QoA). Existing approaches do not take into account providers' adaptation policies in order to select services with high reputation and high reaction to changes, which is important for the composition of self-adaptive Web services. In order to actively participate to compositions, candidate services must negotiate their self-* capabilities. Moreover, they must evaluate the participation constraints against their capabilities specified in terms of QoS and adaptation policies. This paper exploits a variant of particle swarm optimization and kernel density estimation in the selection of service compositions and the concurrent negotiations of their QoS and QoA capabilities. Selection and negotiation processes are held between intelligent agents, which adopt swarm intelligence techniques for achieving optimal selection and optimal agreement on providers' offers. To resolve unknown autonomic behavior of candidate services, we deal with the lack of such information by predicting the real QoA capabilities of a service through the kernel density estimation technique. Experiments show that our solution is efficient in comparison with several state-of-the-art selection approaches. Copyright © 2018 John Wiley & Sons, Ltd.

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
- **my_justification:** "Swarm intelligence + KDE"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0083.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
