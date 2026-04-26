---
id: "paper-1882"
title: "Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing"
authors: ["Liu, Zhicheng", "Wang, Yilan", "Zhao, Yunfeng", "Qiu, Chao", "Zhang, Cheng", "Wang, Xiaofei", "Dong, Mianxiong"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3588142"
url: "https://www.scopus.com/pages/publications/105012290036?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12784--12801"
keywords: ["mobile edge computing", "model inference", "object detection", "task offloading", "Video detection"]
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

# paper-1882 — Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing

## Metadata

- **Authors:** Liu, Zhicheng and Wang, Yilan and Zhao, Yunfeng and Qiu, Chao and Zhang, Cheng and Wang, Xiaofei and Dong, Mianxiong
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3588142
- **URL:** https://www.scopus.com/pages/publications/105012290036?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12784--12801
- **Language:** English
- **Keywords:** mobile edge computing; model inference; object detection; task offloading; Video detection

### Abstract

Real-time video detection is essential for many mobile visual applications, which brings the heavy computational burden of deep neural networks. Mobile edge computing offers a promising solution by deploying computational resources near mobile devices. However, achieving efficient video detection on mobile devices requires addressing challenges such as different performance requirements, diverse computing and network conditions, and system dynamics. We propose a real-time video detection framework in mobile edge computing, where multiple video streams from mobile devices are processed while balancing key performance metrics with consideration of grouping. A joint optimization problem of task scheduling, model selection, and resource provisioning is formulated for the system, where decisions are made on two timescales. To this end, we propose a window controller to unify decision-making at the time-slot level. We design an online scheduling algorithm based on multi-agent deep reinforcement learning to enable adaptive and distributed scheduling, while a masking-enhanced attention mechanism enables efficient explicit information exchange between mobile devices. Experimental evaluations across different numbers of mobile devices demonstrate that, in terms of average reward, the proposed algorithm outperforms local processing by 14.600%, fixed offloading by 10.007%, and four learning-based scheduling baselines by an average of 2.267%.  © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Enabling Real-Time Video Detection With Adaptive and Distributed Scheduling in Mobile Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
