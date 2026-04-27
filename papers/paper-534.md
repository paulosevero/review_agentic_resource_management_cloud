---
id: "paper-534"
title: "Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems"
authors: ["Zhang, Yi", "Zhu, Haihua", "Tang, Dunbing", "Zhou, Tong", "Gui, Yong"]
year: 2022
venue: "Robotics and Computer-Integrated Manufacturing"
venue_type: "journal"
doi: "10.1016/j.rcim.2022.102412"
url: "https://www.scopus.com/pages/publications/85133429544?origin=resultslist"
publisher: "Elsevier Ltd"
pages: ""
keywords: ["Flexible job-shop scheduling problem", "Multi-agent manufacturing system", "Proximal policy optimization", "Reinforcement learning", "Smart manufacturing"]
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
    machine_decision: "include"
    disagreement_type: "doctrine_override_c3_absent"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-534 — Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems

## Metadata

- **Authors:** Zhang, Yi and Zhu, Haihua and Tang, Dunbing and Zhou, Tong and Gui, Yong
- **Year:** 2022
- **Venue:** Robotics and Computer-Integrated Manufacturing
- **DOI:** 10.1016/j.rcim.2022.102412
- **URL:** https://www.scopus.com/pages/publications/85133429544?origin=resultslist
- **Publisher:** Elsevier Ltd
- **Pages:** 
- **Language:** English
- **Keywords:** Flexible job-shop scheduling problem; Multi-agent manufacturing system; Proximal policy optimization; Reinforcement learning; Smart manufacturing

### Abstract

Personalized orders bring challenges to the production paradigm, and there is an urgent need for the dynamic responsiveness and self-adjustment ability of the workshop. Traditional dispatching rules and heuristic algorithms solve the production planning and control problems by making schedules. However, the previous methods cannot work well in a changeable workshop environment when encountering a large number of stochastic disturbances of orders and resources. Recently, the potential of artificial intelligence (AI) algorithms in solving the dynamic scheduling problem has attracted researchers' attention. Therefore, this paper presents a multi-agent manufacturing system based on deep reinforcement learning (DRL), which integrates the self-organization mechanism and self-learning strategy. Firstly, the manufacturing equipment in the workshop is constructed as an equipment agent with the support of edge computing node, and an improved contract network protocol (CNP) is applied to guide the cooperation and competition among multiple agents, so as to complete personalized orders efficiently. Secondly, a multi-layer perceptron is employed to establish the decision-making module called AI scheduler inside the equipment agent. According to the perceived workshop state information, AI scheduler intelligently generates an optimal production strategy to perform task allocation. Then, based on the collected sample trajectories of scheduling process, AI scheduler is periodically trained and updated through the proximal policy optimization (PPO) algorithm to improve its decision-making performance. Finally, in the multi-agent manufacturing system testbed, dynamic events such as stochastic job insertions and unpredictable machine failures are considered in the verification experiments. The experimental results show that the proposed method is capable of obtaining the scheduling solutions that meet various performance metrics, as well as dealing with resource or task disturbances efficiently and autonomously. © 2022 Elsevier Ltd

## 04 — Title Screening

**Title:** Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic job shop scheduling based on deep reinforcement learning for multi-agent manufacturing systems
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
