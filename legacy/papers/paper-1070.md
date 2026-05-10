---
id: "paper-1070"
title: "Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing"
authors: ["Long, Wanqing", "Lu, Hancheng", "Chong, Baolin", "Cheng, Guo"]
year: 2024
venue: "Proceedings - IEEE Global Communications Conference, GLOBECOM"
venue_type: "conference"
doi: "10.1109/GLOBECOM52923.2024.10901737"
url: "https://www.scopus.com/pages/publications/105000820483?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "4624--4629"
keywords: ["Blockchain", "deep reinforcement learning", "resource al-location", "serverless computing", "task scheduling"]
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

# paper-1070 — Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing

## Metadata

- **Authors:** Long, Wanqing and Lu, Hancheng and Chong, Baolin and Cheng, Guo
- **Year:** 2024
- **Venue:** Proceedings - IEEE Global Communications Conference, GLOBECOM
- **DOI:** 10.1109/GLOBECOM52923.2024.10901737
- **URL:** https://www.scopus.com/pages/publications/105000820483?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 4624--4629
- **Language:** English
- **Keywords:** Blockchain; deep reinforcement learning; resource al-location; serverless computing; task scheduling

### Abstract

Serverless computing is gaining popularity due to its "pay-per-use"model and simplified management. Benefiting from the common features of Internet of Things (IoT), the adaptation of serverless in edge computing is extensively researched. To protect nodes in serverless edge computing from potential attacks, blockchain technology plays a crucial role. Considering that the computing time of a single serverless function can be less than the time for a blockchain to generate a block, the blockchain component requires significant computing and bandwidth resources to ensure the generation efficiency of blocks matches the execution efficiency of serverless functions. However, existing studies on minimizing the completion time (a.k.a. makespan) of application workflows in serverless edge computing have never considered the impact brought by blockchain, leading to an imbalance in the resource allocation between the computing and blockchain components. To address this, we propose a Heterogeneous Event-driven Scheduling (HEDS) mechanism, which employs a fine-grained CPU al-location scheme and an event-driven approach, to make the adjustment of resource allocation between the computing and blockchain components more flexible and expeditious, leading to improving the utilization of both computing and bandwidth resources. Meanwhile, a Multi-agent Double Deep Q-network (MADDQN) algorithm is proposed to help agents minimize the makespan while balancing the resource consumption in the computing and blockchain components. Simulation results demonstrate that HEDS with MADDQN outperforms existing algorithms in terms of average makespan over different numbers of functions and nodes while satisfying the latency requirements of block generation. © 2024 IEEE.

## 04 — Title Screening

**Title:** Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Heterogeneous Event-driven Scheduling for Blockchain-based Serverless Edge Computing
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
