---
id: "paper-484"
title: "SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management"
authors: ["Qiu, Haoran", "Mao, Weichao", "Patke, Archit", "Wang, Chen", "Franke, Hubertus", "Kalbarczyk, Zbigniew T.", "Ba\u015far, Tamer", "Iyer, Ravishankar K."]
year: 2022
venue: "SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing"
venue_type: "conference"
doi: "10.1145/3542929.3563475"
url: "https://www.scopus.com/pages/publications/85143252231?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "306--322"
keywords: ["multi-agent", "reinforcement learning", "serverless computing"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-484 — SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management

## Metadata

- **Authors:** Qiu, Haoran and Mao, Weichao and Patke, Archit and Wang, Chen and Franke, Hubertus and Kalbarczyk, Zbigniew T. and Başar, Tamer and Iyer, Ravishankar K.
- **Year:** 2022
- **Venue:** SoCC 2022 - Proceedings of the 13th Symposium on Cloud Computing
- **DOI:** 10.1145/3542929.3563475
- **URL:** https://www.scopus.com/pages/publications/85143252231?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 306--322
- **Language:** English
- **Keywords:** multi-agent; reinforcement learning; serverless computing

### Abstract

Serverless Function-as-a-Service (FaaS) offers improved programmability for customers, yet it is not server-"less"and comes at the cost of more complex infrastructure management (e.g., resource provisioning and scheduling) for cloud providers. To maintain service-level objectives (SLOs) and improve resource utilization efficiency, recent research has been focused on applying online learning algorithms such as reinforcement learning (RL) to manage resources. Despite the initial success of applying RL, we first show in this paper that the state-of-the-art single-agent RL algorithm (S-RL) suffers up to 4.8x higher p99 function latency degradation on multi-tenant serverless FaaS platforms compared to isolated environments and is unable to converge during training. We then design and implement a scalable and incremental multi-agent RL framework based on Proximal Policy Optimization (SIMPPO). Our experiments demonstrate that in multi-tenant environments, SIMPPO enables each RL agent to efficiently converge during training and provides online function latency performance comparable to that of S-RL trained in isolation with minor degradation (<9.2%). In addition, SIMPPO reduces the p99 function latency by 4.5x compared to S-RL in multi-tenant cases.  © 2022 ACM.

## 04 — Title Screening

**Title:** SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SIMPPO: A Scalable and Incremental Online Learning Framework for Serverless Resource Management
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
