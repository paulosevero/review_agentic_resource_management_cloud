---
id: paper-0228
title: 'Fog BEMS: An agent-based hierarchical fog layer architecture for improving scalability in a building energy management system'
authors:
- Na, Uikyun
- Lee, Eun-Kyu
venue: Sustainability (Switzerland)
venue_type: journal
year: 2020
doi: 10.3390/su12072831
url: https://www.scopus.com/pages/publications/85083523737?origin=resultslist
publisher: MDPI
pages: ''
keywords:
- Building energy management system
- Distributed system
- Fog computing
- Hierarchical architecture
- Internet of things
- Multi-agent system
- Scalability
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
    my_justification: Out of scope
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

# paper-0228 — Fog BEMS: An agent-based hierarchical fog layer architecture for improving scalability in a building energy management system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> It has been found that a cloud building energy management system (BEMS) alone cannot support increasing numbers of end devices (e.g., energy equipment and IoT devices) and emerging energy services efficiently. To resolve these limitations, this paper proposes Fog BEMS, which applies an emerging fog computing concept to a BEMS. Fog computing places small computing resources (fog nodes) just next to end devices, and these nodes process data in real time and manage local contexts. In this way, the BEMS becomes distributed and scalable. However, existing fog computing models have barely considered scenarios where many end devices and fog nodes are deployed and interconnected. That is, they do not scale up and cannot be applied to scalable applications like BEMS. To solve the problem, this paper (i) designs a fog network where a list of functionally heterogeneous nodes is deployed in a hierarchy for collaboration and (ii) designs an agent-based, modular programming model that eases the development and management of computing services at a fog node. We develop a prototype of a fog node and build a real-world testbed on a campus to demonstrate the feasibility of the proposed system. We also conduct experiments, and results show that Fog BEMS is scalable enough for a node to connect up to 900 devices and that network traffic is reduced by 27.22-97.63%, with varying numbers of end devices. © 2020 by the authors.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0228.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
