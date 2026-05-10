---
id: paper-0936
title: 'CyTFS: Cyber-Twin Fog System for Delay-Efficient Task Offloading in 6G Mobile Networks'
authors:
- Gopikrishnan, S.
- Sethuraman, Sibi Chakkaravarthy
- Srivastava, Gautam
- Theerthagiri, Sudhakar
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2024
doi: 10.1109/JIOT.2024.3375234
url: https://www.scopus.com/pages/publications/85188012263?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 24698--24714
keywords:
- Cyber Twin (CT)
- deep reinforcement learning (DRL)
- delay reduction
- fog computing (FC)
- sixth-generation (6G) mobile network
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

# paper-0936 — CyTFS: Cyber-Twin Fog System for Delay-Efficient Task Offloading in 6G Mobile Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> —Sixth-generation (6G) mobile computing is a wireless, cutting-edge technology that is made possible by the digital Interconnectedness of Everything (IoE). 6G connection depends on mobile edge and fog computing integration. Due to the mobility of various end users, task offloading in these computing devices is hard and unpredictable. The unexpected mobility of users and dynamic switching of networks from 5G to 6G make mobile fog computing (MFC) benchmarks poor for task offloading. To overcome these inefficient task offloading in dynamic unpredictable 6G mobile environments, this article presents an optimized Cyber Twin (CT)-based solution for task offloading with reduced offload latency in MFC. The proposed solution is built on the CT-based fog computing (CyTFC) system where the computation node predicts server state with a DRL-based multiagent asynchronous advantage actor–Űcritic (MA3C) framework and provides the training data set for task offloading prediction with a reward function. Furthermore, a delay-efficient offloading scheme is also proposed at the CT fog computing nodes. The Lyapunov optimization function was also modified to lower long-term migration costs. Finally, a deep reinforcement learning method called multiagent asynchronous advantage actorŰcritic (MA3C) is suggested to solve the multiobjective dynamic optimization issue. The proposed CT-based solution exceeds existing state-of-the-art benchmarks with network fairness up to 92% and reduces offloading time, offloading failure rate, and task migration cost by 30%, according to the performance assessment findings from the thorough simulation. © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0936.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
