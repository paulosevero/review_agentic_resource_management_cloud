---
id: "paper-2801"
title: "SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds"
authors: ["Tong, Haogang", "Meng, Chunyang", "Song, Shijie", "Pan, Maolin", "Yu, Yang"]
year: 2026
venue: "IEEE Transactions on Services Computing"
venue_type: "journal"
doi: "10.1109/TSC.2026.3672566"
url: "https://www.scopus.com/pages/publications/105032788764?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge-cloud Environ ment", "Graph Convolutional Network", "Microservice Autoscaling", "Multi-Agent Reinforcement Learning", "Quality of Service", "Service-Level Agreements"]
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
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2801 — SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds

## Metadata

- **Authors:** Tong, Haogang and Meng, Chunyang and Song, Shijie and Pan, Maolin and Yu, Yang
- **Year:** 2026
- **Venue:** IEEE Transactions on Services Computing
- **DOI:** 10.1109/TSC.2026.3672566
- **URL:** https://www.scopus.com/pages/publications/105032788764?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge-cloud Environ ment; Graph Convolutional Network; Microservice Autoscaling; Multi-Agent Reinforcement Learning; Quality of Service; Service-Level Agreements

### Abstract

Edge-cloud environments constitute a heterogeneous computing paradigm that integrates resource-constrained edge servers with high-performance cloud servers. While microservices have revolutionized large-scale applications development by enhancing scalability and flexibility, achieving efficient microservice autoscaling—the dynamic adjustment of instances to maintain quality of service (QoS) and meet service-level agreements (SLA) targets—remains challenging in such environments. Most existing autoscaling techniques rely on metric forecasting and centralized or per-node control, causing them to overlook temporal evolution and server relationships and resulting in unstable and weakly coordinated scaling. To address these challenges, we present SynScale, a distributed collaborative autoscaling framework that strengthens both temporal sensitivity and structural coordination. SynScale introduces a spatiotemporal representation module that couples a temporal attention network with a multi graph convolutional model. The temporal component distills behavioral trends from recent observations to ensure coherent responses to time-varying dynamics, while the spatial component performs relational reasoning over explicitly modeled inter server correlations to yield structure-aware representations that support effective cross-node coordination. These spatiotemporal embeddings are then used within a multi-agent reinforcement learning paradigm, enabling distributed agents to generate context-aware scaling decisions that align local adaptability with system-wide efficiency. Experimental evaluations against state of-the-art autoscaling techniques show that SynScale reduces average response time by 59.32%, SLA violations by 85.71%, and P95 latency by 73.2%, while also lowering resource cost. It further improves scaling stability—reflected by lower instance time and longer instance lifetimes—and maintains lightweight, scale-stable runtime overhead, ensuring practical deployability in heterogeneous edge-cloud environments. © 2008-2012 IEEE.

## 04 — Title Screening

**Title:** SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** SynScale: Spatiotemporal Collaborative Autoscaling for Microservices in Edge-Clouds
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
