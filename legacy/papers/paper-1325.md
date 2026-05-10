---
id: "paper-1325"
title: "A Method for Joint Edge Server Deployment and Service Placement"
authors: ["Zhang, Junna", "Han, Chaochen", "Chen, Jiawei", "Zhao, Xiaoyan", "Yuan, Peiyan"]
year: 2024
venue: "Jisuanji Gongcheng/Computer Engineering"
venue_type: "journal"
doi: "10.19678/j.issn.1000-3428.0068576"
url: "https://www.scopus.com/pages/publications/85210251812?origin=resultslist"
publisher: "Editorial Office of Computer Engineering"
pages: "266--280"
keywords: ["Edge Computing(EC)", "Edge Server(ES) deployment", "k-means clustering algorithm", "multi-agent reinforcement learning algorithm", "service placement"]
language: "Chinese"
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

# paper-1325 — A Method for Joint Edge Server Deployment and Service Placement

## Metadata

- **Authors:** Zhang, Junna and Han, Chaochen and Chen, Jiawei and Zhao, Xiaoyan and Yuan, Peiyan
- **Year:** 2024
- **Venue:** Jisuanji Gongcheng/Computer Engineering
- **DOI:** 10.19678/j.issn.1000-3428.0068576
- **URL:** https://www.scopus.com/pages/publications/85210251812?origin=resultslist
- **Publisher:** Editorial Office of Computer Engineering
- **Pages:** 266--280
- **Language:** Chinese
- **Keywords:** Edge Computing(EC); Edge Server(ES) deployment; k-means clustering algorithm; multi-agent reinforcement learning algorithm; service placement

### Abstract

Edge Computing (EC) deploys Edge Servers (ES) at the edge of the network close to the user. Services are placed on the ES to meet users' service needs. Several independent studies have been conducted on ES deployment and service placement. However, a highly coupled relationship exists between the two and they should be studied simultaneously. In addition, the economic benefit of the EC system is a consideration because paid services must be provided for the EC system to earn revenue in processing user service requests; however, the EC system incurs delays and energy costs when processing the user service requests. To maximize the benefits of the EC system under the constraint that user service requests and service prices are different, appropriate service placement solutions are required to increase the overall profit. To that end, this study considers the constraints of the location relationship between ES and base stations, coupling relationship between ES deployment and service placement, number of service replicas, and price of the service and proposes a two-step approach that includes an improved k-means algorithm and a multi-agent reinforcement learning algorithm. The goal is to maximize the benefits of EC systems. First, a joint ES deployment and service placement model is constructed. One of the ES deployments explicitly considers the location relationship between base stations, whereas service placement considers the location of ES deployments as well as different service requests and pricing. Subsequently, based on the location relationship of base stations and service request load of base stations, the k-means algorithm is used under constraints to determine the optimal deployment location and collaborative domain of ES under different constraint conditions. Finally, to maximize the benefits of the EC system, a multi-agent reinforcement learning algorithm is used to place services on the ES. The experimental results show that the proposed algorithm increases the benefits by 7% to 23% relative to the comparison algorithms. © 2024, Editorial Office of Computer Engineering. All rights reserved.

## 04 — Title Screening

**Title:** A Method for Joint Edge Server Deployment and Service Placement

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Method for Joint Edge Server Deployment and Service Placement
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** A Method for Joint Edge Server Deployment and Service Placement
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
