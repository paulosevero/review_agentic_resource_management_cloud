---
id: paper-2461
title: MADRL-Based Collaborative Computation Offloading and Resource Orchestration for Multitask Data Sharing in Smart Agriculture
authors:
- Zhao, Tantan
- Zhang, Miao
- He, Lijun
- Li, Fan
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2024.3481236
url: https://www.scopus.com/pages/publications/85210292291?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3887--3904
keywords:
- Computation offloading
- mobile edge computing (MEC)
- multiagent deep reinforcement learning (MADRL)
- multitask data sharing
- smart agriculture
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

# paper-2461 — MADRL-Based Collaborative Computation Offloading and Resource Orchestration for Multitask Data Sharing in Smart Agriculture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multiple different computation tasks may be simultaneously offloaded to mobile edge computing (MEC) servers in smart agriculture scenarios, where the redundant transmission of shared data among different tasks leads to insufficient utilization of system resources (i.e., computing resources, communication resources, and caching resources) and lagging processing efficiency. Existing schemes optimizing multitask computation offloading with shared data almost focus on identical tasks, which are difficult to apply in real-world scenarios with different tasks to meet various service demands of fairness, low latency, and low energy consumption. In this article, we propose a fair, real-time, and green collaborative optimization scheme of computation offloading and resource orchestration for multitask data sharing in smart agriculture based on multiagent deep reinforcement learning (MADRL), aiming to improve offloading efficiency and system resource utilization to meet diverse tasks’ service demands. First, a collaborative optimization problem of computation offloading and resource orchestration is formulated to minimize the system latency, energy consumption, and caching space occupancy under constraints of redundant data transmission and limited system resources. It is difficult for traditional optimization methods to solve the formulated optimization problem characterized by dynamics, high-dimensionality, nonlinearity, and mixed-integer. Then, we propose an MADRL algorithm named MATD3-CO-RO-MDS based on a hierarchical reward mechanism to solve it and approximate the optimal offloading and orchestration strategy. Finally, experimental results prove that our proposed algorithm achieves smaller latency, energy consumption, and caching space occupancy compared with existing algorithms. It even has a 76.7% advantage in reducing latency when more tasks participate in offloading. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2461.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
