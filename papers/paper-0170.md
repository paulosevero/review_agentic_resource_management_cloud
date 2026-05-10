---
id: paper-0170
title: Multi-agent Reinforcement Learning for Joint Wireless and Computational Resource Allocation in Mobile Edge Computing System
authors:
- Zhang, Yawen
- Xia, Weiwei
- Yan, Feng
- Cheng, Huaqing
- Shen, Lianfeng
venue: Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
venue_type: conference
year: 2019
doi: 10.1007/978-3-030-37262-0_12
url: https://www.scopus.com/pages/publications/85078430470?origin=resultslist
publisher: Springer
pages: 149--161
keywords:
- Joint resource allocation
- Mobile edge computing
- Multi-agent reinforcement learning
- Variable learning rate
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

# paper-0170 — Multi-agent Reinforcement Learning for Joint Wireless and Computational Resource Allocation in Mobile Edge Computing System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing (MEC) is a new paradigm to provide computing capabilities at the edge of pervasive radio access networks in close proximity to intelligent terminals. In this paper, a resource allocation strategy based on the variable learning rate multi-agent reinforcement learning (VLR-MARL) algorithm is proposed in the MEC system to maximize the long term utility of all intelligent terminals while ensuring the intelligent terminals’ quality of service requirement. The novelty of this algorithm is that each agent only needs to maintain its own action value function so that the computationally expensive issue with the large action space can be avoided. Moreover, the learning rate is changed according to the expected payoff of the current strategy to speed up convergence and get the optimal solution. Simulation results show our algorithm performs better than other reinforcement learning algorithm both on the learning speed and users’ long term utilities. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2019.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0170.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
