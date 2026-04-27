---
id: "paper-2392"
title: "Collaborative Multi-Agent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation with Long Term Energy Control"
authors: ["Yu, Chenglong", "Xing, Wang", "Shi, Jinglin", "Zhou, Yiqing", "Liu, Ling"]
year: 2025
venue: "IEEE Vehicular Technology Conference"
venue_type: "conference"
doi: "10.1109/VTC2025-Fall65116.2025.11310234"
url: "https://www.scopus.com/pages/publications/105032463001?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Energy efficiency", "Industrial Internet of Things", "Mobile edge computing", "Multi-agent deep reinforcement learning", "Resource allocation"]
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

# paper-2392 — Collaborative Multi-Agent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation with Long Term Energy Control

## Metadata

- **Authors:** Yu, Chenglong and Xing, Wang and Shi, Jinglin and Zhou, Yiqing and Liu, Ling
- **Year:** 2025
- **Venue:** IEEE Vehicular Technology Conference
- **DOI:** 10.1109/VTC2025-Fall65116.2025.11310234
- **URL:** https://www.scopus.com/pages/publications/105032463001?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Energy efficiency; Industrial Internet of Things; Mobile edge computing; Multi-agent deep reinforcement learning; Resource allocation

### Abstract

In mobile edge computing (MEC) enabled Industrial Internet of Things (MEC-IIoT), task offloading and resource allocation are always jointly optimized to achieve the best energy efficiency of IIoT terminals, which is important for MEC-IIoT. Existing research mainly focused on the instant energy consumption for the current task, ignoring the fact that the energy consumption is long term since energy is also required for subsequent tasks. Excessive energy consumption by the current task will affect the execution of subsequent tasks, leading to a degraded quality of service (QoS). Meanwhile, to solve the joint optimization problem, existing multi-agent deep reinforcement learning (MADRL) based methods face challenges like slow convergence. To tackle these problems, this paper proposes a long-term energy control enabled joint optimization scheme for the task offloading and resource allocation (LTE-JTORA). The main idea is to maximize the terminal energy efficiency while enabling the terminal to complete as many tasks as possible, so that the long-term energy control is realized. Then, an energy efficiency (EE) reward based collaborative MADRL (EE-CMADRL) is proposed to solve the NP-hard optimization problem. Different to MADRL where multiple agents work independently, EE-CMADRL is based on the Centralized Training Distributed Execution (CTDE) framework, where multiple agents can work collaboratively to train one EE reward enabled critic network. With more diverse data from multiple actor networks, EE-CMADRL can converge fast. Simulation results show that, compared to existing MADRL algorithms, the proposed EE-CMADRL improves the convergence speed by 71%. Compared to existing schemes with instant energy control, with the same time and energy constraints, the proposed LTE-JTORA scheme increases the number of completed tasks by 57%, and improves energy efficiency by 68%.  © 2025 IEEE.

## 04 — Title Screening

**Title:** Collaborative Multi-Agent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation with Long Term Energy Control

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** doctrine_override_c3_absent

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Collaborative Multi-Agent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation with Long Term Energy Control
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Collaborative Multi-Agent Deep Reinforcement Learning for Joint Task Offloading and Resource Allocation with Long Term Energy Control
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
