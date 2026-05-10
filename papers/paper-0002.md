---
id: paper-0002
title: A novel clustering-based approach for SaaS services discovery in cloud environment
authors:
- Bey, Kadda Beghdad
- Nacer, Hassina
- El Yazid Boudaren, Mohamed
- Benhammadi, Farid
venue: ICEIS 2017 - Proceedings of the 19th International Conference on Enterprise Information Systems
venue_type: conference
year: 2017
doi: 10.5220/0006328205460553
url: https://www.scopus.com/pages/publications/85022205324?origin=resultslist
publisher: SciTePress
pages: 546--553
keywords:
- Cloud computing
- Clustering methods
- Matching
- Multi-agents systems
- Resource allocation
- Services discovery
- Software as a Service (SaaS)
- Web service
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

# paper-0002 — A novel clustering-based approach for SaaS services discovery in cloud environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is an emerging new computing paradigm in which both software and hardware resources are provided through the internet as a service to users. Software as a Service (SaaS) is one among the important services offered through the cloud that receive substantial attention from both providers and users. Discovery of services is however, a difficult process given the sharp increase of services number offered by different providers. A Multi-agent system (MAS) is a distributed computing paradigm-based on multiple interacting agents-aiming to solve complex problems through a decentralized approach. In this paper, we present a novel approach for SaaS service discovery based on Multi-agents systems in cloud computing environments. More precisely, the purpose of our approach is to satisfy the user's needs in terms of both result accuracy rate and processing time of the request. To establish the interest of the proposed solution, experiments are conducted on a simulated dataset. Copyright © 2017 by SCITEPRESS - Science and Technology Publications, Lda. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0002.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
