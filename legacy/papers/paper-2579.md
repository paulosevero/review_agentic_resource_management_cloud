---
id: "paper-2579"
title: "Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network"
authors: ["Gao, Yunfei", "Wu, Peng", "Yuan, Xiaopeng", "Hu, Yulin", "Cao, Xiaoxiang", "Schmeink, Anke"]
year: 2026
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2026.3656412"
url: "https://www.scopus.com/pages/publications/105028518205?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["3D deployment and association", "federated MADRL", "MEC", "Multi-UAV", "no-fly zones"]
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
    final_score: 0.6667
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-2579 — Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network

## Metadata

- **Authors:** Gao, Yunfei and Wu, Peng and Yuan, Xiaopeng and Hu, Yulin and Cao, Xiaoxiang and Schmeink, Anke
- **Year:** 2026
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2026.3656412
- **URL:** https://www.scopus.com/pages/publications/105028518205?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** 3D deployment and association; federated MADRL; MEC; Multi-UAV; no-fly zones

### Abstract

We investigate a multi-unmanned aerial vehicle (UAV)-aided mobile edge computing (MEC) system where UAVs provide to ground devices (GDs) comprehensive services, including communication, computation, and joint decision-making (CCJD). Specifically, the system is dynamic and heterogeneous, with time-varying task requests and UAVs of diverse capabilities, data processing requirements, and priorities. To enhance the task execution efficiency, we provide a joint optimization design that minimizes the average system operation time by optimizing UAVs' three-dimensional (3D) deployment and GDs association, while adhering to no-fly zones (NFZs) and obstacle constraints. Nevertheless, the formulated problem exhibits high non-convexity with a rapidly scaling complexity w.r.t. the number of both UAVs and GDs. To address the challenges, we propose an efficient and low-complexity learning-based approach accelerated by analytical characterizations on GD's association to enhance algorithm convergence. First, we derive a closed-form solution for GD's association based on the Lagrangian dual method and optimal transmission theory (OTT). We also analytically derive the performance gap between the closed-form association and the optimal exhaustive search-based solution. Theoretical analysis demonstrates that our proposed approach achieves substantial complexity reduction compared to exhaustive search, while almost achieving the same performance. Based on the characterized optimal association, we reformulate the original joint design problem equivalently into a UAV 3D deployment optimization problem without loss of optimality, which is further established as a Markov decision process (MDP). Afterwards, an efficient algorithm based on the proposed federated multi-agent deep reinforcement learning algorithm is proposed to solve the reformulated problem, where the reward function is designed based on the closed-form GD's association and its corresponding average delay, leveraging the dueling network architecture to enhance training stability and accelerate convergence. Finally, simulation results demonstrate the superior performance of the proposed method compared to the benchmarks. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network
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
