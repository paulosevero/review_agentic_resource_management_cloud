---
id: "paper-2684"
title: "Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers"
authors: ["Liu, Hao", "Hu, Xiaonyu", "Wang, Ran", "Hao, Jie", "Wu, Qiang", "Zhang, Hongke"]
year: 2026
venue: "Digital Communications and Networks"
venue_type: "journal"
doi: "10.1016/j.dcan.2025.11.006"
url: "https://www.scopus.com/pages/publications/105030166188?origin=resultslist"
publisher: "KeAi Communications Co."
pages: "236--251"
keywords: ["Geographically distributed data center", "Green communication", "Large language model", "Multi-agent reinforcement learning", "Task scheduling"]
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
    human_justification: "LLM as workload"

---

# paper-2684 — Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers

## Metadata

- **Authors:** Liu, Hao and Hu, Xiaonyu and Wang, Ran and Hao, Jie and Wu, Qiang and Zhang, Hongke
- **Year:** 2026
- **Venue:** Digital Communications and Networks
- **DOI:** 10.1016/j.dcan.2025.11.006
- **URL:** https://www.scopus.com/pages/publications/105030166188?origin=resultslist
- **Publisher:** KeAi Communications Co.
- **Pages:** 236--251
- **Language:** English
- **Keywords:** Geographically distributed data center; Green communication; Large language model; Multi-agent reinforcement learning; Task scheduling

### Abstract

The explosive proliferation of Large Language Models (LLMs) imposes significant energy and operational burdens on Geographically Distributed Data Centers (GDDCs), thereby demanding an efficient mechanism for LLMs task scheduling. While prior geo-distributed scheduling methods reduce cost and carbon emissions by exploiting regional heterogeneity, they largely overlook model and data reuse opportunities and the uncertainty of LLM execution times. In this paper, we introduce GCOS, to the best of our knowledge, the first green scheduling framework that incorporates a dual-cache system for both data and models, while jointly optimizing task assignment and cache migration. We firstly propose a dual-cache mechanism that decouples model and data caching to enable fine-grained reuse and minimize redundant transmissions. Subsequently, we propose the Multi-Agent Cache-aware Cooperative Scheduling (MACCS) algorithm, which leverages reinforcement learning to optimize task placement with a focus on minimizing both carbon emissions and cost. Additionally, we design a lightweight execution time predictor, DiPTree, to address the high variability in task execution times. Extensive experiments on real-world datasets demonstrate that GCOS reduces overall cost by up to 92.6 % and carbon emissions by 90.3 %, significantly outperforming existing baselines. © 2025 Chongqing University of Posts and Telecommunications.

## 04 — Title Screening

**Title:** Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Green scheduling for LLM workloads with model and data reuse across geo-distributed data centers
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
