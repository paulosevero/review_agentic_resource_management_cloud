---
id: "paper-2896"
title: "Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach"
authors: ["Yu, Zihang", "Zhang, Zhenjiang", "Zeadally, Sherali"]
year: 2026
venue: "Journal of Industrial Information Integration"
venue_type: "journal"
doi: "10.1016/j.jii.2025.101037"
url: "https://www.scopus.com/pages/publications/105024310480?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Edge computing", "Industrial Internet of Things", "Lyapunov optimization", "Reinforcement learning"]
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
    human_justification: "RL"

---

# paper-2896 — Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach

## Metadata

- **Authors:** Yu, Zihang and Zhang, Zhenjiang and Zeadally, Sherali
- **Year:** 2026
- **Venue:** Journal of Industrial Information Integration
- **DOI:** 10.1016/j.jii.2025.101037
- **URL:** https://www.scopus.com/pages/publications/105024310480?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Industrial Internet of Things; Lyapunov optimization; Reinforcement learning

### Abstract

Multi-access Edge Computing (MEC) integrated with the Industrial Internet of Things (IIoT) is vital for intelligent manufacturing and industrial automation because it enables low-latency and high-efficiency task offloading from resource-limited devices to an edge server. However, dynamic wireless channels and stochastic task arrivals introduce significant uncertainties, leading to queuing delays, inefficient resource utilization, and high energy consumption. Moreover, the lack of future system information makes real-time offloading decisions particularly challenging. To address these issues, we construct both task queues and delay-aware virtual queues, and we formulate a stochastic optimization problem for joint task offloading and resource allocation. The objective is to minimize long-term energy consumption while ensuring queue stability and satisfying task deadline constraints. To solve this problem, we propose a novel Lyapunov-guided multi-agent deep reinforcement learning framework (LYMADDPG), which integrates Lyapunov optimization with Multi-Agent Deep Deterministic Policy Gradient (MADDPG). Specifically, we use Lyapunov optimization to transform delay constraints into a virtual queue stability control problem, converting the original long-term problem into a series of per-slot optimizations. Next, we use MADDPG to learn optimal offloading and resource allocation policies in a distributed and adaptive manner. Extensive simulation results demonstrate that our method significantly outperforms baseline algorithms in reducing energy consumption, ensuring queue stability, and meeting task deadlines. These results confirm the practical effectiveness of our approach and highlight its strong potential for real-world deployment in MEC-enabled IIoT systems. © 2025 Elsevier Inc.

## 04 — Title Screening

**Title:** Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Energy-efficient task offloading in the Industrial Internet of Things: A Lyapunov-guided multi-agent deep reinforcement learning approach
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
