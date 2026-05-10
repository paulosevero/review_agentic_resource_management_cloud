---
id: paper-0639
title: A Cloud-Edge Computing Method for Integrated Electricity-Gas System Dispatch
authors:
- Li, Xueping
- Wang, Ziyang
venue: Processes
venue_type: journal
year: 2023
doi: 10.3390/pr11082299
url: https://www.scopus.com/pages/publications/85169113925?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- cloud-edge computing
- integrated electric–gas system
- MADDPG
- optimal dispatch
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

# paper-0639 — A Cloud-Edge Computing Method for Integrated Electricity-Gas System Dispatch

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> An integrated electric–gas system (IEGS) is the manifestation and development direction of a modern smart power system. This paper employs the cloud-edge computing method to research IEGS’s optimal dispatch to satisfy data protection requirements between power systems and natural gas systems and reduce data transmission pressure. Based on cloud-edge computing architecture, this paper constructs a cloud-edge computing method based on the Multi-agent Deep Deterministic Policy Gradient (MADDPG) algorithm to solve optimal dispatch problems. Then, this paper proposes an IEGS dispatch strategy based on cloud-edge computing, which conducts distributed computing independently at the edge of power and natural gas, and the cloud implements global dispatch based on boundary information and edge learning parameters. This method does not require the exchange of all information between the power system and natural gas system, effectively protecting data privacy. This paper takes the improved IEGS of the IEEE 9 node and Gas 8 node as an example to analyze. The equipment output of this dispatch method is within a reasonable range, and the cost is reduced by 0.21% to 1.03% compared with other methods, which verifies the effectiveness of the cloud-edge computing method in solving dispatch problems. © 2023 by the authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0639.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
