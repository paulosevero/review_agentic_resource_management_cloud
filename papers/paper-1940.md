---
id: paper-1940
title: Multi-Agent Reinforcement Learning-Based Capacity Planning for On-Demand Vehicular Fog Computing
authors:
- Mao, Wencan
- Yin, Jiaming
- Liu, Yushan
- Cho, Byungjin
- Chen, Yang
- Rao, Weixiong
- Xiao, Yu
venue: IEEE Transactions on Intelligent Vehicles
venue_type: journal
year: 2025
doi: 10.1109/TIV.2024.3422375
url: https://www.scopus.com/pages/publications/105012141794?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1043--1057
keywords:
- Actor-critic
- capacity planning
- multi-agent reinforcement learning (MARL)
- techno-economic analysis
- vehicular fog computing (VFC)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1940 — Multi-Agent Reinforcement Learning-Based Capacity Planning for On-Demand Vehicular Fog Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Fog computing reduces network latency by moving computational resources close to where the data is generated. Vehicular fog computing (VFC) is an emerging computing paradigm where fog nodes deployed on moving vehicles (i.e., vehicular fog nodes (VFNs)) complement stationary fog nodes (e.g., the ones co-located with cellular base stations) to satisfy the spatio-temporally varying demand for computing resources in a cost-efficient manner. On-demand VFC (ODVFC) supports the dynamic routing of VFNs to the places where demand emerges. Different from previous works on capacity planning and vehicle routing that utilize compute-intensive optimization methods such as integer linear programming (ILP), this paper explores the feasibility of applying reinforcement learning to dynamic capacity planning in a time-efficient manner. Specifically, we propose to apply the multi-agent reinforcement learning (MARL) method (i.e., actor-critic) to learn the VFN routing policies. This approach allows distributed VFNs to cooperatively maximize the techno-economic performance of ODVFC. For evaluation, we built an open-source VFC simulation platform that integrates vehicular traffic simulation with 5G NR V2X and MARL environment. Compared with decentralized learning (i.e., each VFN independently learns its routing policy), centralized learning (i.e., using a global agent for VFN routing), and ILP methods, our proposal proves to achieve 8.3% higher revenue and 13.2% higher number of served tasks than decentralized training; and it has 40.6% and 83% lower execution time than centralized learning and ILP, respectively, with only 14% lower revenue than both. It is also scalable to real-life scenarios with a great number of users and VFNs. © 2016 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1940.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
