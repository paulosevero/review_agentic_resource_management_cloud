---
id: "paper-2539"
title: "QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems"
authors: ["Chen, Xuyang", "Feng, Daquan", "Jiang, Wei", "Luo, Qu", "Chen, Gaojie", "Sun, Yao"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2026.3662899"
url: "https://www.scopus.com/pages/publications/105030557637?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "7100--7117"
keywords: ["Mobile edge computing", "resource allocation", "semantic-aware", "task offloading"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2539 — QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems

## Metadata

- **Authors:** Chen, Xuyang and Feng, Daquan and Jiang, Wei and Luo, Qu and Chen, Gaojie and Sun, Yao
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2026.3662899
- **URL:** https://www.scopus.com/pages/publications/105030557637?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 7100--7117
- **Language:** English
- **Keywords:** Mobile edge computing; resource allocation; semantic-aware; task offloading

### Abstract

Mobile edge computing (MEC) provides low-latency offloading solutions for computationally intensive tasks, effectively improving the computing efficiency and battery life of mobile devices. However, for data-intensive tasks or scenarios with limited uplink bandwidth, network congestion might occur due to massive simultaneous offloading nodes, increasing transmission latency, and affecting task performance. In this paper, we propose a semantic-aware multi-task offloading framework to address the challenges posed by limited uplink bandwidth. By introducing a semantic extraction factor, we balance the tradeoff among transmission latency, computation energy consumption, and task performance. To measure the offloading performance of different tasks, we design a unified and fair quality of experience (QoE) metric that includes execution latency, energy consumption, and task performance. We formulate the QoE optimization problem as a Markov decision process (MDP) and exploit the semantic-aware multi-agent proximal policy optimization (MAPPO) reinforcement learning algorithm to jointly optimize the semantic extraction factor and communication and computing resources allocation to maximize overall QoE. Experimental results show that the proposed method achieves a 12.68% improvement in user QoE compared with the semantic-unaware approach. Moreover, the proposed approach can be easily extended to models with different user preferences. © 2026 IEEE.

## 04 — Title Screening

**Title:** QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** QoE-Driven Multi-Task Offloading for Semantic-Aware Edge Computing Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
