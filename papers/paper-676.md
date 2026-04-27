---
id: "paper-676"
title: "Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management"
authors: ["Ma\u0142ota, Andrzej", "Koperek, Pawe\u0142", "Funika, W\u0142odzimierz"]
year: 2023
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-031-36021-3_55"
url: "https://www.scopus.com/pages/publications/85169661987?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "561--575"
keywords: ["cloud resource management", "deep neural networks", "deep reinforcement learning", "explainable artificial intelligence", "explainable reinforcement learning"]
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

# paper-676 — Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management

## Metadata

- **Authors:** Małota, Andrzej and Koperek, Paweł and Funika, Włodzimierz
- **Year:** 2023
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-031-36021-3_55
- **URL:** https://www.scopus.com/pages/publications/85169661987?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 561--575
- **Language:** English
- **Keywords:** cloud resource management; deep neural networks; deep reinforcement learning; explainable artificial intelligence; explainable reinforcement learning

### Abstract

Cloud computing resource management is a critical component of the modern cloud computing platforms, aimed to manage computing resources for a given application by minimizing the cost of the infrastructure while maintaining a Quality-of-Service (QoS) conditions. This task is usually solved using rule-based policies. Due to their limitations more complex solutions, such as Deep Reinforcement Learning (DRL) agents are being researched. Unfortunately, deploying such agents in a production environment can be seen as risky because of the lack of transparency of DRL decision-making policies. There is no way to know why a certain decision is made. To foster the trust in DRL generated policies it is important to provide means of explaining why certain decisions were made given a specific input. In this paper we present a tool applying the Integrated Gradients (IG) method to Deep Neural Networks used by DRL algorithms. This allowed to obtain feature attributions that show the magnitude and direction of each feature’s influence on the agent’s decision. We verify the viability of the proposed solution by applying it to a number of sample use cases with different DRL agents. © 2023, The Author(s), under exclusive license to Springer Nature Switzerland AG.

## 04 — Title Screening

**Title:** Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Towards Understanding of Deep Reinforcement Learning Agents Used in Cloud Resource Management
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
