---
id: paper-0805
title: Distributed Deep Multi-Agent Reinforcement Learning for Cooperative Edge Caching in Internet-of-Vehicles
authors:
- Zhou, Huan
- Jiang, Kai
- He, Shibo
- Min, Geyong
- Wu, Jie
venue: IEEE Transactions on Wireless Communications
venue_type: journal
year: 2023
doi: 10.1109/TWC.2023.3272348
url: https://www.scopus.com/pages/publications/85162891664?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9595--9609
keywords:
- cache replacement
- content delivery
- Edge caching
- Internet-of-Vehicles
- multi-agent reinforcement learning
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

# paper-0805 — Distributed Deep Multi-Agent Reinforcement Learning for Cooperative Edge Caching in Internet-of-Vehicles

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Edge caching is a promising approach to reduce duplicate content transmission in Internet-of-Vehicles (IoVs). Several Reinforcement Learning (RL) based edge caching methods have been proposed to improve the resource utilization and reduce the backhaul traffic load. However, they only obtain the local sub-optimal solution, as they neglect the influence from environments by other agents. This paper investigates the edge caching strategies with consideration of the content delivery and cache replacement by exploiting the distributed Multi-Agent Reinforcement Learning (MARL). A hierarchical edge caching architecture for IoVs is proposed and the corresponding problem is formulated with the goal to minimize the long-term content access cost in the system. Then, we extend the Markov Decision Process (MDP) in the single agent RL to the context of a multi-agent system, and tackle the corresponding combinatorial multi-armed bandit problem based on the framework of a stochastic game. Specifically, we firstly propose a Distributed MARL-based Edge caching method (DMRE), where each agent can adaptively learn its best behaviour in conjunction with other agents for intelligent caching. Meanwhile, we attempt to reduce the computation complexity of DMRE by parameter approximation, which legitimately simplifies the training targets. However, DMRE is enabled to represent and update the parameter by creating a lookup table, essentially a tabular-based method, which generally performs inefficiently in large-scale scenarios. To circumvent the issue and make more expressive parametric models, we incorporate the technical advantage of the Deep- Q Network into DMRE, and further develop a computationally efficient method (DeepDMRE) with neural network-based Nash equilibria approximation. Extensive simulations are conducted to verify the effectiveness of the proposed methods. Especially, DeepDMRE outperforms DMRE, Q -learning, LFU, and LRU, and the edge hit rate is improved by roughly 5%, 19%, 40%, and 35%, respectively, when the cache capacity reaches 1, 000 MB.  © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0805.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
