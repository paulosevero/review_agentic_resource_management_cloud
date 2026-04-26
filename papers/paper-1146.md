---
id: "paper-1146"
title: "TrimCaching: Parameter-Sharing AI Model Caching in Wireless Edge Networks"
authors: ["Qu, Guanqiao", "Lin, Zheng", "Liu, Fangming", "Chen, Xianhao", "Huang, Kaibin"]
year: 2024
venue: "Proceedings - International Conference on Distributed Computing Systems"
venue_type: "conference"
doi: "10.1109/ICDCS60910.2024.00013"
url: "https://www.scopus.com/pages/publications/85199930803?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "36--46"
keywords: ["6G", "Edge AI model caching", "edge computing", "edge intelligence", "model downloading"]
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

# paper-1146 — TrimCaching: Parameter-Sharing AI Model Caching in Wireless Edge Networks

## Metadata

- **Authors:** Qu, Guanqiao and Lin, Zheng and Liu, Fangming and Chen, Xianhao and Huang, Kaibin
- **Year:** 2024
- **Venue:** Proceedings - International Conference on Distributed Computing Systems
- **DOI:** 10.1109/ICDCS60910.2024.00013
- **URL:** https://www.scopus.com/pages/publications/85199930803?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 36--46
- **Language:** English
- **Keywords:** 6G; Edge AI model caching; edge computing; edge intelligence; model downloading

### Abstract

Next-generation mobile networks are expected to facilitate fast AI model downloading to end users. By caching models on edge servers, mobile networks can deliver models to end users with low latency, resulting in a paradigm called edge model caching. In this paper, we develop a novel model placement scheme, called parameter-sharing model caching (TrimCaching). TrimCaching exploits the key observation that a wide range of AI models, such as convolutional neural networks or large language models, can share a significant proportion of parameter blocks containing reusable knowledge, thereby improving storage efficiency. To this end, we formulate a parameter-sharing model placement problem to maximize the cache hit ratio in multi-edge wireless networks by balancing the fundamental tradeoff between storage efficiency and service latency. We show that the formulated problem is a submodular maximization problem with submodular constraints, for which no polynomial-time approximation algorithm exists. To overcome this challenge, we study an important special case, where a small fixed number of parameter blocks are shared across models, which often holds in practice. In such a case, a polynomial-time algorithm with (1 - E) /2-approximation guarantee is developed. Subsequently, we address the original problem for the general case by developing a greedy algorithm. Simulation results demonstrate that the proposed TrimCaching framework significantly improves the cache hit ratio compared with state-of-the-art content caching without exploiting shared parameters in AI models.  © 2024 IEEE.

## 04 — Title Screening

**Title:** TrimCaching: Parameter-Sharing AI Model Caching in Wireless Edge Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** TrimCaching: Parameter-Sharing AI Model Caching in Wireless Edge Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** TrimCaching: Parameter-Sharing AI Model Caching in Wireless Edge Networks
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
