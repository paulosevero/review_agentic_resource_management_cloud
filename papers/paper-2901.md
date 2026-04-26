---
id: "paper-2901"
title: "Joint Latency-Energy Optimization for Two-Tier Multiuser Multitask Offloading in AI-Agent Communication Networks"
authors: ["Zeng, Jie", "Zhang, Yuting", "Yang, Yifan", "Feng, Wei", "Lv, Tiejun"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3665601"
url: "https://www.scopus.com/pages/publications/105030689768?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Artificial intelligence-agent communication networks (ACNs)", "block coordinate descent (BCD)", "Lagrangian relaxation", "minimum cost flow (MCF)", "proximal policy optimization (PPO)", "task offloading"]
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

# paper-2901 — Joint Latency-Energy Optimization for Two-Tier Multiuser Multitask Offloading in AI-Agent Communication Networks

## Metadata

- **Authors:** Zeng, Jie and Zhang, Yuting and Yang, Yifan and Feng, Wei and Lv, Tiejun
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3665601
- **URL:** https://www.scopus.com/pages/publications/105030689768?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Artificial intelligence-agent communication networks (ACNs); block coordinate descent (BCD); Lagrangian relaxation; minimum cost flow (MCF); proximal policy optimization (PPO); task offloading

### Abstract

Artificial intelligence-agent communication networks (ACNs) in the sixth-generation (6G) enable collaborative task execution among agents and butler. However, compared with traditional mobile edge computing (MEC), in ACNs, a large number of agents possess comparable computing capabilities and task proportions need to be jointly determined rather than being predefined, causing high optimization complexity in large-scale deployment scenarios. In this paper, we propose an effective framework to solve the large-scale coupled optimization problem under acceptable complexity. Specifically, we model the joint task allocation, resource allocation, task offloading and computation frequency adjustment problem as an NP-hard nonconvex mixed-integer nonlinear programming (MINLP) problem, and derive its lower bound through Lagrangian relaxation. We decompose the problem into resource allocation and task offloading subproblems, which are solved via proximal policy optimization (PPO) and minimum-cost models within a block coordinate descent (BCD) framework. Simulations demonstrate the tightness of the lower bound, achieving stable convergence for 30 agents while reducing latency from 150 ms to 50 ms and the energy consumption by 28.18%. Our algorithm has great potential for ACNs with many agents deployed in future 6G scenarios, such as autonomous vehicles, robotic swarms and precision telemedicine.  © 2014 IEEE.

## 04 — Title Screening

**Title:** Joint Latency-Energy Optimization for Two-Tier Multiuser Multitask Offloading in AI-Agent Communication Networks

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=0.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Joint Latency-Energy Optimization for Two-Tier Multiuser Multitask Offloading in AI-Agent Communication Networks
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Joint Latency-Energy Optimization for Two-Tier Multiuser Multitask Offloading in AI-Agent Communication Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
