---
id: "paper-435"
title: "Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems"
authors: ["Jia, Yi", "Zhang, Cheng", "Huang, Yongming", "Zhang, Wei"]
year: 2022
venue: "IEEE Transactions on Communications"
venue_type: "journal"
doi: "10.1109/TCOMM.2022.3206885"
url: "https://www.scopus.com/pages/publications/85139394215?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "7418--7433"
keywords: ["computation offloading", "graph convolutional neural network (GCN)", "Lyapunov optimization", "MEC", "multi-agent proximal policy optimization (MAPPO)", "task dependency graph"]
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

# paper-435 — Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems

## Metadata

- **Authors:** Jia, Yi and Zhang, Cheng and Huang, Yongming and Zhang, Wei
- **Year:** 2022
- **Venue:** IEEE Transactions on Communications
- **DOI:** 10.1109/TCOMM.2022.3206885
- **URL:** https://www.scopus.com/pages/publications/85139394215?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 7418--7433
- **Language:** English
- **Keywords:** computation offloading; graph convolutional neural network (GCN); Lyapunov optimization; MEC; multi-agent proximal policy optimization (MAPPO); task dependency graph

### Abstract

Mobile-Edge Computing (MEC) is an emerging paradigm in the Internet of Vehicles (IoV) to meet the ever-increasing computation demands of smart applications. To provide satisfactory computation performance, it is of significant importance to conduct computation offloading in IoV. In this paper, we investigate a multi-vehicle IoV system assisted by MECs with limited computation resources, where vehicles with complex applications can offload their subtasks to MEC servers. Applications are modeled as interdependent subtasks with general random task graphs, different from existing works with independent ones. To maximize the average logarithmic data processing rate (LDPR), the computation offloading problem is formulated as a time-average optimization with long-term constraints, which results from variable vehicle number, various applications and time-varying communication channels. To reduce the cooperation overhead, we propose a multi-agent Proximal Policy Optimization algorithm (Ly-MAPPO) which requires local observation only to solve the subproblems achieved by Lyapunov optimization technique in real time. In addition, to improve the performance of the Ly-MAPPO algorithm, Graph Convolutional Neural Network (GCN) is introduced to extract inter-dependencies between subtasks. Extensive simulations show that the GCN embedded Ly-MAPPO outperforms other baseline algorithms, e.g., greedy algorithm and gene algorithm, etc., for different traffic loads and computation resources in MEC servers.  © 1972-2012 IEEE.

## 04 — Title Screening

**Title:** Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Lyapunov Optimization Based Mobile Edge Computing for Internet of Vehicles Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
