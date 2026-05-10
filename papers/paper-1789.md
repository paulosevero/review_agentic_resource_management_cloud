---
id: paper-1789
title: DRL-Based Joint Task Offloading and Resource Allocation in Air-Ground Integrated Vehicular Edge Computing Network With Energy Harvesting
authors:
- Li, Shichao
- Huang, Qiurong
- Chen, Hongbin
- Jiang, Ruihong
- Dong, Mianxiong
- Ota, Kaoru
- Quek, Tony Q.S.
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2025
doi: 10.1109/TVT.2025.3621730
url: https://www.scopus.com/pages/publications/105019624308?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- air-ground integrated vehicular edge computing (AGI-VEC) network
- energy harvesting
- hybrid dual-clip multi-agent proximal policy optimization (DC-MAPPO)
- task offloading
- unmanned aerial vehicles (UAV)
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

# paper-1789 — DRL-Based Joint Task Offloading and Resource Allocation in Air-Ground Integrated Vehicular Edge Computing Network With Energy Harvesting

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In comparison to traditional vehicular edge computing (VEC) architectures, the air-ground integrated vehicular edge computing (AGI-VEC) network, which combines unmanned aerial vehicles (UAV) and high-altitude platforms (HAP), offers significant advantages. These include seamless coverage, long-distance transmission, reduced latency, enhanced throughput, and alleviation of network congestion, all of which contribute to a more efficient service experience for the Internet of vehicles. To minimize the task offloading delay, this paper investigates a joint multi-computation equipment selection, resource allocation, and UAV trajectory design problem based on energy harvesting in the AGI-VEC network. In order to solve this problem, we first reformulate the problem into a Markov decision process (MDP). And then, we propose a hybrid dual-clip multi-agent proximal policy optimization (DC-MAPPO) algorithm based on the multi-agent proximal policy optimization (MAPPO) algorithm, which introduces the idea of dual-clip (DC), and the adaptive discount factor to enhance the stability and convergence speed of the algorithm. Simulation results demonstrate that the proposed algorithm outperforms other baseline algorithms in reducing task offloading delay. © 1967-2012 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1789.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
