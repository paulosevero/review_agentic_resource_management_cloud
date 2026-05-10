---
id: paper-1029
title: Load Balancing for Task Scheduling Based on Multi-Agent Reinforcement Learning in Cloud-Edge-End Collaborative Environments
authors:
- Li, Zhuo
- Yu, Jie
- Liu, Xiaodong
- Peng, Long
venue: ACM International Conference Proceeding Series
venue_type: conference
year: 2024
doi: 10.1145/3647750.3647765
url: https://www.scopus.com/pages/publications/85191454064?origin=resultslist
publisher: Association for Computing Machinery
pages: 94--100
keywords:
- Cloud-Edge-End collaborative
- Collaborative task scheduling
- Multi-Agent reinforcement learning
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

# paper-1029 — Load Balancing for Task Scheduling Based on Multi-Agent Reinforcement Learning in Cloud-Edge-End Collaborative Environments

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the increasing variety of computational scenarios and task types in cloud-edge-end collaborative networks, task scheduling in cloud-edge-end collaborative environments can better adapt to various task types and application scenarios, thereby enhancing the flexibility and adaptability of cloud-edge-end systems. This paper introduces a multi-agent reinforcement learning approach to conduct research on task load balancing scheduling in the context of cloud-edge-end collaboration, aiming to improve the efficiency of finding optimal task scheduling strategies in a distributed cloud-edge computing environment. In this paper, task scheduling is viewed as a competitive multi-agent system, where intelligent agents compete for a sufficient number of computing resources through the design of efficient task scheduling algorithms. This competition allows agents to reduce task completion latency and energy consumption while meeting task computational requirements. The paper employs Decentralized Partially Observable Markov Decision Process to model the reward maximization problem and designs a multi-agent reinforcement learning algorithm based on attention communication to solve it. Finally, experimental validation is conducted to evaluate the performance of the proposed task scheduling method. © 2024 ACM.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1029.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
