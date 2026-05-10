---
id: "paper-922"
title: "MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC"
authors: ["Gao, Zhen", "Fu, Jiaming", "Jing, Zongming", "Dai, Yu", "Yang, Lei"]
year: 2024
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2024.3362988"
url: "https://www.scopus.com/pages/publications/85184814018?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "18483--18502"
keywords: ["Joint trajectory planning and task offloading (JTPTO)", "multiagent reinforcement learning (MARL)", "multiobjective reinforcement learning", "UAV-assisted mobile edge computing (MEC)", "unmanned aerial vehicle (UAV) cooperation"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-922 — MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC

## Metadata

- **Authors:** Gao, Zhen and Fu, Jiaming and Jing, Zongming and Dai, Yu and Yang, Lei
- **Year:** 2024
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2024.3362988
- **URL:** https://www.scopus.com/pages/publications/85184814018?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 18483--18502
- **Language:** English
- **Keywords:** Joint trajectory planning and task offloading (JTPTO); multiagent reinforcement learning (MARL); multiobjective reinforcement learning; UAV-assisted mobile edge computing (MEC); unmanned aerial vehicle (UAV) cooperation

### Abstract

Existing joint trajectory planning and task offloading (JTPTO) methods provide ultralow latency services for mobile devices (MDs) in unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC). However, UAVs typically provide services to MDs under partial observation, leading to challenges in achieving optimal service performance due to information loss. Moreover, the JTPTO problem typically involves multiobjective optimization, which is challenging because the objectives may conflict with each other. In this article, we present a decentralized JTPTO method based on multiobjective and independently predicted communication multiagent actor-critic (MOIPC-MAAC). First, an IPC network is designed to facilitate UAV agents in learning a prior for communication between UAVs. UAV agents learn this prior through causal reasoning, which represents the mapping of UAV's observation to the level of confidence in choosing communication partners. The effect of one UAV on another UAV is predicted through the critic-network in multiagent reinforcement learning (MARL) and measured to indicate the necessity of UAV-UAV communication. Further, we regularize JTPTO policies to more effectively utilize exchanged messages. Second, a generalized variant of the Bellman optimality operator with multiple objectives is applied to address the JTPTO problem. We use it to learn a single parameterized expression that encompasses all the best JTPTO policies across the space of preferences. Experiments show that compared to existing solutions, MOIPC-MAAC reduces system costs by 14.23%-19.56% and the communication cost to approximately 11.23%. Moreover, compared to training from scratch, MOIPC-MAAC accelerates the adaptation of new JTPTO tasks with unknown preferences by 13.12%.  © 2014 IEEE.

## 04 — Title Screening

**Title:** MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** MOIPC-MAAC: Communication-Assisted Multiobjective MARL for Trajectory Planning and Task Offloading in Multi-UAV-Assisted MEC
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
