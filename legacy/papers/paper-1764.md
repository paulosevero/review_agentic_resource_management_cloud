---
id: "paper-1764"
title: "Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks"
authors: ["Lan, Shizhan", "Guo, Hao", "Wang, Zhenyu", "Yang, Lei"]
year: 2025
venue: "2025 International Conference on Sensor-Cloud and Edge Computing System, SCECS 2025"
venue_type: "conference"
doi: "10.1109/SCECS65243.2025.11065779"
url: "https://www.scopus.com/pages/publications/105012240335?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "163--167"
keywords: ["caching", "data distribution", "dge computing", "reinforcement learningdge computing", "reinforcement learninge", "vehicular network"]
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
    human_justification: "RL"

---

# paper-1764 — Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks

## Metadata

- **Authors:** Lan, Shizhan and Guo, Hao and Wang, Zhenyu and Yang, Lei
- **Year:** 2025
- **Venue:** 2025 International Conference on Sensor-Cloud and Edge Computing System, SCECS 2025
- **DOI:** 10.1109/SCECS65243.2025.11065779
- **URL:** https://www.scopus.com/pages/publications/105012240335?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 163--167
- **Language:** English
- **Keywords:** caching; data distribution; dge computing; reinforcement learningdge computing; reinforcement learninge; vehicular network

### Abstract

The vehicle edge network leverages mobile edge computing (MEC) to provide low-latency data and intelligent services. A key challenge is how to efficiently utilize limited resources to disseminate data and promptly respond to service requests. Existing methods, which cache data at the edge to reduce access delay, only consider single-source data distribution. However, applications like object detection and trajectory prediction involve multiple data copies across edges and vehicles. The destination vehicle can retrieve data from multiple sources, requiring optimal source selection. To tackle these challenges, we formulate a joint optimization problem for data dissemination and caching from multiple sources to multiple destinations, considering data timeliness and request deadlines to maximize request success rates. Specifically, we transform the problem into a minimum Steiner tree problem and propose a multi-agent reinforcement learning algorithm to determine source selection and caching strategies. Extensive experiments demonstrate that our approach significantly improves request success rates compared to benchmarks.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks
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
