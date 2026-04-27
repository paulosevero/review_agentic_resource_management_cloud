---
id: "paper-2521"
title: "Modernization of enterprise payment infrastructure: A case study on LLM-assisted migration of legacy distributed systems"
authors: ["Bhatnagar, Gaurav"]
year: 2026
venue: "Array"
venue_type: "journal"
doi: "10.1016/j.array.2026.100806"
url: "https://www.scopus.com/pages/publications/105035404147?origin=resultslist"
publisher: "Elsevier B.V."
pages: ""
keywords: ["Cloud-native architecture", "Human-in-the-Loop (HITL)", "Large Language Models (LLMs)", "Software engineering case study", "Software modernization", "Technical debt"]
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

# paper-2521 — Modernization of enterprise payment infrastructure: A case study on LLM-assisted migration of legacy distributed systems

## Metadata

- **Authors:** Bhatnagar, Gaurav
- **Year:** 2026
- **Venue:** Array
- **DOI:** 10.1016/j.array.2026.100806
- **URL:** https://www.scopus.com/pages/publications/105035404147?origin=resultslist
- **Publisher:** Elsevier B.V.
- **Pages:** 
- **Language:** English
- **Keywords:** Cloud-native architecture; Human-in-the-Loop (HITL); Large Language Models (LLMs); Software engineering case study; Software modernization; Technical debt

### Abstract

Context: Modernizing mission-critical financial infrastructure is often impeded by the compounding technical debt and architectural inertia of decade-old frameworks. In high-volume environments, these legacy C# implementations pose significant obstacles to cloud-native scalability and PCI compliance. Objectives: This study explores a resource-efficient modernization strategy that utilizes Large Language Models (LLMs) as strategic “thinking partners.” The research specifically investigates the redesign of intricate session management and deeply coupled dependencies, prioritizing low-risk operational continuity over a volatile system replacement. Methods: Employing an industrial case study methodology following Runeson and Höst guidelines, the research details the transition of a legacy distributed system to a cloud-native architecture (GCP Cloud Run/AdonisJS). The migration was governed by a Human-in-the-Loop (HITL) framework, in which AI-driven proposals were rigorously manually validated and refined using constraints. Performance was evaluated across 10 independent test cycles (N=100), mirroring peak-load production volume. Results: The HITL-governed workflow achieved 50% compression of the development lifecycle (change lead time) compared to traditional benchmarks. Post-migration metrics indicated a successful decoupling of monolithic components, resulting in a 67% normalized reduction in anomalous runtime events and a statistically significant 57% reduction in mean response latency (p < 0.001) during peak-load simulations. Conclusion: This research demonstrates that LLMs can substantially mitigate the fiscal and operational overhead of legacy migration when integrated into a structured HITL framework. This acceleration suggests a fundamental evolution in the Senior Software Engineer's mandate—pivoting from manual implementation toward strategic architectural orchestration and high-fidelity validation. © 2026 The Author

## 04 — Title Screening

**Title:** Modernization of enterprise payment infrastructure: A case study on LLM-assisted migration of legacy distributed systems

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Modernization of enterprise payment infrastructure: A case study on LLM-assisted migration of legacy distributed systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Modernization of enterprise payment infrastructure: A case study on LLM-assisted migration of legacy distributed systems
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)

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
