---
id: paper-1769
title: Joint Partitioning, Allocation, and Transmission Optimization for Federated Learning in Satellite Constellations via Multi-Task MARL
authors:
- Lei, Chengjia
- Wu, Shaohua
- Yang, Yi
- Xue, Jiayin
- Chen, Dawei
- Duan, Pengfei
- Zhang, Qinyu
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3568470
url: https://www.scopus.com/pages/publications/105004925831?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 10345--10362
keywords:
- federated learning
- Multi-agent reinforcement learning
- orbital edge computing
- satellite network
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-1769 — Joint Partitioning, Allocation, and Transmission Optimization for Federated Learning in Satellite Constellations via Multi-Task MARL

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Orbital edge computing (OEC) is crucial for supporting space intelligence applications within satellite networks. However, individual satellites face resource constraints, and implementing distributed processing techniques, such as federated learning (FL), across multiple satellites introduces significant scheduling complexity. To address these challenges, we first model the key factors influencing complex satellite networks, including satellite constellations, regional resource demands, inter-satellite communication and routing, energy consumption, and battery aging—a novel aspect invoked by OEC operations. We propose an adaptive aggregation method to fundamentally improve communication efficiency in OEC-based FL. To enhance scheduling performance, we formulate a unified optimization problem that jointly considers data partitioning, resource allocation, and aggregation transmission tasks within a decentralized partially observable Markov decision process (Dec-POMDP) framework. Furthermore, we introduce an episodic-phase-recalling reward shaping (EPRS) method to correlate the influences across these phases. Inspired by multi-task learning, we propose an efficient multi-agent reinforcement learning (MARL) algorithm featuring a multi-head actor-critic (MH-AC) network structure and task-equalized adaptation (TEA) technology, designed to optimize latency, energy consumption, network traffic, and battery aging. Extensive experiments validate the effectiveness of the proposed method, showing a 29.9% reduction in total training time, an 11.5% reduction in network traffic, and superior overall performance compared to rule-based methods. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1769.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
