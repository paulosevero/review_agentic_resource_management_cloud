---
id: "paper-1757"
title: "Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning"
authors: ["Lai, Junyu", "Liu, Huashuo", "Xu, Guoyao", "Jiang, Weiwei", "Wang, Xiong", "Jiang, Dingde"]
year: 2025
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2024.3510562"
url: "https://www.scopus.com/pages/publications/85211213580?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "2554--2567"
keywords: ["computation offloading", "edge computing", "hierarchical reinforcement learning", "LEO satellite network", "load balance", "resource allocation"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-1757 — Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning

## Metadata

- **Authors:** Lai, Junyu and Liu, Huashuo and Xu, Guoyao and Jiang, Weiwei and Wang, Xiong and Jiang, Dingde
- **Year:** 2025
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2024.3510562
- **URL:** https://www.scopus.com/pages/publications/85211213580?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 2554--2567
- **Language:** English
- **Keywords:** computation offloading; edge computing; hierarchical reinforcement learning; LEO satellite network; load balance; resource allocation

### Abstract

The integration of edge computing with LEO satellite broadband networks (LSBNs) offers a transformative potential, yet remains underexplored in the optimization of joint computation offloading and resource allocation (JCORA). This problem is compounded by the issues of load imbalance and hybrid action spaces. To tackle them, we firstly propose a multi-level edge computing architecture that leverages the inter-satellite links to enable collaborative offloading among neighboring satellites, thereby enhancing global resource utilization and load balance in LSBNs. Moreover, existing studies demonstrate the benefits of deep reinforcement learning (DRL) for JCORA optimization but struggle with the complexities of hybrid action spaces. To address this, we elaborate a novel hierarchical multi-agent DRL (HMADRL) framework that decomposes the JCORA problem into two-layered subproblems, namely global computation offloading and local resource allocation. This decomposition effectively mitigates the challenge posed by hybrid action spaces. The computation offloading subproblem is formulated as a delayed-reward partially observable Markov decision process, optimized by using multi-agent deep Q-networks specialized in discrete action outputs. Meanwhile, the resource allocation subproblem is addressed through the deep deterministic policy gradient model, adept at handling continuous actions. Extensive experiments validate our approach, demonstrating improvements in delay reduction, outrage rate, and load balancing compared to baselines. © 2015 IEEE.

## 04 — Title Screening

**Title:** Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint Computation Offloading and Resource Allocation for LEO Satellite Networks Using Hierarchical Multi-Agent Reinforcement Learning
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
