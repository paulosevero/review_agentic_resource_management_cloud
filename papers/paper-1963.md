---
id: paper-1963
title: Hierarchical Multi-Agent RL TE in SD-WAN based Cloud Edge Continuum Interconnection
authors:
- Mokhtari, Ayoub
- Ksentini, Adlen
venue: MSWiM 2025 - 27th International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems
venue_type: conference
year: 2025
doi: 10.1109/MSWiM67937.2025.11308726
url: https://www.scopus.com/pages/publications/105032536579?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 234--241
keywords:
- Cloud-Edge Continuum
- Hierarchical MARL
- Reinforcement Learning
- SD-WAN
- Traffic Engineering
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1963 — Hierarchical Multi-Agent RL TE in SD-WAN based Cloud Edge Continuum Interconnection

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of IoT and the rise of latency-sensitive services are pushing computation from centralised clouds toward a Cloud-Edge Continuum (CEC), where services of the same application are deployed across different CEC nodes, with services requiring low latency closer to the user. This transition introduces new challenges, especially interconnecting these CEC nodes and deployed services dynamically to meet their service level agreements (SLAs). In this paper, we address dynamic Traffic Engineering (TE) in SD-WAN in order to maximise services' QoS requirements fulfilment. We introduce a solution based on Hierarchical Multi-Agent Reinforcement Learning (H-MARL) for dynamically routing service flows through appropriate overlay links that maximise the QoS and reduce the network cost. Simulation results show the efficiency of the proposed solution in dropping overall latency and improving QoS fulfilment by about 10% compared with a flat single-layer MARL. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1963.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
