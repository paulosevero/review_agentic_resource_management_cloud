---
id: paper-0274
title: Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks
authors:
- Chen, Xing
- Liu, Guizhong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2021
doi: 10.1109/JIOT.2021.3050804
url: https://www.scopus.com/pages/publications/85099563631?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10843--10856
keywords:
- Augmented reality (AR)
- Deep reinforcement learning
- Internet of Things (IoT)
- Mobile-edge computing (MEC)
- Multiagent deep deterministic policy gradient (MADDPG)
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

# paper-0274 — Energy-Efficient Task Offloading and Resource Allocation via Deep Reinforcement Learning for Augmented Reality in Mobile Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The augmented reality (AR) applications have been widely used in the field of Internet of Things (IoT) because of good immersion experience for users, but their ultralow delay demand and high energy consumption bring a huge challenge to the current communication system and terminal power. The emergence of mobile-edge computing (MEC) provides a good thinking to solve this challenge. In this article, we study an energy-efficient task offloading and resource allocation scheme for AR in both the single-MEC and multi-MEC systems. First, a more specific and detailed AR application model is established as a directed acyclic graph according to its internal functionality. Second, based on this AR model, a joint optimization problem of task offloading and resource allocation is formulated to minimize the energy consumption of each user subject to the latency requirement and the limited resources. The problem is a mixed multiuser competition and cooperation problem, which involves the task offloading decision, uplink/downlink transmission resources allocation, and computing resources allocation of users and MEC server. Since it is an NP-hard problem and the communication environment is dynamic, it is difficult for genetic algorithms or heuristic algorithms to solve. Therefore, we propose an intelligent and efficient resource allocation and task offloading algorithm based on the deep reinforcement learning framework of multiagent deep deterministic policy gradient (MADDPG) in a dynamic communication environment. Finally, simulation results show that the proposed algorithm can greatly reduce the energy consumption of each user terminal. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0274.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
