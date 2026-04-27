---
id: "paper-577"
title: "Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning"
authors: ["Danino, Tom", "Ben-Shimol, Yehuda", "Greenberg, Shlomo"]
year: 2023
venue: "Electronics (Switzerland)"
venue_type: "journal"
doi: "10.3390/electronics12122614"
url: "https://www.scopus.com/pages/publications/85163810011?origin=resultslist"
publisher: "MDPI"
pages: ""
keywords: ["actor\u2013critic", "cloud computing", "Deep-RL", "Kubernetes", "multi-agent"]
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

# paper-577 — Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning

## Metadata

- **Authors:** Danino, Tom and Ben-Shimol, Yehuda and Greenberg, Shlomo
- **Year:** 2023
- **Venue:** Electronics (Switzerland)
- **DOI:** 10.3390/electronics12122614
- **URL:** https://www.scopus.com/pages/publications/85163810011?origin=resultslist
- **Publisher:** MDPI
- **Pages:** 
- **Language:** English
- **Keywords:** actor–critic; cloud computing; Deep-RL; Kubernetes; multi-agent

### Abstract

Nowadays, many computation tasks are carried out using cloud computing services and virtualization technology. The intensive resource requirements of virtual machines have led to the adoption of a lighter solution based on containers. Containers isolate packaged applications and their dependencies, and they can also operate as part of distributed applications. Containers can be distributed over a cluster of computers with available resources, such as the CPU, memory, and communication bandwidth. Any container distribution mechanism should consider resource availability and their impact on overall performance. This work suggests a new approach to assigning containers to servers in the cloud, while meeting computing and communication resource requirements and minimizing the overall task completion time. We introduce a multi-agent environment using a deep reinforcement learning-based decision mechanism. The high action space complexity is tackled by decentralizing the allocation decisions among multiple agents. Considering the interactions among the agents, we introduce a new cooperative mechanism for a state and reward design, resulting in efficient container assignments. The performances of both long short term memory (LSTM) and memory augmented-based agents are examined, for solving the challenging container assignment problem. Experimental results demonstrated an improvement of up to 28% in the execution runtime compared to existing bin-packing heuristics and the common Kubernetes industrial tool. © 2023 by the authors.

## 04 — Title Screening

**Title:** Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Container Allocation in Cloud Environment Using Multi-Agent Deep Reinforcement Learning
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
