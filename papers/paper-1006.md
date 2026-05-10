---
id: paper-1006
title: A multi-agent collaboration scheme for energy-efficient task scheduling in a 3D UAV-MEC space; [三维无人机-多接入边缘计算场景下的多智能体协作任务调度能效优化方案]
authors:
- Li, Yang
- Wei, Ziling
- Su, Jinshu
- Zhao, Baokang
venue: Frontiers of Information Technology and Electronic Engineering
venue_type: journal
year: 2024
doi: 10.1631/FITEE.2300393
url: https://www.scopus.com/pages/publications/85197524934?origin=resultslist
publisher: Zhejiang University
pages: 824--838
keywords:
- Multi-access edge computing
- Multi-agent reinforcement learning
- Task scheduling
- TP301.6
- Unmanned aerial vehicles
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

# paper-1006 — A multi-agent collaboration scheme for energy-efficient task scheduling in a 3D UAV-MEC space; [三维无人机-多接入边缘计算场景下的多智能体协作任务调度能效优化方案]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing (MEC) presents computing services at the edge of networks to address the enormous processing requirements of intelligent applications. Due to the maneuverability of unmanned aerial vehicles (UAVs), they can be used as temporal aerial edge nodes for providing edge services to ground users in MEC. However, MEC environment is usually dynamic and complicated. It is a challenge for multiple UAVs to select appropriate service strategies. Besides, most of existing works study UAV-MEC with the assumption that the flight heights of UAVs are fixed; i.e., the flying is considered to occur with reference to a two-dimensional plane, which neglects the importance of the height. In this paper, with consideration of the co-channel interference, an optimization problem of energy efficiency is investigated to maximize the number of fulfilled tasks, where multiple UAVs in a three-dimensional space collaboratively fulfill the task computation of ground users. In the formulated problem, we try to obtain the optimal flight and sub-channel selection strategies for UAVs and schedule strategies for tasks. Based on the multi-agent deep deterministic policy gradient (MADDPG) algorithm, we propose a curiosity-driven and twin-networks-structured MADDPG (CTMADDPG) algorithm to solve the formulated problem. It uses the inner reward to facilitate the state exploration of agents, avoiding convergence at the sub-optimal strategy. Furthermore, we adopt the twin critic networks for update stabilization to reduce the probability of Q value overestimation. The simulation results show that CTMADDPG is outstanding in maximizing the energy efficiency of the whole system and outperforms the other benchmarks. © Zhejiang University Press 2024.

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
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1006.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
