---
id: paper-2295
title: Joint Caching and Computation in UAV-Assisted Vehicle Networks via Multi-Agent Deep Reinforcement Learning
authors:
- Wu, Yuhua
- Huang, Yuchao
- Wang, Ziyou
- Xu, Changming
venue: Drones
venue_type: journal
year: 2025
doi: 10.3390/drones9070456
url: https://www.scopus.com/pages/publications/105011633972?origin=resultslist
publisher: Multidisciplinary Digital Publishing Institute (MDPI)
pages: ''
keywords:
- mobile edge computing
- multi-agent deep reinforcement learning
- UAV-assisted vehicular networks
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2295 — Joint Caching and Computation in UAV-Assisted Vehicle Networks via Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Intelligent Connected Vehicles (ICVs) impose stringent requirements on real-time computational services. However, limited onboard resources and the high latency of remote cloud servers restrict traditional solutions. Unmanned Aerial Vehicle (UAV)-assisted Mobile Edge Computing (MEC), which deploys computing and storage resources at the network edge, offers a promising solution. In UAV-assisted vehicular networks, jointly optimizing content and service caching, computation offloading, and UAV trajectories to maximize system performance is a critical challenge. This requires balancing system energy consumption and resource allocation fairness while maximizing cache hit rate and minimizing task latency. To this end, we introduce system efficiency as a unified metric, aiming to maximize overall system performance through joint optimization. This metric comprehensively considers cache hit rate, task computation latency, system energy consumption, and resource allocation fairness. The problem involves discrete decisions (caching, offloading) and continuous variables (UAV trajectories), exhibiting high dynamism and non-convexity, making it challenging for traditional optimization methods. Concurrently, existing multi-agent deep reinforcement learning (MADRL) methods often encounter training instability and convergence issues in such dynamic and non-stationary environments. To address these challenges, this paper proposes a MADRL-based joint optimization approach. We precisely model the problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) and adopt the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm, which follows the Centralized Training Decentralized Execution (CTDE) paradigm. Our method aims to maximize system efficiency by achieving a judicious balance among multiple performance metrics, such as cache hit rate, task delay, energy consumption, and fairness. Simulation results demonstrate that, compared to various representative baseline methods, the proposed MAPPO algorithm exhibits significant superiority in achieving higher cumulative rewards and an approximately 82% cache hit rate. © 2025 by the authors.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2295.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
