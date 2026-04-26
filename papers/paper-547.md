---
id: "paper-547"
title: "Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture"
authors: ["Akbari, Mohammad", "Syed, Aisha", "Kennedy, W. Sean", "Erol-Kantarci, Melike"]
year: 2023
venue: "IEEE Transactions on Machine Learning in Communications and Networking"
venue_type: "journal"
doi: "10.1109/TMLCN.2023.3311749"
url: "https://www.scopus.com/pages/publications/105027867571?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers"
pages: "277--295"
keywords: ["age of information", "constraint MDP", "federated reinforcement learning", "Internet of Things", "network function virtualization", "UAV-Aided mobile edge computing (UAV-Aided MEC)"]
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
    human_decision: ""
    human_justification: ""

---

# paper-547 — Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture

## Metadata

- **Authors:** Akbari, Mohammad and Syed, Aisha and Kennedy, W. Sean and Erol-Kantarci, Melike
- **Year:** 2023
- **Venue:** IEEE Transactions on Machine Learning in Communications and Networking
- **DOI:** 10.1109/TMLCN.2023.3311749
- **URL:** https://www.scopus.com/pages/publications/105027867571?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers
- **Pages:** 277--295
- **Language:** English
- **Keywords:** age of information; constraint MDP; federated reinforcement learning; Internet of Things; network function virtualization; UAV-Aided mobile edge computing (UAV-Aided MEC)

### Abstract

For a wide range of smart agriculture use cases, the prospects of utilizing the Internet of Things (IoT) are immense. Many IoT devices can be deployed for precision farming, soil management, automated irritation, information gathering, or performing some local processing to provide various services. Due to the computational capacity limitation of IoT devices and their limited power, UAV-Aided mobile-edge computing (MEC) is proposed to provide IoT nodes with additional resources by hosting their computation functions and making smart agriculture use cases more operational. On the other hand, from the implementation viewpoint, Network Function Virtualization (NFV) is an emerging approach recently proposed for flexible management of such computation functions in UAVs and MEC-server. However, efficient orchestration of the virtualized functions is a challenge. In this paper, we consider a decentralized UAV-Aided MEC system in which the NFV-enabled processing nodes manage the computational tasks. To be more specific, we consider the smart agriculture use cases that need live streaming/analysis, such as surveillance or environmental monitoring. In such a network, we propose a method for orchestrating the NFVs efficiently, while the network energy consumption throughout the network is minimized. This problem becomes even more crucial when considering a strict condition on the instantaneous AoI values. Therefore, the problem is first formulated as a Decentralized Constrained Multi-Agent Markov Decision Process (Dec-CMMDP). As the formulated problem is NEXP, in the next step, we exploit some structural features of the considered network and introduce the concept of symmetry to simplify the problem. Then, inspired by Augmented Lagrangian dual optimization, a novel decentralized, federated learning-based solution is proposed to solve the problem. Simulation results show the effectiveness of the proposed approach in minimizing the total network energy consumption, minimizing the average AoI, and satisfying the strict condition of AoI < 100 msec for supporting real-Time applications in our network parameter settings.  © 2023 CCBY.

## 04 — Title Screening

**Title:** Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Constrained Federated Learning for AoI-Limited SFC in UAV-Aided MEC for Smart Agriculture
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
