---
id: "paper-2428"
title: "ECMSA: Dual-Agent Learning-Based Edge Caching with Multi-Strategy Adaptation in Dynamic Environments"
authors: ["Zhang, Jiayi", "Wang, Ting", "Yang, Lu", "Shi, Yuanming", "Cai, Haibin"]
year: 2025
venue: "Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS"
venue_type: "conference"
doi: "10.1109/ICPADS67057.2025.11323217"
url: "https://www.scopus.com/pages/publications/105032459436?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Edge Caching", "Edge Computing"]
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
    human_decision: ""
    human_justification: ""

---

# paper-2428 — ECMSA: Dual-Agent Learning-Based Edge Caching with Multi-Strategy Adaptation in Dynamic Environments

## Metadata

- **Authors:** Zhang, Jiayi and Wang, Ting and Yang, Lu and Shi, Yuanming and Cai, Haibin
- **Year:** 2025
- **Venue:** Proceedings of the International Conference on Parallel and Distributed Systems - ICPADS
- **DOI:** 10.1109/ICPADS67057.2025.11323217
- **URL:** https://www.scopus.com/pages/publications/105032459436?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Edge Caching; Edge Computing

### Abstract

With the proliferation of mobile devices and IoT applications, edge caching has become vital for mitigating network congestion and enhancing user Quality of Experience (QoE). However, traditional caching policies, such as Least Frequently Used (LFU), First-In-First-Out (FIFO), and Least Recently Used (LRU), often struggle to perform effectively in highly dynamic and heterogeneous environments, particularly when content sizes vary significantly. Moreover, existing approaches, whether AI-driven or heuristic-based, typically adopt a single caching strategy, which inherently limits their flexibility and adaptability. To address these limitations, we propose ECMSA, a learning-based multi-strategy edge caching algorithm that integrates a reinforcement learning-driven proactive caching strategy with three conventional reactive caching strategies. Specifically, ECMSA operates in two stages: First, it generates four candidate cache lists - three derived from traditional caching policies (LFU, FIFO, LRU) and one produced by our self-attention-enhanced Deep Deterministic Policy Gradient (Atten-Actor DDPG)-based proactive caching strategy. Next, it employs another Atten-Actor DDPG agent to dynamically select the optimal strategy in real time, leveraging current state features. This dual-agent framework enables continuous learning and adaptation of caching decisions, effectively optimizing content placement and update policies in response to evolving user demands. Extensive experiments conducted on both synthetic and real-world datasets demonstrate that ECMSA achieves 15-17% higher cache-hit ratios and 16-22% lower latency than baseline methods under constrained cache capacities and diverse content sizes. Furthermore, ECMSA exhibits strong robustness and generalization ability, allowing it to rapidly adapt to unseen environments. © 2025 IEEE.

## 04 — Title Screening

**Title:** ECMSA: Dual-Agent Learning-Based Edge Caching with Multi-Strategy Adaptation in Dynamic Environments

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** ECMSA: Dual-Agent Learning-Based Edge Caching with Multi-Strategy Adaptation in Dynamic Environments
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** ECMSA: Dual-Agent Learning-Based Edge Caching with Multi-Strategy Adaptation in Dynamic Environments
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
