---
id: paper-0343
title: Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets
authors:
- Shi, Bing
- Song, Zhaoxiang
- Xu, Jianqiao
venue: Journal of Sensors
venue_type: journal
year: 2021
doi: 10.1155/2021/9651117
url: https://www.scopus.com/pages/publications/85122858739?origin=resultslist
publisher: Hindawi Limited
pages: ''
keywords:
- Commerce
- Computation theory
- Costs
- Decision making
- Edge computing
- Electronic trading
- Financial markets
- Game theory
- Internet of things
- Learning algorithms
- Mean field theory
- Multi agent systems
- Reinforcement learning
- Resource allocation
- Sensor networks
- Auction markets
- Double auction
- Edge server
- Fictitious play
- Market pricing
- Mean-field theories
- Network algorithms
- Pricing strategy
- Sensors network
- Trading strategies
- Deep learning
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0343 — Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the development of the IoT (Internet of Things), sensors networks can bring a large amount of valuable data. In addition to be utilized in the local IoT applications, the data can also be traded in the connected edge servers. As an efficient resource allocation mechanism, the double auction has been widely used in the stock and futures markets and can be also applied in the data resource allocation in sensor networks. Currently, there usually exist multiple edge servers running double auctions competing with each other to attract data users (buyers) and producers (sellers). Therefore, the double auction market run on each edge server needs efficient mechanism to improve the allocation efficiency. Specifically, the pricing strategy of the double auction plays an important role on affecting traders' profit, and thus, will affect the traders' market choices and bidding strategies, which in turn affect the competition result of double auction markets. In addition, the traders' trading strategies will also affect the market's pricing strategy. Therefore, we need to analyze the double auction markets' pricing strategy and traders' trading strategies. Specifically, we use a deep reinforcement learning algorithm combined with mean field theory to solve this problem with a huge state and action space. For trading strategies, we use the Independent Parametrized Deep Q-Network (I-PDQN) algorithm combined with mean field theory to compute the Nash equilibrium strategies. We then compare it with the fictitious play (FP) algorithm. The experimental results show that the computation speed of I-PDQN algorithm is significantly faster than that of FP algorithm. For pricing strategies, the double auction markets will dynamically adjust the pricing strategy according to traders' trading strategies. This is a sequential decision-making process involving multiple agents. Therefore, we model it as a Markov game. We adopt Multiagent Deep Deterministic Policy Gradient (MADDPG) algorithm to analyze the Nash equilibrium pricing strategies. The experimental results show that the MADDPG algorithm solves the problem faster than the FP algorithm.  © 2021 Bing Shi et al.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0343.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
