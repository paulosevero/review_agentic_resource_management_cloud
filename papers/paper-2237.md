---
id: "paper-2237"
title: "A distributed UAV analytics framework for DAO-based swarm systems"
authors: ["Vasalos, Averkios", "Economopoulos, Achileas", "Oikonomakis, Andreas", "Chakraborty, Abhinaba", "Kourtis, Michail-Alexandros", "Alexandridis, Georgios", "Tavernier, Wouter", "Xilouris, George", "Chochliouros, Ioannis", "Vasalos, Ioannis", "Trakadas, Panagiotis"]
year: 2025
venue: "Proceedings of the IEEE Symposium on Reliable Distributed Systems"
venue_type: "conference"
doi: "10.1109/SRDS69199.2025.00057"
url: "https://www.scopus.com/pages/publications/105033366253?origin=resultslist"
publisher: "IEEE Computer Society"
pages: "458--464"
keywords: ["Decentralized Data Processing", "Drone Swarm", "Edge Computing"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2237 — A distributed UAV analytics framework for DAO-based swarm systems

## Metadata

- **Authors:** Vasalos, Averkios and Economopoulos, Achileas and Oikonomakis, Andreas and Chakraborty, Abhinaba and Kourtis, Michail-Alexandros and Alexandridis, Georgios and Tavernier, Wouter and Xilouris, George and Chochliouros, Ioannis and Vasalos, Ioannis and Trakadas, Panagiotis
- **Year:** 2025
- **Venue:** Proceedings of the IEEE Symposium on Reliable Distributed Systems
- **DOI:** 10.1109/SRDS69199.2025.00057
- **URL:** https://www.scopus.com/pages/publications/105033366253?origin=resultslist
- **Publisher:** IEEE Computer Society
- **Pages:** 458--464
- **Language:** English
- **Keywords:** Decentralized Data Processing; Drone Swarm; Edge Computing

### Abstract

Unmanned Aerial Vehicles (UAVs) are increasingly deployed in inspection and monitoring missions, yet onboard computation and communication impose significant energy burdens that limit flight time and operational scope. In this work, we introduce a novel, blockchain-enabled framework—grounded in the Distributed Autonomous Organization (DAO) paradigm—for orchestrating distributed analytics across a swarm of UAVs. Leveraging the OASEES project’s smart-contract architecture, each drone embeds a Metrics Module for real-time power monitoring, a Behavioral Module for adaptive control, and a Blockchain Agent that autonomously proposes, votes on, and executes collective decisions. Three concurrent threads—Proposal Trigger, Voting, and Action Execution—enable fully decentralized governance of swarm behavior: from detecting critical energy thresholds and formulating swarm-wide conservation maneuvers, to executing approved strategies across all members. We validate our framework in a UAV-based infrastructure inspection scenario, employing a YOLOv5 object-detection pipeline to classify four corrosion classes on a telecommunications mast under three video-capture modalities (short-distance, long-distance, and horizontally concatenated streams). Across all configurations, our system achieves near-perfect precision, recall, and mean Average Precision (mAP50–95 ≈ 0.995), demonstrating both the efficacy of distributed workload inference and the feasibility of treating a single drone as a multi-feed processor. These results underscore the potential of DAO-driven UAV swarms for energy-aware, resilient aerial analytics, and pave the way for fully decentralized 5G/6G-enabled airborne networks. ©2025 IEEE.

## 04 — Title Screening

**Title:** A distributed UAV analytics framework for DAO-based swarm systems

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.5
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** A distributed UAV analytics framework for DAO-based swarm systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** A distributed UAV analytics framework for DAO-based swarm systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
