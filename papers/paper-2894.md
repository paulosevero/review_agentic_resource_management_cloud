---
id: "paper-2894"
title: "AWTO: A latency-optimized task offloading scheme for LLM-driven agentic workflows on heterogeneous edge"
authors: ["Yu, Peng", "Liu, Bo", "Tang, Shaomin", "Li, Dongdong", "Lin, Weiwei"]
year: 2026
venue: "Future Generation Computer Systems"
venue_type: "journal"
doi: "10.1016/j.future.2026.108415"
url: "https://www.scopus.com/pages/publications/105030625983?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Agentic workflow", "Deep reinforcement learning", "Edge computing", "Large language model", "Task offloading"]
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
    human_justification: "LLM as workload"

---

# paper-2894 — AWTO: A latency-optimized task offloading scheme for LLM-driven agentic workflows on heterogeneous edge

## Metadata

- **Authors:** Yu, Peng and Liu, Bo and Tang, Shaomin and Li, Dongdong and Lin, Weiwei
- **Year:** 2026
- **Venue:** Future Generation Computer Systems
- **DOI:** 10.1016/j.future.2026.108415
- **URL:** https://www.scopus.com/pages/publications/105030625983?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Agentic workflow; Deep reinforcement learning; Edge computing; Large language model; Task offloading

### Abstract

Agentic workflows, driven by Large Language Models (LLMs), present new opportunities for realizing advanced edge intelligence in data-sensitive domains such as finance and healthcare. However, deploying these workflows in private, resource-constrained edge environments poses unique challenges. Unlike public cloud services, these scenarios require computations to be performed locally on dedicated edge clusters to meet strict data compliance and privacy regulations. This restriction, coupled with the limited memory capacity of edge devices relative to the massive size of LLMs, makes dynamic memory management and model loading critical factors. Furthermore, the autoregressive nature of LLMs introduces high dynamic uncertainty in inference latency and memory footprint, fundamentally contradicting the static information assumptions of traditional scheduling methods. To address these challenges, we propose AWTO, a Deep Reinforcement Learning (DRL) offloading scheme designed to minimize the makespan of agentic workflows in isolated edge environments. The core of AWTO is a task-by-task dynamic decision-making mechanism that explicitly handles on-demand model loading and memory contention. We formulate this problem as a Markov Decision Process (MDP) and employ a Proximal Policy Optimization (PPO)-based algorithm. A novel three-module LSTM encoder is designed to capture task dependencies, device heterogeneity, and real-time memory states. Experimental results in heterogeneous environments demonstrate that AWTO reduces the average makespan by 16.99% to 36.36% compared to heuristic baselines. Furthermore, it achieves a 14.00% gain over DRL methods, validating its adaptability to dynamic memory constraints and cache-aware scheduling. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

## 04 — Title Screening

**Title:** AWTO: A latency-optimized task offloading scheme for LLM-driven agentic workflows on heterogeneous edge

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** AWTO: A latency-optimized task offloading scheme for LLM-driven agentic workflows on heterogeneous edge
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** AWTO: A latency-optimized task offloading scheme for LLM-driven agentic workflows on heterogeneous edge
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
