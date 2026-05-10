---
id: paper-0509
title: 'Reliability Optimization for Channel Resource Allocation in Multihop Wireless Network: A Multigranularity Deep Reinforcement Learning Approach'
authors:
- Wang, Ying
- Shang, Fengjun
- Lei, Jianjun
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2022
doi: 10.1109/JIOT.2022.3170875
url: https://www.scopus.com/pages/publications/85129662890?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 19971--19987
keywords:
- Deep reinforcement learning (DRL)
- joint resource allocation
- mobile-edge computing (MEC)
- wireless resource allocations
- wireless sensor networks (WSNs)
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)
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

# paper-0509 — Reliability Optimization for Channel Resource Allocation in Multihop Wireless Network: A Multigranularity Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article investigates the high-reliable data transmission for multihop and multichannel wireless sensor networks (WSNs), which jointly optimizes the channel allocation and channel access mechanisms. We propose a novel wireless paradigm empowered by mobile-edge computing (MEC) and deep reinforcement learning (DRL) to improve the data process ability of WSNs and formulate the joint resource allocation problem for reliability maximization as a partially observable Markov decision process (POMDP). Meanwhile, we introduce the distributed decision-making (DDM) framework to decouple channel optimization into two subproblems: 1) channel allocation and 2) channel access. Correspondingly, we present an asynchronous channel allocation algorithm for multiagent scenario and enable the neighbor cooperation to tackle the nonstationary problem, which can significantly improve the network convergence speed. Besides, we present a collision-free channel access algorithm including three submodules that can simultaneously eliminate vanishing nodes, hidden terminal, and exposed terminal problems in large-scale WSNs. Simulation results demonstrate that the proposed algorithm significantly improves network performance in terms of convergence, throughput, collision, and packet delivery ratio (PDR).  © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0509.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
