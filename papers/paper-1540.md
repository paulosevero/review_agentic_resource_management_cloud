---
id: paper-1540
title: An Attention-Driven Heterogeneous Multiagent Framework for UAV and Satellite-Assisted Task Offloading in Hybrid Ground Device Networks
authors:
- Du, Tianjiao
- Gui, Xiaolin
- Dai, Huijun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3621490
url: https://www.scopus.com/pages/publications/105019551448?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 54672--54689
keywords:
- Efficient task offloading
- mobile edge computing (MEC)
- multiagent deep reinforcement learning (DRL)
- unmanned aerial vehicle (UAV)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1540 — An Attention-Driven Heterogeneous Multiagent Framework for UAV and Satellite-Assisted Task Offloading in Hybrid Ground Device Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article proposes an integrated satellite-unmanned aerial vehicle (UAV)-terrestrial collaborative computing framework that incorporates a low Earth orbit (LEO) satellite, UAVs equipped with mobile edge computing (MEC) servers, ground infrastructures, and terrestrial users. A novel three-tier hybrid task decomposition and computation architecture is designed to support efficient task offloading in dynamic and heterogeneous environments. By exploiting the complementary advantages of the LEO satellite and UAVs in communication coverage and deployment flexibility, and by utilizing remote high-performance servers, the system ensures improved quality of service (QoS), enhanced coverage, scalability, and robustness. To address the heterogeneity in computation demand, latency sensitivity, and mobility patterns of ground devices, the cross-regional task offloading and decomposition problem is formulated as a decentralized partially observable Markov decision process (Dec-POMDP), enabling efficient collaborative decision-making among agents with overlapping observations. Furthermore, under the centralized training with decentralized execution (CTDE) paradigm, we propose a hierarchical scheduling algorithm based on heterogeneous multiagent deep reinforcement learning (DRL), allowing LEO satellite and UAVs to jointly learn optimal strategies during training while autonomously executing decisions in real time. To address the challenges posed by high-dimensional state spaces, we introduce an attention-driven UAV and satellite-assisted task offloading (ADUS) algorithm. A multihead attention mechanism is incorporated into the critic networks, allowing agents to focus on critical features and avoid reliance on full joint state-action representations. Experimental results demonstrate that the proposed algorithm significantly outperforms other baseline methods, including ADUS-NAT, ADUS-NPP, MADDPG, DDPG, and MATORA, achieving improvements of 5.45%, 12.04%, 19.61%, 33.25%, and 42.35%, respectively.  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "This article proposes an integ" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multiagent" }`
  - `{ category: classical_agents, pattern_id: cls_agent_term, matched_substring: "agents" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1540.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
