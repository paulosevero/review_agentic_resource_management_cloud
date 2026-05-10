---
id: paper-1478
title: 'Multi-Agent Coordinated Optimization for Enhanced Task Offloading in mmWave RIS-MEC System: Balancing Power and Rate'
authors:
- Chen, Yanran
- Xu, Peng
- Zhao, Wenting
venue: 2025 7th International Conference on Frontier Technologies of Information and Computer, ICFTIC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICFTIC68075.2025.11324559
url: https://www.scopus.com/pages/publications/105035252735?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 931--936
keywords:
- mobile edge computing (MEC)
- multi agent deep deterministic policy gradient (MADDPG)
- phase-shift
- power allocation
- reconfigurable intelligent surface (RIS)
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

# paper-1478 — Multi-Agent Coordinated Optimization for Enhanced Task Offloading in mmWave RIS-MEC System: Balancing Power and Rate

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This paper proposes an enhanced millimeter-wave (mmWave) mobile edge computing (MEC) architecture based on a Reconfigurable Intelligent Surface (RIS), which employs the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm to achieve balanced optimization between the Weighted Sum Rate (WSR) for task offloading and the total power consumption of user equipment (UEs). To address the challenge of jointly optimizing RIS phase-shift and multi-user power allocation in mmWave channels, a MADDPG-based approach is introduced: firstly, a RIS agent is constructed to optimize RIS phase-shift for maximizing the WSR of task offloading; secondly, multiple UE agents are designed to optimize their transmission and computation power for minimizing the total power consumption; finally, under the Centralized Training with Decentralized Execution (CTDE) framework, a balanced optimization between the offloading rate and power consumption is achieved. Simulation results demonstrate that the proposed algorithm outperforms baseline methods, including centralized DDPG, TD3, and sequential optimization, in terms of both WSR and power consumption, exhibiting superior adaptability and balanced performance under strict power constraints and rate requirements. © 2025 IEEE.

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
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "This paper proposes an enhance" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "Multi-Agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1478.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
