---
id: "paper-2394"
title: "Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments"
authors: ["Yu, Deshui", "Liu, Xianhui", "Ning, Jia", "Wang, Shengyi", "Zhu, Chenglin", "Zhao, Weidong"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3620126"
url: "https://www.scopus.com/pages/publications/105019620716?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "54256--54273"
keywords: ["AI task offloading", "cloud-edge-device computing", "deep reinforcement learning", "Industrial Internet of Things (IIoT)", "multiagents"]
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

# paper-2394 — Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments

## Metadata

- **Authors:** Yu, Deshui and Liu, Xianhui and Ning, Jia and Wang, Shengyi and Zhu, Chenglin and Zhao, Weidong
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3620126
- **URL:** https://www.scopus.com/pages/publications/105019620716?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 54256--54273
- **Language:** English
- **Keywords:** AI task offloading; cloud-edge-device computing; deep reinforcement learning; Industrial Internet of Things (IIoT); multiagents

### Abstract

As a key enabler of Industry 4.0, the Industrial Internet of Things (IIoT) has been rapidly advancing, driving the increasingly widespread adoption of artificial intelligence (AI) in industrial production. However, the high computational demands of AI tasks contrast sharply with the limited computing resources available in industrial environments, highlighting the need for efficient task offloading strategies. This article addresses AI task offloading under resource-constrained IIoT scenarios by proposing LSTM-enhanced hierarchical-classification offloading with DQN (LHC-DQN). The proposed framework adopts a two-layer offloading architecture: the first layer performs global scheduling by assigning tasks to cloud, edge, or device resources, while the second layer refines the allocation. Cloud and edge nodes apply mathematical optimization, whereas device nodes leverage DRL agents for autonomous decision-making. To handle AI task heterogeneity, a classification-aware mechanism is introduced in the first layer, deploying separate DQN agents for inference and training tasks to improve adaptability and efficiency. Furthermore, an LSTM module is integrated into the DQN backbone to capture temporal dependencies in task states. Experimental results in a simulated environment demonstrate that LHC-DQN significantly outperforms traditional methods, increasing task completion rates approximately from 47% to 68%. Ablation and generalization tests further confirm the robustness and effectiveness of the proposed method. Overall, LHC-DQN offers a practical and efficient solution for intelligent task offloading and resource scheduling in IIoT environments. © 2014 IEEE.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning-Based AI Task Offloading in Resource-Constrained IIoT Computing Environments
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
