---
id: "paper-2827"
title: "iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation"
authors: ["Wang, Puwei", "Liu, Ruiheng", "Huang, Keman", "Du, Xiaoyong"]
year: 2026
venue: "IEEE Transactions on Software Engineering"
venue_type: "journal"
doi: "10.1109/TSE.2026.3656819"
url: "https://www.scopus.com/pages/publications/105028438290?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["GraphQL+", "Inter-Service Data Communication", "LLM-based Multi-Agent System", "Unified Computation"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2827 — iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation

## Metadata

- **Authors:** Wang, Puwei and Liu, Ruiheng and Huang, Keman and Du, Xiaoyong
- **Year:** 2026
- **Venue:** IEEE Transactions on Software Engineering
- **DOI:** 10.1109/TSE.2026.3656819
- **URL:** https://www.scopus.com/pages/publications/105028438290?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** GraphQL+; Inter-Service Data Communication; LLM-based Multi-Agent System; Unified Computation

### Abstract

In data-intensive microservice-based systems, frequent and large-scale inter-service communication poses a critical performance bottleneck, degrading throughput and escalating latency. Existing solutions exhibit notable limitations: microservice merging sacrifices loose coupling and system evolvability; resource-aware scheduling enhances communication efficiency but fails to reduce data volume; dynamic deployment reduces network distances while introducing compute-resource contention; and unnecessary data transfer elimination remains ineffective under massive data loads. Hence, to overcome these challenges, we propose iRUC, an approach for inter-service data communication Reduction via Unified Computation. In particular, we first design GraphQL+, an executable declarative language that extends GraphQL with service-interaction semantics to achieve unified, cross-language modeling of data processing and transmission across microservices. Second, we develop an LLM-based multi-agent system leveraging Claude 4.5 Sonnet and Gemini 2.5 Pro to automatically parse microservice code and synthesize corresponding GraphQL+ models. Third, we implement the unified execution engine for GraphQL+ models, including the database gateway that preserves microservice database autonomy while enabling cross-database queries. This design enables iRUC to perform the unified modeling and execution of data processing and transmission across microservices, thereby significantly reducing inter-service data transfer while maintaining microservice independence. Experimental evaluation on nine GitHub open-source microservice projects deployed on Huawei Cloud demonstrates iRUC’s effectiveness: compared with the unnecessary transfer elimination, dynamic deployment, and serverless computing approaches, iRUC improves throughput by 5.57×, 1.52×, and 1.87×, respectively, while reducing latency to 7.7%, 40.7%, and 37.4% of those approaches. These results show that iRUC achieves significant performance improvements in large-scale data processing scenarios. © 1976-2012 IEEE.

## 04 — Title Screening

**Title:** iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** iRUC: Reducing Inter-Microservice Data Communication in Data-Intensive Systems via Unified Computation
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
