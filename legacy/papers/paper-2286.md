---
id: "paper-2286"
title: "Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks"
authors: ["Wei, Yuting", "Ji, Zhe", "Wu, Sheng", "Jia, Haoge", "Xiao, Ailing", "Kuang, Linling"]
year: 2025
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2025.3605153"
url: "https://www.scopus.com/pages/publications/105015582022?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["hierarchical reinforcement learning", "MATD3 algorithm for UAVs", "Space-air integrated edge computing", "task scheduling", "TD3-based controller for satellite-level coordination"]
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
    final_score: 0.75
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "strong_disagreement"
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2286 — Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks

## Metadata

- **Authors:** Wei, Yuting and Ji, Zhe and Wu, Sheng and Jia, Haoge and Xiao, Ailing and Kuang, Linling
- **Year:** 2025
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2025.3605153
- **URL:** https://www.scopus.com/pages/publications/105015582022?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** hierarchical reinforcement learning; MATD3 algorithm for UAVs; Space-air integrated edge computing; task scheduling; TD3-based controller for satellite-level coordination

### Abstract

In space–air–ground integrated networks (SAGINs), efficient task scheduling is critical to ensuring low latency and energy efficiency for computation-intensive applications. This paper proposes a hierarchical reinforcement learning (HRL)–based task scheduling framework for space–air integrated edge computing systems, consisting of low Earth orbit (LEO) satellites and unmanned aerial vehicles (UAVs). The architecture is structured into two layers: UAVs handle task reception and local execution, while satellites assist in offloaded task processing. To enable intelligent and decentralized decision-making, we employ a multi-agent twin delayed deep deterministic policy gradient (MATD3) algorithm for UAVs and a TD3-based controller for satellite-level coordination. A shared reward mechanism is introduced to promote cross-layer optimization. Simulation results demonstrate that the proposed framework significantly reduces task execution delay and energy consumption compared to baseline schemes, achieving faster convergence. These results verify the effectiveness and practicality of the proposed method in dynamic and resource-constrained space–air environments. The proposed method reduces average total cost (ATC) by at least 13% compared to existing methods. © 2014 IEEE.

## 04 — Title Screening

**Title:** Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Hierarchical Reinforcement Learning for Task Scheduling in Space-Air Integrated Edge Computing Networks
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
