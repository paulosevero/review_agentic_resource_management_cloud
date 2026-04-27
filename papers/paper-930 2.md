---
id: "paper-930"
title: "Deploying Stateful Network Functions Efficiently using Large Language Models"
authors: ["Ghasemirahni, Hamid", "Farshin, Alireza", "Scazzariello, Mariano", "Chiesa, Marco", "Kosti\u0107, Dejan"]
year: 2024
venue: "EuroMLSys 2024 - Proceedings of the 2024 4th Workshop on Machine Learning and Systems"
venue_type: "conference"
doi: "10.1145/3642970.3655836"
url: "https://www.scopus.com/pages/publications/85192276579?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "28--38"
keywords: ["Intra-Server Load Balancing", "LLMs", "RSS Configuration", "Stateful Network Functions", "Static Code Analysis"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-930 — Deploying Stateful Network Functions Efficiently using Large Language Models

## Metadata

- **Authors:** Ghasemirahni, Hamid and Farshin, Alireza and Scazzariello, Mariano and Chiesa, Marco and Kostić, Dejan
- **Year:** 2024
- **Venue:** EuroMLSys 2024 - Proceedings of the 2024 4th Workshop on Machine Learning and Systems
- **DOI:** 10.1145/3642970.3655836
- **URL:** https://www.scopus.com/pages/publications/85192276579?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 28--38
- **Language:** English
- **Keywords:** Intra-Server Load Balancing; LLMs; RSS Configuration; Stateful Network Functions; Static Code Analysis

### Abstract

Stateful network functions are increasingly used in data centers. However, their scalability remains a significant challenge since parallelizing packet processing across multiple cores requires careful configuration t o avoid compromising the application’s semantics or performance. This challenge is particularly important when deploying multiple stateful functions on multi-core servers. This paper proposes FlowMage, a system that leverages Large Language Models (LLMs) to perform code analysis and extract essential information from stateful network functions (NFs) prior to their deployment on a server. FlowMage uses this data to find an efficient configuration of an NF chain that maximizes performance while preserving the semantics of the NF chain. Our evaluation shows that, utilizing GPT-4, FlowMage is able to find and apply optimized configuration when deploying stateful NFs chain on a server, resulting in significant p erformance i mprovement (up t o 1 1×) in comparison to the default configuration of the system. © 2024 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** Deploying Stateful Network Functions Efficiently using Large Language Models

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deploying Stateful Network Functions Efficiently using Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deploying Stateful Network Functions Efficiently using Large Language Models
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
