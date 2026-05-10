---
id: "paper-820"
title: "Multi-Agent Reinforcement Learning for Distributed Workflow Orchestration at the Tactical Edge"
authors: ["Amato, Alessandro", "Morelli, Alessandro", "Fogli, Mattia", "Galliera, Raffaele", "Suri, Niranjan"]
year: 2024
venue: "Proceedings - IEEE Military Communications Conference MILCOM"
venue_type: "conference"
doi: "10.1109/MILCOM61039.2024.10773787"
url: "https://www.scopus.com/pages/publications/85214560186?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "64--69"
keywords: ["Edge Computing", "MARL", "Service Orchestration", "Tactical Edge", "Workflow", "Workflow Deployment"]
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

# paper-820 — Multi-Agent Reinforcement Learning for Distributed Workflow Orchestration at the Tactical Edge

## Metadata

- **Authors:** Amato, Alessandro and Morelli, Alessandro and Fogli, Mattia and Galliera, Raffaele and Suri, Niranjan
- **Year:** 2024
- **Venue:** Proceedings - IEEE Military Communications Conference MILCOM
- **DOI:** 10.1109/MILCOM61039.2024.10773787
- **URL:** https://www.scopus.com/pages/publications/85214560186?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 64--69
- **Language:** English
- **Keywords:** Edge Computing; MARL; Service Orchestration; Tactical Edge; Workflow; Workflow Deployment

### Abstract

The dynamic nature of tactical edge networks has led to the design of architectures that enable real-time data processing and analytics at the edge, to ensure the continuation of operations when the connection to the headquarters is unavailable. However, workflow orchestration faces unique challenges over frequently disconnected, intermittent, and limited (DIL) networks, where traditional approaches, mainly developed for cloud-like environments, lack the flexibility to react promptly to ever-changing conditions. This paper presents a novel decentralized partially observable Markov decision process (DEC-POMDP) formulation for the distributed workflow orchestration problem, where agents need to cooperate to maximize the computation efficiency while reducing the data transmission time. We propose a solution based on multi-agent reinforcement learning (MARL) that leverages graph convolutional reinforcement learning (DGN) and graph attention networks (GAT) to enable agents to share information with each other, capture the network's structural information, ensure scalability, and eliminate the needs for global knowledge of the network. Training and experiments, which compare our solution with the corresponding constraint satisfaction problem (CSP), are conducted in a simulated 2D urban scenario that mimics nodes' mobility and communications, showing promising results. © 2024 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning for Distributed Workflow Orchestration at the Tactical Edge

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning for Distributed Workflow Orchestration at the Tactical Edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning for Distributed Workflow Orchestration at the Tactical Edge
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
