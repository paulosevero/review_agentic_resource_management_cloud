---
id: "paper-928"
title: "Bottom-Up Resource Orchestration in Edge Computing: An Agent-Based Modeling Approach"
authors: ["Ghasemi, Abdorasoul", "Schranz, Melanie"]
year: 2024
venue: "International IEEE Conference  proceedings, IS"
venue_type: "conference"
doi: "10.1109/IS61756.2024.10705177"
url: "https://www.scopus.com/pages/publications/85208439081?origin=resultslist"
publisher: "Institute of Electrical and Electronics Engineers Inc."
pages: ""
keywords: ["bottom-up resource orchestration", "edge computing", "edge micro data centers", "multiagent systems"]
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
    final_score: 1.0
    threshold_used: 0.67
    machine_decision: "include"
    disagreement_type: "agreement_include"
    human_decision: ""
    human_justification: ""

---

# paper-928 — Bottom-Up Resource Orchestration in Edge Computing: An Agent-Based Modeling Approach

## Metadata

- **Authors:** Ghasemi, Abdorasoul and Schranz, Melanie
- **Year:** 2024
- **Venue:** International IEEE Conference  proceedings, IS
- **DOI:** 10.1109/IS61756.2024.10705177
- **URL:** https://www.scopus.com/pages/publications/85208439081?origin=resultslist
- **Publisher:** Institute of Electrical and Electronics Engineers Inc.
- **Pages:** 
- **Language:** English
- **Keywords:** bottom-up resource orchestration; edge computing; edge micro data centers; multiagent systems

### Abstract

Edge computing addresses delay-sensitive microservices near applications, supplementing cloud computing. The dynamic nature of resources and workloads in edge clusters challenges traditional machine learning tools for resource prediction and allocation for each request (pod in the Kubernetes context). This paper models edge infrastructure as a multi-agent system with a master, a worker, and two types of arriving pods: rigid and elastic. Rigid pods have an estimate of their CPU/RAM demands, and strict execution times, and may only utilize some assigned resources, leading to slack. Elastic pods have more flexible execution times and aim to utilize these slack resources. We propose a scalable bottom-up algorithm that maintains the coarse-grained footprint of deployed rigid pods in a few buckets. The algorithm selects an appropriate bucket based on the demand of the new arriving elastic pod and chooses the host rigid pod randomly and with uniform probability from that bucket. We evaluate the system performance in terms of CPU/RAM utilization and the satisfaction rate of pods, comparing the results with random and non-scalable best strategies. Our findings show that the bottom-up swarm intelligence-inspired mechanism can complement the inefficiency in estimating the exact demand needs in a dynamic edge environment.  © 2024 IEEE.

## 04 — Title Screening

**Title:** Bottom-Up Resource Orchestration in Edge Computing: An Agent-Based Modeling Approach

### Machine Screening

- **Final Score:** 1.0 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** agreement_include

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Bottom-Up Resource Orchestration in Edge Computing: An Agent-Based Modeling Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=1.0
- **Final Score:** 1.0
- **Decision:** include
- **Evidence Excerpt:** Bottom-Up Resource Orchestration in Edge Computing: An Agent-Based Modeling Approach
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

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
