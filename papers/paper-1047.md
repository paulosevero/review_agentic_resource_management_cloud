---
id: "paper-1047"
title: "A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control"
authors: ["Lin, Wenjun", "Lin, Weiwei", "Lin, Jianpeng", "Zhong, Haocheng", "Wang, Jiangtao", "He, Ligang"]
year: 2024
venue: "Sustainable Computing: Informatics and Systems"
venue_type: "journal"
doi: "10.1016/j.suscom.2024.100977"
url: "https://www.scopus.com/pages/publications/85184797831?origin=resultslist"
publisher: "Elsevier Inc."
pages: ""
keywords: ["DVFS", "Multi-agent", "Reinforcement learning", "Server fan"]
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

# paper-1047 — A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control

## Metadata

- **Authors:** Lin, Wenjun and Lin, Weiwei and Lin, Jianpeng and Zhong, Haocheng and Wang, Jiangtao and He, Ligang
- **Year:** 2024
- **Venue:** Sustainable Computing: Informatics and Systems
- **DOI:** 10.1016/j.suscom.2024.100977
- **URL:** https://www.scopus.com/pages/publications/85184797831?origin=resultslist
- **Publisher:** Elsevier Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** DVFS; Multi-agent; Reinforcement learning; Server fan

### Abstract

With the rapid development of the digital economy and intelligent industry, the energy consumption of data centers (DCs) has increased significantly. Various optimization methods are proposed to improve the energy efficiency of servers in DCs. However, existing solutions usually adopt model-based heuristics and best practices to select operations, which are not universally applicable. Moreover, existing works primarily focus on the optimization methods for individual components, with a lack of work on the joint optimization of multiple components. Therefore, we propose a multi-agent reinforcement learning-based method, named MRDF, combining DVFS and dynamic fan control to achieve a trade-off between power consumption and performance while satisfying thermal constraints. MRDF is model-free and learns by continuously interacting with the real server without prior knowledge. To enhance the stability of MRDF in dynamic environments, we design a data-driven baseline comparison method to evaluate the actual contribution of a single agent to the global reward. In addition, an improved Q-learning is proposed to deal with the large state and action space of the multi-core server. We implement MRDF on a Huawei Taishan 200 server and verify the effectiveness by running benchmarks. Experimental results show that the proposed method improves energy efficiency by an average of 3.9% compared to the best baseline solution, while flexibly adapting to different thermal constraints. © 2024

## 04 — Title Screening

**Title:** A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A multi-agent reinforcement learning-based method for server energy efficiency optimization combining DVFS and dynamic fan control
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
