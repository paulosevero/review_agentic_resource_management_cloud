---
id: "paper-2374"
title: "Enhancing LLM QoS Through Cloud-Edge Collaboration: A Diffusion-Based Multi-Agent Reinforcement Learning Approach"
authors: ["Yao, Zhi", "Tang, Zhiqing", "Yang, Wenmian", "Jia, Weijia"]
year: 2025
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2025.3562362"
url: "https://www.scopus.com/pages/publications/105007982160?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1412--1427"
keywords: ["diffusion model", "Edge computing", "multi-agent reinforcement learning", "request scheduling", "vector database"]
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

# paper-2374 — Enhancing LLM QoS Through Cloud-Edge Collaboration: A Diffusion-Based Multi-Agent Reinforcement Learning Approach

## Metadata

- **Authors:** Yao, Zhi and Tang, Zhiqing and Yang, Wenmian and Jia, Weijia
- **Year:** 2025
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2025.3562362
- **URL:** https://www.scopus.com/pages/publications/105007982160?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1412--1427
- **Language:** English
- **Keywords:** diffusion model; Edge computing; multi-agent reinforcement learning; request scheduling; vector database

### Abstract

Large Language Models (LLMs) are widely used across various domains, but deploying them in cloud data centers often leads to significant response delays and high costs, undermining Quality of Service (QoS) at the network edge. Although caching LLM request results at the edge using vector databases can greatly reduce response times and costs for similar requests, this approach has been overlooked in prior research. To address this, we propose a novel Vector database-assisted cloud-Edge collaborative LLM QoS Optimization (VELO) framework that caches LLM request results at the edge using vector databases, thereby reducing response times for subsequent similar requests. Unlike methods that modify LLMs directly, VELO leaves the LLM's internal structure intact and is applicable to various LLMs. Building on VELO, we formulate the QoS optimization problem as a Markov Decision Process (MDP) and design an algorithm based on Multi-Agent Reinforcement Learning (MARL). Our algorithm employs a diffusion-based policy network to extract the LLM request features, determining whether to request the LLM in the cloud or retrieve results from the edge's vector database. Implemented in a real edge system, our experimental results demonstrate that VELO significantly enhances user satisfaction by simultaneously reducing delays and resource consumption for edge users of LLMs. Our DLRS algorithm improves performance by 15.0% on average for similar requests and by 14.6% for new requests compared to the baselines. © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** Enhancing LLM QoS Through Cloud-Edge Collaboration: A Diffusion-Based Multi-Agent Reinforcement Learning Approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Enhancing LLM QoS Through Cloud-Edge Collaboration: A Diffusion-Based Multi-Agent Reinforcement Learning Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Enhancing LLM QoS Through Cloud-Edge Collaboration: A Diffusion-Based Multi-Agent Reinforcement Learning Approach
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
