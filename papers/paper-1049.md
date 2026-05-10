---
id: paper-1049
title: Resource Management for QoS-Guaranteed Marine Data Feedback Based on Space-Air-Ground-Sea Network
authors:
- Lin, Yuanmo
- Xu, Zhiyong
- Li, Jianhua
- Wang, Jingyuan
- Li, Cheng
- Huang, Zhonghu
- Xu, Yanli
venue: IEEE Systems Journal
venue_type: journal
year: 2024
doi: 10.1109/JSYST.2024.3439343
url: https://www.scopus.com/pages/publications/85203875778?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1741--1752
keywords:
- Marine communications
- multiagent deep reinforcement learning (MARL)
- resource management
- space air ground sea integrated network (SAGSIN)
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

# paper-1049 — Resource Management for QoS-Guaranteed Marine Data Feedback Based on Space-Air-Ground-Sea Network

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> More developed marine sensors for various applications has induced a rapid increase in marine data. The feedback from these marine data becomes challenging due to the backward marine communication techniques. The space-air-ground-sea integrated network (SAGSIN) provides a possible solution to solve this challenge by making use of the advantages of different networks. However, how to coordinate these networks and manage heterogeneous resources to satisfy the communication requirements of different marine applications remains to be solved. In this article, we investigate the resource management problem of SAGSIN for marine applications. A resource management architecture is proposed in which software-defined networking (SDN) controllers are employed. Based on this architecture, heterogeneous resources can be scheduled, and the data from devices with different communication modes can be transmitted via SAGSIN without changing the communication mode of the devices. We further propose two multiagent deep reinforcement learning resource management schemes to help individual devices find optimal access and resource allocation decisions to feed their data back to the terrestrial data centers. The design of these proposed schemes fully considers the scarce communication resources of marine scenarios, which makes data feedback more communication efficient while satisfying quality of service (QoS) requirements. Simulation results show that the improved MA_SDN_Centralized resource management scheme can significantly reduce the blocking probability of the system with guaranteed QoS, while reducing the communication overhead of learning. © 2007-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1049.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
