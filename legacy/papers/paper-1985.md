---
id: "paper-1985"
title: "A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments"
authors: ["Naser, Zainab Saadoon", "Marouane, Hend", "Fakhfakh, Ahmed", "Almatwari, Zaid Abdulsalam"]
year: 2025
venue: "Proceedings - International Conference on Informatics and Computational Sciences"
venue_type: "conference"
doi: "10.1109/ICICoS68590.2025.11330010"
url: "https://www.scopus.com/pages/publications/105032385383?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "126--131"
keywords: ["Adaptive traffic signal control", "cloud computing", "deep reinforcement learning", "multi-agent systems", "real-time traffic optimization", "scalable architecture"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1985 — A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments

## Metadata

- **Authors:** Naser, Zainab Saadoon and Marouane, Hend and Fakhfakh, Ahmed and Almatwari, Zaid Abdulsalam
- **Year:** 2025
- **Venue:** Proceedings - International Conference on Informatics and Computational Sciences
- **DOI:** 10.1109/ICICoS68590.2025.11330010
- **URL:** https://www.scopus.com/pages/publications/105032385383?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 126--131
- **Language:** English
- **Keywords:** Adaptive traffic signal control; cloud computing; deep reinforcement learning; multi-agent systems; real-time traffic optimization; scalable architecture

### Abstract

Efficient traffic signal control is a cornerstone of modern urban mobility, playing a critical role in reducing congestion, travel delays, and emissions. Traditional fixed-time or rule-based traffic signal systems often lack the flexibility to adapt to dynamic and non-uniform traffic patterns, particularly in densely populated cities. To address these limitations, this paper proposes a scalable, cloud-based framework for adaptive traffic signal optimization using multi-agent deep reinforcement learning (DRL). In the proposed system, each intersection is governed by an independent agent trained with the Proximal Policy Optimization (PPO) algorithm. Agents learn traffic signal policies from localized, real-time observations, including vehicle counts, waiting times, and signal states, enabling decentralized, context-aware control. The framework is designed for cloud deployment, leveraging Google Colab and Google Cloud Storage for scalable training, consistent metric logging, and reproducible post-simulation analysis. Traffic behavior is modeled using the Simulation of Urban Mobility (SUMO) platform, ensuring a realistic and flexible environment for evaluation. Extensive experiments demonstrate that the DRL-based system significantly outperforms traditional fixed-time control across key metrics such as average waiting time, vehicle queue length, throughput, and congestion levels. Performance improvements are especially evident under high-density and variable traffic conditions, where adaptability is most critical. In addition, the system exhibits robust convergence across episodes, while the cloud-integrated design ensures scalability, reproducibility, and practical applicability for smart city deployment.  © 2025 IEEE.

## 04 — Title Screening

**Title:** A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Scalable Cloud-Based Framework for Adaptive Traffic Signal Control Utilizing Deep Reinforcement Learning in Urban Environments
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
