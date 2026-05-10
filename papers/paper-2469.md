---
id: paper-2469
title: Delay Optimization for UAV-Assisted Collaborative Offloading with Ground MEC Servers in Task-Intensive Scenarios
authors:
- Zheng, Zhenkai
- Lin, Na
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2025
doi: 10.1109/ICCT67417.2025.11374078
url: https://www.scopus.com/pages/publications/105034150862?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1033--1039
keywords:
- bi-level optimization □ Soft Actor-Critic(SAC)
- computation offloading
- Mobile edge computing (MEC)
- unmanned aerial vehicle (UAV)
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

# paper-2469 — Delay Optimization for UAV-Assisted Collaborative Offloading with Ground MEC Servers in Task-Intensive Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In computation-intensive networks, Mobile Edge Computing (MEC) presents a viable approach to improving the user experience for applications that are sensitive to latency. This study examines the latency challenges inherent in MEC systems and proposes an edge-coordinated Multi-Agent Soft Actor-Critic (EMSAC) algorithm aimed at the intelligent management of Unmanned Aerial Vehicle (UAV) trajectory planning and data offloading strategies. The system model comprises ground edge servers and UAVs that work in tandem to deliver offloading services to users. We employ a bi-level optimization framework: the lower-level follower problem is dedicated to optimizing UAV movements at each time interval, striving to achieve a balance between efficient energy consumption and the coverage of a greater number of users; conversely, the upper-level leader problem is concerned with optimizing task offloading strategies, with the overarching objective of minimizing total system latency. This research offers a scalable and adaptive solution for UAVassisted MEC networks operating in dynamic environments, thereby providing dependable support for critical tasks and applications that are sensitive to latency. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2469.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
