---
id: "paper-2449"
title: "Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding"
authors: ["Zhang, Jingjing", "Deng, Xiaoheng", "Gui, Jinsong", "Chen, Xuechen", "Wan, Shaohua", "Min, Geyong"]
year: 2025
venue: "IEEE Transactions on Cloud Computing"
venue_type: "journal"
doi: "10.1109/TCC.2025.3571095"
url: "https://www.scopus.com/pages/publications/105005465650?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "854--866"
keywords: ["Cloud gaming", "deep reinforcement learning", "quality-of-experience (QoE)", "resource allocation", "video encoding configuration"]
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

# paper-2449 — Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding

## Metadata

- **Authors:** Zhang, Jingjing and Deng, Xiaoheng and Gui, Jinsong and Chen, Xuechen and Wan, Shaohua and Min, Geyong
- **Year:** 2025
- **Venue:** IEEE Transactions on Cloud Computing
- **DOI:** 10.1109/TCC.2025.3571095
- **URL:** https://www.scopus.com/pages/publications/105005465650?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 854--866
- **Language:** English
- **Keywords:** Cloud gaming; deep reinforcement learning; quality-of-experience (QoE); resource allocation; video encoding configuration

### Abstract

Cloud gaming represents a major part of contemporary gaming. To boost the Quality-of-Experience (QoE) of cloud gaming, the integration of Dynamic Adaptive Video Encoding (DAVE) with Multi-access Edge Computing (MEC) has become the natural candidate owing to its flexibility and reliable transmission support for real-time interactions. However, as multiple gamers compete for limited resources to achieve personalized QoE, such as ultra-high video quality and ultra-low latency, how to support efficient edge resource optimization is a fundamental and important problem. Furthermore, determining the optimal game video encoding configuration in real-time poses significant challenges, especially when lacking the information on future video and edge network resources. To address these key issues, we jointly optimize the video encoding as well as computing and communication resource allocation by active mutual adaptation of video coding configurations and physical resources in a Software Defined Networking (SDN)-assisted edge network. This eliminates the performance bottleneck caused by decoupling optimization of coding parameter configuration and physical resource allocation. The SDN-assisted edge network architecture supports efficient on-demand resource management, provides global network information, and meets the stringent time-varying game requests. Due to the significant time scale difference between video chunk and physical resource block, we propose a novel Asynchronous Decision-Making Multi Agent Proximal Policy Optimization algorithm (AD-MAPPO), which can address the credit assignment problem with a single agent. It can also adapt to the highly dynamic cloud gaming environment without prior knowledge and a deterministic environmental model. Extensive experimentation based on real cloud gaming datasets convincingly demonstrates that our approach can significantly enhance the overall QoE of gamers. © 2013 IEEE.

## 04 — Title Screening

**Title:** Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Personalized Cloud Gaming: Multi-Objective Optimization for Resource Utilization and Video Encoding
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
