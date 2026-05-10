---
id: paper-2080
title: 'Green Multi-Agent Collaborative Networking with Integrated Sensing, Communication, and Computing: A Reinforcement Learning Approach'
authors:
- Ren, Yuzheng
- Nie, Junfeng
- Fan, Liuqi
- Cao, Xueyan
- Sun, Chunlei
venue: Proceeding of 2025 IEEE 4th International Conference on Computing, Communication, Perception and Quantum Technology, CCPQT 2025
venue_type: conference
year: 2025
doi: 10.1109/CCPQT66408.2025.11383452
url: https://www.scopus.com/pages/publications/105034872457?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- and Computing
- Communication
- Deep Reinforcement Learning
- Integrated Sensing
- Mobile Edge Computing
- Proximal Policy Optimization
- Resource Allocation
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

# paper-2080 — Green Multi-Agent Collaborative Networking with Integrated Sensing, Communication, and Computing: A Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The convergence of the internet of things and artificial intelligence is pushing networked systems toward collaborative operation, in which sensing, communication, and computing must be coordinated under dynamic conditions. Edge and mobile devices face tight energy budgets as well as nonstationary wireless rates and computing capacity, calling for energy-aware designs that ensure feasibility in each time slot and low latency. We study cooperative offloading and execution in unmanned aerial vehicle (UAV) swarms with mobile edge computing (MEC). Our approach captures the coupling among queueing, latency, and energy, supports cooperation within the same time slot, treats wireless resources as exogenous outcomes of lower layer scheduling, enforces a total mobile edge computing budget, and employs fixed cooperative routing. We formulate the problem as a centralized Markov decision process (MDP) in which a single centralized policy outputs a tripartite allocation for each UAV across local processing, device-to-device (D2D) cooperation, and MEC offloading. A lightweight feasibility allocator maps proposed service amounts to executable quantities in each time slot by allocating edge computing capacity and trimming requests according to realized link rates, computing limits, and power limits. A policy trained with proximal policy optimization (PPO) yields stable learning and scalable online inference. Simulations with stochastic arrivals and fast-varying dynamics show consistently lower end-to-end delay and total energy consumption compared to random and equal split baselines, with modest runtime overhead. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2080.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
