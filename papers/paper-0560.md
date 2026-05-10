---
id: paper-0560
title: Multitask Multiobjective Deep Reinforcement Learning-Based Computation Offloading Method for Industrial Internet of Things
authors:
- Cai, Jun
- Fu, Hongtian
- Liu, Yan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2022.3209987
url: https://www.scopus.com/pages/publications/85139422791?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1848--1859
keywords:
- Cloud-edge-device system
- computation offloading
- Industrial Internet of Things (IIoT)
- multiagent reinforcement learning
- multiobjective optimization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0560 — Multitask Multiobjective Deep Reinforcement Learning-Based Computation Offloading Method for Industrial Internet of Things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge computing has emerged as a promising paradigm to deploy computing resources to the network edge. However, most existing computation offloading strategies consider only one objective, including latency, energy consumption, and weighted sum of latency and energy consumption. It is challenging to meet different requirements of the heterogeneous Industrial Internet of Things (IIoT) systems, simultaneously. To address this challenge, a multiagent deep reinforcement learning (MADRL)-based computation offloading method is proposed for cloud-edge-device computing, which aims to meet various requirements of different tasks. In the proposed model, two typical types of tasks are considered: 1) latency-sensitive tasks and 2) energy-sensitive tasks. Each type of task can be executed in one of the three layers, i.e., cloud, edge, or device layer. In addition, in the MADRL model, two agents are defined to make global offloading decisions for the two types of tasks according to the task characteristics and network resource status. The experimental results show that the proposed model can guarantee the quality of service in a heterogeneous IIoT system and achieve better system performance in terms of latency and energy consumption than weighted-sum optimization methods.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0560.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
