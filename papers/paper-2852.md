---
id: paper-2852
title: Model-Based Decentralized Joint Optimization of Resource Allocation, Phase Shift, and UAV Trajectory for Energy-Efficient RIS Assisted UAV-MEC Systems
authors:
- Wu, Liangshun
- Tao, Tao
- Zhang, Bin
- Wang, Kezhi
- Du, Jianbo
- Qu, Junsuo
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2026
doi: 10.1109/TVT.2026.3666220
url: https://www.scopus.com/pages/publications/105030697217?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Mobile Edge Computing
- Multi-Agent Reinforcement Learning
- Reconfigurable Intelligent Surfaces
- Unmanned Aerial Vehicles
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

# paper-2852 — Model-Based Decentralized Joint Optimization of Resource Allocation, Phase Shift, and UAV Trajectory for Energy-Efficient RIS Assisted UAV-MEC Systems

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) enables low-latency, energy-efficient offloading in next-generation wireless networks, but its performance degrades when direct links are blocked in dense urban areas. To address this, recent studies integrate Unmanned Aerial Vehicles (UAVs) and Reconfigurable Intelligent Surfaces (RIS) to enhance coverage and efficiency through UAV mobility and RIS-assisted virtual line-of-sight paths. However, existing centralized optimization approaches suffer from high complexity and communication overhead, making real-time coordination difficult in dynamic multi-UAV settings. To overcome these challenges, we propose a decentralized, model-based reinforcement learning (RL) framework for UAV-RIS-MEC systems, where each UAV learns trajectory, RIS configuration, task offloading, and resource allocation policies using local observations and limited κ-hop neighbor communication. By employing short-horizon branched rollouts with Proximal Policy Optimization (PPO), the proposed method achieves stable and sample-efficient learning with theoretical convergence guarantees. Simulation results show notable gains in throughput and energy efficiency over centralized and conventional decentralized baselines, demonstrating the effectiveness and scalability of the proposed approach for future MEC deployments. © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2852.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
