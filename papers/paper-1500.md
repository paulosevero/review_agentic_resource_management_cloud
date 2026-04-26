---
id: "paper-1500"
title: "Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing"
authors: ["Cui, Hanshuai", "Tang, Zhiqing", "Wu, Yuan", "Jia, Weijia"]
year: 2025
venue: "IEEE Transactions on Mobile Computing"
venue_type: "journal"
doi: "10.1109/TMC.2025.3583153"
url: "https://www.scopus.com/pages/publications/105009746660?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "12314--12328"
keywords: ["Container update", "edge computing", "edge-cloud collaboration", "layer sharing", "reinforcement learning"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-1500 — Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing

## Metadata

- **Authors:** Cui, Hanshuai and Tang, Zhiqing and Wu, Yuan and Jia, Weijia
- **Year:** 2025
- **Venue:** IEEE Transactions on Mobile Computing
- **DOI:** 10.1109/TMC.2025.3583153
- **URL:** https://www.scopus.com/pages/publications/105009746660?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 12314--12328
- **Language:** English
- **Keywords:** Container update; edge computing; edge-cloud collaboration; layer sharing; reinforcement learning

### Abstract

Containers have become popular for deploying applications in Edge Computing (EC) for their seamless integration and easy deployment. Frequent container updates are essential to enhance performance and introduce new challenges for cutting-edge applications such as large language models and digital twins. However, traditional container update methods result in substantial download costs and task interruptions, which are unacceptable for latency-sensitive tasks in resource-constrained EC. Existing work has largely overlooked the layered structure of container images. By leveraging this layered structure, duplicate downloads can be reduced, and various layers can be transferred from other edges, reducing burden on the remote cloud. In this paper, we model the layer-aware container update problem with edge-cloud collaboration to minimize update and scheduling costs. We present the Layer-aware Edge-cloud collaborative Container Update (LECU) algorithm based on reinforcement learning to make container update decisions. Moreover, a task scheduling algorithm is devised to schedule tasks affected by container updates to other edges, minimizing the impact of task interruptions. We implement our LECU algorithm on an edge system with real-world data traces to demonstrate its effectiveness and conduct larger-scale simulations to evaluate its scalability. Results demonstrate that our algorithms reduce container update and task scheduling costs by 14% and 19%, respectively, compared to baselines. © 2002-2012 IEEE.

## 04 — Title Screening

**Title:** Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Layer-Aware Cost-Effective Container Updates With Edge-Cloud Collaboration in Edge Computing
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
