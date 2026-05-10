---
id: paper-2132
title: D2D-Assisted MEC Bidirectional Task Offloading and Resource Allocation in IIoT
authors:
- Shi, Huaguang
- Kang, Yazhi
- Huang, Jian
- Li, Wei
- Zhou, Yi
venue: Proceedings of 2025 IEEE 14th Data Driven Control and Learning Systems Conference, DDCLS 2025
venue_type: conference
year: 2025
doi: 10.1109/DDCLS66240.2025.11065830
url: https://www.scopus.com/pages/publications/105011825481?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 226--232
keywords:
- deep reinforcement learning
- Device-to-Device (D2D)
- Mobile Edge Computing (MEC)
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

# paper-2132 — D2D-Assisted MEC Bidirectional Task Offloading and Resource Allocation in IIoT

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) and Device-to-Device (D2D) communication show remarkable effects in solving the problem of insufficient device computing resources in Industrial Internet of Things (IIoT). Tasks can be offloaded to MEC servers or idle robots to reduce computation delay and avoid network congestion. However, with D2D communication, the dimensionality explosion problem arises due to complex offloading strategies in real-world scenarios. To address this concern, we design a Bidirectional Task Offloading and Resource Allocation (BTORA) algorithm based on multi-agent deep reinforcement learning. The BTORA algorithm employs an action mask mechanism to dynamically limit the offloading action space of the task generating device to fully utilize the computational resources. In addition, Transformer is utilized to allow Mixing network to focus on the key informations of task offloading, thus optimizing the task offloading decision. Simulation results show that the BTORA algorithm outperforms existing algorithms in terms of cumulative reward, average processing delay, and average offloading success rate while maintaining a lightweight model. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2132.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
