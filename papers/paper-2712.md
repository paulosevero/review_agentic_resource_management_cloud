---
id: paper-2712
title: 'RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design'
authors:
- Manjunath, T.C.
- Sreerama, M.P.
- Shrivatsa, K.S.
- Khanam, Tanzila
- Modi, Nandini
- Balakrishna, R.
venue: 7th International Conference on Mobile Computing and Sustainable Informatics, ICMCSI 2026
venue_type: conference
year: 2026
doi: 10.1109/ICMCSI67283.2026.11412692
url: https://www.scopus.com/pages/publications/105034864460?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 885--891
keywords:
- Adaptive Systems
- Deep Reinforcement Learning
- Kernel Scheduling
- Lock-Free Algorithms
- Memory Allocation
- NUMA
- Operating Systems
- Q-Learning
- Rust
- VRRP
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

# paper-2712 — RATM: Reinforcement Learning for Co-Optimized CPU Scheduling and NUMA Memory Management in Compiler Design

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The current OS uses the stationary heuristic methods & are set-up systematically while designing the system for handling of the CPU schedules & allocating of memories. These heuristics fundamentally fail under the different dynamically shifting workloads characteristic of current data centres, where batch processing, real-time analytics, and interactive applications coexist. This paper introduces RATM (Resource-Aware Adaptive Task Manager), an innovative'Authoritative Controller'architecture developed in Rust that substitutes static policies with a Deep Q-Network (DQN) reinforcement learning agent capable of optimising kernel behaviour during runtime. Our system has a rigorous Policy-Mechanism Separation. The model-free DQN agent watches the system state all the time and chooses actions. The VRRP (Varying Response Ratio Priority) Scheduler and NAAT (NUMA-Aware Adaptive Tiered) Allocator, on the other hand, are passive, configurable mechanisms that carry out commands. The RATM controller acts as a middleman between these layers, making sure that safety rules are followed and turning abstract actions into real API calls. The experimental results show that our RL-driven kernel cuts the average wait time in calibration scenarios by more than 70% compared to the static baseline, while still being very fair. The RL agent learns to proactively activate NUMA page migrations during workload phase changes, which 'flattens the curve' of latency spikes that are common in traditional schedulers. Results shows the power of methodology presented here. © 2026 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2712.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
