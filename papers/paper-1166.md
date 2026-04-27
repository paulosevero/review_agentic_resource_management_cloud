---
id: "paper-1166"
title: "LearnChain: Transparent and cooperative reinforcement learning on Blockchain"
authors: ["Sami, Hani", "Mizouni, Rabeb", "Otrok, Hadi", "Singh, Shakti", "Bentahar, Jamal", "Mourad, Azzam"]
year: 2024
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2023.09.012"
url: "https://www.scopus.com/pages/publications/85171891314?origin=resultslist"
publisher: "Elsevier B.V."
pages: "255--271"
keywords: ["Blockchain", "Cooperative artificial intelligence (AI)", "Ethereum", "Quorum", "Reinforcement learning", "Transparency", "Trust", "Vehicular edge computing"]
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

# paper-1166 — LearnChain: Transparent and cooperative reinforcement learning on Blockchain

## Metadata

- **Authors:** Sami, Hani and Mizouni, Rabeb and Otrok, Hadi and Singh, Shakti and Bentahar, Jamal and Mourad, Azzam
- **Year:** 2024
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2023.09.012
- **URL:** https://www.scopus.com/pages/publications/85171891314?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 255--271
- **Language:** English
- **Keywords:** Blockchain; Cooperative artificial intelligence (AI); Ethereum; Quorum; Reinforcement learning; Transparency; Trust; Vehicular edge computing

### Abstract

We consider multi-agent reinforcement learning (MARL) with the popular paradigm of centralized training and decentralized execution (CTDE). CTDE empowers sharing knowledge from agents in different environments for updating a shared model. A wide range of applications is supported through CTDE in MARL, such as self-driving vehicle coordination, traffic lights synchronization, or cooperation in various aspects of the Internet of Things (IoT), including resource management. Despite the drawbacks of relying on a central authority for handling model updates, incorporating multiple sources of data raises concerns about the trustworthiness of the process. For instance, participating agents could provide data in the favor of their experiences to shift the model towards certain behaviors. Similarly, sending falsified data for updates could lead to adversarial attacks. To overcome these challenges, it is essential to integrate the Ethereum Blockchain technology to handle model updates in the CTDE paradigm by achieving decentralized storage and consensus mechanism for model updates. In the literature, there exist multiple efforts that propose using reinforcement learning (RL) on Blockchain; however, none of them have considered updating MARL of CTDE on-chain, allowing transparent and auditable record of the training process. Therefore, we propose LearnChain, a framework that offers an integration between the CTDE mechanism and a Consortium Blockchain built between authorized participants, thus avoiding gas costs. At the core of LearnChain, RL is integrated with Quorum, offering separate smart contracts for deployment, data handling with incentive mechanisms, training, target update, and inference. Based on a real use-case entailing management of Vehicular Edge Computing tasks through multi-agent synchronization, we implement LearnChain and evaluate its performance and cost in different settings. Our results show the ability to improve learning from shared experiences and to adapt to environment changes on the Quorum BlockChain. © 2023

## 04 — Title Screening

**Title:** LearnChain: Transparent and cooperative reinforcement learning on Blockchain

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** LearnChain: Transparent and cooperative reinforcement learning on Blockchain
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** LearnChain: Transparent and cooperative reinforcement learning on Blockchain
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
