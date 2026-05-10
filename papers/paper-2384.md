---
id: paper-2384
title: 'Joint Offloading Decision and Spectrum Assignment in D2D-Enhanced MEC Network: A Deep Reinforcement Learning Approach'
authors:
- Yi, Chenyang
- Qian, Yurong
- Xu, Wei
venue: Journal of Communications and Information Networks
venue_type: journal
year: 2025
doi: 10.23919/JCIN.2025.11207207
url: https://www.scopus.com/pages/publications/105028090025?origin=resultslist
publisher: Posts and Telecom Press Co Ltd
pages: 201--214
keywords:
- deep reinforcement learning
- device-to-device
- mobile edge computing
- resource assignment
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2384 — Joint Offloading Decision and Spectrum Assignment in D2D-Enhanced MEC Network: A Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to the adaptability to dynamic environments and the capability of optimizing complex decision-making processes, deep reinforcement learning (DRL) has been recently applied to scheduling and resource allocation problems in wireless communications. In this paper, we propose a DRL-based joint task offloading and spectrum assignment approach in a device-to-device (D2D) enhanced mobile edge computing (MEC) scenario, where multiple resource devices (RDs) and an edge server collaboratively provide auxiliary task offloading services to task devices (TDs). Considering the time-varying wireless channel conditions, we formulate an optimization problem to jointly design the offloading decision and sequential spectrum assignment across multiple coherent time slots. The optimization objective is to minimize offloading latency while ensuring the offloading success rate for all TDs. To address this problem, we propose a two-step approach, comprising a game-based offloading matching (GBOM) to obtain the Nash equilibrium (NE) of offloading decisions, and a multi-agent DRL (MADRL) to solve the sequential spectrum assignment problem. Numerical results show that the proposed GBOM-MADRL algorithm mitigates the system offloading latency and improves the average probability of successful offloading. © 2025, Posts and Telecom Press Co Ltd. All rights reserved.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2384.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
