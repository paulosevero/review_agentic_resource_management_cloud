---
id: paper-2857
title: 'Task Offloading in Hierarchical UAV-Enabled MEC Network: A Trust Region Policy Optimization-Based Approach'
authors:
- Xiao, Tianqin
- Lu, Conghui
- Xu, Xin
- Zhang, Yang
venue: IEEE Transactions on Transportation Electrification
venue_type: journal
year: 2026
doi: 10.1109/TTE.2026.3658558
url: https://www.scopus.com/pages/publications/105029018913?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3999--4010
keywords:
- Mobile edge computing (MEC)
- offloading strategy
- reinforcement learning (RL)
- uncrewed aerial vehicle (UAV)
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

# paper-2857 — Task Offloading in Hierarchical UAV-Enabled MEC Network: A Trust Region Policy Optimization-Based Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the explosion of multimedia applications and heterogeneous Internet of Things (IoT) devices in service under 5G, the flying ad hoc network (FANET), which acts as an edge server, is overwhelmed by traffic overload. Existing FANET architectures are incomplete for large-scale scenarios, and it is a challenge to optimize uncrewed aerial vehicles (UAVs) offloading decisions and coordinate within the network. In this article, we propose a novel three-layer computational framework for UAVs, which specifies the functions and roles of UAVs in the system. To analyze model performance quantitatively, the interactions of units and tasks are formulated as Markov decision processes (MDPs). Then, we consider delay, energy, and resource allocation to minimize the total system cost. To solve the problem, a multiagent TRPO-based hierarchical computation and offloading (MATRPO-HCO) scheme is proposed to determine the optimal offloading decision for large-scale networks. Simulation results show that the proposed framework is superior to alternative schemes with respect to quality of service (QoS) and fairness. © 2015 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2857.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
