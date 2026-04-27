---
id: "paper-846"
title: "Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications"
authors: ["Cao, Hao", "Xu, Jingao", "Yang, Zheng", "Shangguan, Longfei", "Zhang, Jialin", "He, Xiaowu", "Liu, Yunhao"]
year: 2024
venue: "IEEE/ACM Transactions on Networking"
venue_type: "journal"
doi: "10.1109/TNET.2023.3330763"
url: "https://www.scopus.com/pages/publications/85178016314?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1823--1838"
keywords: ["collaborative mapping", "edge computing", "multi-agent SLAM", "Visual SLAM"]
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

# paper-846 — Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications

## Metadata

- **Authors:** Cao, Hao and Xu, Jingao and Yang, Zheng and Shangguan, Longfei and Zhang, Jialin and He, Xiaowu and Liu, Yunhao
- **Year:** 2024
- **Venue:** IEEE/ACM Transactions on Networking
- **DOI:** 10.1109/TNET.2023.3330763
- **URL:** https://www.scopus.com/pages/publications/85178016314?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1823--1838
- **Language:** English
- **Keywords:** collaborative mapping; edge computing; multi-agent SLAM; Visual SLAM

### Abstract

The edge-based multi-agent visual SLAM is crucial for emerging mobile applications like search-and-rescue, inventory automation, and industrial inspection. It uses a central node to manage the global map and schedule tasks for agents. However, as the number of agents increases, the system faces scalability challenges due to operational overhead, such as data redundancy, bandwidth consumption, and localization errors. In this paper, we introduce SwarmMap, a framework designed to enhance the scalability of collaborative visual SLAM service in edge offloading settings. SwarmMap consists of three system modules: a change log-based server-client synchronization mechanism, a priority-aware task scheduler, and a lean global map representation. These modules work together to address the challenges of data explosion problems. SwarmMap is open-source and compatible with the robotic operating system (ROS). Existing visual SLAM applications could incorporate SwarmMap through SwarmAPI, a set of well-packaged APIs, to compose SwarmMap's function modules to enhance their performance and capacity in multi-agent scenarios. Comprehensive evaluations and a three-month case study at one of the world's largest oilfields demonstrate that SwarmMap can serve 2× more agents (> 20 agents) than the state-of-the-arts with the same resource overhead, meanwhile maintaining an average trajectory error of 38cm , outperforming existing works by > 55%.  © 1993-2012 IEEE.

## 04 — Title Screening

**Title:** Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Scaling Up Edge-Assisted Real-Time Collaborative Visual SLAM Applications
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
