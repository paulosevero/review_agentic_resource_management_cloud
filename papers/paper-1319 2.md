---
id: "paper-1319"
title: "Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics"
authors: ["Yue, Xiaofei", "Yang, Song", "Zhu, Liehuang", "Trajanovski, Stojan", "Li, Fan", "Fu, Xiaoming"]
year: 2024
venue: "IEEE/ACM Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TNET.2024.3486788"
url: "https://www.scopus.com/pages/publications/85208668133?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["data analytics", "function placement", "reinforcement learning", "resource allocation", "Serverless computing"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1319 — Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics

## Metadata

- **Authors:** Yue, Xiaofei and Yang, Song and Zhu, Liehuang and Trajanovski, Stojan and Li, Fan and Fu, Xiaoming
- **Year:** 2024
- **Venue:** IEEE/ACM Transactions on Networking
- **DOI:** 10.1109/TNET.2024.3486788
- **URL:** https://www.scopus.com/pages/publications/85208668133?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** data analytics; function placement; reinforcement learning; resource allocation; Serverless computing

### Abstract

With the flourishing of global services, low-latency analytics on large-volume geo-distributed data has been a regular requirement for application decision-making. Serverless computing, with its rapid function start-up and lightweight deployment, provides a compelling way for geo-distributed analytics. However, existing research focuses on elastic resource scaling at the stage granularity, struggling to heterogeneous resource demands across component functions in wide-area settings. The neglect potentially results in the cost inefficiency and Service Level Objective (SLO) violations. In this paper, we advocate for fine-grained function orchestration to exploit wide-area resource elasticity. We thereby present Demeter, a fine-grained function orchestrator that saves job execution costs for geo-distributed serverless analytics while ensuring SLO compliance. By learning from volatile and bursty environments, Demeter jointly makes per-function placement and resource allocation decisions using a well-optimized multi-agent reinforcement learning algorithm with a pruning mechanism. It prevent the irreparable performance loss by function congestion control. Ultimately, we implement Demeter and evaluate it with the realistic workloads. Experimental results reveal that Demeter outperforms the baselines by up to 46.6% on cost, while reducing SLO violation by over 23.7% and bringing it to below 15%.  © 1993-2012 IEEE.

## 04 — Title Screening

**Title:** Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Exploiting Wide-Area Resource Elasticity With Fine-Grained Orchestration for Serverless Analytics
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
