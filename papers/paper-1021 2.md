---
id: "paper-1021"
title: "Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing"
authors: ["Li, Mingchu", "Li, Shuai", "Qi, Wanying"]
year: 2024
venue: "Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST"
venue_type: "conference"
doi: "10.1007/978-3-031-54521-4_23"
url: "https://www.scopus.com/pages/publications/85187709342?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "421--439"
keywords: ["Dynamic trade-off", "Edge computing", "Meta deep reinforcement learning", "Smart homes", "Task offloading"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
  "05-abstract-screening": pending
  "06-full-text-screening": pending
  "07-taxonomy": pending
  "08-analysis": pending
screening:
  "04-title-screening":
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-1021 — Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing

## Metadata

- **Authors:** Li, Mingchu and Li, Shuai and Qi, Wanying
- **Year:** 2024
- **Venue:** Lecture Notes of the Institute for Computer Sciences, Social-Informatics and Telecommunications Engineering, LNICST
- **DOI:** 10.1007/978-3-031-54521-4_23
- **URL:** https://www.scopus.com/pages/publications/85187709342?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 421--439
- **Language:** English
- **Keywords:** Dynamic trade-off; Edge computing; Meta deep reinforcement learning; Smart homes; Task offloading

### Abstract

In the edge computing enabled smart home scenario. Various smart home devices generate a large number of computing tasks, and users can offload these tasks to servers or perform them locally. Offloading to the server will result in lower delay, but it will also require paying the corresponding offloading cost. Therefore, users need to consider the low delay and additional costs caused by offloading. Different users have different trade-offs between latency and offload costs at different times. If the trade-off is set as a fixed hyperparameter, it will give users a poor experience. In the case of dynamic trade-offs, the model may have difficulty adapting to arrive at an optimal offloading decision. By jointly optimizing the task delay and offloading cost, We model it as a long-term cost minimization problem under dynamic trade-off (DT-LCMP). To solve the problem, we propose an offloading algorithm based on multi-agent meta deep reinforcement learning and load prediction (MAMRL-L). Combined with the idea of meta-learning, the DDQN method is used to train the network. By training the sampling data in different environments, the agent can adapt to the dynamic environment quickly. In order to improve the performance of the model, LSTNet is used to predict the load level of the next slot server in real time. The simulation results show that our algorithm has higher performance than the existing algorithms and benchmark algorithms. © ICST Institute for Computer Sciences, Social Informatics and Telecommunications Engineering 2024.

## 04 — Title Screening

**Title:** Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic Offloading Based on Meta Deep Reinforcement Learning and Load Prediction in Smart Home Edge Computing
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
