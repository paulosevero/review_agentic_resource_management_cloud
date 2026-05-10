---
id: paper-0251
title: Distributed reinforcement learning for NOMA-enabled mobile edge computing
authors:
- Yang, Zhong
- Liu, Yuanwei
- Chen, Yue
venue: 2020 IEEE International Conference on Communications Workshops, ICC Workshops 2020 - Proceedings
venue_type: conference
year: 2020
doi: 10.1109/ICCWorkshops49005.2020.9145457
url: https://www.scopus.com/pages/publications/85090280958?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Edge computing
- Energy utilization
- Green computing
- Multi agent systems
- Reinforcement learning
- Resource allocation
- Software agents
- Computation resource allocations
- Conventional reinforcement learning
- Distributed reinforcement learning
- Extensive simulations
- Historical experience
- Multi-agent Q-learning
- Resource allocation problem
- Resource allocation strategies
- Learning algorithms
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-0251 — Distributed reinforcement learning for NOMA-enabled mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A novel non-orthogonal multiple access (NOMA) enabled cache-aided mobile edge computing (MEC) framework is proposed, for minimizing the sum energy consumption. The NOMA strategy enables mobile users to offload computation tasks to the access point (AP) simultaneously, which improves the spectrum efficiency. In this article, the considered resource allocation problem is formulated as a long-term reward maximization problem that involves a joint optimization of task offloading decision, computation resource allocation, and caching decision. To tackle this nontrivial problem, a single-agent Q-learning (SAQ-learning) algorithm is invoked to learn a long-term resource allocation strategy from historical experience. Moreover, a Bayesian learning automata (BLA) based multi-agent Q-learning (MAQ-learning) algorithm is proposed for task offloading decisions. More specifically, a BLA based action select scheme is proposed for the agents in MAQ-learning to select the optimal actions in every state. The proposed BLA based action selection scheme is instantaneously self-correcting, consequently, if the probabilities of two computing models (i.e., local computing and offloading computing) are not equal, the optimal action unveils eventually. Extensive simulations demonstrate that: 1) The proposed cache-aided NOMA MEC framework significantly outperforms the other representative benchmark schemes under various network setups. 2) The effectiveness of the proposed BAL-MAQ-learning algorithm is confirmed from the comparison with the results of conventional reinforcement learning algorithms. © 2020 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0251.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
