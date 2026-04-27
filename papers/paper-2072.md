---
id: "paper-2072"
title: "Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments"
authors: ["Rasool, Hussein Ali", "Abdul-Sadah, Ali Muhssen", "Taha, Mohand S.", "Najim, Ali Hamzah", "Said, Maizatul Alice Meor"]
year: 2025
venue: "International Journal of Intelligent Engineering and Systems"
venue_type: "journal"
doi: "10.22266/ijies2025.1130.62"
url: "https://www.scopus.com/pages/publications/105019569945?origin=resultslist"
publisher: "Intelligent Network and Systems Society"
pages: "987--999"
keywords: ["Adaptive traffic management", "City traffic", "Intelligent signals", "Learning agents", "Real-time response"]
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
    human_decision: "exclude"
    human_justification: "RL"

---

# paper-2072 — Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments

## Metadata

- **Authors:** Rasool, Hussein Ali and Abdul-Sadah, Ali Muhssen and Taha, Mohand S. and Najim, Ali Hamzah and Said, Maizatul Alice Meor
- **Year:** 2025
- **Venue:** International Journal of Intelligent Engineering and Systems
- **DOI:** 10.22266/ijies2025.1130.62
- **URL:** https://www.scopus.com/pages/publications/105019569945?origin=resultslist
- **Publisher:** Intelligent Network and Systems Society
- **Pages:** 987--999
- **Language:** English
- **Keywords:** Adaptive traffic management; City traffic; Intelligent signals; Learning agents; Real-time response

### Abstract

The growth of urban mobility and networked vehicles has expedited the need for smart traffic management systems that can operate optimally in the next-generation wireless environment. This paper introduces an innovative Multi-Agent Reinforcement Learning (MARL) system for real-time traffic signal control in 6G-enabled Vehicular Ad Hoc Networks (VANETs). In contrast to conventional approaches that optimize solely traffic-related metrics like delay or queue length, the presented system adopts traffic-oriented and communication-aware metrics such as average waiting time, congestion index, packet delivery ratio, and bandwidth utilization under a common reward framework. Dynamic scalarization allows MARL agents to adaptively weigh these objectives based on real-time traffic and network conditions. The proposed framework was validated using four datasets: the Vehicular Network State Dataset (Kaggle), Secure VANET Vehicle Dataset, VANET Real-Time Route Optimization Dataset, and 5G-VANET MEC Dataset. All traffic signals are designed as independent MARL agents, learning signal phases based on local observations and fast inter-agent communication via 6G links. The innovation is the simultaneous optimization of vehicle flow and network-level performance for end-to-end real-time coordination and scalability in highly dense urban VANET environments. Compared to standard fixed-time control algorithms, MA2C, DQN-based controllers on the same dataset, the suggested framework provides an 32.6% decrease in mean waiting time, a noteworthy reduction in congestion, a 21.4% increase in packet delivery ratio, and a 27.8% increase in bandwidth efficiency. The results confirm the framework’s robustness and generalizability across diverse VANET scenarios. © This article is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License. License details: https://creativecommons.org/licenses/by-sa/4.0/

## 04 — Title Screening

**Title:** Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.5
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=0.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Multi-agent Reinforcement Learning for Real-time Traffic Control in 6G-Enabled VANET Environments
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)

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
