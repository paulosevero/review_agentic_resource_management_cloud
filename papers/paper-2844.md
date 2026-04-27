---
id: "paper-2844"
title: "HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks"
authors: ["Wen, Jinbo", "Su, Cheng", "Kang, Jiawen", "Nie, Jiangtian", "Zhang, Yang", "Tang, Jianhang", "Niyato, Dusit", "Yuen, Chau"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3637120"
url: "https://www.scopus.com/pages/publications/105023666575?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6547--6562"
keywords: ["deep reinforcement learning", "HybridRAG", "LLMs", "Low-altitude economy", "low-carbon multi-UAV-assisted MEC networks", "regularization diffusion models"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI."

---

# paper-2844 — HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks

## Metadata

- **Authors:** Wen, Jinbo and Su, Cheng and Kang, Jiawen and Nie, Jiangtian and Zhang, Yang and Tang, Jianhang and Niyato, Dusit and Yuen, Chau
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3637120
- **URL:** https://www.scopus.com/pages/publications/105023666575?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6547--6562
- **Language:** English
- **Keywords:** deep reinforcement learning; HybridRAG; LLMs; Low-altitude economy; low-carbon multi-UAV-assisted MEC networks; regularization diffusion models

### Abstract

Low-Altitude Economy Networks (LAENets) are emerging as a promising paradigm to support various low-altitude services through integrated air-ground infrastructure. To satisfy low-latency and high-computation demands, the integration of Unmanned Aerial Vehicles (UAVs) with Mobile Edge Computing (MEC) systems plays a vital role, which offloads computing tasks from terminal devices to nearby UAVs, enabling flexible and resilient service provisions for ground users. To promote the development of LAENets, it is significant to achieve low-carbon multi-UAV-assisted MEC networks. However, several challenges hinder this implementation, including the complexity of multidimensional UAV modeling and the difficulty of multi-objective coupled optimization. To this end, this paper proposes a novel Retrieval Augmented Generation (RAG)-based Large Language Model (LLM) agent framework for model formulation. Specifically, we develop HybridRAG by combining KeywordRAG, VectorRAG, and GraphRAG, empowering LLM agents to efficiently retrieve structural information from expert databases and generate more accurate optimization problems compared with traditional RAG-based LLM agents. After customizing carbon emission optimization problems for multi-UAV-assisted MEC networks, we propose a Double Regularization Diffusion-enhanced Soft Actor-Critic (R<sup>2</sup>DSAC) algorithm to solve the formulated multi-objective optimization problem. The R<sup>2</sup>DSAC algorithm incorporates diffusion entropy regularization and action entropy regularization to improve the performance of the diffusion policy. Furthermore, we dynamically mask unimportant neurons in the actor network to reduce the carbon emissions associated with model training. Simulation results demonstrate the reliability of the proposed HybridRAG-based LLM agent framework, which achieves a 6.6% improvement in F1 scores over traditional RAG, and validate the effectiveness of the R<sup>2</sup>DSAC algorithm, which outperforms the SAC algorithm by up to 64.17%. © 2025 IEEE. All rights reserved,

## 04 — Title Screening

**Title:** HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** HybridRAG-Based LLM Agents for Low-Carbon Optimization in Low-Altitude Economy Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
