---
id: paper-1654
title: Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems
authors:
- Hou, Peng
- Zhu, Hongbin
- Lu, Zhihui
- Huang, Shin-Chia
- Yang, Yang
- Chai, Hongfeng
venue: IEEE Transactions on Green Communications and Networking
venue_type: journal
year: 2025
doi: 10.1109/TGCN.2024.3492028
url: https://www.scopus.com/pages/publications/85208591176?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1414--1428
keywords:
- Integrated sensing and communications
- intelligent transportation systems
- multi-access edge computing
- reinforcement learning
- unmanned aerial vehicles
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1654 — Learning-Based Over-the-Air Integrated Sensing, Communication and Computation in UAV Swarm-Enabled Intelligent Transportation Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The Over-the-air Integrated Sensing, Communication, and Computation (Air-ISCC), supported by Unmanned Aerial Vehicles (UAVs), is a key technology for future 6G wireless networks. Air-ISCC can facilitate the mutual gain of communication, sensing, and computation functions. Equipping UAVs with sensing and communication units and computation resources empowers them to sense network environments and incorporate sensing information to provide computation offloading and mobile computing services. To optimize sensing, communication, and computation performance jointly, we present a multi-objective optimization framework in this paper. This framework jointly optimizes time slot scheduling, power control, resource allocation, and service association to maximize the service success of Air-ISCC while minimizing the energy consumption of UAVs. We transform the Air-ISCC problem into a sequential decision-making problem and propose a Proximity policy optimization-Based Intelligent Air-ISCC algorithm (PBIA) based on deep reinforcement learning. Leveraging the parallelization capability of the PBIA algorithm, we further propose training intelligent agents based on parallel deep reinforcement learning to realize autonomous decision-making of UAV swarm. Experimental results show that PBIA can learn effective policies with high learning efficiency and stability. Compared to baselines, PBIA significantly enhances the service success rate from 16.32% to 61.44%. © 2017 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1654.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
