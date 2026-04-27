---
id: "paper-2914"
title: "Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information"
authors: ["Zhang, Jing", "Shen, Fei", "Yan, Feng", "Li, Jie"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3634598"
url: "https://www.scopus.com/pages/publications/105022251819?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "3499--3515"
keywords: ["Multi-agent reinforcement learning", "Nash equilibrium", "partially observable Markov decision process (POMDP)", "stochastic game", "vehicular edge offloading"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2914 — Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information

## Metadata

- **Authors:** Zhang, Jing and Shen, Fei and Yan, Feng and Li, Jie
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3634598
- **URL:** https://www.scopus.com/pages/publications/105022251819?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 3499--3515
- **Language:** English
- **Keywords:** Multi-agent reinforcement learning; Nash equilibrium; partially observable Markov decision process (POMDP); stochastic game; vehicular edge offloading

### Abstract

Edge computing provides low-latency computational services for task offloading in vehicular networks. However, challenges such as dynamic transmission rates, resource limitations, and information-sharing constraints impede efficient offloading. Few studies address these issues concurrently in designing dynamic offloading strategies, often resulting in sub-optimal system utility. This paper aims to achieve efficient vehicular task offloading via an idleness-aware edge server (ES) from a game theory perspective. We propose a Gated Recurrent Unit (GRU) prediction model with an attention mechanism to guide vehicles to the nearest idle ES. The offloading decision process is modeled as a stochastic game, proving the existence of a Nash equilibrium (NE). Additionally, we model it as a multi-agent partially observable Markov decision process (POMDP) to account for limited information access among vehicles. To solve the POMDP and achieve near-optimal NE, we introduce a Multi-Agent Reinforcement Learning-based Task Offloading (MATO) algorithm, combining a Differentiable Neural Computer (DNC) and an Advantageous Actor-Critic (A2C) framework. The DNC’s external memory stores structured representations of past information, enabling deeper exploration of the strategy space. Adjusting the reward representation enhances training efficiency. Experimental results driven by real-world datasets demonstrate that MATO effectively improves the computing offloading utility while increasing the convergence speed compared to existing schemes. © 2013 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning Based Idle-Aware Task Offloading in Dynamic Vehicular Networks With Partial Information
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
