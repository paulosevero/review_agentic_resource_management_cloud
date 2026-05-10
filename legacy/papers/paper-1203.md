---
id: "paper-1203"
title: "Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement"
authors: ["Soumplis, Polyzois", "Kontos, Georgios", "Kokkinos, Panagiotis", "Kretsis, Aristotelis", "Barrachina-Mu\u00f1oz, Sergio", "Nikbakht, Rasoul", "Baranda, Jorge", "Payar\u00f3, Miquel", "Mangues-Bafalluy, Josep", "Varvarigos, Emmanuel"]
year: 2024
venue: "SN Computer Science"
venue_type: "journal"
doi: "10.1007/s42979-024-02630-w"
url: "https://www.scopus.com/pages/publications/85187721285?origin=resultslist"
publisher: "Springer"
pages: ""
keywords: ["Cloud edge continuum", "Cloud native applications", "Multi-agent rollout", "Reinforcement learning", "Resource allocation"]
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
    human_decision: "include"
    human_justification: "Talvez tenha algo de LLM e/ou Agentic AI (MAS)."

---

# paper-1203 — Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement

## Metadata

- **Authors:** Soumplis, Polyzois and Kontos, Georgios and Kokkinos, Panagiotis and Kretsis, Aristotelis and Barrachina-Muñoz, Sergio and Nikbakht, Rasoul and Baranda, Jorge and Payaró, Miquel and Mangues-Bafalluy, Josep and Varvarigos, Emmanuel
- **Year:** 2024
- **Venue:** SN Computer Science
- **DOI:** 10.1007/s42979-024-02630-w
- **URL:** https://www.scopus.com/pages/publications/85187721285?origin=resultslist
- **Publisher:** Springer
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud edge continuum; Cloud native applications; Multi-agent rollout; Reinforcement learning; Resource allocation

### Abstract

The advancements in virtualization technologies and distributed computing infrastructures have sparked the development of cloud-native applications. This is grounded in the breakdown of a monolithic application into smaller, loosely connected components, often referred to as microservices, enabling enhancements in the application’s performance, flexibility, and resilience, along with better resource utilization. When optimizing the performance of cloud-native applications, specific demands arise in terms of application latency and communication delays between microservices that are not taken into consideration by generic orchestration algorithms. In this work, we propose mechanisms for automating the allocation of computing resources to optimize the service delivery of cloud-native applications over the edge-cloud continuum. We initially introduce the problem’s Mixed Integer Linear Programming (MILP) formulation. Given the potentially overwhelming execution time for real-sized problems, we propose a greedy algorithm, which allocates resources sequentially in a best-fit manner. To further improve the performance, we introduce a multi-agent rollout mechanism that evaluates the immediate effect of decisions but also leverages the underlying greedy heuristic to simulate the decisions anticipated from other agents, encapsulating this in a Reinforcement Learning framework. This approach allows us to effectively manage the performance–execution time trade-off and enhance performance by controlling the exploration of the Rollout mechanism. This flexibility ensures that the system remains adaptive to varied scenarios, making the most of the available computational resources while still ensuring high-quality decisions. © The Author(s) 2024.

## 04 — Title Screening

**Title:** Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.5 C3=1.0
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Performance Optimization Across the Edge-Cloud Continuum: A Multi-agent Rollout Approach for Cloud-Native Application Workload Placement
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
