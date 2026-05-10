---
id: paper-0436
title: A collaborative optimization strategy for computing offloading and resource allocation based on multi-agent deep reinforcement learning
authors:
- Jiang, Yingying
- Mao, Yuxuan
- Wu, Gaoxiang
- Cai, Zhenhua
- Hao, Yixue
venue: Computers and Electrical Engineering
venue_type: journal
year: 2022
doi: 10.1016/j.compeleceng.2022.108278
url: https://www.scopus.com/pages/publications/85136512704?origin=resultslist
publisher: Elsevier Ltd
pages: ''
keywords:
- MADRL
- MEC
- Resource allocation
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0436 — A collaborative optimization strategy for computing offloading and resource allocation based on multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of mobile edge computing (MEC), the edge cloud with certain computing power is deployed closer to the mobile device, which can well solve the computing and delay requirements of the mobile device. In 5G ultra-dense heterogeneous networks, where the macro base station (MBS) and multiple dense small base stations (SBS) are deployed in the region, the offloading decision faces multiple choices. In order to solve the problem of computing offloading and resource allocation in 5G ultra-dense heterogeneous networks, we propose a collaborative optimization strategy based on multi-agent deep reinforcement learning (MADRL). At each time, the mobile device only needs to make the optimal offloading decision according to its own historical offloading decision, the allocated bandwidth and computing resources at the past time, as well as the service response delay and energy consumption at the past time, without knowing other user information and dynamic network environment information. Simulation results show that the proposed collaborative optimization strategy is better than the other three baseline schemes in terms of service response delay and energy consumption performance. © 2022 Elsevier Ltd

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0436.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
