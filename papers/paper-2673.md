---
id: "paper-2673"
title: "Networked Edge Resource Orchestration for Mobile AI-Generated Content Services"
authors: ["Liang, Yuxin", "Yang, Peng", "Dai, Xiangxiang", "He, Yuanyuan", "Lyu, Feng"]
year: 2026
venue: "IEEE Transactions on Cognitive Communications and Networking"
venue_type: "journal"
doi: "10.1109/TCCN.2025.3643988"
url: "https://www.scopus.com/pages/publications/105025452719?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "5063--5076"
keywords: ["AIGC", "edge networks", "fairness", "model deployment", "resource allocation"]
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

# paper-2673 — Networked Edge Resource Orchestration for Mobile AI-Generated Content Services

## Metadata

- **Authors:** Liang, Yuxin and Yang, Peng and Dai, Xiangxiang and He, Yuanyuan and Lyu, Feng
- **Year:** 2026
- **Venue:** IEEE Transactions on Cognitive Communications and Networking
- **DOI:** 10.1109/TCCN.2025.3643988
- **URL:** https://www.scopus.com/pages/publications/105025452719?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 5063--5076
- **Language:** English
- **Keywords:** AIGC; edge networks; fairness; model deployment; resource allocation

### Abstract

In this paper, we design an edge-assisted mobile Artificial Intelligence-Generated Content (AIGC) service system. The core of this system is the orchestrated multi-dimensional resource allocation and generative AI model deployment for efficient AIGC service provisioning at the edge. The heterogeneous resource demands of these models strain scarce resources of edge servers. This scarcity calls for a resource-efficient allocation policy whose goal conflicts with ensuring resource fairness for tasks requested by concurrent users. Specifically, such a policy risks enabling resource monopolization by certain tasks, starving others. To address these challenges, we start by characterizing behaviors of the resource demand, fairness-efficiency trade-off and model deployment, including the dominant resource and recency-aware model reuse. Accordingly, the system incorporates two key modules that work in tandem: an Elastic Multi-Resource Allocator, employs a \delta -fairness elastic allocation policy to balance fairness and efficiency by controlling deviations from absolute fairness; and a Model Deployment Manager, updates deployment status by adapting model recency and storage cost. To jointly optimize the actions of both modules, we formulate a mixed-integer nonlinear programming problem. Considering timescale decoupling between the per-slot resource allocation and sporadic model deployment, we decouple it into two subproblems and solve them via meta-heuristics and progressive filling. Extensive experimental results reveal the effectiveness of our system, which improves the utility of resource allocation by up to 17.39%, and the utility of model deployment by 11.22% while ensuring fairness, as well as its scalability under increased user concurrency. © 2015 IEEE.

## 04 — Title Screening

**Title:** Networked Edge Resource Orchestration for Mobile AI-Generated Content Services

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.5 C2=1.0 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Networked Edge Resource Orchestration for Mobile AI-Generated Content Services
- **Rationale:** C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Networked Edge Resource Orchestration for Mobile AI-Generated Content Services
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
