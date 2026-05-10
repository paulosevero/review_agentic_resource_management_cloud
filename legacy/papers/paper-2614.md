---
id: "paper-2614"
title: "KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems"
authors: ["Huang, Congyue", "Tan, Wei", "Ou, Miaohua", "Yang, Erfu", "Li, Yun"]
year: 2026
venue: "IEEE Internet of Things Journal"
venue_type: "journal"
doi: "10.1109/JIOT.2026.3658608"
url: "https://www.scopus.com/pages/publications/105028891283?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["Edge computing", "Kubernetes", "multi-agent proximal policy optimization", "reinforcement learning"]
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

# paper-2614 — KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems

## Metadata

- **Authors:** Huang, Congyue and Tan, Wei and Ou, Miaohua and Yang, Erfu and Li, Yun
- **Year:** 2026
- **Venue:** IEEE Internet of Things Journal
- **DOI:** 10.1109/JIOT.2026.3658608
- **URL:** https://www.scopus.com/pages/publications/105028891283?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** Edge computing; Kubernetes; multi-agent proximal policy optimization; reinforcement learning

### Abstract

Kubernetes (K8s) provides the foundation for integrating distributed edge-cloud resources. However, existing frameworks struggle to address the challenges of cross-cluster coordination and dynamic resource changes, limiting throughput. We propose KMPS, a deep reinforcement learning-based scheduling framework to enhance long-term throughput. KMPS integrates a multi-agent proximal policy optimization algorithm for autonomous edge access point scheduling, combined with gRPC cross-cluster scheduling and invalid target filtering; utilizes graph neural networks to embed system state information, decomposing high-dimensional service orchestration actions through multiple separate policy networks; and constructs a three-time-scale coordination mechanism (0.25s, 2s, 25s) to coordinate scheduling and orchestration, with K8s compatibility. Experiments on real workloads verify that KMPS operates stably under dynamic loads, sudden emergency tasks, and multi-cluster scenarios. Compared to baselines, the proposed framework achieves an over 5.3% increase in long-term throughput and a 60% reduction in cross-cluster scheduling latency. © 2014 IEEE.

## 04 — Title Screening

**Title:** KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=0.0 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** KMPS: A Reinforcement Learning Scheduler for Kubernetes Edge-Cloud Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
