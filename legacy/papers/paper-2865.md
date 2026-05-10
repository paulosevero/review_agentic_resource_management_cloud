---
id: "paper-2865"
title: "Joint Task Offloading and Resource Allocation for Collaborative VEC Network"
authors: ["Xu, Zhenyuan", "Li, Yanjun", "Chen, Yuzhe", "Cheng, Zhen", "Wang, Zhibo"]
year: 2026
venue: "IEEE Transactions on Intelligent Transportation Systems"
venue_type: "journal"
doi: "10.1109/TITS.2025.3631306"
url: "https://www.scopus.com/pages/publications/105021658661?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1814--1828"
keywords: ["convex optimization", "multi-agent deep reinforcement learning", "resource allocation", "task offloading", "Vehicular edge computing"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2865 — Joint Task Offloading and Resource Allocation for Collaborative VEC Network

## Metadata

- **Authors:** Xu, Zhenyuan and Li, Yanjun and Chen, Yuzhe and Cheng, Zhen and Wang, Zhibo
- **Year:** 2026
- **Venue:** IEEE Transactions on Intelligent Transportation Systems
- **DOI:** 10.1109/TITS.2025.3631306
- **URL:** https://www.scopus.com/pages/publications/105021658661?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1814--1828
- **Language:** English
- **Keywords:** convex optimization; multi-agent deep reinforcement learning; resource allocation; task offloading; Vehicular edge computing

### Abstract

Vehicular edge computing (VEC) is a promising technique for handling computation-intensive and delay-sensitive tasks by offloading them to roadside units (RSUs) or base stations (BSs) equipped with edge computing servers. However, the uneven spatial-temporal distribution of vehicles causes load imbalances among edge servers. To address this challenge, we propose a two-layer collaborative VEC network paradigm that incorporates offloading modes such as vehicle-to-RSU (V2R), vehicle-to-BS (V2B), and RSU-to-RSU collaboration. Within this framework, task offloading and resource allocation are jointly optimized to maximize system utility, which integrates revenue, delay, and energy consumption, while ensuring that vehicular tasks meet their delay requirements. Given the problem's complexity and scalability concerns, we introduce a distributed framework and propose the joint task offloading and resource allocation (JTORA) algorithm. This algorithm decomposes the original problem into two sub-problems: task offloading and resource allocation. The task offloading sub-problem is modeled as a potential game and solved using the multi-agent twin delayed deep deterministic policy gradient (MATD3) framework. Based on the offloading decisions, the resource allocation sub-problem is further divided into multiple convex optimization problems. The system utility, derived from task offloading and resource allocation decisions, serves as a reward to iteratively evaluate, train the learning model, and refine the offloading strategy. Theoretical analysis confirms that the JTORA algorithm converges to the Nash equilibrium (NE). Simulations using real traffic data validate the proposed algorithm's effectiveness and superiority over existing methods. Specifically, the JTORA algorithm improves overall system utility by reducing task processing delays and energy consumption while increasing the task completion rate. © 2000-2011 IEEE.

## 04 — Title Screening

**Title:** Joint Task Offloading and Resource Allocation for Collaborative VEC Network

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint Task Offloading and Resource Allocation for Collaborative VEC Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Task Offloading and Resource Allocation for Collaborative VEC Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
