---
id: paper-0140
title: Energy efficient opportunistic edge computing for the Internet of Things
authors:
- Leppanen, Teemu
- Riekki, Jukka
venue: Web Intelligence
venue_type: journal
year: 2019
doi: 10.3233/WEB-190414
url: https://www.scopus.com/pages/publications/85071160555?origin=resultslist
publisher: IOS Press
pages: 209--227
keywords:
- embedded web services
- Internet of Things
- mobile agents
- multi-agent systems
- representational state transfer
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0140 — Energy efficient opportunistic edge computing for the Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing in Internet of Things enhances application execution by retrieving cloud resources to the close proximity of resource-constrained end devices at the edge and by enabling task offloading from these devices to the edge. In this paper, edge computing platforms are extended into the data producing end devices, including wireless sensor network nodes and smartphones, with mobile agents. Mobile agents operate, as a multi-agent system, on the opportunistic network of heterogeneous end devices. The benefits include autonomous, asynchronous and adaptive execution and relocation of application-specific computational tasks, while taking into account the local resource availability. In addition to the vertical edge connectivity, mobile agents enable horizontal sharing of information between these devices. Use cases are presented where mobile agents address challenges in current edge computing platforms. An edge application is evaluated where mobile agents as a multi-agent system process sensor data in a heterogeneous set of end devices, control the operation of the devices and share their tasks results in the system. The mobile agents operate atop a REST-compliant software agent framework that relies on embedded Web services for interoperability. A real-world evaluation and large-scale simulations show that energy consumption is reduced significantly, up to 60%, in the edge application execution. © 2019 - IOS Press and the authors. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0140.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
