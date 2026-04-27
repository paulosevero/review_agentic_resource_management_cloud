---
id: "paper-897"
title: "Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach"
authors: ["Ejaz, Muhammad Asim", "Wu, Guowei", "Ahmed, Adeel", "Iftikhar, Saman", "Bawazeer, Shaikhan"]
year: 2024
venue: "Sensors"
venue_type: "journal"
doi: "10.3390/s24175558"
url: "https://www.scopus.com/pages/publications/85203879202?origin=resultslist"
publisher: "Multidisciplinary Digital Publishing Institute (MDPI)"
pages: ""
keywords: ["deep reinforcement learning (DRL)", "end-to-end network slicing", "Internet of Things (IoT)", "mobile edge computing (MEC)", "multi-agent", "utility optimization"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-897 — Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach

## Metadata

- **Authors:** Ejaz, Muhammad Asim and Wu, Guowei and Ahmed, Adeel and Iftikhar, Saman and Bawazeer, Shaikhan
- **Year:** 2024
- **Venue:** Sensors
- **DOI:** 10.3390/s24175558
- **URL:** https://www.scopus.com/pages/publications/85203879202?origin=resultslist
- **Publisher:** Multidisciplinary Digital Publishing Institute (MDPI)
- **Pages:** 
- **Language:** English
- **Keywords:** deep reinforcement learning (DRL); end-to-end network slicing; Internet of Things (IoT); mobile edge computing (MEC); multi-agent; utility optimization

### Abstract

Mobile Edge Computing (MEC) is crucial for reducing latency by bringing computational resources closer to the network edge, thereby enhancing the quality of services (QoS). However, the broad deployment of cloudlets poses challenges in efficient network slicing, particularly when traffic distribution is uneven. Therefore, these challenges include managing diverse resource requirements across widely distributed cloudlets, minimizing resource conflicts and delays, and maintaining service quality amid fluctuating request rates. Addressing this requires intelligent strategies to predict request types (common or urgent), assess resource needs, and allocate resources efficiently. Emerging technologies like edge computing and 5G with network slicing can handle delay-sensitive IoT requests rapidly, but a robust mechanism for real-time resource and utility optimization remains necessary. To address these challenges, we designed an end-to-end network slicing approach that predicts common and urgent user requests through T distribution. We formulated our problem as a multi-agent Markov decision process (MDP) and introduced a multi-agent soft actor–critic (MAgSAC) algorithm. This algorithm prevents the wastage of scarce resources by intelligently activating and deactivating virtual network function (VNF) instances, thereby balancing the allocation process. Our approach aims to optimize overall utility, balancing trade-offs between revenue, energy consumption costs, and latency. We evaluated our method, MAgSAC, through simulations, comparing it with the following six benchmark schemes: MAA3C, SACT, DDPG, S2Vec, Random, and Greedy. The results demonstrate that our approach, MAgSAC, optimizes utility by 30%, minimizes energy consumption costs by 12.4%, and reduces execution time by 21.7% compared to the closest related multi-agent approach named MAA3C. © 2024 by the authors.

## 04 — Title Screening

**Title:** Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Utility-Driven End-to-End Network Slicing for Diverse IoT Users in MEC: A Multi-Agent Deep Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
