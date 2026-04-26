---
id: "paper-1212"
title: "Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach"
authors: ["Sun, Haifeng", "Zhou, Yuqiang", "Zhang, Hui", "Ale, Laha", "Dai, Hongning", "Zhang, Ning"]
year: 2024
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2024.3456846"
url: "https://www.scopus.com/pages/publications/85204154729?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "40996--41007"
keywords: ["Aerial access networks (AANs)", "joint optimization", "mobile edge computing (MEC)", "multiagent deep deterministic policy gradient (MADDPG)", "task offloading"]
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

# paper-1212 — Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach

## Metadata

- **Authors:** Sun, Haifeng and Zhou, Yuqiang and Zhang, Hui and Ale, Laha and Dai, Hongning and Zhang, Ning
- **Year:** 2024
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2024.3456846
- **URL:** https://www.scopus.com/pages/publications/85204154729?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 40996--41007
- **Language:** English
- **Keywords:** Aerial access networks (AANs); joint optimization; mobile edge computing (MEC); multiagent deep deterministic policy gradient (MADDPG); task offloading

### Abstract

The 6G network is expected to accommodate a wide array of connected devices, supporting diverse services from any location at any time. In this article, we introduce an aerial mobile edge computing (MEC) framework composed of high-altitude platforms (HAPs) and low-altitude unmanned aerial vehicles (UAVs), to cater to computing offloading for Internet of Things (IoT) devices, particularly in rural/remote areas or disaster zones. The framework accommodates various types of tasks, each computed by the corresponding Docker container. The objective is to achieve optimal workload fairness for UAVs while simultaneously minimizing the weighted processing costs among IoT devices in terms of task computation latency and energy consumption over the long term. This is achieved by jointly optimizing the flight trajectories and Docker image caching decisions of the UAVs with limited storage capacities, alongside ensuring service fairness for IoT devices. We tailor a multiagent deep deterministic policy gradient (MADDPG)-based approach to solve the long-term joint optimization problem, normalizing continuous actions and sampling discrete actions by generalizing the Gumbel-Softmax reparameterization trick. Experimental results indicate that our approach significantly outperforms benchmark schemes in terms of processing delay, energy consumption, and fairness.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Optimization of Caching, Computing, and Trajectory Planning in Aerial Mobile Edge Computing Networks: An MADDPG Approach
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
