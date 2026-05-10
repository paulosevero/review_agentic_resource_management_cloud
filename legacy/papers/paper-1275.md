---
id: "paper-1275"
title: "Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks"
authors: ["Wu, Yingying", "Zhang, Zhifei", "Ge, Yiyang", "Mao, Jin", "Chu, Zhipeng", "Xiong, Ke", "Fan, Pingyi"]
year: 2024
venue: "2024 9th International Conference on Computer and Communication Systems, ICCCS 2024"
venue_type: "conference"
doi: "10.1109/ICCCS61882.2024.10603138"
url: "https://www.scopus.com/pages/publications/85201318830?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "718--724"
keywords: ["Age of Information (AoI)", "High-Speed Railway Networks (HSRNs)", "Mobile Edge Computing (MEC)", "Multiple Agent", "Reinforcement Learning"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1275 — Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks

## Metadata

- **Authors:** Wu, Yingying and Zhang, Zhifei and Ge, Yiyang and Mao, Jin and Chu, Zhipeng and Xiong, Ke and Fan, Pingyi
- **Year:** 2024
- **Venue:** 2024 9th International Conference on Computer and Communication Systems, ICCCS 2024
- **DOI:** 10.1109/ICCCS61882.2024.10603138
- **URL:** https://www.scopus.com/pages/publications/85201318830?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 718--724
- **Language:** English
- **Keywords:** Age of Information (AoI); High-Speed Railway Networks (HSRNs); Mobile Edge Computing (MEC); Multiple Agent; Reinforcement Learning

### Abstract

This paper investigates mobile edge computing (MEC) assisted high-speed railway networks (HSRNs), where a MEC server positioned at the ground base station (GBS) assists train users in task computing. When the computing capacity of users' equipment is insufficient, the users are allowed to offload their tasks to the MEC server. To well measure the timeliness of users' task computation, we extend the traditional age of information (AoI) to the concept of age of computing (AoC), which is defined as the time elapsed since the last completed task was generated. To pursue the green HSRN design, this paper formulates an energy minimization problem by jointly optimizing task offloading vectors and power allocation vectors. To ensure the timeliness of task execution, AoC is taken as constraints into account. Besides, the maximum available power constraints are also considered. To tackle this non-convex mixed integer nonlinear programming (MINLP) problem, we firstly reformulate it as a Markov Decision Process (MDP) and then propose a Multi-Agent Twin Delayed Deep Deterministic Policy Gradient based resource allocation (MATD3-RA) framework. To characterize the energy consumption of user equipment under the constraints of AoC, we define a utility function as the negative linear combination of the violation of AoC constraints and the energy consumption. Simulation results show that the utility function value of the proposed MATD3-RA is increased by about 14% and about 39% respectively compared to the resource allocation with only MEC and local computing, about 23% compared to the Multi-agent Deep Deterministic Policy Gradient based resource allocation (MADDPG-RA) method, and about 28% compared to the random power allocation method. We also observe that there is a trade-off between energy consumption and AoC. © 2024 IEEE.

## 04 — Title Screening

**Title:** Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Age-of-Computing Constrained Energy-minimal Resource Allocation in MEC-Assisted High-Speed Railway Networks
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
