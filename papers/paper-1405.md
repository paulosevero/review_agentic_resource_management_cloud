---
id: "paper-1405"
title: "A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks"
authors: ["Ayepah-Mensah, Daniel", "Ghebreziabiher, Amine Kidane", "Boateng, Gordon Owusu", "Mizouni, Rabeb", "Mourad, Azzam", "Otrok, Hadi", "Bentahar, Jamal", "Muhaidat, Sami"]
year: 2025
venue: "International Conference on Wireless and Mobile Computing, Networking and Communications"
venue_type: "conference"
doi: "10.1109/WiMob66857.2025.11257559"
url: "https://www.scopus.com/pages/publications/105029900367?origin=resultslist"
publisher: "IEEE Computer Society"
pages: ""
keywords: ["Deep Reinforcement Learning", "Edge-Cloud Orchestration", "Large Language Models (LLMs)", "Microservice Deployment", "Retrieval-Augmented Generation (RAG)"]
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

# paper-1405 — A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks

## Metadata

- **Authors:** Ayepah-Mensah, Daniel and Ghebreziabiher, Amine Kidane and Boateng, Gordon Owusu and Mizouni, Rabeb and Mourad, Azzam and Otrok, Hadi and Bentahar, Jamal and Muhaidat, Sami
- **Year:** 2025
- **Venue:** International Conference on Wireless and Mobile Computing, Networking and Communications
- **DOI:** 10.1109/WiMob66857.2025.11257559
- **URL:** https://www.scopus.com/pages/publications/105029900367?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 
- **Language:** English
- **Keywords:** Deep Reinforcement Learning; Edge-Cloud Orchestration; Large Language Models (LLMs); Microservice Deployment; Retrieval-Augmented Generation (RAG)

### Abstract

Modern edge cloud platforms must efficiently deploy and route containerized microservice DAGs under strict latency and cost constraints, while adapting to rapidly changing workloads and infrastructure states. Deep Reinforcement Learning (DRL) schedulers adapt well to dynamics but often lack semantic awareness of service intent and task dependencies, resulting in suboptimal decisions in unseen scenarios. To overcome these limitations, we introduce a Retrieval-Augmented Generation-assisted DRL (RAG-DRL) framework that integrates a lightweight DRL agent with a graph-based RAG module powered by a partially frozen LLM. A dynamic memory graph encodes contextual information such as node resources, network latencies, and SLA feedback. The LLM retrieves relevant historical deployments and current service intents to generate soft placement plans and reward estimates, which guide the DRL agent. These priors accelerate convergence, improve generalization across diverse conditions, and ensure real-time responsiveness. Evaluations on a realistic urban-scale edge cloud testbed confirm that RAG-DRL significantly reduces SLA violations, end-to-end latency, and resource imbalance, outperforming modern container-based schedulers. Our framework converges faster, maintains latency below 65 ms on scale, limits SLA violations to 12% under heavy load, and achieves 90 % resource utilization with balanced distribution.  © 2025 IEEE.

## 04 — Title Screening

**Title:** A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** A RAG-Assisted DRL Framework for Microservices Deployment in 6G Vehicular Networks
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
