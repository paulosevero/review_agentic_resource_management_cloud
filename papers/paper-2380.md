---
id: paper-2380
title: Multi-Agents Service Migration Strategy Under Vehicle Edge Computing
authors:
- Ye, Lei
- Chen, Yulan
- Han, Qingwen
- Zeng, Lingqiu
- Ling, Kaiwen
venue: IEEE Intelligent Vehicles Symposium, Proceedings
venue_type: conference
year: 2025
doi: 10.1109/IV64158.2025.11097660
url: https://www.scopus.com/pages/publications/105014238404?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 958--963
keywords:
- Decision making
- Information services
- Intelligent agents
- Intelligent systems
- Intelligent vehicle highway systems
- Quality of service
- Telecommunication services
- Traffic control
- Vehicles
- Edge computing
- Experience replay
- Intelligent transport
- Migration strategy
- Multi agent
- Policy optimization
- Resource-scheduling
- Service migration
- Traffic safety
- Transport systems
- Efficiency
- Multi agent systems
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
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (MAS).
    agrees_with_regex: false
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

# paper-2380 — Multi-Agents Service Migration Strategy Under Vehicle Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As Intelligent Transport Systems (ITS) advance, the Internet of Vehicles (IoV) improves traffic efficiency and safety. Vehicle Edge Computing (VEC) provides strong computing and storage capabilities. However, high vehicle speeds require efficient service migration to maintain service continuity. This study proposes a real-time service migration strategy that optimizes both Quality of Service (QoS) and response latency. To support dynamic decision-making in the VEC framework, this study introduces Priority Experience Replay and Four-Trajectory exploration (PERFT), Recurrent Neural Networks (RNNs) and attention mechanisms into the Proximal Policy Optimization (PPO) algorithm. This leads to the PERFT-PPO, which addresses issues such as long sequence handling, sparse reward problems, and problems of limited exploration depth of long trajectories in single-agent scenarios. To address multi-agents resource scheduling in VEC, this study integrates Centralized Training and Distributed Execution (CTDE) into PERFT-PPO, creating the Prioritized Experience Replay Four-Trajectory Multi-Agent Proximal Policy Optimization (PERFT-MAPPO). The simulation results show that PERFT-MAPPO addresses the challenges of real-time decision-making and resource scheduling, achieving lower system cost. Compared to PERFT-PPO, PERFT-MAPPO demonstrates superior adaptability in dynamic network conditions, further optimizing system efficiency and Qos.  © 2025 IEEE.

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
- **agrees_with_regex:** False
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
  - `{ category: rl, pattern_id: rl_mappo, matched_substring: "MAPPO" }`
  - `{ category: rl, pattern_id: rl_mappo, matched_substring: "MAPPO" }`
  - `{ category: rl, pattern_id: rl_mappo, matched_substring: "MAPPO" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "As Intelligent Transport Syste" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agents" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2380.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
