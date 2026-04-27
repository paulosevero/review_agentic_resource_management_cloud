---
id: "paper-888"
title: "DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning"
authors: ["Dong, Chongwu", "Shafiq, Muhammad", "Al Dabel, Maryam M.", "Sun, Yanbin", "Tian, Zhihong"]
year: 2024
venue: "IEEE Transactions on Consumer Electronics"
venue_type: "journal"
doi: "10.1109/TCE.2023.3339468"
url: "https://www.scopus.com/pages/publications/85179795899?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1519--1530"
keywords: ["DNN inference", "edge intelligence", "industrial Internet of Things", "Industry 5.0", "multi-agent reinforcement learning"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-888 — DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning

## Metadata

- **Authors:** Dong, Chongwu and Shafiq, Muhammad and Al Dabel, Maryam M. and Sun, Yanbin and Tian, Zhihong
- **Year:** 2024
- **Venue:** IEEE Transactions on Consumer Electronics
- **DOI:** 10.1109/TCE.2023.3339468
- **URL:** https://www.scopus.com/pages/publications/85179795899?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1519--1530
- **Language:** English
- **Keywords:** DNN inference; edge intelligence; industrial Internet of Things; Industry 5.0; multi-agent reinforcement learning

### Abstract

With the emergence of Industry 5.0, there has been a significant surge in the need for intelligent services within the realm of smart devices. Currently, deep neural networks (DNNs) have become the predominant technology in driving advancements in intelligent applications. With the collaboration of mobile edge computing (MEC), resource-constraint smart devices, such as the industrial Internet of Things (IIoT) devices, can meet the requirement of high computing for DNN-based inference by computation offloading. In the task offloading strategy obtained by a central decision-maker with global information, all devices in the MEC can get the optimal optimization for DNN inference acceleration. However, in a practical environment, central decision-making may get into trouble, such as information synchronization delay, irrational behavior of devices, and privacy leakage. In this paper, we explore the optimization of distributed task offloading for smart devices to deal with these challenges regarding DNN inference acceleration, considering the character of an early exit in the DNN model to balance the accuracy and latency. In our system model, the optimization is formulated as a decentralized partially observable Markov decision process (Dec-POMDP). Each smart device performs its strategy, including task offloading decision and DNN branch selection with local observation, and cooperatively optimizes the overall Quality of Experience for DNN inference. Based on the model of Dec-POMDP, we propose one algorithm based on Multi-agent Reinforcement Learning to solve the above problem. In our algorithm, we utilize the advanced function based on the counterfactual baseline to guide policy gradient learning to overcome the credit allocation problem in cooperative optimization. In addition, LSTM is introduced to improve the robustness of the algorithm. Finally, detailed performance evaluation and comparison are performed to show the effectiveness of our strategy.  © 2023 IEEE.

## 04 — Title Screening

**Title:** DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning
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
