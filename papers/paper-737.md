---
id: "paper-737"
title: "GMA: Graph Multi-agent Microservice Autoscaling Algorithm in Edge-Cloud Environment"
authors: ["Tong, Ganghao", "Meng, Chunyang", "Song, Shijie", "Pan, Maolin", "Yu, Yang"]
year: 2023
venue: "Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023"
venue_type: "conference"
doi: "10.1109/ICWS60048.2023.00058"
url: "https://www.scopus.com/pages/publications/85173838267?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "393--404"
keywords: ["Edge-cloud environment", "Graph convolutional networks", "Microservice autoscaling", "Multi-agent reinforecment learning", "Server collaboration"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-737 — GMA: Graph Multi-agent Microservice Autoscaling Algorithm in Edge-Cloud Environment

## Metadata

- **Authors:** Tong, Ganghao and Meng, Chunyang and Song, Shijie and Pan, Maolin and Yu, Yang
- **Year:** 2023
- **Venue:** Proceedings - 2023 IEEE International Conference on Web Services, ICWS 2023
- **DOI:** 10.1109/ICWS60048.2023.00058
- **URL:** https://www.scopus.com/pages/publications/85173838267?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 393--404
- **Language:** English
- **Keywords:** Edge-cloud environment; Graph convolutional networks; Microservice autoscaling; Multi-agent reinforecment learning; Server collaboration

### Abstract

The emerging edge-cloud computing paradigm, comprising cloud centers and multiple distributed edge servers, extends the computing capability from the cloud center to a range of servers. Although the microservice autoscaling problem has been intensively studied in the context of cloud computing, existing algorithms in most cases cannot be effectively migrated to the edge-cloud environment because servers are geographically distributed and heterogeneous, and information is not synchronized between servers. Existing works, however, mainly focus on centralized strategies with time-consuming synchronization methods, i.e. strategies shared by all servers, without comprehensively considering the heterogeneity and distribution of the environment. Soft information synchronization, autonomy and collaboration is proposed to tackle the aforementioned issues, and refer to it as SAC paradigm. According to the SAC paradigm, each server with inferred information of other servers can collaborate with others by a dedicated autoscaling strategy, that is, server collaboration. The microservice autoscaling problem is then transformed into the Graph-based Jointly Microservice Autoscaling (GJMA) problem based on spectral graph theory. GJMA problem aims to minimize average waiting time of microservice-based application while reducing service-level agreement(SLA) violation rate and fluctuations in the autoscaling process, taking into account resource heterogeneity. Graph-based Multi-agent Algorithm(GMA), an implementation of SAC paradigm based on graph convolutional networks and multi-agent reinforcement learning, is implemented to solve GJMA problem. Experimental results show that the proposed algorithm for the edge-cloud environment is always efficient to find a better autoscaling strategy compared to the implemented comparison algorithms. © 2023 IEEE.

## 04 — Title Screening

**Title:** GMA: Graph Multi-agent Microservice Autoscaling Algorithm in Edge-Cloud Environment

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** GMA: Graph Multi-agent Microservice Autoscaling Algorithm in Edge-Cloud Environment
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** GMA: Graph Multi-agent Microservice Autoscaling Algorithm in Edge-Cloud Environment
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
