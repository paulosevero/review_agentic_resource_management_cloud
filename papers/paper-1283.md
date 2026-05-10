---
id: paper-1283
title: Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing
authors:
- Wu, Changmao
- Xu, Zhengwei
- He, Xiaoming
- Lou, Qi
- Xia, Yuanyuan
- Huang, Shuman
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2024
doi: 10.1109/TPDS.2024.3406027
url: https://www.scopus.com/pages/publications/85194843074?origin=resultslist
publisher: IEEE Computer Society
pages: 1387--1399
keywords:
- 6G
- deep reinforcement learning
- distributed edge computing
- multi-agent learning architecture
- proactive caching
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

# paper-1283 — Proactive Caching With Distributed Deep Reinforcement Learning in 6G Cloud-Edge Collaboration Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Proactive caching in 6G cloud-edge collaboration scenarios, intelligently and periodically updating the cached contents, can either alleviate the traffic congestion of backhaul link and edge cooperative link or bring multimedia services to mobile users. To further improve the network performance of 6G cloud-edge, we consider the issue of multi-objective joint optimization, i.e., maximizing edge hit ratio while minimizing content access latency and traffic cost. To solve this complex problem, we focus on the distributed deep reinforcement learning (DRL)-based method for proactive caching, including content prediction and content decision-making. Specifically, since the prior information of user requests is seldom available practically in the current time period, a novel method named temporal convolution sequence network (TCSN) based on the temporal convolution network (TCN) and attention model is used to improve the accuracy of content prediction. Furthermore, according to the value of content prediction, the distributional deep Q network (DDQN) seeks to build a distribution model on returns to optimize the policy of content decision-making. The generative adversarial network (GAN) is adapted in a distributed fashion, emphasizing learning the data distribution and generating compelling data across multiple nodes. In addition, the prioritized experience replay (PER) is helpful to learn from the most effective sample. So we propose a multivariate fusion algorithm called PG-DDQN. Finally, faced with such a complex scenario, a distributed learning architecture, i.e., multi-agent learning architecture is efficiently used to learn DRL-based methods in a manner of centralized training and distributed inference. The experiments prove that our proposal achieves satisfactory performance in terms of edge hit ratio, traffic cost and content access latency. © 2024 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1283.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
