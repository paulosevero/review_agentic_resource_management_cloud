---
id: "paper-2481"
title: "DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge"
authors: ["Zhu, Changhong", "Zhang, Haitao", "Xu, Xingtao"]
year: 2025
venue: "Concurrency and Computation: Practice and Experience"
venue_type: "journal"
doi: "10.1002/cpe.70174"
url: "https://www.scopus.com/pages/publications/105009843742?origin=resultslist"
publisher: "John Wiley and Sons Ltd"
pages: ""
keywords: ["dual-stage GPU-CPU task", "edge computing", "quality of service (QoS)", "reinforcement learning", "soft real-time"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-2481 — DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge

## Metadata

- **Authors:** Zhu, Changhong and Zhang, Haitao and Xu, Xingtao
- **Year:** 2025
- **Venue:** Concurrency and Computation: Practice and Experience
- **DOI:** 10.1002/cpe.70174
- **URL:** https://www.scopus.com/pages/publications/105009843742?origin=resultslist
- **Publisher:** John Wiley and Sons Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** dual-stage GPU-CPU task; edge computing; quality of service (QoS); reinforcement learning; soft real-time

### Abstract

Edge cameras are ubiquitous, together with the recent boom in computer vision technology, and a variety of video analytics tasks are being processed at the edge. It is challenging to support more complex video analytics tasks on edge servers with unpredictable request loads and limited resources. However, most of these works use only a single optimization approach, focusing only on the improvement of a certain performance metric in a single processing stage, ignoring the balance of other performance metrics, and the space available for optimization is often very limited. Especially when dealing with video analytics tasks that need to be divided into two GPU-CPU stages for completion, this unidirectional focus may lead to execution performance imbalance or even negative quality of service (QoS) optimization. In addition, to fully utilize the valuable resources on the edge servers, it is often necessary to schedule multiple types of video analytics tasks on the edge servers. However, most of the existing scheduling strategies only focus on how to allocate computational resources for end-to-end tasks. They lack the awareness and consideration of the execution of tasks in different execution stages, as well as the mutual interference among tasks. These scheduling strategies, lacking stage-sensitivity and interference-sensitivity, may cause performance conflicts in environments running multiple tasks involving GPU-CPU dual-stage processing, thus affecting the overall QoS. To address these challenges, we first evaluate the impact of batch processing, frame rate control, resolution selection, and CPU concurrency processing on throughput, latency, and accuracy when running dual-stage tasks on edge platforms. Then, we propose DualRT, a soft real-time video analytics framework for dual-stage tasks, to optimize the QoS of dual-stage tasks while avoiding request stacking on edge platforms. In the scheduling module of DualRT, we design a scheduling method using a multi-agent deep reinforcement learning algorithm and a variable time window approach to schedule multiple dual-stage tasks with joint control of batch size, resolution, frame rate, and CPU concurrency for each task. Our experimental results show that DualRT improves QoS by an average of 13.3% and maximum throughput by an average of 24.6% compared to state-of-the-art solutions. © 2025 John Wiley & Sons Ltd.

## 04 — Title Screening

**Title:** DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** DualRT: A Qos-Aware Soft Real-Time Video Analytics Framework for Dual-Stage GPU-CPU Tasks on Edge
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
