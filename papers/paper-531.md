---
id: "paper-531"
title: "Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms"
authors: ["Zafeiropoulos, Anastasios", "Fotopoulou, Eleni", "Filinis, Nikos", "Papavassiliou, Symeon"]
year: 2022
venue: "Simulation Modelling Practice and Theory"
venue_type: "journal"
doi: "10.1016/j.simpat.2021.102461"
url: "https://www.scopus.com/pages/publications/85122667567?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Autoscaling", "Intelligent orchestration", "Reinforcement learning", "Serverless application", "Serverless computing"]
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

# paper-531 — Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms

## Metadata

- **Authors:** Zafeiropoulos, Anastasios and Fotopoulou, Eleni and Filinis, Nikos and Papavassiliou, Symeon
- **Year:** 2022
- **Venue:** Simulation Modelling Practice and Theory
- **DOI:** 10.1016/j.simpat.2021.102461
- **URL:** https://www.scopus.com/pages/publications/85122667567?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Autoscaling; Intelligent orchestration; Reinforcement learning; Serverless application; Serverless computing

### Abstract

Serverless computing is emerging as a cloud computing paradigm that provisions computing resources on demand, while billing is taking place based on the exact usage of the cloud resources. The responsibility for infrastructure management is undertaken by cloud providers, enabling developers to focus on the development of the business logic of their applications. For managing scalability, various autoscaling mechanisms have been proposed that try to optimize the provisioning of resources based on the posed workload. These mechanisms are configured and managed by the cloud provider, imposing non negligible administration overhead. A set of challenges are identified for introducing automation and optimizing the provisioning of resources, while in parallel respecting the agreed Service Level Agreement between cloud and application providers. To address these challenges, we have developed autoscaling mechanisms for serverless applications that are powered by Reinforcement Learning (RL) techniques. A set of RL environments and agents have been implemented (based on Q-learning, DynaQ+ and Deep Q-learning algorithms) for driving autoscaling mechanisms, able to autonomously manage dynamic workloads with Quality of Service (QoS) guarantees, while opting for efficient usage of resources. The produced environments and agents are evaluated in real and simulated environments, taking advantage of the Kubeless open-source serverless platform. The evaluation results validate the suitability of the proposed mechanisms to efficiently tackle scalability management for serverless applications. © 2022 Elsevier B.V.

## 04 — Title Screening

**Title:** Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Reinforcement learning-assisted autoscaling mechanisms for serverless computing platforms
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
