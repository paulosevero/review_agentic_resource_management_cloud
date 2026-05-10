---
id: "paper-1037"
title: "Reliability-assured service function chain migration strategy in edge networks using deep reinforcement learning"
authors: ["Li, Yilin", "Zhang, Peiying", "Kumar, Neeraj", "Guizani, Mohsen", "Wang, Jian", "Kostromitin, Konstantin Igorevich", "Wang, Yi", "Tan, Lizhuang"]
year: 2024
venue: "Journal of Network and Computer Applications"
venue_type: "journal"
doi: "10.1016/j.jnca.2024.103999"
url: "https://www.scopus.com/pages/publications/85201462829?origin=resultslist"
publisher: "Academic Press"
pages: ""
keywords: ["Edge network", "Network function virtualization", "Reliability", "Service function chain migration"]
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

# paper-1037 — Reliability-assured service function chain migration strategy in edge networks using deep reinforcement learning

## Metadata

- **Authors:** Li, Yilin and Zhang, Peiying and Kumar, Neeraj and Guizani, Mohsen and Wang, Jian and Kostromitin, Konstantin Igorevich and Wang, Yi and Tan, Lizhuang
- **Year:** 2024
- **Venue:** Journal of Network and Computer Applications
- **DOI:** 10.1016/j.jnca.2024.103999
- **URL:** https://www.scopus.com/pages/publications/85201462829?origin=resultslist
- **Publisher:** Academic Press
- **Pages:** 
- **Language:** English
- **Keywords:** Edge network; Network function virtualization; Reliability; Service function chain migration

### Abstract

With the widespread adoption of edge computing and the rollout of 5G technology, the edge network is experiencing rapid growth. Edge computing enables the execution of certain computational tasks on edge devices, fostering more efficient resource utilization. However, the reliability of the edge network is constrained by its network connections. Network instability can significantly compromise service quality. An effective service function chain (SFC) migration algorithm is essential to optimize resource utilization, enhance service quality. This paper begins by analyzing the current research landscape of edge networks and SFC migration algorithms. Subsequently, the challenges associated with edge network and SFC migration are formally articulated, leading to the proposal of a SFC migration algorithm based on deep reinforcement learning (DRL) with a focus on reliability assurance (RA-SFCM). The algorithm leverages multi-agent deep reinforcement learning to dynamically perceive changes in the edge network environment. It introduces an advantage function to evaluate the performance of each agent relative to the average level and incorporates a central attention mechanism with multiple attention heads to better capture the interdependencies and relationships among different agents. Additionally, this paper innovatively defines and quantifies the reliability of the migration process. By introducing a reliability penalty mechanism based on the migration target nodes and link capacity, it enhances the reliability of the migration schemes. The experimental results conclusively demonstrate the remarkable advantages of the RA-SFCM algorithm in terms of real-time performance, resource utilization efficiency, and reliability. Compared to algorithms such as Sa-VNFM, ROVM, and DLTSAC, RA-SFCM exhibits superior performance. For RA-SFCM, the optimized deployment migration strategy enhances real-time performance, precise resource management improves utilization efficiency, and advanced fault tolerance mechanisms strengthen reliability. © 2024 Elsevier Ltd

## 04 — Title Screening

**Title:** Reliability-assured service function chain migration strategy in edge networks using deep reinforcement learning

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Reliability-assured service function chain migration strategy in edge networks using deep reinforcement learning
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Reliability-assured service function chain migration strategy in edge networks using deep reinforcement learning
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
