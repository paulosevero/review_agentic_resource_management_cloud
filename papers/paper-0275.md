---
id: paper-0275
title: Research on Resource Allocation and Offloading Decision Based on Multi-agent Architecture in Cloud-fog Hybrid Network; [云雾混合网络下基于多智能体架构的资源分配及卸载决策研究]
authors:
- Chen, Qianbin
- Tan, Qi
- He, Lanqin
- Tang, Lun
venue: Dianzi Yu Xinxi Xuebao/Journal of Electronics and Information Technology
venue_type: journal
year: 2021
doi: 10.11999/JEIT200256
url: https://www.scopus.com/pages/publications/85115171324?origin=resultslist
publisher: Science Press
pages: 2654--2662
keywords:
- Cloud-fog hybrid network
- Computation offloading
- D2D
- Multi-agent
- Resource allocation
language: Chinese
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: include
  05-abstract-screening: exclude
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
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: RL
    winning_category: rl
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-0275 — Research on Resource Allocation and Offloading Decision Based on Multi-agent Architecture in Cloud-fog Hybrid Network; [云雾混合网络下基于多智能体架构的资源分配及卸载决策研究]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To optimize strategy of resource allocation and task offloading decision on D2D-assisted cloud-fog architecture, a joint resource allocation and offloading decision algorithm based on a multi-agent architecture deep reinforcement learning method is proposed. Firstly, considering incentive constraints, energy constraints, and network resource constraints, the algorithm jointly optimizes wireless resource allocation, computing resource allocation, and offloading decisions. Further, the algorithm establishes a stochastic optimization model that maximizes the total user Quality of Experience (QoE) of the system, and transfers it into an MDP problem. Secondly, the algorithm factorizes the original MDP problem and models a Markov game. Then, a centralized training and distributed execution mechanism based on the Actor-Critic (AC) algorithm is proposed. In the centralized training process, multi-agents obtains the global information through cooperation to optimize the resource allocation and task offloading decision strategies. After the training process, each agent performs independently resource allocation and task offloading based on the current system state and strategy. Finally, the simulation results demonstrate that the algorithm can effectively improve user QoE, and reduce delay and energy consumption. © 2021, Science Press. All right reserved.

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
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "RL"
- **winning_category:** 'rl'
- **overrides_applied:** []
- **evidence_trail:**
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "To optimize strategy of resour" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agents" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agent" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0275.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
