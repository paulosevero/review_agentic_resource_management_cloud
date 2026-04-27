---
id: "paper-260"
title: "A deep reinforcement learning approach for service migration in MEC-enabled vehicular networks"
authors: ["Abouaomar, Amine", "Mlika, Zoubeir", "Filali, Abderrahime", "Cherkaoui, Soumaya", "Kobbane, Abdellatif"]
year: 2021
venue: "Proceedings - Conference on Local Computer Networks, LCN"
venue_type: "conference"
doi: "10.1109/LCN52139.2021.9524882"
url: "https://www.scopus.com/pages/publications/85118466383?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "273--280"
keywords: ["Multi-access edge computing", "Reinforcement learning", "Service migration", "Vehicular networks"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-260 — A deep reinforcement learning approach for service migration in MEC-enabled vehicular networks

## Metadata

- **Authors:** Abouaomar, Amine and Mlika, Zoubeir and Filali, Abderrahime and Cherkaoui, Soumaya and Kobbane, Abdellatif
- **Year:** 2021
- **Venue:** Proceedings - Conference on Local Computer Networks, LCN
- **DOI:** 10.1109/LCN52139.2021.9524882
- **URL:** https://www.scopus.com/pages/publications/85118466383?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 273--280
- **Language:** English
- **Keywords:** Multi-access edge computing; Reinforcement learning; Service migration; Vehicular networks

### Abstract

Multi-access edge computing (MEC) is a key enabler to reduce the latency of vehicular network. Due to the vehicles mobility, their requested services (e.g., infotainment services) should frequently be migrated across different MEC servers to guarantee their stringent quality of service requirements. In this paper, we study the problem of service migration in a MEC-enabled vehicular network in order to minimize the total service latency and migration cost. This problem is formulated as a nonlinear integer program and is linearized to help obtaining the optimal solution using off-the-shelf solvers. Then, to obtain an efficient solution, it is modeled as a multi-agent Markov decision process and solved by leveraging deep Q learning (DQL) algorithm. The proposed DQL scheme performs a proactive services migration while ensuring their continuity under high mobility constraints. Finally, simulations results show that the proposed DQL scheme achieves close-to-optimal performance.  © 2021 IEEE.

## 04 — Title Screening

**Title:** A deep reinforcement learning approach for service migration in MEC-enabled vehicular networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A deep reinforcement learning approach for service migration in MEC-enabled vehicular networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A deep reinforcement learning approach for service migration in MEC-enabled vehicular networks
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
