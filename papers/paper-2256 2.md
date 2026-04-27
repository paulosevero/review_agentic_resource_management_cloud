---
id: "paper-2256"
title: "Dependency-Aware Deployment and Retrieval of Intelligent Microservices in AI-RAN"
authors: ["Wang, Leyao", "Chen, Zihan", "Guo, Kun"]
year: 2025
venue: "2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025"
venue_type: "conference"
doi: "10.1109/WCSP68525.2025.1010511"
url: "https://www.scopus.com/pages/publications/105033644718?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Dual timescales", "microservice deployment", "microservice retrieval"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: ""
    human_justification: ""

---

# paper-2256 — Dependency-Aware Deployment and Retrieval of Intelligent Microservices in AI-RAN

## Metadata

- **Authors:** Wang, Leyao and Chen, Zihan and Guo, Kun
- **Year:** 2025
- **Venue:** 2025 17th International Conference on Wireless Communications and Signal Processing, WCSP 2025
- **DOI:** 10.1109/WCSP68525.2025.1010511
- **URL:** https://www.scopus.com/pages/publications/105033644718?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Dual timescales; microservice deployment; microservice retrieval

### Abstract

Microservices architecture has emerged as a key enabler for low-latency and scalable deployment and retrieval of intelligent microservices in artificial intelligence-native radio access networks (AI-RAN), owing to its modularity and flexibility. However, orchestrating intelligent microservices (e.g., subnetworks within a neural network for inference) with complex invocation dependencies remains challenging, in the presence of dynamic user requests, limited network resources, and varying network topologies. To address this, we propose a dependencyaware dual timescale optimization framework, with the goal of minimizing the average service response delay. Specifically, a deep reinforcement learning (DRL) agent is employed at the long timescale to determine the deployment of intelligent microservices. At the short timescale, retrieval is performed based on the request access path, which is determined by efficiently solving an integer linear programming problem. The DRL agent is trained using cumulative service delay from the short-term optimization as feedback. Experimental results validate the robustness and effectiveness of the proposed framework in terms of deployment success rate and service response delay. © 2025 IEEE.

## 04 — Title Screening

**Title:** Dependency-Aware Deployment and Retrieval of Intelligent Microservices in AI-RAN

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Dependency-Aware Deployment and Retrieval of Intelligent Microservices in AI-RAN
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dependency-Aware Deployment and Retrieval of Intelligent Microservices in AI-RAN
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
