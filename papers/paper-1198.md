---
id: paper-1198
title: DRL-based Joint Resource Scheduling of eMBB and URLLC in O-RAN
authors:
- Sohaib, Rana M.
- Shah, Syed Tariq
- Onireti, Oluwakayode
- Sambo, Yusuf
- Abbasi, Qammer H.
- Imran, M.A.
venue: 2024 IEEE International Conference on Communications Workshops, ICC Workshops 2024
venue_type: conference
year: 2024
doi: 10.1109/ICCWorkshops59551.2024.10615451
url: https://www.scopus.com/pages/publications/85200392848?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1523--1528
keywords:
- DRL
- eMBB
- O-RAN
- Resource Allocation
- URLLC
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1198 — DRL-based Joint Resource Scheduling of eMBB and URLLC in O-RAN

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This work addresses resource allocation challenges in multi-cell wireless systems catering to enhanced Mobile Broad-band (eMBB) and Ultra-Reliable Low Latency Communications (URLLC) users. We present a distributed learning framework tailored to O-RAN network architectures. Leveraging a Thompson sampling-based Deep Reinforcement Learning (DRL) algorithm, our approach provides real-time resource allocation decisions, aligning with evolving network structures. The proposed approach facilitates online decision-making for resource allocation by deploying trained execution agents at Near-Real Time Radio Access Network Intelligent Controllers (Near-RT RICs) located at network edges. Simulation results demonstrate the algorithm's effectiveness in meeting Quality of Service (QoS) requirements for both eMBB and URLLC users, offering insights into optimising resource utilisation in dynamic wireless environments. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1198.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
