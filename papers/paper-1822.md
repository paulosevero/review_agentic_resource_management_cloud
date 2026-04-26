---
id: "paper-1822"
title: "ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services"
authors: ["Li, Yiting", "Wang, Desheng", "Zhang, Weizhe", "Chen, Sichao", "Feng, Yuming"]
year: 2025
venue: "Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS"
venue_type: "conference"
doi: "10.1109/ICPADS67057.2025.11323056"
url: "https://www.scopus.com/pages/publications/105032492705?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Cold Start", "LLM inference", "Scalability", "Serverless"]
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

# paper-1822 — ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services

## Metadata

- **Authors:** Li, Yiting and Wang, Desheng and Zhang, Weizhe and Chen, Sichao and Feng, Yuming
- **Year:** 2025
- **Venue:** Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS
- **DOI:** 10.1109/ICPADS67057.2025.11323056
- **URL:** https://www.scopus.com/pages/publications/105032492705?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Cold Start; LLM inference; Scalability; Serverless

### Abstract

Inference of large language models (LLMs) is common in cloud environments. As the elastic resource management capabilities and the flexible pay-as-you-go billing model offered by serverless, LLM inference services are increasingly migrated to serverless platforms. However, the increasing size of LLMs in recent years has introduced a new cold start issue for serverless frameworks, which in turn impacts their scalability under dynamic workloads. To address these issues, we propose ServerlessLego, an elastic serverless computing framework. ServerlessLego partitions LLMs into layers, then groups and deploys them to different instances, and loads these groups in parallel. These instances perform a subscription-based pipeline. To address dynamically request loads, ServerlessLego models the incoming request patterns and the inference time of running requests, providing an SLO-Aware instance scheduling. Experiments show that ServerlessLego reduces the cold start time of serverless frameworks by 58.15 % and improves throughput by 43.39 % compared to the baseline for dynamic workloads. Moreover, ServerlessLego can horizontally schedule instance based on request SLOs and arrival rates. © 2025 IEEE.

## 04 — Title Screening

**Title:** ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ServerlessLego: An Elastic Serverless Framework Assembling Model Building Blocks to Provide SLO-Aware Inference Services
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
