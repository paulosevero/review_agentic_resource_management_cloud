---
id: "paper-1840"
title: "Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments"
authors: ["Liang, Yi", "Xu, Guimei", "Wang, Yinzhou", "Ruan, NianYi"]
year: 2025
venue: "ICCCR 2025 - 2025 5th International Conference on Computer, Control and Robotics"
venue_type: "conference"
doi: "10.1109/ICCCR65461.2025.11072649"
url: "https://www.scopus.com/pages/publications/105012139600?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "483--488"
keywords: ["cumulative data processing applications", "multi-agent reinforcement learning", "multi-cloud", "scheduling"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-1840 — Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments

## Metadata

- **Authors:** Liang, Yi and Xu, Guimei and Wang, Yinzhou and Ruan, NianYi
- **Year:** 2025
- **Venue:** ICCCR 2025 - 2025 5th International Conference on Computer, Control and Robotics
- **DOI:** 10.1109/ICCCR65461.2025.11072649
- **URL:** https://www.scopus.com/pages/publications/105012139600?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 483--488
- **Language:** English
- **Keywords:** cumulative data processing applications; multi-agent reinforcement learning; multi-cloud; scheduling

### Abstract

Cumulative Data Processing (CDP) is a typical application in multi-cloud environments, where efficient job scheduling is crucial for achieving high performance and low-cost operation. However, existing multi-cloud job scheduling approaches fail to address the unique characteristics of CDP applications, such as long-term execution, dynamic job generation, and stage-wise differentiated resource demands, as they lack the capability to collaboratively optimize long-term scheduling decisions. To solve this, we propose CDP-MARL, a multi-agent reinforcement learning approach for job scheduling of CDP applications in multi-cloud environments. Built on the Multi-Agent Proximal Policy Optimization (MAPPO) algorithm, CDP-MARL enables autonomous and collaborative decision-making for data center schedulers in distributed multi-cloud environments and employs MAPPO to solve the optimized scheduling strategy. It utilizes the simplified global state representation to reduce the training cost of the Actor and Critic networks in MAPPO. Additionally, a self-attention mechanism is integrated into the Critic network to improve global state representation, while a GRU-based Dynamic Policy Sub-Network (GRU-DPSN) is introduced in the Actor network to address the delayed reward issue in long-term scheduling. Experimental results demonstrate that, compared to state-of-the-art approaches, CDP-MARL reduces the resource cost by 35.97% and the Service Level Agreement (SLA) violation rate by 25.25% on average for CDP applications.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Reinforcement Learning-Based Job Scheduling for Cumulative Data Processing in Multi-Cloud Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
