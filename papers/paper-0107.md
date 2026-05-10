---
id: paper-0107
title: 'Design and analysis of distributed load management: Mobile agent based probabilistic model and fuzzy integrated model'
authors:
- Ali, Moazam
- Bagchi, Susmit
venue: Applied Intelligence
venue_type: journal
year: 2019
doi: 10.1007/s10489-019-01454-z
url: https://www.scopus.com/pages/publications/85064522998?origin=resultslist
publisher: Springer New York LLC
pages: 3464--3489
keywords:
- Cloud computing
- Distributed systems
- Load monitoring
- Mobile agents
- Resource utilization
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0107 — Design and analysis of distributed load management: Mobile agent based probabilistic model and fuzzy integrated model

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In large-scale distributed systems, performing load monitoring and load balancing is a challenging task in terms of load management. In order to enhance the overall system performance, we have developed and implemented two different models for large-scale distributed load management. The mobile agent-based system is based on a probabilistic normed estimation model. This model uses mobile agents for collecting the instantaneous status of currently available node resources autonomously. The mobile agent is goal oriented and consumes less network and system resources, which is ideal for load monitoring for large-scale distributed systems. Moreover, we have proposed an integrated load balancing and monitoring model for distributed computing systems employing type-1 fuzzy logic. Furthermore, we have proposed a smooth and composite fuzzy membership function in order to model fine-grained load information in a system. In this paper, a detailed software architectural design for mobile agent based load monitoring system as well as the fuzzy-based load balancing approach are presented. The experimental evaluation is presented to compare the behavior and performance of the mobile agent-based probabilistic model and fuzzy integrated model under different load conditions. A detail comparative analysis is presented for the mobile agent-based probabilistic model and fuzzy integrated model to show the performance and efficiency of each model. In this paper, we have computed cross-correlation to find the relation between our proposed models (FIM and MABMS). © 2019, Springer Science+Business Media, LLC, part of Springer Nature.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0107.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
