---
id: paper-0535
title: Joint Communication and Computation Resource Allocation in Fog-Based Vehicular Networks
authors:
- Zhang, Xinran
- Peng, Mugen
- Yan, Shi
- Sun, Yaohua
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3140811
url: https://www.scopus.com/pages/publications/85122887470?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 13195--13208
keywords:
- Computation offloading
- fog-computing-based vehicular networks (VNs)
- multiagent deep reinforcement learning (DRL)
- resource allocation
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

# paper-0535 — Joint Communication and Computation Resource Allocation in Fog-Based Vehicular Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To satisfy the low-latency requirements of emerging computation-intensive vehicular services, offloading these services to edge or cloud servers has been recognized as an effective solution. Due to the limited resources of edge servers and the faraway distance of cloud servers, it is challenging to provide an efficient resource allocation strategy to balance the latency, throughput and the resource utilization. In this paper, an end-edge-cloud collaboration paradigm is presented for computation offloading in fog-based vehicular networks (FVNETs) by incorporating vehicles with idle resources as fog user equipments (F-UEs). To adaptively orchestrate end-edge-cloud resources in different load cases, a two-timescale resource reservation and allocation framework is proposed. Wherein, a Stackelberg-game-based dynamic F-UE incentive problem is first formulated with the cloud server as the leader and multiple F-UEs as the followers, and then an iterative algorithm is proposed to achieve the Stackelberg equilibrium of the computation resource pricing and reservation. On a small timescale, the joint communication and computation resource allocation problem is transferred into a multiagent stochastic game and a lenient multiagent deep-reinforcement-learning-based distributed algorithm is developed to minimize the sum latency. When latency performance deteriorates, F-UE incentive optimization will be triggered to reserve more resources of F-UEs. Simulation results show that the proposed end-edge-cloud orchestrated computation offloading scheme in FVNETs outperforms baselines in terms of average latency.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0535.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
