---
id: "paper-590"
title: "Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing"
authors: ["Gao, Zhen", "Yang, Lei", "Dai, Yu"]
year: 2023
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2022.3228246"
url: "https://www.scopus.com/pages/publications/85144761162?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6818--6835"
keywords: ["Mobile-edge computing (MEC)", "multiagent reinforcement learning (MARL)", "task offloading", "vehicular fog computing (VFC)"]
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

# paper-590 — Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing

## Metadata

- **Authors:** Gao, Zhen and Yang, Lei and Dai, Yu
- **Year:** 2023
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2022.3228246
- **URL:** https://www.scopus.com/pages/publications/85144761162?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6818--6835
- **Language:** English
- **Keywords:** Mobile-edge computing (MEC); multiagent reinforcement learning (MARL); task offloading; vehicular fog computing (VFC)

### Abstract

In vehicular fog computing, task offloading enables mobile vehicles (MVs) to offer ultralow latency services for computation-intensive tasks. Nevertheless, the edge server (ES) may have a high load when a large number of MVs offload their tasks to it, causing many tasks either experience long processing times or being dropped, particularly for latency-sensitive tasks. Moreover, most existing methods are largely limited to training a model from scratch for new environments. This is because they focus more on model structures with fixed input and output sizes, impeding the transfer of trained models across different environments. To solve these problems, we propose a decentralized task offloading method based on transformer and policy decoupling-based multiagent actor-critic (TPDMAAC). We first introduce a transformer-based long sequence forecasting network (TLSFN) for predicting the current and future queuing delay of ESs to solve uncertain load. Second, we redesign the actor-network using transformer-based temporal feature extraction network (TTFEN) and policy decoupling network (PDN). TTFEN can adapt to various input sizes through a transformer that accepts different tokens we build from the raw input. PDN provides a mapping between the transformer-based embedding features and offloading policies utilizing self-attention mechanism to address various output dimensions. Finally, the experiments on two real-world data sets show that TPDMAAC can quickly adapt to a new environment. And compared to existing algorithms, TPDMAAC reduces the system cost by 11.01%-12.03% as well as improves task completion rates by 10.45%-13.56%.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Fast Adaptive Task Offloading and Resource Allocation via Multiagent Reinforcement Learning in Heterogeneous Vehicular Fog Computing
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
