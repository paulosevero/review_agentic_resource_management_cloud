---
id: "paper-541"
title: "Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers"
authors: ["Zhou, Amelie Chi", "Luo, Juanyun", "Qiu, Ruibo", "Tan, Haobin", "He, Bingsheng", "Mao, Rui"]
year: 2022
venue: "Proceedings - International Conference on Data Engineering"
venue_type: "conference"
doi: "10.1109/ICDE53745.2022.00256"
url: "https://www.scopus.com/pages/publications/85136418941?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "2818--2830"
keywords: ["geo-distributed DCs", "graph partitioning", "reinforcement learning"]
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
    human_decision: ""
    human_justification: ""

---

# paper-541 — Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers

## Metadata

- **Authors:** Zhou, Amelie Chi and Luo, Juanyun and Qiu, Ruibo and Tan, Haobin and He, Bingsheng and Mao, Rui
- **Year:** 2022
- **Venue:** Proceedings - International Conference on Data Engineering
- **DOI:** 10.1109/ICDE53745.2022.00256
- **URL:** https://www.scopus.com/pages/publications/85136418941?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 2818--2830
- **Language:** English
- **Keywords:** geo-distributed DCs; graph partitioning; reinforcement learning

### Abstract

Graph partitioning is an important problem to the performance and cost optimization of graph analytics in geo-distributed environments. Modern hybrid-cut model is expected to obtain better performance and cost optimizations than traditional partitioning models, but can further complicate geo-distributed graph partitioning which is already a challenging problem due to large graph sizes and network heterogeneities of geo-distributed DCs. Existing studies usually adopt heuristic-based methods to achieve fast partitioning for large graphs, which unfortunately sacrifices optimization effectiveness. Further, graph structures of many applications can change at various frequencies. Dynamic partitioning methods usually focus on achieving low latency to quickly adapt to changes, which may again sacrifice partitioning effectiveness. Also, such methods are not aware of the dynamicity of graphs and can over sacrifice effectiveness for unnecessarily low latency. In this paper, we propose RLCut, which uses Reinforcement Learning (RL) to help taming the complexity of the problem. Specifically, RLCut uses multi-agent learning which is more efficient than single agent RL and incorporates a sampling based optimization to adaptively control the training process to satisfy required trade-off between partitioning effectiveness and efficiency according to graph dynamicity. Experiments using real cloud DCs and real-world graphs show that, compared to state-of-the-art static partitioning methods, RLCut improves the performance of geo-distributed graph analytics by 10%-100% with comparable overhead. When users tolerate longer partitioning overhead, we can further improve the performance by up to 43%. With varying graph changing frequencies, RLCut can improve the performance by up to 60% compared to state-of-the-art dynamic partitioning.  © 2022 IEEE.

## 04 — Title Screening

**Title:** Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers

### Machine Screening

- **Final Score:** 0.1666 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=0.5
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Adaptive Partitioning for Large-Scale Graph Analytics in Geo-Distributed Data Centers
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
