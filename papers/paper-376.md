---
id: "paper-376"
title: "Learning-Based Computation Offloading Approaches in UAVs-Assisted Edge Computing"
authors: ["Zhu, Shichao", "Gui, Lin", "Zhao, Dongmei", "Cheng, Nan", "Zhang, Qi", "Lang, Xiupu"]
year: 2021
venue: "IEEE Transactions on Vehicular Technology"
venue_type: "journal"
doi: "10.1109/TVT.2020.3048938"
url: "https://www.scopus.com/pages/publications/85099260066?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "928--944"
keywords: ["Bandwidth allocation", "computation offloading", "inter-dependencies", "multi-agent reinforcement learning", "UAV"]
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

# paper-376 — Learning-Based Computation Offloading Approaches in UAVs-Assisted Edge Computing

## Metadata

- **Authors:** Zhu, Shichao and Gui, Lin and Zhao, Dongmei and Cheng, Nan and Zhang, Qi and Lang, Xiupu
- **Year:** 2021
- **Venue:** IEEE Transactions on Vehicular Technology
- **DOI:** 10.1109/TVT.2020.3048938
- **URL:** https://www.scopus.com/pages/publications/85099260066?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 928--944
- **Language:** English
- **Keywords:** Bandwidth allocation; computation offloading; inter-dependencies; multi-agent reinforcement learning; UAV

### Abstract

Technological evolutions in unmanned aerial vehicle (UAV) industry have granted UAVs more computing and storage resources, leading to the vision of UAVs-assisted edge computing, in which the computing missions can be offloaded from a cellular network to a UAV cloudlet. In this paper, we propose a UAVs-assisted computation offloading paradigm, where a group of UAVs fly around, while providing value-added edge computing services. The complex computing missions are decomposed as some typical task-flows with inter-dependencies. By taking into consideration the inter-dependencies of the tasks, dynamic network states, and energy constraints of the UAVs, we formulate the average mission response time minimization problem and then model it as a Markov decision process. Specifically, each time a mission arrives or a task execution finishes, we should decide the target helper for the next task execution and the fraction of the bandwidth allocated to the communication. To separate the evaluation of the integrated decision, we propose multi-agent reinforcement learning (MARL) algorithms, where the target helper and the bandwidth allocation are determined by two agents. We design respective advantage evaluation functions for the agents to solve the multi-agent credit assignment challenge, and further extend the on-policy algorithm to off-policy. Simulation results show that the proposed MARL-based approaches have desirable convergence property, and can adapt to the dynamic environment. The proposed approaches can significantly reduce the average mission response time compared with other benchmark approaches. © 1967-2012 IEEE.

## 04 — Title Screening

**Title:** Learning-Based Computation Offloading Approaches in UAVs-Assisted Edge Computing

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Learning-Based Computation Offloading Approaches in UAVs-Assisted Edge Computing
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Learning-Based Computation Offloading Approaches in UAVs-Assisted Edge Computing
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
