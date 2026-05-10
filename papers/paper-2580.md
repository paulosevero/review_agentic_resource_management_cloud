---
id: paper-2580
title: 'AI-Enabled Vehicular Data Offloading for Sustainable Smart Cities: Taxonomy, KPI Models, and Open Challenges'
authors:
- Garai, Mouna
- Sliti, Maha
- Mrabet, Manel
- Ben Ammar, Lassaad
venue: IEEE Access
venue_type: journal
year: 2026
doi: 10.1109/ACCESS.2025.3648539
url: https://www.scopus.com/pages/publications/105026049209?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1468--1492
keywords:
- artificial intelligence
- computation offloading
- edge caching
- SDG11
- SDG13
- SDG7
- SDG9
- smart cities
- sustainability
- Vehicular edge computing (VEC)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Review
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

# paper-2580 — AI-Enabled Vehicular Data Offloading for Sustainable Smart Cities: Taxonomy, KPI Models, and Open Challenges

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is emerging as a key enabler for intelligent transportation systems that are both latency- and energy-sensitive. This survey is motivated by the need for a unified, KPI-driven view of AI-based vehicular computation offloading that explicitly links performance gains to sustainability objectives in smart cities. We synthesize recent advances in AI-powered offloading for vehicular networks, with emphasis on deep reinforcement learning (DRL) and multi-agent variants that learn adaptive, sequential policies under dynamic topology, fluctuating wireless capacity, and heterogeneous workloads. We propose a unified taxonomy that spans infrastructure-based, vehicle-assisted, and hybrid architectures; map offloading decisions to key performance dimensions (end-to-end latency, energy efficiency, reliability, throughput, and task-success rate); and formalize a minimal KPI model that links radio, compute, and caching components. The review compares algorithmic designs (DQN/DDPG/A3C/SAC, prioritized and federated variants, DRL+optimizer hybrids), scheduling granularities and baseline choices, while examining reproducibility factors such as simulators, mobility models, and dataset availability. We further discuss integration with enabling technologies (cellular vehicle-to-everything (C-V2X)/NR-V2X, reconfigurable intelligent surfaces (RIS), UAV relays, edge caching), security and privacy considerations, and the sustainability implications of AI-driven offloading for intelligent urban environments. The paper concludes with open challenges including non-stationarity, sim-to-real transfer, safety constraints, and explainability and outlines a research agenda toward robust, accountable, and resource-efficient offloading policies deployable in real world VEC systems. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "Review"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2580.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
