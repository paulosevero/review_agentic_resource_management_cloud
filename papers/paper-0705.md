---
id: paper-0705
title: Virtual Commissioning of Distributed Systems in the Industrial Internet of Things
authors:
- Rosenberger, Julia
- Selig, Andreas
- Ristic, Mirjana
- Bühren, Michael
- Schramm, Dieter
venue: Sensors
venue_type: journal
year: 2023
doi: 10.3390/s23073545
url: https://www.scopus.com/pages/publications/85152338986?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- distributed stream processing system (DSPS)
- edge computing
- hardware-in-the-loop (HiL)
- Industrial Internet of Things (IIoT)
- simulation
- virtual commissioning (VICO)
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0705 — Virtual Commissioning of Distributed Systems in the Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the convergence of information technology (IT) and operational technology (OT) in Industry 4.0, edge computing is increasingly relevant in the context of the Industrial Internet of Things (IIoT). While the use of simulation is already the state of the art in almost every engineering discipline, e.g., dynamic systems, plant engineering, and logistics, it is less common for edge computing. This work discusses different use cases concerning edge computing in IIoT that can profit from the use of OT simulation methods. In addition to enabling machine learning, the focus of this work is on the virtual commissioning of data stream processing systems. To evaluate the proposed approach, an exemplary application of the middleware layer, i.e., a multi-agent reinforcement learning system for intelligent edge resource allocation, is combined with a physical simulation model of an industrial plant. It confirms the feasibility of the proposed use of simulation for virtual commissioning of an industrial edge computing system using Hardware-in-the-Loop. In summary, edge computing in IIoT is highlighted as a new application area for existing simulation methods from the OT perspective. The benefits in IIoT are exemplified by various use cases for the logic or middleware layer using physical simulation of the target environment. The relevance for real-life IIoT systems is confirmed by an experimental evaluation, and limitations are pointed out. © 2023 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0705.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
