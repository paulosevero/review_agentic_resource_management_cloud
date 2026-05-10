---
id: "paper-1569"
title: "Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks"
authors: ["Feng, Zideng", "Lu, Lu", "Li, Qin", "Chai, Yuhao", "Zhang, Zhenyu", "Zhang, Yong", "Teng, Yinglei", "Guo, Da"]
year: 2025
venue: "IEEE International Conference on Communications"
venue_type: "conference"
doi: "10.1109/ICC52391.2025.11160773"
url: "https://www.scopus.com/pages/publications/105018456705?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "6161--6166"
keywords: ["deep reinforcement learning", "edge-cloud computing", "Large language model", "model partition"]
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
    human_justification: "LLM as workload"

---

# paper-1569 — Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks

## Metadata

- **Authors:** Feng, Zideng and Lu, Lu and Li, Qin and Chai, Yuhao and Zhang, Zhenyu and Zhang, Yong and Teng, Yinglei and Guo, Da
- **Year:** 2025
- **Venue:** IEEE International Conference on Communications
- **DOI:** 10.1109/ICC52391.2025.11160773
- **URL:** https://www.scopus.com/pages/publications/105018456705?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 6161--6166
- **Language:** English
- **Keywords:** deep reinforcement learning; edge-cloud computing; Large language model; model partition

### Abstract

With the progressive evolution of large language models (LLMs) and the increasing need of computing for 6G, it becomes crucial for multiple network nodes with limited computing resources to share the need for large model inference. Model partition methods have been proposed to enable computation-intensive artificial intelligence (AI) services by splitting an AI model across multi-edge and cloud nodes. In this paper, a distributed inference optimization framework for transformer decoder-only based LLMs (DIO-LLMs) is proposed in edge-cloud collaborative networks. The partitioning and offloading strategy is determined based on the computing workload and network status. DIO-LLMs specifically accounts for the parallel execution capabilities of the transformer architecture. It employs a two-phase model partitioning strategy, comprising inter-layer and intra-layer partitions, to effectively distribute LLMs across edge and cloud nodes. Additionally, to mitigate inference latency under resource limitations, a Greedy Proximal Policy Optimization (GPPO) based algorithm has been developed to devise optimal strategies. Simulation results indicate that under memory constraints, the proposed algorithm can reduce inference latency more effectively than other baseline algorithms.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Distributed Inference Optimization for Large Language Model in Edge-Cloud Collaborative Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
