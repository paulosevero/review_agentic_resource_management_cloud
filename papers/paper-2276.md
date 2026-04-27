---
id: "paper-2276"
title: "Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers"
authors: ["Wang, Ting", "Cheng, Kai", "Du, Xiao"]
year: 2025
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM55648.2025.11044699"
url: "https://www.scopus.com/pages/publications/105011040149?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Agents", "Collaborative learning", "Congestion control (communication)", "Distributed computer systems", "Learning algorithms", "Multi-task learning", "Optimization", "Robustness (control systems)", "Traffic congestion", "Collaborative network", "Data center networks", "Datacenter", "Multi tasks", "Network optimization", "Optimization strategy", "Performance", "Reinforcement learnings", "Sub-optimal performance", "Traffic scheduling", "Multi agent systems"]
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
    final_score: 0.25
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2276 — Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers

## Metadata

- **Authors:** Wang, Ting and Cheng, Kai and Du, Xiao
- **Year:** 2025
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM55648.2025.11044699
- **URL:** https://www.scopus.com/pages/publications/105011040149?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Agents; Collaborative learning; Congestion control (communication); Distributed computer systems; Learning algorithms; Multi-task learning; Optimization; Robustness (control systems); Traffic congestion; Collaborative network; Data center networks; Datacenter; Multi tasks; Network optimization; Optimization strategy; Performance; Reinforcement learnings; Sub-optimal performance; Traffic scheduling; Multi agent systems

### Abstract

As data center networks increasingly grow in complexity and scale, efficiently managing traffic scheduling and congestion control becomes crucial for optimizing network performance. Traditional single-task optimization strategies often fall short, failing to adequately address the interplay between different tasks and resulting in suboptimal performance with inefficiencies and robustness issues. To tackle these challenges, this paper proposes a novel Multi-Task Reinforcement Learning (MTRL)-based collaborative Network Optimization scheme, termed MTRLNO, which establishes a structured framework with central and edge systems (i.e., hosts and switches). The SDN-enabled central system incorporates an MTRL agent that simultaneously optimizes traffic scheduling and congestion control tasks, leveraging global network state information to formulate instructive optimization policies for edge systems. Switches implement decentralized multi-agent RL agents to facilitate automatic ECN tuning for congestion control, with the ability to handle incast issues. Hosts feature an MTRL-guided Multiple Level Feedback Queue (MLFQ) demotion threshold adjustment scheme for adaptive traffic scheduling. We further develop a Prioritized Experience Replay-based Soft Actor-Critic (PERSAC) algorithm to enhance learning efficiency and a customized multi-task learning algorithm via improved parameter-sharing to effectively adapt across multiple tasks. Experimental results demonstrate that MTRLNO significantly outperforms state-of-the-art approaches in terms of FCT, latency, and robustness across diverse network conditions.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers

### Machine Screening

- **Final Score:** 0.25 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.5 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Task Reinforcement Learning for Collaborative Network Optimization in Data Centers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
