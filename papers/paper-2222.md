---
id: paper-2222
title: MADDPG-based task offloading and resource pricing in edge collaboration environment
authors:
- Tong, Zhao
- Deng, Xin
- Zhang, Yuanyang
- Mei, Jing
- Wang, Can
- Li, Keqin
venue: Journal of Systems Architecture
venue_type: journal
year: 2025
doi: 10.1016/j.sysarc.2025.103433
url: https://www.scopus.com/pages/publications/105005264565?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Mobile edge computing
- Resource pricing
- Stackelberg game
- Task offloading
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

# paper-2222 — MADDPG-based task offloading and resource pricing in edge collaboration environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid advancement of fifth-generation communication technologies, the data produced by the Internet of Everything is growing exponentially. As mobile cloud computing struggles to keep up with the demands for massive data processing and low latency, mobile edge computing (MEC) has emerged as a solution. By shifting services from centralized cloud platforms to edge servers located closer to data sources, MEC achieves reduced latency, enhanced computing efficiency, and an improved user experience. This paper introduces a task offloading algorithm designed for a multi-base station cooperative mobile edge environment, addressing the challenges of task offloading and resource pricing. The system architecture includes a macro base station and several micro base stations, strategically deployed in a densely populated mobile device area. Each mobile device serves as an autonomous decision-making unit, offloading tasks to an optimal base station. We model the interactions between base stations and end-users using a Stackelberg game approach, with strategy optimization achieved through a multi-agent deep deterministic policy gradient algorithm. The proposed TO-SG-MADDPG algorithm intelligently coordinates the policies of multiple base stations and end-users by centralized training and distributed execution, resulting in globally optimal task offloading and resource pricing. The results demonstrate that the proposed algorithm not only reduces the task loss rate but also safeguards the interests of all stakeholders. © 2025

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2222.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
