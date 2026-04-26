---
id: "paper-310"
title: "A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments"
authors: ["Long, Saiqin", "Long, Weifan", "Li, Zhetao", "Li, Kenli", "Xia, Yuanqing", "Tang, Zhuo"]
year: 2021
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2020.3041029"
url: "https://www.scopus.com/pages/publications/85097394725?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1629--1640"
keywords: ["Data centers", "game theory", "mutliple agent system", "QoS constraint", "queueing system"]
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
    human_decision: ""
    human_justification: ""

---

# paper-310 — A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments

## Metadata

- **Authors:** Long, Saiqin and Long, Weifan and Li, Zhetao and Li, Kenli and Xia, Yuanqing and Tang, Zhuo
- **Year:** 2021
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2020.3041029
- **URL:** https://www.scopus.com/pages/publications/85097394725?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1629--1640
- **Language:** English
- **Keywords:** Data centers; game theory; mutliple agent system; QoS constraint; queueing system

### Abstract

With the development of the Internet of Things, the data that needs to be processed is increasing rapidly. Therefore, the collaboration of cloud and edge emerges as the times require. Edge nodes are mainly responsible for collecting data, and decide to process the data locally or offload to cloud data centers. Cloud data centers are suitable for data analysis, model training, and managing edge nodes. In this article, we focus on the task assignment problems in collaborative edge and cloud environments and study it in a distributed, non-cooperative environment. An M/M/1 queueing model is established to characterize the task transmission. Because of the multi-core processors, we set an M/M/C queueing model to characterize the task computation. We consider the problem from the perspective of game theory and formulate it into a non-cooperative game among multi-agents (multiple edge data centers) in which each agent is informed with incomplete information (allocation strategies) of others. For each agent, we define a function of the expected cost of tasks as the disutility function, and minimize it subject to the QoS constraint. We analyze the existence of Nash equilibrium and develop a Greedy Energy-aware Algorithm (GEA) to choose active servers using the Limit Searching Algorithm (LSA) to find the ceiling utilization. Then we propose the Best Response Algorithm (BRA) to optimize the utility function. The convergence of the BRA algorithm has been discussed. Finally, the results demonstrate that the BRA algorithm can get a solution close to Nash equilibrium and reach it quickly. © 1990-2012 IEEE.

## 04 — Title Screening

**Title:** A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Game-Based Approach for Cost-Aware Task Assignment with QoS Constraint in Collaborative Edge and Cloud Environments
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
