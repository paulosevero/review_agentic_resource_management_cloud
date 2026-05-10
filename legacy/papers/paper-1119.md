---
id: "paper-1119"
title: "Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-Distributed Cloud"
authors: ["Park, Jeonghyeon", "Kim, Daero", "Kim, Jiseon", "Han, Jungkyu", "Chun, Sejin"]
year: 2024
venue: "IEEE International Conference on Cloud Computing, CLOUD"
venue_type: "conference"
doi: "10.1109/CLOUD62652.2024.00062"
url: "https://www.scopus.com/pages/publications/85203258078?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "494--501"
keywords: ["carbon-aware", "deep learning", "fault-tolerant", "geo-distributed cloud", "task migration"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-1119 — Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-Distributed Cloud

## Metadata

- **Authors:** Park, Jeonghyeon and Kim, Daero and Kim, Jiseon and Han, Jungkyu and Chun, Sejin
- **Year:** 2024
- **Venue:** IEEE International Conference on Cloud Computing, CLOUD
- **DOI:** 10.1109/CLOUD62652.2024.00062
- **URL:** https://www.scopus.com/pages/publications/85203258078?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 494--501
- **Language:** English
- **Keywords:** carbon-aware; deep learning; fault-tolerant; geo-distributed cloud; task migration

### Abstract

Recently, many deep learning models have been trained in geographically distributed data centers. The carbon emissions produced by training the models may pose a significant threat to climate change like increasing temperatures. Existing studies have a hardship in shifting the workload of training models to a data center with low carbon emissions. So, they fail to ensure low emissions of the workload during training, especially when long-term workloads like Large Language Models (LLMs) are trained. To cope with this problem, we propose a method that shifts the workload to a cloud with low carbon emissions while enduring a lack of computational resources. Specifically, we define a task scheduler that includes states and their transitions to migrate mini-batches dynamically. Next, we present a fault-tolerant control that optimizes a GPU frequency to adapt to workload variations of training models while guaranteeing its power consumption. Last, we conducted exhaustive experiments using real-world data in terms of carbon emissions, transfer time, and power consumption compared to state-of-the-art methods.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-Distributed Cloud

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-Distributed Cloud
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Carbon-Aware and Fault-Tolerant Migration of Deep Learning Workloads in the Geo-Distributed Cloud
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
