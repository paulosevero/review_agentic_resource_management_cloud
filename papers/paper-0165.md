---
id: paper-0165
title: Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning
authors:
- Wang, Yuandou
- Liu, Hang
- Zheng, Wanbo
- Xia, Yunni
- Li, Yawen
- Chen, Peng
- Guo, Kunyin
- Xie, Hong
venue: IEEE Access
venue_type: journal
year: 2019
doi: 10.1109/ACCESS.2019.2902846
url: https://www.scopus.com/pages/publications/85064241175?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 39974--39982
keywords:
- deep-Q-network (DQN)
- infrastructure-as-a-service (IaaS) cloud
- multi-agent reinforcement learning (MARL)
- Multi-objective workflow scheduling
- quality-of-service (QoS)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0165 — Multi-objective workflow scheduling with deep-Q-network-based multi-agent reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud Computing provides an effective platform for executing large-scale and complex workflow applications with a pay-as-you-go model. Nevertheless, various challenges, especially its optimal scheduling for multiple conflicting objectives, are yet to be addressed properly. The existing multi-objective workflow scheduling approaches are still limited in many ways, e.g., encoding is restricted by prior experts' knowledge when handling a dynamic real-time problem, which strongly influences the performance of scheduling. In this paper, we apply a deep-Q-network model in a multi-agent reinforcement learning setting to guide the scheduling of multi-workflows over infrastructure-as-a-service clouds. To optimize multi-workflow completion time and user's cost, we consider a Markov game model, which takes the number of workflow applications and heterogeneous virtual machines as state input and the maximum completion time and cost as rewards. The game model is capable of seeking for correlated equilibrium between make-span and cost criteria without prior experts' knowledge and converges to the correlated equilibrium policy in a dynamic real-time environment. To validate our proposed approach, we conduct extensive case studies based on multiple well-known scientific workflow templates and Amazon EC2 cloud. The experimental results clearly suggest that our proposed approach outperforms traditional ones, e.g., non-dominated sorting genetic algorithm-II, multi-objective particle swarm optimization, and game-theoretic-based greedy algorithms, in terms of optimality of scheduling plans generated. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0165.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
