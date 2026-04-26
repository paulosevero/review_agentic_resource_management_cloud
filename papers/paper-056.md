---
id: "paper-056"
title: "Distributed and Efficient Resource Balancing among Many Suppliers and Consumers"
authors: ["Chaturvedi, Kamal", "Yu, Jia Yuan", "Rao, Shrisha"]
year: 2018
venue: "Proceedings - 2018 IEEE International Conference on Systems, Man, and Cybernetics, SMC 2018"
venue_type: "conference"
doi: "10.1109/SMC.2018.00606"
url: "https://www.scopus.com/pages/publications/85062232773?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "3584--3589"
keywords: ["AIMD", "distributed optimization", "multi-agent systems", "profit maximization", "supplier-consumer problem"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": exclude
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-056 — Distributed and Efficient Resource Balancing among Many Suppliers and Consumers

## Metadata

- **Authors:** Chaturvedi, Kamal and Yu, Jia Yuan and Rao, Shrisha
- **Year:** 2018
- **Venue:** Proceedings - 2018 IEEE International Conference on Systems, Man, and Cybernetics, SMC 2018
- **DOI:** 10.1109/SMC.2018.00606
- **URL:** https://www.scopus.com/pages/publications/85062232773?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 3584--3589
- **Language:** English
- **Keywords:** AIMD; distributed optimization; multi-agent systems; profit maximization; supplier-consumer problem

### Abstract

Achieving a balance of supply and demand in a multi-agent system with many individual self-interested and rational agents that act as suppliers and consumers is a natural problem in a variety of real-life domains - smart power grids, data centers, and others. In this paper, we address the profit-maximization problem for a group of distributed supplier and consumer agents, with no inter-agent communication. We simulate a scenario of a market with S suppliers and C consumers such that at every instant, each supplier agent supplies a certain quantity and simultaneously, each consumer agent consumes a certain quantity. The information about the total amount supplied and consumed is only kept with the center. The proposed algorithm is a combination of the classical additive-increase multiplicative-decrease (AIMD) algorithm in conjunction with a probabilistic rule for the agents to respond to a capacity signal. This leads to a nonhomogeneous Markov chain and we show almost sure convergence of this chain to the social optimum, for our market of distributed supplier and consumer agents. Employing this AIMD-type algorithm, the center sends a feedback message to the agents in the supplier side if there is a scenario of excess supply, or to the consumer agents if there is excess consumption. Each agent has a concave utility function whose derivative tends to 0 when an optimum quantity is supplied/consumed. Hence when social convergence is reached, each agent supplies or consumes a quantity which leads to its individual maximum profit, without the need of any communication. So eventually, each agent supplies or consumes a quantity which leads to its individual maximum profit, without communicating with any other agents. Our simulations show the efficacy of this approach. © 2018 IEEE.

## 04 — Title Screening

**Title:** Distributed and Efficient Resource Balancing among Many Suppliers and Consumers

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed and Efficient Resource Balancing among Many Suppliers and Consumers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Distributed and Efficient Resource Balancing among Many Suppliers and Consumers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

### Human Review

- **My Final Decision:** _(fill in spreadsheet)_
- **My Justification:** _(fill in spreadsheet)_

## 05 — Abstract Screening

<!-- Populated by /05-abstract-screening -->

## 06 — Full-Text Screening

<!-- Populated by /06-full-text-screening -->

## 07 — Taxonomy

<!-- Populated by /07-taxonomy-development -->

## 08 — Analysis

<!-- Populated by /08-analysis -->
