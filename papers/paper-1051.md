---
id: "paper-1051"
title: "SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments"
authors: ["Lin, Liduo", "Pan, Li", "Liu, Shijun"]
year: 2024
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2024.3422828"
url: "https://www.scopus.com/pages/publications/85197553447?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2904--2917"
keywords: ["Heterogeneous cloud environments", "IaaS", "on-demand instance", "spot instance"]
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

# paper-1051 — SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments

## Metadata

- **Authors:** Lin, Liduo and Pan, Li and Liu, Shijun
- **Year:** 2024
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2024.3422828
- **URL:** https://www.scopus.com/pages/publications/85197553447?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2904--2917
- **Language:** English
- **Keywords:** Heterogeneous cloud environments; IaaS; on-demand instance; spot instance

### Abstract

As increasingly complex functions are implemented in applications, directed acyclic graphs (DAGs) are widely used to model the inter-dependencies between individual functions. Cloud-based data processing platforms need to consider the complex topology of DAGs and arbitrary deadlines given by users for job scheduling, leading to an NP-hard decision-making problem. Leveraging spot instances in data processing platforms can achieve significant cost savings, but the unpredictable interruption of spot instances makes the problem of VM scaling and job scheduling more difficult. In this paper, a Reinforcement Learning (RL) based approach called SpotDAG is proposed to solve the auto-scaling problem for jobs modeled as DAGs on a data processing platform where spot instances are introduced. SpotDAG makes cluster scaling and job scheduling decisions at the same time by mapping its output to several meta-policies. This paper introduces the self-attention mechanism for feature extraction to help the intelligent agent learn faster. A mask layer after the output of the proposed RL-based algorithm circumvents illegal actions to ensure that a job is completed by its deadline. Extensive experimental results show that the proposed approach can significantly reduce the cost of instances for data processing platforms while ensuring that jobs are completed in time.  © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.

## 04 — Title Screening

**Title:** SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SpotDAG: An RL-Based Algorithm for DAG Workflow Scheduling in Heterogeneous Cloud Environments
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
