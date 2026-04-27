---
id: "paper-1401"
title: "Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability"
authors: ["Asadi, Navidreza", "Ursu, R\u01cezvan-Mihai", "Wong, Leon", "Kellerer, Wolfgang"]
year: 2025
venue: "NGNO 2025 - Proceedings of the 2025 1st Workshop on Next-Generation Network Observability, Part of SIGCOMM 2025"
venue_type: "conference"
doi: "10.1145/3748496.3748991"
url: "https://www.scopus.com/pages/publications/105019924497?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "21--28"
keywords: ["Adversarial Benchmarking", "Adversarial Patterns", "Autonomous Networks", "Bayesian Optimization", "Chaos Engineering", "Cost Optimization", "Fault Tolerance", "Microservice Autoscaling", "Multi-Agent Systems", "Parallel Environments", "Proactive Observability", "Reinforcement Learning", "System Dependability"]
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

# paper-1401 — Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability

## Metadata

- **Authors:** Asadi, Navidreza and Ursu, Rǎzvan-Mihai and Wong, Leon and Kellerer, Wolfgang
- **Year:** 2025
- **Venue:** NGNO 2025 - Proceedings of the 2025 1st Workshop on Next-Generation Network Observability, Part of SIGCOMM 2025
- **DOI:** 10.1145/3748496.3748991
- **URL:** https://www.scopus.com/pages/publications/105019924497?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 21--28
- **Language:** English
- **Keywords:** Adversarial Benchmarking; Adversarial Patterns; Autonomous Networks; Bayesian Optimization; Chaos Engineering; Cost Optimization; Fault Tolerance; Microservice Autoscaling; Multi-Agent Systems; Parallel Environments; Proactive Observability; Reinforcement Learning; System Dependability

### Abstract

Microservices autoscaling is essential for dynamically adjusting resources to meet fluctuating workload demands and maintain service-level objectives (SLOs), such as latency, while minimizing resource usage. However, the control logic of modern autoscalers is susceptible to exploitation. Assessing its performance requires more than passive monitoring; the rapid evolution of application development has outpaced the availability of observability tools to benchmark and identify corner cases in autoscaling configurations relative to an application's behavior. In this work, we aim to address a critical yet underexplored question: Can we systematically identify adversarial inputs, i.e., traffic anti-patterns that disproportionately increase SLO violations or operational costs - -or both? We propose Simurgh, an adversarial benchmarking framework designed to generate traffic patterns tailored for finding autoscaling anti-patterns. It evolves strategies based on real-time observability signals from both the application and infrastructure layers. This problem is inherently complex due to its large solution space. To address this, we introduce heuristics that relax the problem while leveraging multiple parallel systems, each paired with a local controller and optimizer. These controllers act as individual agents being managed by a global controller, asynchronously generating diverse traffic patterns while collectively optimizing toward a shared adversarial objective. We evaluate our framework on two applications and three optimization methods, including Bayesian optimization, chaos engineering, and a distributed reinforcement learning approach. Our preliminary empirical results illustrate Simurgh's effectiveness in identifying anti-patterns with respect to different objectives, such as SLO violations and operational costs, and demonstrate generalizability across different applications and cluster sizes of 10× larger. © 2025 Owner/Author.

## 04 — Title Screening

**Title:** Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=0.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Simurgh: Multi-Agent Adversarial Benchmarking for Proactive Microservice Observability
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
