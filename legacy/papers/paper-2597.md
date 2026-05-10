---
id: "paper-2597"
title: "Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing"
authors: ["He, Yifan", "Xu, Zhan", "Lin, Jian", "Li, Yuanzhuang", "Zhang, Shiyu"]
year: 2026
venue: "Neurocomputing"
venue_type: "journal"
doi: "10.1016/j.neucom.2026.133115"
url: "https://www.scopus.com/pages/publications/105030879198?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Deep reinforcement learning", "Dynamic workflow scheduling", "Fog computing", "Genetic programming"]
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

# paper-2597 — Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing

## Metadata

- **Authors:** He, Yifan and Xu, Zhan and Lin, Jian and Li, Yuanzhuang and Zhang, Shiyu
- **Year:** 2026
- **Venue:** Neurocomputing
- **DOI:** 10.1016/j.neucom.2026.133115
- **URL:** https://www.scopus.com/pages/publications/105030879198?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Deep reinforcement learning; Dynamic workflow scheduling; Fog computing; Genetic programming

### Abstract

Dynamic workflow scheduling in distributed fog computing (DWSDFC) is a critical optimization problem with significant implications for meeting the computational demands of modern applications. The dynamic and distributed nature of DWSDFC renders it a highly challenging task, particularly difficult to address using traditional scheduling methods. Recently, deep reinforcement learning (DRL) has emerged as a powerful solution for dynamic scheduling problems, selecting appropriate scheduling rules as actions at various decision points. The effectiveness of DRL is largely determined by these scheduling rules. However, these scheduling rules are often manually designed and require substantial domain expertise. For this reason, this study concentrates on automating the design of DRL actions to boost its problem-solving performance. First, DWSDFC is formulated as a decentralized partially observable Markov decision process. Then, a multi-agent DRL framework is proposed, incorporating a routing agent and a sequencing agent to tackle DWSDFC. Specifically, the actions in the sequencing agent are generated using an evolutionary algorithm known as genetic programming (GP). To enhance the diversity of this evolved action set and consequently the performance of DRL, a niching technique based on behavioral differences between actions is integrated into GP. Extensive experimental results on a variety of DWSDFC instances demonstrate the effectiveness of the proposed method over common scheduling rules as well as the state-of-the-art DRL and GP methods. © 2026 Elsevier B.V.

## 04 — Title Screening

**Title:** Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Deep reinforcement learning with evolved actions for dynamic workflow scheduling in distributed fog computing
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
