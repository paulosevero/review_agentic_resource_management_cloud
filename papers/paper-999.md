---
id: "paper-999"
title: "Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach"
authors: ["Lang, Junyi", "Zheng, Xiaokang", "Sun, Yimeng", "Ding, Zhaohao"]
year: 2024
venue: "2024 IEEE IAS Industrial and Commercial Power System Asia, I and CPS Asia 2024"
venue_type: "conference"
doi: "10.1109/ICPSAsia61913.2024.10761284"
url: "https://www.scopus.com/pages/publications/85214487717?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "748--753"
keywords: ["data locality", "Geo-distributed data centers", "job scheduling", "power consumption", "reinforcement learning"]
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

# paper-999 — Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach

## Metadata

- **Authors:** Lang, Junyi and Zheng, Xiaokang and Sun, Yimeng and Ding, Zhaohao
- **Year:** 2024
- **Venue:** 2024 IEEE IAS Industrial and Commercial Power System Asia, I and CPS Asia 2024
- **DOI:** 10.1109/ICPSAsia61913.2024.10761284
- **URL:** https://www.scopus.com/pages/publications/85214487717?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 748--753
- **Language:** English
- **Keywords:** data locality; Geo-distributed data centers; job scheduling; power consumption; reinforcement learning

### Abstract

With the rapid growth of cloud computing, geo-distributed data centers are becoming more energy-intensive. Given the unique characteristics of computing jobs, they can be executed across data centers in different geographic locations to better utilize lower electricity prices. However, data locality is a crucial factor to be considered in this process, as it is a precondition for the execution of jobs. In this paper, we propose a multi-agent deep reinforcement learning-based job scheduling algorithm that addresses constraints such as data locality and job deadlines to achieve real-time scheduling of jobs and data across data centers to optimize energy costs. First, we formulate the data locality-aware job scheduling problem across geo-distributed data centers as a Partially Observable Markov Decision Process (POMDP). Then, we develop a multi-agent system where agents handle job scheduling and data transfer respectively. The job scheduling agent needs to consider data transfer conditions when taking actions, as the necessary data for job execution must be available before executing. These agents collaborate by sharing the reward function to optimize the scheduling strategy, reducing the overall energy costs of job execution and data transfer. Finally, we conduct numerical experiments to validate the effectiveness of our proposed scheduling method in reducing data center energy costs while maintaining high service quality. © 2024 IEEE.

## 04 — Title Screening

**Title:** Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Online Job Scheduling for Energy Cost Optimization in Geo-Distributed Data Centers Considering Data Locality: A Multi-Agent Reinforcement Learning Approach
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
