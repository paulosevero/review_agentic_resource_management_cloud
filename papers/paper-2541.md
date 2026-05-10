---
id: paper-2541
title: Task Offloading and Resource Optimization Based on Dependency-Aware Graph and Collaborative Deep Reinforcement Learning in Mobile Edge Computing
authors:
- Chen, Xiangyi
- Bi, Yuanguo
- Zhang, Juan
- Yuan, Xiaoming
- Niyato, Dusit
- Zhao, Liang
- Wang, Xingwei
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2026
doi: 10.1109/TMC.2026.3665729
url: https://www.scopus.com/pages/publications/105030719682?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- dependency-aware task offloading
- graph neural networks
- Mobile edge computing
- multi-agent deep reinforcement learning
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
    proposed_decision: Include
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
    agrees_with_regex: false
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

# paper-2541 — Task Offloading and Resource Optimization Based on Dependency-Aware Graph and Collaborative Deep Reinforcement Learning in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In mobile edge computing (MEC), computation offloading serves as an effective solution to bridge the gap between the stringent latency requirements of computational tasks and the limited processing capabilities of terminal devices (TDs). However, complex inter-task dependencies, dynamic network conditions, and the decentralized architecture of MEC systems pose significant challenges to efficient and adaptive task offloading. To address these challenges, this paper investigates dependency-aware task offloading and resource optimization in MEC environments. First, we propose a task feature extraction method based on dependency-aware graph neural networks (FEDG), which captures the hierarchical structure and varying importance of subtask dependencies by adaptively learning the aggregation weights of predecessor nodes and edges. Then, to address the joint dependency-aware task offloading and resource allocation problem under partial observability in MEC networks, we design a Dependency-aware Graph-based Multi-Agent deep reinforcement learning (DGMA) algorithm. DGMA integrates adaptive prioritized experience replay and correlation-based selective parameter sharing to improve learning efficiency and accelerate convergence in multi-agent environments. Extensive simulations demonstrate that DGMA achieves superior performance in terms of delay, energy consumption, offloading utility, and deadline violation rate. © 2002-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2541.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
