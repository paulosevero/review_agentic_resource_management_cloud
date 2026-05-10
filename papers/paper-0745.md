---
id: paper-0745
title: 'Cache-Aided MEC for IoT: Resource Allocation Using Deep Graph Reinforcement Learning'
authors:
- Wang, Dan
- Bai, Yalu
- Huang, Gang
- Song, Bin
- Yu, F. Richard
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2023
doi: 10.1109/JIOT.2023.3244909
url: https://www.scopus.com/pages/publications/85149367181?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11486--11496
keywords:
- Computation offloading
- deep reinforcement learning
- graph convolutional network
- Internet of Things (IoT)
- multiaccess edge computing (MEC)
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

# paper-0745 — Cache-Aided MEC for IoT: Resource Allocation Using Deep Graph Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the growing demand for latency-sensitive and compute-intensive services in the Internet of Things (IoT), multiaccess edge computing (MEC)-enabled IoT is envisioned as a promising technique that allows network nodes to have computing and caching capabilities. In this article, we propose a cache-aided MEC (CA-MEC) offloading framework for joint optimization of communication, computing, and caching (3C) resources in the MEC-enabled IoT. Our goal is to optimize the offloading decision and resource allocation strategy to minimize the system latency subject to dynamic cache capacities and computing resource constraints. We first formulate this optimization problem as a multiagent decision problem, a partially observable Markov decision process (POMDP). Then, the deep graph convolution reinforcement learning (DGRL) method is applied to motivate the agents to learn optimal strategies cooperatively in a highly dynamic environment. Simulations show that our method is highly effective for computation offloading and resource allocation and performs superior results in a large-scale network. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0745.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
