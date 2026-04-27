---
id: "paper-2836"
title: "Split Learning Based Cloud-Edge-End Collaborative Model Training in Heterogeneous Networks"
authors: ["Wang, Jian", "Feng, Gang", "Liu, Yi-Jing", "Xu, Xinyi", "Cheng, Lei", "Jiang, Wei", "Qian, Li Ping"]
year: 2026
venue: "IEEE Transactions on Network Science and Engineering"
venue_type: "journal"
doi: "10.1109/TNSE.2025.3597161"
url: "https://www.scopus.com/pages/publications/105012727682?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "1569--1585"
keywords: ["Collaborative fine-tuning", "heterogeneous networks", "large language models", "split learning"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2836 — Split Learning Based Cloud-Edge-End Collaborative Model Training in Heterogeneous Networks

## Metadata

- **Authors:** Wang, Jian and Feng, Gang and Liu, Yi-Jing and Xu, Xinyi and Cheng, Lei and Jiang, Wei and Qian, Li Ping
- **Year:** 2026
- **Venue:** IEEE Transactions on Network Science and Engineering
- **DOI:** 10.1109/TNSE.2025.3597161
- **URL:** https://www.scopus.com/pages/publications/105012727682?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 1569--1585
- **Language:** English
- **Keywords:** Collaborative fine-tuning; heterogeneous networks; large language models; split learning

### Abstract

Large language models (LLMs) demonstrate significant potential for enabling intelligent endogenous networks owing to their amazing intelligence level. LLMs are currently deployed on cloud servers as their vast parameter scales introduce a substantial computational burden to pre-training and inference processes. This deployment paradigm faces severe challenges, including insufficient personalization, high inference latency, and privacy concerns, as an increasing number of mobile users enjoy the LLM services. To enhance the personalization of pre-trained LLMs, exploiting massive local datasets distributed across edge devices to fine-tune LLMs is essential. In this paper, we propose a split learning-based cloud-edge-end collaborative training framework (SCCT) to harness the abundant computational resources of cloud and edge servers while exploiting massive distributed datasets on edge devices for LLM fine-tuning. In SCCT, an LLM with a parameter-efficient fine-tuning module is deployed on the cloud server, while a small-scale language model (SLM) is deployed across each edge device participating in SCCT and its associated edge server in the manner of split learning. SLM and LLM collaborate in a serial manner for training and inference. To optimize the collaboration efficiency, we formulate a mixed integer nonlinear programming problem to minimize the training latency of SCCT, considering the resource heterogeneity of edge devices and network dynamics. To solve this problem, a two-timescale optimization algorithm is proposed to determine the optimal split points on the large timescale and the allocation of communication and computational resources of the edge server on the small timescale. Numerical results demonstrate that the proposed two-timescale optimization algorithm assisted SCCT outperforms the state-of-the-art LLMs deployment and training paradigm in terms of training efficiency and inference performance. © 2013 IEEE.

## 04 — Title Screening

**Title:** Split Learning Based Cloud-Edge-End Collaborative Model Training in Heterogeneous Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Split Learning Based Cloud-Edge-End Collaborative Model Training in Heterogeneous Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Split Learning Based Cloud-Edge-End Collaborative Model Training in Heterogeneous Networks
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
