---
id: paper-2414
title: A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks
authors:
- Zhang, Yiwei
- Li, Yaping
- Lee, Yong
- Yan, Qing
- Yang, Yang
venue: 2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025
venue_type: conference
year: 2025
doi: 10.1109/WCSP68525.2025.1010647
url: https://www.scopus.com/pages/publications/105033702220?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- deep deterministic policy gradient
- Drone-enabled edge computing systems
- energy consumption
- latency
- prioritized experience replay
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2414 — A Deep Reinforcement Learning Framework for the Latency-Energy Trade-Off in Drone-Enabled Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With their mobility and flexibility, drones can serve as edge computing nodes to effectively enlarge the traditional mobile edge computing (MEC) coverage. However, the requirements of high energy efficiency and low latency seriously constrain the performance of drone-enabled MEC systems. In this paper, we investigate a deep reinforcement learning (DRL) scheme for minimizing the latency and energy consumption in drone-enabled MEC systems, where the computational tasks can be intelligently offloaded in two tiers between ground users (GUs), drones, and base stations (BSs), respectively. Specifically, a multi-agent (MA) deep deterministic policy gradient (DDPG) is employed to jointly allocate the power and reduce the offloading latency. Due to the randomness of tasks' arrival, the computational cost is formulated as a non-convex optimization problem of both latency and energy consumption cost, which satisfies the power constraints and maximum computation capacity. Further, a heterogeneous MA prioritized experience replay (PER) DDPGbased power allocation (HMP-DPA) algorithm is proposed, which operates by decentralized training and decentralized execution (DTDE) to avoid exponential growth of action space. Especially, PER can accelerate the algorithm convergence and the reward is designed to enhance the DRL training stability. Simulation results demonstrate that the proposed HMP-DPA can effectively explore an optimal task offloading strategy to minimize the latency and energy consumption in different tiers, and significantly outperform other baselines with an average computation cost reduction of 17.35%, 18.94%, and 28.17 % under different weights. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2414.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
