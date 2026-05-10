---
id: "paper-2582"
title: "MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems"
authors: ["Ghosh, Aswini", "Sharma, Nelson", "Mishra, Shivendu", "Misra, Rajiv", "Das, Sajal K."]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2025.3632862"
url: "https://www.scopus.com/pages/publications/105021668238?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "477--490"
keywords: ["Internet of Things", "mobility aware edge computing", "offloading", "sequence to sequence deep Q-learning", "transformer"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2582 — MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems

## Metadata

- **Authors:** Ghosh, Aswini and Sharma, Nelson and Mishra, Shivendu and Misra, Rajiv and Das, Sajal K.
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2025.3632862
- **URL:** https://www.scopus.com/pages/publications/105021668238?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 477--490
- **Language:** English
- **Keywords:** Internet of Things; mobility aware edge computing; offloading; sequence to sequence deep Q-learning; transformer

### Abstract

Mobility introduces significant challenges for optimal computation offloading, latency minimization, and efficient resource utilization in multi-access edge computing (MEC) systems. A key difficulty lies in leveraging real user trajectories to jointly optimize horizontal (inter-edge) and vertical (edge-to-cloud) task offloading decisions. This paper proposes a two-dimensional offloading scheme for a multi-layer edge–cloud architecture that enables collaborative task execution among resource-constrained edge nodes under mobility conditions. We present MGCO (Mobility-Aware Generative Computation Offloading), a generative AI–driven Transformer-based sequence-to-sequence Deep Q-Network (s2s-DQN) framework that learns from real-time trajectory data to anticipate user movement and optimize task placement dynamically. The Transformer architecture is adopted because its multi-head self-attention effectively captures long-range dependencies in mobility and task-demand patterns while avoiding vanishing gradients and sequential bottlenecks inherent to LSTM/GRU models. This design enables parallel contextual reasoning and stable autoregressive action generation, supporting real-time offloading decisions within strict operational latency constraints. Experimental results demonstrate that MGCO consistently outperforms existing methods, achieving up to 41.61% reduction in turnaround time compared to GASTO, and substantial improvements over DMQTO and HMAOA, reaching up to 645.40% and 751.90%, respectively, for longer prediction horizons (48 time slots of 5 seconds each). These results highlight MGCO’s robustness, scalability, and effectiveness in managing complex mobility scenarios in dynamic edge–cloud environments. © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MGCO: Mobility-Aware Generative Computation Offloading in Edge-Cloud Systems
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
