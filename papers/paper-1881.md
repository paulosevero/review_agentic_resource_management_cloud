---
id: "paper-1881"
title: "Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning"
authors: ["Liu, Qi", "Yang, Jianzheng", "Yan, Zhixian"]
year: 2025
venue: "Knowledge and Information Systems"
venue_type: "journal"
doi: "10.1007/s10115-025-02507-1"
url: "https://www.scopus.com/pages/publications/105008824769?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "9363--9383"
keywords: ["Edge computing", "Multi-agent", "Quality of service", "Reinforcement learning", "Resource orchestration"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1881 — Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning

## Metadata

- **Authors:** Liu, Qi and Yang, Jianzheng and Yan, Zhixian
- **Year:** 2025
- **Venue:** Knowledge and Information Systems
- **DOI:** 10.1007/s10115-025-02507-1
- **URL:** https://www.scopus.com/pages/publications/105008824769?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 9363--9383
- **Language:** English
- **Keywords:** Edge computing; Multi-agent; Quality of service; Reinforcement learning; Resource orchestration

### Abstract

This paper presents a dynamic resource orchestration framework for edge computing environments, utilizing multi-agent reinforcement learning (MARL) to enhance resource allocation and task scheduling. The proposed system consists of edge nodes (E), a centralized resource manager (CRM), and communication infrastructure (CI). Edge nodes execute computational tasks at the network’s periphery, while the CRM oversees resource distribution and task assignment using a global system perspective. The CI supports efficient communication among these components. The MARL framework enables collaborative learning among agents, where each agent selects optimal actions—such as resource allocation, task scheduling, and migration—based on system states that include resource availability, task queue lengths, network conditions, and task priorities. A deep Q-network (DQN)-based training approach is employed, allowing agents to maximize cumulative rewards by balancing task completion efficiency, resource utilization, and latency minimization. The proposed framework is evaluated through comprehensive simulations against traditional heuristic-based and static resource allocation methods. Results demonstrate that our MARL-based approach reduces average task completion latency by 12.3% and improves resource utilization by 8.7% compared to heuristic baselines. Additionally, the framework dynamically adapts to variations in network conditions and workload distribution, ensuring consistent quality of service (QoS) under dynamic edge computing scenarios. © The Author(s), under exclusive licence to Springer-Verlag London Ltd., part of Springer Nature 2025.

## 04 — Title Screening

**Title:** Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Dynamic resource orchestration in edge computing environments using multi-agent reinforcement learning
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
