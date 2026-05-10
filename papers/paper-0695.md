---
id: paper-0695
title: When RAN Intelligent Controller in O-RAN Meets Multi-UAV Enable Wireless Network
authors:
- Pham, Chuan
- Fami, Foroutan
- Nguyen, Kim Khoa
- Cheriet, Mohamed
venue: IEEE Transactions on Cloud Computing
venue_type: journal
year: 2023
doi: 10.1109/TCC.2022.3193939
url: https://www.scopus.com/pages/publications/85135742798?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2245--2259
keywords:
- online learning
- open radio access network (O-RAN)
- reinforcement learning
- resource allocation
- task offloading
- Unmanned aerial vehicles (UAVs)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0695 — When RAN Intelligent Controller in O-RAN Meets Multi-UAV Enable Wireless Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicles (UAVs) are projected to be utilized in a variety of unexpected applications, including agriculture, firefighting, emergency response, intelligent transportation, and so on. Wireless communication is one of the primary facilitators in bringing UAVs into a new phase in such applications. To realize the vision in fifth-generation (5G) networks, we propose a 5G-integration of the flexible multi-UAV system and the Open Radio Access Network (O-RAN) architecture, named U-ORAN. Although different studies have been proposed to optimize the UAV trajectory and resource allocation in the radio access network (RAN), our work is the first study to investigate the benefits of adopting UAVs in the O-RAN architecture. In U-ORAN, we consider a flying base station system and propose a joint optimization problem of multi-UAV trajectory and offloading tasks (UTOT) in which UTOT can optimize the routes from users to the core network as well as resource allocation to process offloading tasks. We decompose UTOT into two sub-problems and provide learning solutions based on the multi-agent reinforcement learning and online learning methodologies, both of which are well supported by the O-RAN architecture. Our intensive numerical simulations show that the proposed approaches outperform in a variety of settings and validation scenarios.  © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0695.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
