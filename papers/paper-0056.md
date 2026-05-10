---
id: paper-0056
title: Distributed and Efficient Resource Balancing among Many Suppliers and Consumers
authors:
- Chaturvedi, Kamal
- Yu, Jia Yuan
- Rao, Shrisha
venue: Proceedings - 2018 IEEE International Conference on Systems, Man, and Cybernetics, SMC 2018
venue_type: conference
year: 2018
doi: 10.1109/SMC.2018.00606
url: https://www.scopus.com/pages/publications/85062232773?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 3584--3589
keywords:
- AIMD
- distributed optimization
- multi-agent systems
- profit maximization
- supplier-consumer problem
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-0056 — Distributed and Efficient Resource Balancing among Many Suppliers and Consumers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Achieving a balance of supply and demand in a multi-agent system with many individual self-interested and rational agents that act as suppliers and consumers is a natural problem in a variety of real-life domains - smart power grids, data centers, and others. In this paper, we address the profit-maximization problem for a group of distributed supplier and consumer agents, with no inter-agent communication. We simulate a scenario of a market with S suppliers and C consumers such that at every instant, each supplier agent supplies a certain quantity and simultaneously, each consumer agent consumes a certain quantity. The information about the total amount supplied and consumed is only kept with the center. The proposed algorithm is a combination of the classical additive-increase multiplicative-decrease (AIMD) algorithm in conjunction with a probabilistic rule for the agents to respond to a capacity signal. This leads to a nonhomogeneous Markov chain and we show almost sure convergence of this chain to the social optimum, for our market of distributed supplier and consumer agents. Employing this AIMD-type algorithm, the center sends a feedback message to the agents in the supplier side if there is a scenario of excess supply, or to the consumer agents if there is excess consumption. Each agent has a concave utility function whose derivative tends to 0 when an optimum quantity is supplied/consumed. Hence when social convergence is reached, each agent supplies or consumes a quantity which leads to its individual maximum profit, without the need of any communication. So eventually, each agent supplies or consumes a quantity which leads to its individual maximum profit, without communicating with any other agents. Our simulations show the efficacy of this approach. © 2018 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0056.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
