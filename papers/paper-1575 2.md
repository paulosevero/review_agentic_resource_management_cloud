---
id: "paper-1575"
title: "GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training"
authors: ["Gan, Xinbiao", "Li, Tiejun", "Wu, Liang", "Zhang, Qiang", "Song, Lingyun", "Yang, Bo", "Liu, Jie", "Lu, Kai"]
year: 2025
venue: "WWW 2025 - Proceedings of the ACM Web Conference"
venue_type: "conference"
doi: "10.1145/3696410.3714741"
url: "https://www.scopus.com/pages/publications/105005139119?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "786--795"
keywords: ["graph model", "graph processing", "Graph500", "message aggregation", "supercomputers"]
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

# paper-1575 — GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training

## Metadata

- **Authors:** Gan, Xinbiao and Li, Tiejun and Wu, Liang and Zhang, Qiang and Song, Lingyun and Yang, Bo and Liu, Jie and Lu, Kai
- **Year:** 2025
- **Venue:** WWW 2025 - Proceedings of the ACM Web Conference
- **DOI:** 10.1145/3696410.3714741
- **URL:** https://www.scopus.com/pages/publications/105005139119?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 786--795
- **Language:** English
- **Keywords:** graph model; graph processing; Graph500; message aggregation; supercomputers

### Abstract

Efficient processing of large-scale graphs with billions to trillions of edges is essential for training graph-based large language models (LLMs) in web-scale systems. The increasing complexity and size of these models create significant communication challenges due to the extensive message exchanges required across distributed nodes. Current graph engines struggle to effectively scale across hundreds of computing nodes because they often overlook variations in communication costs within the interconnection hierarchy. This paper presents GraphCom, a communication-efficient message graph engine for graph processing on supercomputers. Our key idea is to leverage the network topology information to perform communication hierarchy-aware message aggregation, where messages are (i) gathered to the responsible nodes (referred to as monitors) in the source domains, (ii) transferred between monitors, and (iii) scattered to the target nodes in the target domains. GraphCom’s aggregation is more aggressive in that each source domain (instead of the source node). We have implemented GraphCom on top of MPI. We demonstrate GraphCom’s effectiveness with synthetic benchmarks and real-world graphs, utilizing up to 79,024 nodes and over 1.2 million processor cores, demonstrating that GraphCom surpasses leading graph-parallel systems and state-of-the-art counterparts in both throughput and scalability. Moreover, we have deployed GraphCom on a production supercomputer, where it consistently outperforms the top solutions on the Graph500 list. These results highlight the potential GraphCom has to significantly improve the efficiency of distributed large-scale graph-based LLM training by optimizing communication between distributed systems, making it an invaluable graph engine for distributed training tasks on web-scale graphs. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** GraphCom: Communication Hierarchy-aware Graph Engine for Distributed Model Training
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
