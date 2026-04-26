---
id: "paper-1268"
title: "Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters"
authors: ["Wei, Xile", "Wei, Hengyi", "Lu, Meili", "Zhang, Zhen", "Chang, Siyuan", "Zeng, Shunqi", "Wang, Fei", "Chen, Minghui"]
year: 2024
venue: "IEEE Transactions on Industrial Informatics"
venue_type: "journal"
doi: "10.1109/TII.2024.3423330"
url: "https://www.scopus.com/pages/publications/85208709928?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "12575--12585"
keywords: ["Distributed computing", "embedded system", "large language model (LLM)", "message passing interface (MPI)", "neural networks"]
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
    human_decision: ""
    human_justification: ""

---

# paper-1268 — Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters

## Metadata

- **Authors:** Wei, Xile and Wei, Hengyi and Lu, Meili and Zhang, Zhen and Chang, Siyuan and Zeng, Shunqi and Wang, Fei and Chen, Minghui
- **Year:** 2024
- **Venue:** IEEE Transactions on Industrial Informatics
- **DOI:** 10.1109/TII.2024.3423330
- **URL:** https://www.scopus.com/pages/publications/85208709928?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 12575--12585
- **Language:** English
- **Keywords:** Distributed computing; embedded system; large language model (LLM); message passing interface (MPI); neural networks

### Abstract

Distributed architecture is expected to be an effective solution for large-scale edge computing tasks in terminal devices. However, it remains a great challenge to resolve the conflict between parallel efficiency and constrained physical resources in a specific embedded structure. This article proposes a universal scalable off-chip parallel computing architecture to maximize the computing efficiency for distributed embedded computing clusters. This architecture is based on an improved Message Passing Interface (Improved-MPI). To address the limited communication speed in embedded environments, a multilevel communication mechanism is employed to alleviate the communication pressure on nodes. By flexibly allocating computing tasks, efficient utilization of every embedded cluster node is ensured, while also solving the problem of single point of failure. In addition, to overcome the challenge of limited RAM in embedded devices, the architecture utilizes the interleaved memory initialization mechanism to run larger computing tasks. Based on this architecture, a specific embedded cluster platform is constructed using the RK3399 board. Various large-scale tasks are deployed on this platform to validate the performance of the architecture. First, a large-scale randomly connected neural network is executed, which serves to verify the architecture's outstanding computational performance and communication capability. Secondly, a functional model of Small-World Spiking Neural Network is constructed, achieving real-time and efficient digital speech recognition. Finally, the implementation of Large Language Models demonstrates that the embedded clusters can achieve performance comparable to modern computers.  © 2005-2012 IEEE.

## 04 — Title Screening

**Title:** Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Large-Scale Parallel Embedded Computing With Improved-MPI in Off-Chip Distributed Clusters
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
