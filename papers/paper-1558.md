---
id: "paper-1558"
title: "Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach"
authors: ["Fan, Xiaokun", "Chen, Yali", "Liu, Min", "Zhu, Yuchen", "Li, Zhongcheng"]
year: 2025
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2025.111540"
url: "https://www.scopus.com/pages/publications/105011040057?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Edge computing", "Joint sensing and computing", "Multi-agent deep reinforcement learning", "Unmanned aerial vehicle", "Video surveillance"]
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

# paper-1558 — Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach

## Metadata

- **Authors:** Fan, Xiaokun and Chen, Yali and Liu, Min and Zhu, Yuchen and Li, Zhongcheng
- **Year:** 2025
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2025.111540
- **URL:** https://www.scopus.com/pages/publications/105011040057?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Joint sensing and computing; Multi-agent deep reinforcement learning; Unmanned aerial vehicle; Video surveillance

### Abstract

Unmanned aerial vehicles (UAVs) are increasingly used for surveillance applications to take videos for Points of Interests (PoIs). Then, the sampled video data is fed into deep neural networks (DNNs) for inference. Due to the high computational complexity of DNNs, directly running DNN inference tasks on resource-constrained UAVs is intractable. To alleviate this issue, edge computing provides a promising solution by offloading tasks to the ground edge servers (ESs). However, how to flexibly schedule and tradeoff various resources for high-accuracy and low-delay inference is a challenge, especially in the complex scenario where video data sensing and DNN task processing are tightly coupled. Thus, this paper studies joint optimization for data sensing and computing in the air–ground collaborative inference framework. Specifically, the models for multi-UAV collaborative data sensing and collaborative inference between multiple UAVs and multiple ESs are designed. Then, we formulate an inference delay minimization problem by jointly optimizing UAVs’ 3D trajectories, number of sampled video frames and computation offloading, while satisfying accuracy, UAV energy budget and sensing mission requirements. Considering mixed continuous–discrete optimization variables, we propose a multi-agent proximal policy optimization (MAPPO) algorithm with a hybrid action space, called “MAPPO-HA”, to learn the optimal policies. Finally, simulation results demonstrate that our algorithm can achieve better performance compared with other optimization approaches. © 2025

## 04 — Title Screening

**Title:** Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint optimization of data sensing and computing in the air–ground collaborative inference framework: A multi-agent hybrid-action DRL approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
