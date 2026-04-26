---
id: "paper-920"
title: "Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning"
authors: ["Gao, Zhen", "Yang, Lei", "Dai, Yu"]
year: 2024
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2023.3285950"
url: "https://www.scopus.com/pages/publications/85162722954?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "758--776"
keywords: ["Multiaccess edge computing (MEC)", "multiagent reinforcement learning (MARL)", "recurrent graph neural networks (R-GNNs)", "resources allocation", "task offloading"]
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

# paper-920 — Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning

## Metadata

- **Authors:** Gao, Zhen and Yang, Lei and Dai, Yu
- **Year:** 2024
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2023.3285950
- **URL:** https://www.scopus.com/pages/publications/85162722954?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 758--776
- **Language:** English
- **Keywords:** Multiaccess edge computing (MEC); multiagent reinforcement learning (MARL); recurrent graph neural networks (R-GNNs); resources allocation; task offloading

### Abstract

In multiaccess edge computing (MEC), when many mobile devices (MDs) offload their tasks to an edge server (ES), its resources might become constrained. These tasks may take a long time to complete or even be thrown away. Since the unknown information of both the ESs and other MDs, it is difficult for each MD to determine its offloading policy independently. Furthermore, most offloading methods have poor generalization to new environment since they focus on model architecture with a fixed quantity of MDs and ESs, preventing trained models from transferring to other environments. In this article, we provide a full decentralized offloading scheme based on the curriculum attention-weighted graph recurrent network-based multiagent actor-critic (CAGR-MAAC). First, we build MEC as a shared MD agents-ESs graph and an AGR-based message network is designed to enable each MD aggregate the information of ESs and other MDs and solve the partial observability of MD agents for MEC system. Second, a learnable differentiable encoder network is introduced to construct MD agent's local information encoding. Subsequently, the MD agent converts overall the information regarding the MEC system into a fixed-size embedding via an AGR Network to handle different quantity of MDs and ESs. Finally, we introduce curriculum learning to address the huge complexity of the MEC system and the training difficulties induced by the large amounts of MDs and ESs. Experiments demonstrate that compared with existing algorithms, CAGR-MAAC boosts task completion rates and decreases system costs by 13.01%-15.03% and 16.45%-18.56%, and can quickly adapt to the new environment.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Fast Adaptive Task Offloading and Resource Allocation in Large-Scale MEC Systems via Multiagent Graph Reinforcement Learning
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
