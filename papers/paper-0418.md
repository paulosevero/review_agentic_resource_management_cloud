---
id: paper-0418
title: Joint Task Offloading and Resource Allocation in STAR-RIS assisted NOMA System
authors:
- Guo, Liang
- Jia, Jie
- Chen, Jian
- Du, An
- Wang, Xingwei
venue: IEEE Vehicular Technology Conference
venue_type: conference
year: 2022
doi: 10.1109/VTC2022-Fall57202.2022.10013059
url: https://www.scopus.com/pages/publications/85146980919?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- MADRL
- MEC
- Resource allocation
- SGF-NOMA
- STAR-RIS
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-0418 — Joint Task Offloading and Resource Allocation in STAR-RIS assisted NOMA System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, the joint task offloading and resource allocation are investigated for the semi-grant-free (SGF) non-orthogonal multiple access (NOMA) assisted mobile edge computing (MEC) system. Moreover, simultaneously transmitting and reflecting reconfigurable intelligent surfaces (STAR-RIS) are deployed to improve the quality of wireless communications under the mode switching protocol. Each MU can partially or fully offload its task to the base station (BS) based on its differentiated channel conditions and computing capacity in the proposed MEC system. We formulate the joint task offloading, channel assignment, power allocation, and the RIS coefficients design problem to save energy consumption. The formulated problem is modeled from a long-term optimization perspective as a multi-agent Markov game (MG). Then, a multi-agent deep reinforcement learning (MADRL) based joint task offloading and resource allocation (JTORA) algorithm is proposed to solve the problem. The simulation results confirm that the applied SGF-NOMA scheme can significantly reduce energy consumption under a stringent latency constraint. Moreover, the effectiveness of the STAR-RIS and the proposed algorithm are confirmed.  © 2022 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0418.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
