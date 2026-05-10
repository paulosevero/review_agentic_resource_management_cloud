---
id: paper-0304
title: 'On Joint Offloading and Resource Allocation: A Double Deep Q-Network Approach'
authors:
- Khoramnejad, Fahime
- Erol-Kantarci, Melike
venue: IEEE Transactions on Cognitive Communications and Networking
venue_type: journal
year: 2021
doi: 10.1109/TCCN.2021.3116251
url: https://www.scopus.com/pages/publications/85116933779?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1126--1141
keywords:
- 5G
- 6G
- Machine learning
- Multi-access edge computing
- Reinforcement learning
- Resource management
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

# paper-0304 — On Joint Offloading and Resource Allocation: A Double Deep Q-Network Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) is an important enabling technology for 5G and 6G networks. With MEC, mobile devices can offload their computationally heavy tasks to a nearby server which can be a simple node at a base station, a vehicle or another device. With the increasing number of devices, slices and multiple radio access technologies, the problem of task offloading is becoming an increasingly complex problem. Thus, traditional approaches experience limitations while machine learning algorithms emerge as promising methods. In this paper, we consider binary and partial offloading problems and aim to jointly find optimal decisions for offloading and resource allocation which maximize the number of computed bits while minimizing the energy consumption. This allows improved usage of uplink transmit power and local CPU resources. We propose the Deep Reinforcement Learning for Joint Resource Allocation and Offloading (DJROM) algorithm that uses the double deep Q-network approach and models UEs as agents. We compare the proposed approach with two other machine learning based techniques, namely, multi-agent deep Q-learning (MARL-DQL) and multi-agent deep Q network (MARL-DQN) under fixed and mobile scenarios. Our results show that, DJROM scheme enhances the efficiency better than the other compared algorithms. © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0304.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
