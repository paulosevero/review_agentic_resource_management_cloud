---
id: paper-0888
title: DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning
authors:
- Dong, Chongwu
- Shafiq, Muhammad
- Al Dabel, Maryam M.
- Sun, Yanbin
- Tian, Zhihong
venue: IEEE Transactions on Consumer Electronics
venue_type: journal
year: 2024
doi: 10.1109/TCE.2023.3339468
url: https://www.scopus.com/pages/publications/85179795899?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1519--1530
keywords:
- DNN inference
- edge intelligence
- industrial Internet of Things
- Industry 5.0
- multi-agent reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0888 — DNN Inference Acceleration for Smart Devices in Industry 5.0 by Decentralized Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the emergence of Industry 5.0, there has been a significant surge in the need for intelligent services within the realm of smart devices. Currently, deep neural networks (DNNs) have become the predominant technology in driving advancements in intelligent applications. With the collaboration of mobile edge computing (MEC), resource-constraint smart devices, such as the industrial Internet of Things (IIoT) devices, can meet the requirement of high computing for DNN-based inference by computation offloading. In the task offloading strategy obtained by a central decision-maker with global information, all devices in the MEC can get the optimal optimization for DNN inference acceleration. However, in a practical environment, central decision-making may get into trouble, such as information synchronization delay, irrational behavior of devices, and privacy leakage. In this paper, we explore the optimization of distributed task offloading for smart devices to deal with these challenges regarding DNN inference acceleration, considering the character of an early exit in the DNN model to balance the accuracy and latency. In our system model, the optimization is formulated as a decentralized partially observable Markov decision process (Dec-POMDP). Each smart device performs its strategy, including task offloading decision and DNN branch selection with local observation, and cooperatively optimizes the overall Quality of Experience for DNN inference. Based on the model of Dec-POMDP, we propose one algorithm based on Multi-agent Reinforcement Learning to solve the above problem. In our algorithm, we utilize the advanced function based on the counterfactual baseline to guide policy gradient learning to overcome the credit allocation problem in cooperative optimization. In addition, LSTM is introduced to improve the robustness of the algorithm. Finally, detailed performance evaluation and comparison are performed to show the effectiveness of our strategy.  © 2023 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0888.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
