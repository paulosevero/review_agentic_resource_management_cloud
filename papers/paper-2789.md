---
id: paper-2789
title: Multiagent Deep Reinforcement Learning for Device-Enhanced Distributed Task Scheduling in Terminal-Edge Collaborative Computing Networks
authors:
- Sun, Yukun
- Yu, Wenhan
- Zhou, Xinyu
- Zhao, Jun
- Zhang, Xing
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2026
doi: 10.1109/JIOT.2025.3646683
url: https://www.scopus.com/pages/publications/105026480951?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 11619--11635
keywords:
- Computing offloading
- device-enhanced mobile edge computing (MEC)
- distributed task scheduling
- game theory
- multiagent deep reinforcement learning (DRL)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2789 — Multiagent Deep Reinforcement Learning for Device-Enhanced Distributed Task Scheduling in Terminal-Edge Collaborative Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Device-enhanced mobile edge computing (MEC) is an emerging technology designed to handle intensive and delaysensitive tasks through device-to-device (D2D) communication. In this article, we present a terminal-edge collaborative computing network to investigate device-enhanced distributed tasks scheduling (DDTS) with specific application deployment. Our optimization focuses on offloading choices, bandwidths, and computing frequencies, aiming to minimize execution costs, including processing delay and energy consumption. We decouple the joint multiple goals optimization problem into several subproblems, which are solved by mathematical optimization methods, except for the NP-hard offloading choices subproblem. This NP-hard problem is modeled as a multitask scheduling game (MTSG), which we demonstrate to be a potential game with at least one Nash equilibrium (NE) solution. However, considering further the dynamic nature of real-world application deployment and the complexity of large-scale games, the problem evolves into a stochastic game with a Markov policy (SGMP). Thus, we propose a multiagent DDTS algorithm based on a dueling double deep Q-network (D3QN) to approximate an optimal solution. Extensive experiments confirm the feasibility and efficiency of our approach.  © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2789.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
