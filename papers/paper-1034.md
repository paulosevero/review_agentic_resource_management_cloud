---
id: "paper-1034"
title: "Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]"
authors: ["Li, Yun", "Zhang, Jianxin", "Yao, Zhixiu", "Xia, Shichao"]
year: 2024
venue: "Scientia Sinica Informationis"
venue_type: "journal"
doi: "10.1360/SSI-2023-0177"
url: "https://www.scopus.com/pages/publications/85196969902?origin=resultslist"
publisher: "Science China Press"
pages: "413--429"
keywords: ["computing offloading", "graph attention network", "mobile edge computing", "multi-agent reinforcement learning", "resource allocation"]
language: "Chinese"
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1034 — Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]

## Metadata

- **Authors:** Li, Yun and Zhang, Jianxin and Yao, Zhixiu and Xia, Shichao
- **Year:** 2024
- **Venue:** Scientia Sinica Informationis
- **DOI:** 10.1360/SSI-2023-0177
- **URL:** https://www.scopus.com/pages/publications/85196969902?origin=resultslist
- **Publisher:** Science China Press
- **Pages:** 413--429
- **Language:** Chinese
- **Keywords:** computing offloading; graph attention network; mobile edge computing; multi-agent reinforcement learning; resource allocation

### Abstract

With the emergence of massive compute-intensive and delay-sensitive tasks, mobile edge computing (MEC) has become an active research field to improve user experience and reduce system energy consumption. However, in densely deployed MEC networks, the complex spatial relations and dynamics of the wireless network state present serious challenges for designing offloading schemes. In this paper, an intelligent collaborative computing offload and resource allocation algorithm is proposed for a multibase station and multiuser MEC network. First, we formulate a joint optimization problem of offloading decision, channel allocation, transmit power allocation, and computation resource allocation to minimize the system energy consumption under delay constraints. Then, because this problem is a mixed integer nonlinear programming problem, we propose a graph attention network -based hybrid-action multiagent reinforcement learning algorithm (Gat-HMARL), where each base station refers to an agent and configures the Gat-HMARL algorithm. Gat-HMARL adopts a graph attention network to capture the potential spatial relations of wireless network states, allowing the base stations to selectively attend to the wireless network state of other base stations to learn better computing offloading and resource allocation strategies. Finally, the simulation results demonstrate that the proposed Gat-HMARL algorithm exhibits a remarkable performance improvement than the benchmark algorithms. © 2024 Science China Press. All rights reserved.

## 04 — Title Screening

**Title:** Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Neighborhood-aware distributed intelligent computing offloading and resource allocation for edge computing; [邻域感知的分布式智能边缘计算卸载和资源分配算法]
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
