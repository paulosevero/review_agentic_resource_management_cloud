---
id: paper-1795
title: 'Energy-Efficient UAV-Driven Multi-Access Edge Computing: A Distributed Many-Agent Perspective'
authors:
- Li, Yuanjian
- Madhukumar, A.S.
- Zheng Hui Ernest, Tan
- Zheng, Gan
- Saad, Walid
- Aghvami, Hamid
venue: IEEE Transactions on Communications
venue_type: journal
year: 2025
doi: 10.1109/TCOMM.2025.3552746
url: https://www.scopus.com/pages/publications/105000871413?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 8405--8420
keywords:
- energy efficiency maximization
- Multi-access edge computing (MEC)
- multi-agent deep reinforcement learning (MADRL)
- path planning
- uncrewed aerial vehicle (UAV)
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
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent).
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

# paper-1795 — Energy-Efficient UAV-Driven Multi-Access Edge Computing: A Distributed Many-Agent Perspective

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this paper, the problem of energy-efficient uncrewed aerial vehicle (UAV)-assisted multi-access task offloading is investigated. In the studied system, several UAVs are deployed as edge servers to cooperatively aid task executions for several energy-limited computation-scarce terrestrial user equipments (UEs). An expected energy efficiency maximization problem is then formulated to jointly optimize UAV trajectories, UE local central processing unit (CPU) clock speeds, UAV-UE associations, time slot slicing, and UE offloading powers. This optimization is subject to practical constraints, including UAV mobility, local computing capabilities, mixed-integer UAV-UE pairing indicators, time slot division, UE transmit power, UAV computational capacities, and information causality. To tackle the multi-dimensional optimization problem under consideration, the duo-staggered perturbed actor-critic with modular networks (DSPAC-MN) solution in a multi-agent deep reinforcement learning (MADRL) setup, is proposed and tailored, after mapping the original problem into a stochastic (Markov) game. Time complexity and communication overhead are analyzed, while convergence performance is discussed. Compared to representative benchmarks, e.g., multi-agent deep deterministic policy gradient (MADDPG) and multi-agent twin-delayed DDPG (MATD3), the proposed DSPAC-MN is validated to be able to achieve the optimal performance of average energy efficiency, while ensuring 100% safe flights. © 1972-2012 IEEE.

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
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent)."
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
  - `{ category: rl, pattern_id: rl_madrl, matched_substring: "MADRL" }`
  - `{ category: rl, pattern_id: rl_maddpg, matched_substring: "MADDPG" }`
  - `{ category: rl, pattern_id: rl_matd3, matched_substring: "MATD3" }`
  - `{ category: rl, pattern_id: rl_ma_rl_combo, matched_substring: "In this paper" }`
  - `{ category: classical_agents, pattern_id: cls_mas_term, matched_substring: "multi-agent" }`
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1795.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
