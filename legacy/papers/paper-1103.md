---
id: "paper-1103"
title: "A Task Offloading Optimization Scheme Combining V2I and V2V"
authors: ["Ni, Sujie", "Chen, Bing", "Shi, You"]
year: 2024
venue: "Jisuanji Gongcheng/Computer Engineering"
venue_type: "journal"
doi: "10.19678/j.issn.1000-3428.0068415"
url: "https://www.scopus.com/pages/publications/85216314206?origin=resultslist"
publisher: "Editorial Office of Computer Engineering"
pages: "174--183"
keywords: ["multi-agent deep reinforcement learning", "task division", "task offloading", "V2I and V2V joint offloading", "vehicle edge computing"]
language: "Chinese"
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1103 — A Task Offloading Optimization Scheme Combining V2I and V2V

## Metadata

- **Authors:** Ni, Sujie and Chen, Bing and Shi, You
- **Year:** 2024
- **Venue:** Jisuanji Gongcheng/Computer Engineering
- **DOI:** 10.19678/j.issn.1000-3428.0068415
- **URL:** https://www.scopus.com/pages/publications/85216314206?origin=resultslist
- **Publisher:** Editorial Office of Computer Engineering
- **Pages:** 174--183
- **Language:** Chinese
- **Keywords:** multi-agent deep reinforcement learning; task division; task offloading; V2I and V2V joint offloading; vehicle edge computing

### Abstract

In vehicle edge computing systems, individual vehicles frequently encounter difficulties in executing computation-intensive tasks due to their constrained processing capacities. Furthermore, the highly dynamic nature of the Internet of Vehicles (IoV) environment exacerbates the challenge, as vehicles struggle to gather comprehensive global information about their surroundings and the task offloading behaviors of neighboring vehicles. This complexity hampers effective decision-making in task offloading. To mitigate these challenges—limited computational resources, fluctuating environmental conditions, and restricted observational capabilities—this study introduces an online algorithm based on the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) framework. The proposed approach synergistically integrates both Vehicle-to-Infrastructure (V2I) and Vehicle-to-Vehicle (V2V) offloading mechanisms while also incorporating task division to optimize overall system performance. First, by considering vehicle location, connection duration, and available computational resources, the vehicle with the highest service performance value is selected as the candidate service vehicle. Second, an optimization problem is formulated to minimize the system's average task offloading delay, and this problem is modeled as a Markov decision process. Through centralized training, vehicles are able to obtain information from other vehicles, enabling them to adjust their own policies accordingly. In the online execution phase, vehicles can make rapid task offloading decisions based on local observations. Finally, the proposed algorithm is compared against benchmark algorithms. The experimental results demonstrate that, compared to the deep deterministic policy gradient method and the equal task division method, the proposed task offloading algorithm reduces the average task offloading delay by 75% and 66%, respectively, and exhibits a faster convergence rate, validating the algorithm's effectiveness. © 2024, Editorial Office of Computer Engineering. All rights reserved.

## 04 — Title Screening

**Title:** A Task Offloading Optimization Scheme Combining V2I and V2V

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Task Offloading Optimization Scheme Combining V2I and V2V
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** A Task Offloading Optimization Scheme Combining V2I and V2V
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
