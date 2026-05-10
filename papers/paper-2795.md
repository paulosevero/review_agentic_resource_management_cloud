---
id: paper-2795
title: 'SkyLink: Joint Deployment and Scheduling in Collaborative Integrated Ground-Air-Space Network'
authors:
- Tan, Lin
- Guo, Songtao
- Kuang, Zhufang
- Zhou, Pengzhan
- Li, Mingyan
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2026
doi: 10.1109/TWC.2025.3581412
url: https://www.scopus.com/pages/publications/105009414893?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 90--106
keywords:
- aerial platform deployment
- collaborative edge computing
- Integrated ground-air-space networks
- multi-agent deep reinforcement learning
- resource allocation
- task offloading
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2795 — SkyLink: Joint Deployment and Scheduling in Collaborative Integrated Ground-Air-Space Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Low Earth Orbit (LEO) satellite networks hold great promise in the field of wireless communication due to their global coverage. However, the long communication distances and massive data computations present significant challenges for current satellite networks. To overcome these barriers, we propose SkyLink, a universal Integrated Ground-Air-Space Collaborative Edge Computing system that leverages horizontal collaboration among aerial platforms (AirXs) as well as vertical collaboration among Ground-Air-Space. We propose a bi-level optimization framework based on a Multi-Agent Twin Delayed Deep Deterministic policy gradient (MATD3) with Hybrid Action Space and constructe a latent representation space for each agent to allow the agent to learn the latent policy. This enabling each AirX to act as an agent and autonomously optimize its hybrid action decisions to improve system efficiency in real-time based on the dynamic network environment, a capability not achievable by conventional DRL methods. This includes continuous optimization variables such as AirX deployment (location changes) and resource allocation, as well as discrete optimization variables for collaborative task offloading decisions. Extensive experiments against state-of-the-art algorithms (e.g., MADDPG, QMIX) demonstrate that the proposed system improves energy efficiency by 27.2% and task completion rate by 6.8% compared to traditional Integrated Ground-Air-Space (IG) Network. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2795.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
