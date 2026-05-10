---
id: "paper-1702"
title: "Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling"
authors: ["Jiang, Qiangqiang", "Han, Peng", "Xin, Xu", "Chen, Kang"]
year: 2025
venue: "IEEE Transactions on Aerospace and Electronic Systems"
venue_type: "journal"
doi: "10.1109/TAES.2025.3583276"
url: "https://www.scopus.com/pages/publications/105009275986?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "14143--14159"
keywords: ["Multiagent deep reinforcement learning (MADRL)", "multisatellite on-orbit computation", "satellite edge computing (SEC)", "task scheduling"]
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

# paper-1702 — Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling

## Metadata

- **Authors:** Jiang, Qiangqiang and Han, Peng and Xin, Xu and Chen, Kang
- **Year:** 2025
- **Venue:** IEEE Transactions on Aerospace and Electronic Systems
- **DOI:** 10.1109/TAES.2025.3583276
- **URL:** https://www.scopus.com/pages/publications/105009275986?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 14143--14159
- **Language:** English
- **Keywords:** Multiagent deep reinforcement learning (MADRL); multisatellite on-orbit computation; satellite edge computing (SEC); task scheduling

### Abstract

Today’s satellite applications often require the immediate processing of exploding data, which has driven a shift to on-orbit computing needs. Due to the limited onboard resources and energy supply, satellite edge computing is developed for intersatellite and satellite–ground collaborations. However, it is a challenge to achieve efficient multisatellite on-orbit computation considering the harsh satellite-to-ground transmission. Therefore, this article proposes an edge-computing-enabled multisatellite on-orbit computation scheduling (MSOCS) through multiagent deep reinforcement learning (MADRL). First, we formulate the MSOCS problem, where on-orbit computation tasks are described as a directed acyclic graph, and the intermittent satellite-to-ground link is established as connectable and disconnectable constraints. Second, a multiagent proximal policy optimization-based algorithm is developed by modeling the MSOCS problem via a partially observable Markov decision process. To cope with the dynamic change of observational input, we design a problem-specific embedding constructor, which is also utilized as the structural basis of the policy and value networks. Finally, practical remote sensing data processing missions are employed as the case study to conduct evaluation experiments. Simulation results validate the scheduling effectiveness of the proposed MSOCS algorithm in the test instances with different data scales, which surpasses other MADRL approaches. Moreover, our MSOCS improves the efficiency of on-orbit computation by 70.48% in time and 68.33% in energy, compared with the baseline without scheduling optimization. © 1965-2011 IEEE.

## 04 — Title Screening

**Title:** Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep Reinforcement Learning and Edge Computing for Multisatellite On-Orbit Task Scheduling
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
