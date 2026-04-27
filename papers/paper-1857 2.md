---
id: "paper-1857"
title: "Multi-Agent Computing-Energy-Efficiency Optimization in Vehicular Edge Computing: Non-Cooperative Versus Cooperative Solutions"
authors: ["Lin, Yan", "Xiao, Liqin", "Tao, Yiyu", "Zhang, Yijin", "Shu, Feng", "Li, Jun"]
year: 2025
venue: "IEEE Transactions on Wireless Communications"
venue_type: "journal"
doi: "10.1109/TWC.2025.3547377"
url: "https://www.scopus.com/pages/publications/105000043262?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5461--5476"
keywords: ["computation energy efficiency", "graph attention networks", "multi-agent reinforcement learning", "task offloading", "Vehicular edge computing"]
language: "English"
source:
  databases: ["Scopus"]
  exports: ["scopus-2026-04-26.bib"]
  dedup:
    merged_from: []
    merge_reason: ""
status:
  "04-title-screening": include
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
    human_decision: ""
    human_justification: ""

---

# paper-1857 — Multi-Agent Computing-Energy-Efficiency Optimization in Vehicular Edge Computing: Non-Cooperative Versus Cooperative Solutions

## Metadata

- **Authors:** Lin, Yan and Xiao, Liqin and Tao, Yiyu and Zhang, Yijin and Shu, Feng and Li, Jun
- **Year:** 2025
- **Venue:** IEEE Transactions on Wireless Communications
- **DOI:** 10.1109/TWC.2025.3547377
- **URL:** https://www.scopus.com/pages/publications/105000043262?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5461--5476
- **Language:** English
- **Keywords:** computation energy efficiency; graph attention networks; multi-agent reinforcement learning; task offloading; Vehicular edge computing

### Abstract

Vehicular edge computing (VEC) has driven the proliferation of computation-intensive and delay-sensitive vehicular services by deploying computing and energy resources at the edge. However, the exploitation of edge resources faces challenges due to unpredictable environmental dynamics and partial observability. To this end, this paper investigates the computing energy efficiency (CEE) problem in twin-timescale VEC scenarios by dynamically adjusting the offloading policy. Based upon modeling the problem as a decentralized partially observable Markov decision process (Dec-POMDP), a pair of non-cooperative and cooperative offloading solutions are proposed relying on multi-agent reinforcement learning (MARL), respectively. Specifically, the non-cooperative solution employs multi-agent independent proximal policy optimization (IPPO) to enable vehicular user equipments (VUEs) to learn their policies in a fully distributed manner without any information sharing. By contrast, the cooperative solution combines the multi-agent shared PPO with graph attention networks (MAPPO-GAT), where the relationship among agents is learned cooperatively and the historical learning experience is shared. Additionally, we compare the computational complexity and analyze the convergence. Simulation results show that in terms of the trade-off between offloading delay and offloading energy consumption, the proposed cooperative solution is superior to the non-cooperative counterpart with the cost of moderate training overhead for cooperative learning. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Multi-Agent Computing-Energy-Efficiency Optimization in Vehicular Edge Computing: Non-Cooperative Versus Cooperative Solutions

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Computing-Energy-Efficiency Optimization in Vehicular Edge Computing: Non-Cooperative Versus Cooperative Solutions
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Computing-Energy-Efficiency Optimization in Vehicular Edge Computing: Non-Cooperative Versus Cooperative Solutions
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
