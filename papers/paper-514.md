---
id: "paper-514"
title: "Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks"
authors: ["Xia, Shichao", "Yao, Zhixiu", "Wu, Guangfu", "Li, Yun"]
year: 2022
venue: "IEEE Transactions on Intelligent Transportation Systems"
venue_type: "journal"
doi: "10.1109/TITS.2022.3190280"
url: "https://www.scopus.com/pages/publications/85135225295?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "16701--16714"
keywords: ["Cooperative intelligent transportation system (C-ITS)", "multi-access edge computing (MEC)", "multi-agent deep deterministic policy gradient (MADDPG)", "Stackelberg game"]
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
    final_score: 0.5
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-514 — Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks

## Metadata

- **Authors:** Xia, Shichao and Yao, Zhixiu and Wu, Guangfu and Li, Yun
- **Year:** 2022
- **Venue:** IEEE Transactions on Intelligent Transportation Systems
- **DOI:** 10.1109/TITS.2022.3190280
- **URL:** https://www.scopus.com/pages/publications/85135225295?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 16701--16714
- **Language:** English
- **Keywords:** Cooperative intelligent transportation system (C-ITS); multi-access edge computing (MEC); multi-agent deep deterministic policy gradient (MADDPG); Stackelberg game

### Abstract

With the rapid advancement of the Internet of Vehicles and artificial intelligence (AI) technologies, the cooperative intelligent transportation system (C-ITS) has drawn great attention in recent years. To provide an ultra-reliable, low-latency computation experience of C-ITS, computation offloading is deemed indispensable by working with edge-cloud servers. In this paper, we first investigate a distributed dynamic computation offloading model for multi-access edge computing (MEC) enabled C-ITS under a heterogeneous road network, in which the multiple and heterogeneous computing power sources cooperatively provide computation offloading services for vehicles. Considering the autonomous offloading manner of the vehicles, we formulate the task offloading and computing power allocation as a distributed Stackelberg game, where the MEC servers as the leader to allocate computing resources and manage local energy, and the vehicles as the followers to offload local computation task. Since the observable states in the game is incomplete, the problem of resolving the optimal strategies for each game player is modeled as a partially observable Markov decision process (POMDP) to maximize the long-term cumulative reward. Then we develop a computation offloading algorithm using Stackelberg game-based multi-agent deep deterministic policy gradient (SG-MADDPG), which uses a centralized training and decentralized execution method to learn the optimal computing power allocation and computation offloading policies. Finally, extensive simulations are carried out and show the rationality and effectiveness of the proposed algorithm.  © 2000-2011 IEEE.

## 04 — Title Screening

**Title:** Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks

### Machine Screening

- **Final Score:** 0.5 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.5
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Offloading for Cooperative Intelligent Transportation Under Heterogeneous Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
