---
id: "paper-2196"
title: "Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers"
authors: ["Tan, Haobin", "Xiao, Yao", "Zhou, Amelie Chi", "Lu, Kezhong", "Yang, Xuan"]
year: 2025
venue: "IEEE Transactions on Parallel and Distributed Systems"
venue_type: "journal"
doi: "10.1109/TPDS.2025.3557610"
url: "https://www.scopus.com/pages/publications/105003272052?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1161--1174"
keywords: ["geo-distributed data centers", "Graph partitioning", "reinforcement learning"]
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
    final_score: 0.1666
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2196 — Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers

## Metadata

- **Authors:** Tan, Haobin and Xiao, Yao and Zhou, Amelie Chi and Lu, Kezhong and Yang, Xuan
- **Year:** 2025
- **Venue:** IEEE Transactions on Parallel and Distributed Systems
- **DOI:** 10.1109/TPDS.2025.3557610
- **URL:** https://www.scopus.com/pages/publications/105003272052?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1161--1174
- **Language:** English
- **Keywords:** geo-distributed data centers; Graph partitioning; reinforcement learning

### Abstract

Graph partitioning is of great importance to optimizing the performance and cost of geo-distributed graph analytics applications. However, it is non-trivial to obtain efficient and effective partitioning due to the challenges brought by the large graph scales, dynamic graph changes and the network heterogeneity in geo-distributed data centers (DCs). Existing studies usually adopt heuristic-based methods to achieve fast and balanced partitioning for large graphs, which are not powerful enough to address the complexity in our problem. Further, graph structures of many applications can change at various frequencies. Dynamic partitioning methods usually focus on achieving low latency to quickly adapt to changes, which unfortunately sacrifices partitioning effectiveness. Also, such methods are not aware of the dynamicity of graphs and can over sacrifice effectiveness for unnecessarily low latency. To address the limitations of existing studies, we propose DistRLCut, a novel graph partitioner which leverages Multi-Agent Reinforcement Learning (MARL) to solve the complexity of the partitioning problem. To achieve fast partitioning for large graphs, DistRLCut adapts MARL to a distributed implementation which significantly accelerates the learning process. Further, DistRLCut incorporates two techniques to trade-off between partitioning effectiveness and efficiency, including local training and agent sampling. By adaptively tuning the number of local training iterations and the agent sampling rate, DistRLCut is able to achieve good partitioning results within an overhead constraint required by graph dynamicity. Experiments using real cloud DCs and real-world graphs show that, compared to state-of-the-art static partitioning methods, DistRLCut improves the performance of geo-distributed graph analytics by 11%-95%. DistRLCut can partition over 28 million edges per second, showcasing its scalability for large graphs. With varying graph changing frequencies, DistRLCut can improve the performance by up to 71% compared to state-of-the-art dynamic partitioning. © 1990-2012 IEEE.

## 04 — Title Screening

**Title:** Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.5
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Distributed and Adaptive Partitioning for Large Graphs in Geo-Distributed Data Centers
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
