---
id: paper-1677
title: Multiagent Deep Reinforcement Learning for Decentralized Multi-AAV Mobile Edge Computing Networks
authors:
- Hwang, Sangwon
- Lee, Hoon
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3527016
url: https://www.scopus.com/pages/publications/85214520237?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 14484--14497
keywords:
- Mobile edge computing (MEC)
- multiagent deep reinforcement learning (MADRL)
- unmanned aerial vehicle (UAV)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1677 — Multiagent Deep Reinforcement Learning for Decentralized Multi-AAV Mobile Edge Computing Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This article studies a new multiagent deep reinforcement learning (MADRL) approach for unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) networks, where UAV-mounted servers provide offloading services to mobile users (MUs). We aim to minimize the total energy consumption of MUs by optimizing UAV mobility, UAV-MU association, resource allocation, and task offloading ratios. In the multi-UAV scenario, we model the MEC network as a multiagent partially observable Markov decision process (POMDP), where each UAV agent operates with limited information for decentralized decision-making. Conventional MADRL methods manually design such UAV interaction messages, thereby incurring performance degradation. To address this issue, we propose a new neural network (NN)-based UAV interaction mechanism that generates autonomously task-oriented messages to minimize energy consumption. Such message-generating NNs are developed under the MADRL framework, which allows for joint optimization of UAV interactions and decentralized decisions in an end-to-end manner. Numerical results demonstrate that our approach outperforms traditional MADRL methods and achieves performance close to ideal centralized schemes while maintaining scalability with varying UAV numbers. © 2014 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1677.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
