---
id: "paper-343"
title: "Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets"
authors: ["Shi, Bing", "Song, Zhaoxiang", "Xu, Jianqiao"]
year: 2021
venue: "Journal of Sensors"
venue_type: "journal"
doi: "10.1155/2021/9651117"
url: "https://www.scopus.com/pages/publications/85122858739?origin=resultslist"
publisher: "Hindawi Limited"
pages: ""
keywords: ["Commerce", "Computation theory", "Costs", "Decision making", "Edge computing", "Electronic trading", "Financial markets", "Game theory", "Internet of things", "Learning algorithms", "Mean field theory", "Multi agent systems", "Reinforcement learning", "Resource allocation", "Sensor networks", "Auction markets", "Double auction", "Edge server", "Fictitious play", "Market pricing", "Mean-field theories", "Network algorithms", "Pricing strategy", "Sensors network", "Trading strategies", "Deep learning"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-343 — Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets

## Metadata

- **Authors:** Shi, Bing and Song, Zhaoxiang and Xu, Jianqiao
- **Year:** 2021
- **Venue:** Journal of Sensors
- **DOI:** 10.1155/2021/9651117
- **URL:** https://www.scopus.com/pages/publications/85122858739?origin=resultslist
- **Publisher:** Hindawi Limited
- **Pages:** 
- **Language:** English
- **Keywords:** Commerce; Computation theory; Costs; Decision making; Edge computing; Electronic trading; Financial markets; Game theory; Internet of things; Learning algorithms; Mean field theory; Multi agent systems; Reinforcement learning; Resource allocation; Sensor networks; Auction markets; Double auction; Edge server; Fictitious play; Market pricing; Mean-field theories; Network algorithms; Pricing strategy; Sensors network; Trading strategies; Deep learning

### Abstract

With the development of the IoT (Internet of Things), sensors networks can bring a large amount of valuable data. In addition to be utilized in the local IoT applications, the data can also be traded in the connected edge servers. As an efficient resource allocation mechanism, the double auction has been widely used in the stock and futures markets and can be also applied in the data resource allocation in sensor networks. Currently, there usually exist multiple edge servers running double auctions competing with each other to attract data users (buyers) and producers (sellers). Therefore, the double auction market run on each edge server needs efficient mechanism to improve the allocation efficiency. Specifically, the pricing strategy of the double auction plays an important role on affecting traders' profit, and thus, will affect the traders' market choices and bidding strategies, which in turn affect the competition result of double auction markets. In addition, the traders' trading strategies will also affect the market's pricing strategy. Therefore, we need to analyze the double auction markets' pricing strategy and traders' trading strategies. Specifically, we use a deep reinforcement learning algorithm combined with mean field theory to solve this problem with a huge state and action space. For trading strategies, we use the Independent Parametrized Deep Q-Network (I-PDQN) algorithm combined with mean field theory to compute the Nash equilibrium strategies. We then compare it with the fictitious play (FP) algorithm. The experimental results show that the computation speed of I-PDQN algorithm is significantly faster than that of FP algorithm. For pricing strategies, the double auction markets will dynamically adjust the pricing strategy according to traders' trading strategies. This is a sequential decision-making process involving multiple agents. Therefore, we model it as a Markov game. We adopt Multiagent Deep Deterministic Policy Gradient (MADDPG) algorithm to analyze the Nash equilibrium pricing strategies. The experimental results show that the MADDPG algorithm solves the problem faster than the FP algorithm.  © 2021 Bing Shi et al.

## 04 — Title Screening

**Title:** Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Trading and Pricing Sensor Data in Competing Edge Servers with Double Auction Markets
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
