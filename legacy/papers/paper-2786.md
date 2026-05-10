---
id: "paper-2786"
title: "Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning"
authors: ["Sun, Yunhe", "Wang, Yu", "Hawbani, Ammar", "Hao, Fei", "Othman, Wajdy", "Yang, Dongsheng", "Zhao, Liang"]
year: 2026
venue: "Computer Networks"
venue_type: "journal"
doi: "10.1016/j.comnet.2026.112282"
url: "https://www.scopus.com/pages/publications/105035101196?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Deep reinforcement learning", "Energy optimization", "Satellite edge computing", "Task offloading"]
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

# paper-2786 — Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning

## Metadata

- **Authors:** Sun, Yunhe and Wang, Yu and Hawbani, Ammar and Hao, Fei and Othman, Wajdy and Yang, Dongsheng and Zhao, Liang
- **Year:** 2026
- **Venue:** Computer Networks
- **DOI:** 10.1016/j.comnet.2026.112282
- **URL:** https://www.scopus.com/pages/publications/105035101196?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Deep reinforcement learning; Energy optimization; Satellite edge computing; Task offloading

### Abstract

Low Earth orbit (LEO) satellite constellations face stringent constraints on energy and computational resources during long-term operation. Among these constraints, the lifetime of onboard batteries is a key factor limiting satellite service duration. As the intensity of computational tasks increases, onboard data processing has become a major source of energy consumption, further exacerbating battery energy constraints. To this end, this paper proposes a three-layer heterogeneous Satellite Mobile Edge Computing (SMEC) architecture to address these challenges, integrating Ground Stations (GS), Remote Sensing Satellites (RSS), and Computing Satellites (CS). The proposed architecture minimizes local computational load while extending battery lifespan. A joint optimization model incorporates key performance indicators including energy consumption, latency, task loss, and battery Depth of Discharge (DoD). Based on this model, and considering the dynamic complexity of satellite networks, we develop a computation offloading strategy using the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. This strategy enables RSS to autonomously determine optimal offloading decisions in dynamic environments, facilitating multi-agent collaborative optimization. Simulation results confirm the proposed method's superior prformance over benchmark algorithms in task latency, energy efficiency, task loss rate, and DoD management, while significantly extending satellite lifespan. © 2026

## 04 — Title Screening

**Title:** Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Dynamic task offloading in satellite edge computing: Energy optimization through deep reinforcement learning
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
