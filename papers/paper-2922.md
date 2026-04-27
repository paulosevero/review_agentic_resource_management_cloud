---
id: "paper-2922"
title: "Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks"
authors: ["Zhang, Guanlei", "Zhang, Qiyang", "Feng, Lei", "Zhou, Fanqin", "Donta, Praveen Kumar", "Dustdar, Schahram"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3650680"
url: "https://www.scopus.com/pages/publications/105027279751?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Deep Reinforcement Learning", "Distributed Inference", "Mobile Edge Computing", "Model Partitioning", "Resource Allocation"]
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
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI (usa somente IA, RL, etc.)"

---

# paper-2922 — Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks

## Metadata

- **Authors:** Zhang, Guanlei and Zhang, Qiyang and Feng, Lei and Zhou, Fanqin and Donta, Praveen Kumar and Dustdar, Schahram
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3650680
- **URL:** https://www.scopus.com/pages/publications/105027279751?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Deep Reinforcement Learning; Distributed Inference; Mobile Edge Computing; Model Partitioning; Resource Allocation

### Abstract

Mobile devices (MDs) are increasingly incorporating deep neural network (DNN) inference into their systems due to the rapid growth of intelligent applications. Mobile edge computing-based distributed DNN collaborative inference has gained popularity due to limited on-device computation and energy budgets. However, the resource competition among MDs, along with the coupling of collaborative inference tasks across MDs and servers, creates significant challenges for efficient resource management. This issue is further exacerbated by the complexity of directed acyclic graph (DAG)-structured DNNs. Most prior studies do not jointly address the dual challenges of partitioning complex-structured DNNs and leveraging advanced optimization for collaborative inference, and their resilience to channel condition fluctuations remains underexplored. To address these challenges, we propose a novel task-aware collaborative inference framework. First, we devise a fine-grained partitioning point search algorithm based on a bidirectional graph linked list, which enables one-dimensional and flexible partitioning of DAG-structured DNNs. We then reformulate the problem of minimizing collaborative inference energy consumption and latency as a task-aware Markov decision process (MDP), which partitions each user's inference task queue into consecutive task windows for resource allocation. Building on this, we propose an Embedded Multi-Agent Hybrid Proximal Policy Optimization (EMH-PPO) algorithm to learn effective policies. Extensive experiments conducted across diverse network scenarios reveal that, compared to local DNN inference on MDs, our proposed method reduces inference latency by up to 64% and energy consumption by up to 46%. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Task-Aware Collaborative Inference and Fine-Grained DNN Partitioning in MEC Networks
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
