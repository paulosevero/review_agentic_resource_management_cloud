---
id: "paper-723"
title: "Security-Aware Resource Allocation in the Edge-Cloud Continuum"
authors: ["Soumplis, Polyzois", "Kontos, Georgios", "Kretsis, Aristotelis", "Kokkinos, Panagiotis", "Nanos, Anastassios", "Varvarigos, Emmanouel"]
year: 2023
venue: "2023 IEEE 12th International Conference on Cloud Networking, CloudNet 2023"
venue_type: "conference"
doi: "10.1109/CloudNet59005.2023.10490073"
url: "https://www.scopus.com/pages/publications/85191254330?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: "161--169"
keywords: ["cloud edge continuum", "cloud-native applications", "resource allocation", "security", "workload isolation"]
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
    human_decision: ""
    human_justification: ""

---

# paper-723 — Security-Aware Resource Allocation in the Edge-Cloud Continuum

## Metadata

- **Authors:** Soumplis, Polyzois and Kontos, Georgios and Kretsis, Aristotelis and Kokkinos, Panagiotis and Nanos, Anastassios and Varvarigos, Emmanouel
- **Year:** 2023
- **Venue:** 2023 IEEE 12th International Conference on Cloud Networking, CloudNet 2023
- **DOI:** 10.1109/CloudNet59005.2023.10490073
- **URL:** https://www.scopus.com/pages/publications/85191254330?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 161--169
- **Language:** English
- **Keywords:** cloud edge continuum; cloud-native applications; resource allocation; security; workload isolation

### Abstract

Cloud-native applications, comprised of multiple services, optimize their execution on the edge cloud continuum, by leveraging both edge for time-critical computations and the more distant (but abundant) cloud resources for time-driven computations. The infrastructure is controlled by a hierarchical orchestrator logic, with sub-modules at each level managing a specific set of resources. A crucial challenge in deploying applications over such a distributed infrastructure is the allocation of resources, considering jointly application-specific security requirements and computing and networking constraints, that increase significantly the complexity of the decision-making process. In this work, we assume varying levels of workload isolation achievable through lightweight virtualization mechanisms, establishing distinct tiers of security and trustworthiness, each with its own quantified computational and storage requirements. We model the respective resource allocation problem, i.e., of provisioning edge-cloud continuum resources for cloud-native applications subject to applications' performance and security requirements, as a Mixed Integer Linear Program. Additionally, a best-fit heuristic is introduced to reduce the execution time for real-size scenarios, performing a fast allocation of resources for the applications while maintaining a tolerable optimality gap. Finally, a Multi-agent Rollout Mechanism is proposed that trades off execution time with performance, leveraging the greedy heuristic for the approximation of future decisions in a Reinforcement Learning manner. Several simulation experiments were performed to showcase the effectiveness of the developed mechanisms, while simultaneously addressing the needs of conflicting objectives. © 2023 IEEE.

## 04 — Title Screening

**Title:** Security-Aware Resource Allocation in the Edge-Cloud Continuum

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Security-Aware Resource Allocation in the Edge-Cloud Continuum
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Security-Aware Resource Allocation in the Edge-Cloud Continuum
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
