---
id: "paper-2264"
title: "Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning"
authors: ["Wang, Yang", "Tang, Tengda", "Fang, Zhou", "Deng, Yingnan", "Duan, Yifei"]
year: 2025
venue: "2025 IEEE 7th International Conference on Communications, Information System and Computer Engineering, CISCE 2025"
venue_type: "conference"
doi: "10.1109/CISCE65916.2025.11065827"
url: "https://www.scopus.com/pages/publications/105011978021?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "585--589"
keywords: ["A3C algorithm", "Microservice architecture", "reinforcement learning", "resource scheduling"]
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

# paper-2264 — Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning

## Metadata

- **Authors:** Wang, Yang and Tang, Tengda and Fang, Zhou and Deng, Yingnan and Duan, Yifei
- **Year:** 2025
- **Venue:** 2025 IEEE 7th International Conference on Communications, Information System and Computer Engineering, CISCE 2025
- **DOI:** 10.1109/CISCE65916.2025.11065827
- **URL:** https://www.scopus.com/pages/publications/105011978021?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 585--589
- **Language:** English
- **Keywords:** A3C algorithm; Microservice architecture; reinforcement learning; resource scheduling

### Abstract

To address the challenges of high resource dynamism and intensive task concurrency in microservice systems, this paper proposes an adaptive resource scheduling method based on the A3C reinforcement learning algorithm. The scheduling problem is modeled as a Markov Decision Process, where policy and value networks are jointly optimized to enable fine-grained resource allocation under varying load conditions. The method incorporates an asynchronous multi-threaded learning mechanism, allowing multiple agents to perform parallel sampling and synchronize updates to the global network parameters. This design improves both policy convergence efficiency and model stability. In the experimental section, a real-world dataset is used to construct a scheduling scenario. The proposed method is compared with several typical approaches across multiple evaluation metrics, including task delay, scheduling success rate, resource utilization, and convergence speed. The results show that the proposed method delivers high scheduling performance and system stability in multi-task concurrent environments. It effectively alleviates the resource allocation bottlenecks faced by traditional methods under heavy load, demonstrating its practical value for intelligent scheduling in microservice systems.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Intelligent Task Scheduling for Microservices via A3C-Based Reinforcement Learning
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
