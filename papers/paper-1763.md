---
id: paper-1763
title: Age of Information and Energy-Efficiency Optimization in RIS-Assisted Vehicular Edge Computing via Hierarchical Deep Reinforcement Learning
authors:
- Lan, Jun
- Jia, Xiangdong
- Kou, Zhilong
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3598039
url: https://www.scopus.com/pages/publications/105013215595?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 43681--43695
keywords:
- Age of Information (AoI)
- deep reinforcement learning (DRL)
- federated multiagent deep deterministic policy gradient (FMADDPG)
- reconfigurable intelligent surface (RIS)
- soft-coupled collaboration
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1763 — Age of Information and Energy-Efficiency Optimization in RIS-Assisted Vehicular Edge Computing via Hierarchical Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of the Internet of Vehicles (IoV) and the increasing demand for real-time data processing, efficient resource allocation (RA) has become a critical challenge in vehicular edge computing (VEC) systems. In this article, we present a novel hybrid deep reinforcement learning (DRL) framework for optimizing RA in reconfigurable intelligent surface (RIS)-assisted VEC systems. The proposed framework addresses the dual challenges of minimizing the Age of Information (AoI) and maximizing energy efficiency in dynamic vehicular networks. By leveraging a hierarchical decomposition strategy, the framework separates the optimization of RIS phase shifts and federated power allocation, enabling efficient management of high-dimensional decision spaces. The upper layer employs a twin delayed deep deterministic policy gradient (TD3)-based RIS controller to optimize phase shifts, while the lower layer utilizes a federated multiagent deep deterministic policy gradient (FMADDPG) algorithm for power allocation. To enhance policy awareness and accelerate convergence, a trajectory pool of upper-layer RIS phase shifts is constructed and embedded into the lower-layer state space, thereby achieving soft-coupled collaboration among hierarchical policies. Simulation results under realistic urban mobility patterns and 3-D geometric channel models demonstrate that the proposed framework significantly outperforms benchmark algorithms, including soft actor–critic (SAC), QMIX, and block coordinate descent (BCD), in terms of AoI reduction, energy efficiency, and communication throughput. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1763.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
