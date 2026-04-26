---
id: "paper-2885"
title: "LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks"
authors: ["Ye, Ziqiang", "Gao, Yulan", "Xiao, Yue", "Lei, Xianfu", "Fan, Pingzhi", "Karagiannidis, George K."]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3647682"
url: "https://www.scopus.com/pages/publications/105025782335?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "5247--5261"
keywords: ["hop-frequency planning", "IAA", "LAENet", "LLM", "security communication", "trajectory prediction"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2885 — LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks

## Metadata

- **Authors:** Ye, Ziqiang and Gao, Yulan and Xiao, Yue and Lei, Xianfu and Fan, Pingzhi and Karagiannidis, George K.
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3647682
- **URL:** https://www.scopus.com/pages/publications/105025782335?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 5247--5261
- **Language:** English
- **Keywords:** hop-frequency planning; IAA; LAENet; LLM; security communication; trajectory prediction

### Abstract

Secure communications in low-altitude economy networks (LAENets) are critical because the broadcast nature of air-ground links, the strong line-of-sight (LoS) propagation, and the high mobility of intelligent aerial agents (IAAs) inherently expose transmissions to agile, coordinated jamming and eavesdropping. In this paper, we consider a dynamic adversarial scenario where a legitimate IAA simultaneously provides service to multiple terrestrial receivers, while being threatened by collaborative adversarial entities comprising an intelligent UAV-based jammer and a ground-level eavesdropper. The adversaries cooperatively optimize their spatial trajectories and spectrum allocation strategies through real-time adaptive coordination. To counter such coordinated threats, we propose a synergistic framework where a lightweight retrieval-augmented generation (RAG)-enhanced large language model (LLM) predicts, from sequential wireless observations, the probabilistic jamming/eavesdropping intent distributions across frequency bands and the jammer’s next-step trajectory. These predictions are then exploited by a soft actor-critic (SAC)-based reinforcement learning agent at the IAA to jointly optimize frequency-hopping selection, trajectory control, and power allocation, thereby enabling anticipatory and context-aware secure communication. Simulation results demonstrate that, compared to baseline models from deep learning (DL) and reinforcement learning (RL) approaches, our framework achieves an average secrecy-rate improvement of approximately 53.84%, while also delivering faster convergence and greater robustness against adaptive, coordinated attacks. The experiments are conducted under comparable training budgets, and our approach outperforms typical DL models (e.g., convolutional neural network (CNN), long short-term memory (LSTM), Transformer) and optimization baselines (e.g., proximal policy optimization (PPO), simulated annealing) across secrecy rate, convergence speed, and robustness. This establishes the proposed framework as a practical solution for securing next-generation LAENets under coordinated jamming and eavesdropping. © 2013 IEEE.

## 04 — Title Screening

**Title:** LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** LLM-Aided Prediction and RL-Based Optimization for Secure Communications in Low-Altitude Economy Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
