---
id: "paper-485"
title: "Learning-based Multi-Drone Network Edge Orchestration for Video Analytics"
authors: ["Qu, Chengyi", "Singh, Rounak", "Esquivel-Morel, Alicia", "Calyam, Prasad"]
year: 2022
venue: "Proceedings - IEEE INFOCOM"
venue_type: "conference"
doi: "10.1109/INFOCOM48880.2022.9796706"
url: "https://www.scopus.com/pages/publications/85133283256?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "1219--1228"
keywords: ["Multi-access edge computing", "Multi-drone networks", "Network protocols", "Reinforcement learning"]
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
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-485 — Learning-based Multi-Drone Network Edge Orchestration for Video Analytics

## Metadata

- **Authors:** Qu, Chengyi and Singh, Rounak and Esquivel-Morel, Alicia and Calyam, Prasad
- **Year:** 2022
- **Venue:** Proceedings - IEEE INFOCOM
- **DOI:** 10.1109/INFOCOM48880.2022.9796706
- **URL:** https://www.scopus.com/pages/publications/85133283256?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 1219--1228
- **Language:** English
- **Keywords:** Multi-access edge computing; Multi-drone networks; Network protocols; Reinforcement learning

### Abstract

Unmanned aerial vehicles (a.k.a. drones) with high-resolution video cameras are useful for applications in e.g., public safety and smart farming. Inefficient configurations in drone video analytics applications due to edge network miscon-figurations can result in degraded video quality and inefficient resource utilization. In this paper, we present a novel scheme for offline/online learning-based network edge orchestration to achieve pertinent selection of both network protocols and video properties in multi-drone based video analytics. Our approach features both supervised and unsupervised machine learning algorithms to enable decision making for selection of both network protocols and video properties in the drones' pre-takeoff stage i.e., offline stage. In addition, our approach facilitates drone trajectory optimization during drone flights through an online reinforcement learning-based multi-agent deep Q-network algorithm. Evaluation results show how our offline orchestration can suitably choose network protocols (i.e., amongst TCP/HTTP, UDP/RTP, QUIC). We also demonstrate how our unsupervised learning approach outperforms existing learning approaches, and achieves efficient offloading while also improving the network performance (i.e., throughput and round-trip time) by least 25% with satisfactory video quality. Lastly, we show via trace-based simulations, how our online orchestration achieves 91% of oracle baseline network throughput performance with comparable video quality. © 2022 IEEE.

## 04 — Title Screening

**Title:** Learning-based Multi-Drone Network Edge Orchestration for Video Analytics

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Learning-based Multi-Drone Network Edge Orchestration for Video Analytics
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Learning-based Multi-Drone Network Edge Orchestration for Video Analytics
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
