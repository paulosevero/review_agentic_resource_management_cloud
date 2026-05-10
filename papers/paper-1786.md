---
id: paper-1786
title: 'Collaborative Task Offloading and Resource Allocation in Small-Cell MEC: A Multi-Agent PPO-Based Scheme'
authors:
- Li, Han
- Xiong, Ke
- Lu, Yuping
- Chen, Wei
- Fan, Pingyi
- Letaief, Khaled Ben
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2024.3496536
url: https://www.scopus.com/pages/publications/85209751688?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 2346--2359
keywords:
- Mobile edge computing
- multi-agent deep reinforcement learning
- resource allocation
- small-cell networks
- task offloading
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

# paper-1786 — Collaborative Task Offloading and Resource Allocation in Small-Cell MEC: A Multi-Agent PPO-Based Scheme

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Small-cell mobile edge computing (SE-MEC) networks amalgamate the virtues of MEC and small-cell networks, enhancing data processing capabilities of user devices (UDs). Nevertheless, time-varying wireless channels, dynamic UD requirements, and severe interference among UDs make it difficult to fully exploit the limited network resources and stably provide computing services for UDs. Therefore, efficient task offloading and resource allocation (TORA) is essential. Moreover, since multiple small cells are deployed, decentralized TORA schemes are preferred in practice. Thus, this paper aims to design distributed adaptive TORA schemes for SE-MEC networks. In pursuit of an eco-friendly design, an optimization problem is formulated to minimize the total energy consumption (TEC) of UDs subject to delay constraints. To effectively deal with network's dynamic characteristics, the reinforce learning framework is applied, where the TEC minimization problem is first modeled as a partially observable Markov decision process (POMDP), and then an efficient multi-agent proximal policy optimization (MAPPO)-based scheme is presented to solve it. In the presented scheme, each small-cell base station (SBS) serves as an agent and is capable of making TORA decisions only with its own local information. To promote collaboration among multiple agents, a global reward function is designed. A state normalization mechanism is also introduced into the presented scheme for enhancing learning performance. Simulation results show that although the proposed MAPPO-based scheme works in a distributed manner, it achieves very similar performance to the centralized one. In addition, it is demonstrated that the state normalization mechanism has a significant effect on reducing TEC.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1786.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
