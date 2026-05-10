---
id: paper-2315
title: 'MVPOA: A Learning-Based Vehicle Proposal Offloading for Cloud-Edge-Vehicle Networks'
authors:
- Xiao, Wenjing
- Ling, Xin
- Chen, Miaojiang
- Liang, Junbin
- Alqahtani, Salman A.
- Chen, Min
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3524469
url: https://www.scopus.com/pages/publications/85214314321?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 4738--4749
keywords:
- Cloud-assisted computing
- mobility
- multiagent reinforcement learning
- resource allocation
- task offloading
- vehicular edge computing (VEC)
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
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2315 — MVPOA: A Learning-Based Vehicle Proposal Offloading for Cloud-Edge-Vehicle Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular edge computing (VEC) is an emerging computing paradigm that is rapidly advancing the development of the Internet of Vehicles (IoV). However, edge server has limited data storage capacity and computing resource, making it difficult to handle the massive offloading requests from IoV applications. Moreover, the mobility of vehicles and dynamic data traffic make it highly challenging to design optimal offloading and resource allocation strategies. To address the challenges mentioned above, we design a cloud-edge-vehicle hierarchical architecture for IoV task offloading, introducing a cloud server to assist in computation and alleviate the overload pressure on edge server. Considering the impact of vehicle mobility on task offloading, we propose a mobility detection method to predict which vehicles might leave the communication range of the base station, thereby preventing task offloading failures. Additionally, to achieve efficient task offloading and resource allocation in this complex IoV system, we propose a multiagent-reinforcement-learning-based vehicle proposal offloading algorithm (MVPOA). This algorithm enables vehicles to autonomously decide whether to process tasks locally or propose offloading to edge server. The edge server then decides whether to accept offloading requests based on task priority and sends rejected tasks to cloud server for processing, thereby maximizing the utilization of resources at each layer of the system. Simulation results demonstrate that MVPOA outperforms other baseline approaches in optimizing system delay and energy consumption.  © 2014 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2315.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
