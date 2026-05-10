---
id: paper-0238
title: Multi-agent strategy for low voltage DC supply for a smart home
authors:
- Suresh, N.S.
- Kumar, Manish
- Arul Daniel, S.
venue: Smart and Sustainable Built Environment
venue_type: journal
year: 2020
doi: 10.1108/SASBE-05-2019-0060
url: https://www.scopus.com/pages/publications/85076097488?origin=resultslist
publisher: Emerald Publishing
pages: 73--90
keywords:
- Control strategy
- DC grid
- Load management
- Low voltage DC system
- Multi-agent system
- Smart home appliances
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-0238 — Multi-agent strategy for low voltage DC supply for a smart home

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Purpose: The researchers and policy makers worldwide have proposed many ideas for smart cities and homes in urban areas. The extensive work done for urban smart homes neglects the unique constraints of homes at remote mountain tops and deserts and rural village homes. The purpose of this paper is to propose a smart energy management system for a self-sustained home of any type situated in any geographical location with the availability of renewable energy sources like solar, etc. The purpose is mainly to highlight the importance and advantages of direct current (DC) homes with DC loads rather than a conventional alternating current (AC) home with both AC and DC loads. An attempt has been made to evolve a multi-agent coordinated control for the low voltage direct current (LVDC) smart home system. Design/methodology/approach: LVDC supply systems with in situ power generation are providing an efficient solution for the energy needs of a DC smart home. The individual sub-systems of the LVDC system have their unique functions and priorities and hence require both coordinated and independent control. The entire DC smart home system is modeled in the Matlab and codes are implemented for each agent of the home. LVDC grid is operating either in battery connected mode or utility grid-connected mode, and the DC link voltage is held constant in both the cases. Energy imported from the utility grid is minimized by load shedding during the rectifier mode of the bidirectional converter. In addition, load shedding is also done when the battery is discharging to increase the discharge time of the battery. Load shedding is done on the basis of a fixed priority of loads. A 48 s simulation is performed on the Matlab model to bring out the 24-hour operation of the proposed system. Various modes are simulated and the corresponding actions of the agents are tested. Findings: A new control strategy with agents for each sub-system of the LVDC system is presented. Each individual agent works in tandem with other agents and meets its own control imperatives without compromising the requirements of the overall system. Unlike the centralized control system, the proposed control strategy is a distributed control system. The control algorithm for each of the agents is developed, and the pseudo code is presented. The results of the simulation of the proposed scheme are presented to confirm the usefulness of the new control approach. Originality/value: The multi-agent concept for an energy management system is less addressed and thus its potential for efficient home energy management is presented. The proposed multi-agent strategy for a complete DC smart home with exclusive DC loads is not done earlier and is reported for the first time. The success of this strategy can be extended to other DC micro-grid systems like telecom power systems, ships, aircraft, datacentres, server rooms, residential complexes and commercial malls. © 2019, Emerald Publishing Limited.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0238.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
