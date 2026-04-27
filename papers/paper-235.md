---
id: "paper-235"
title: "A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center"
authors: ["Santos Filho, Reiner H.", "Ferreira, Tadeu N.", "Mattos, Diogo M. F.", "Medeiros, Dianne S. V."]
year: 2020
venue: "International Conference on Systems, Signals, and Image Processing"
venue_type: "conference"
doi: "10.1109/IWSSIP48289.2020.9145174"
url: "https://www.scopus.com/pages/publications/85089141959?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "331--336"
keywords: ["bandwidth provisioning", "data center", "markov decision process", "reinforcement learning"]
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

# paper-235 — A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center

## Metadata

- **Authors:** Santos Filho, Reiner H. and Ferreira, Tadeu N. and Mattos, Diogo M. F. and Medeiros, Dianne S. V.
- **Year:** 2020
- **Venue:** International Conference on Systems, Signals, and Image Processing
- **DOI:** 10.1109/IWSSIP48289.2020.9145174
- **URL:** https://www.scopus.com/pages/publications/85089141959?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 331--336
- **Language:** English
- **Keywords:** bandwidth provisioning; data center; markov decision process; reinforcement learning

### Abstract

Efficient management of cloud traffic leads to resource sharing among clients. To meet clients' performance restrictions, however, cloud providers adopt strict resource allocation that implies idle resources as clients' bandwidth thresholds are over-provisioned. We propose a dynamic mechanism to provide resources on-demand in a multitenant data center. The mechanism relies on Q-learning multi-agent for managing each client access to the cloud resources. The proposed mechanism either measure the throughput continuously or map the CPU usage into bandwidth usage. We assess our mechanism in an emulated environment, in which a network controller provisions bandwidth. Results show that the mechanism reduces cloud idleness, allowing low-priority clients to use bandwidth while there is idle capacity. Our mechanism incurs low processing overhead, even when the number of states and action space grow, while the memory cost per agent increases, peaking at 300 kB for 200 states and actions. When mapping CPU usage into bandwidth usage, the mechanism achieves fair bandwidth sharing at the cost of small increase on the convergence time to an optimal policy. © 2020 IEEE.

## 04 — Title Screening

**Title:** A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Lightweight Reinforcement-Learning-Based Mechanism for Bandwidth Provisioning on Multitenant Data Center
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
