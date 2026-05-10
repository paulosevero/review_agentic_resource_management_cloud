---
id: "paper-932"
title: "COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning"
authors: ["Giannopoulos, Anastasios", "Paralikas, Ilias", "Spantideas, Sotirios", "Trakadas, Panagiotis"]
year: 2024
venue: "2024 International Conference on Intelligent Computing, Communication, Networking and Services, ICCNS 2024"
venue_type: "conference"
doi: "10.1109/ICCNS62192.2024.10776151"
url: "https://www.scopus.com/pages/publications/85215271305?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "9--16"
keywords: ["6G network", "deep reinforcement learning", "edge computing", "edge-cloud continuum", "resource management", "task offloading"]
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

# paper-932 — COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Giannopoulos, Anastasios and Paralikas, Ilias and Spantideas, Sotirios and Trakadas, Panagiotis
- **Year:** 2024
- **Venue:** 2024 International Conference on Intelligent Computing, Communication, Networking and Services, ICCNS 2024
- **DOI:** 10.1109/ICCNS62192.2024.10776151
- **URL:** https://www.scopus.com/pages/publications/85215271305?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 9--16
- **Language:** English
- **Keywords:** 6G network; deep reinforcement learning; edge computing; edge-cloud continuum; resource management; task offloading

### Abstract

In the burgeoning domain of the edge-cloud con-tinuum (ECC), the efficient management of computational tasks offloaded from mobile devices to edge nodes is paramount. This paper introduces a Cooperative cOmputation Offloading scheme for ECC via Latency-aware multi-agent Reinforcement learning (COOLER), a distributed framework designed to address the challenges posed by the uncertain load dynamics at edge nodes. COOLER enables each edge node to autonomously make offloading decisions, optimizing for non-divisible, delay-sensitive tasks without prior knowledge of other nodes' task models and decisions. By formulating a multi-agent computation offloading problem, COOLER aims to minimize the expected long-term latency and task drop ratio. Following the ECC requirements for seamless task flow both within Edge layer and between Edge-Cloud layers, COOLER considers that task computation decisions are three-fold: (i) local computation, (ii) horizontal offloading to another edge node, or (iii) vertical offloading to the Cloud. The integration of advanced techniques such as long short-term memory (LSTM), double deep Q-network (DQN) and dueling DQN enhances the estimation of long-term costs, thereby improving decision-making efficacy. Simulation results demonstrate that COOLER significantly outperforms baseline offloading algorithms, reducing both the ratio of dropped tasks and average delay, and better harnessing the processing capacities of edge nodes. © 2024 IEEE.

## 04 — Title Screening

**Title:** COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** COOLER: Cooperative Computation Offloading in Edge-Cloud Continuum Under Latency Constraints via Multi-Agent Deep Reinforcement Learning
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
