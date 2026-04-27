---
id: "paper-2518"
title: "Multi-Agent Stateless Orchestration for Distributed Data Pipelines Implementation"
authors: ["Bertozzi, Nicol\u00f2", "Geraci, Anna", "Sacchet, Marco", "Ferrera, Enrico", "Pastrone, Claudio"]
year: 2026
venue: "Communications in Computer and Information Science"
venue_type: "conference"
doi: "10.1007/978-3-032-09555-8_9"
url: "https://www.scopus.com/pages/publications/105023194597?origin=resultslist"
publisher: "Springer Science and Business Media Deutschland GmbH"
pages: "141--156"
keywords: ["Asynchronous Communication", "Distributed Architecture", "Multi-Agent Systems", "Stateless Orchestration"]
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

# paper-2518 — Multi-Agent Stateless Orchestration for Distributed Data Pipelines Implementation

## Metadata

- **Authors:** Bertozzi, Nicolò and Geraci, Anna and Sacchet, Marco and Ferrera, Enrico and Pastrone, Claudio
- **Year:** 2026
- **Venue:** Communications in Computer and Information Science
- **DOI:** 10.1007/978-3-032-09555-8_9
- **URL:** https://www.scopus.com/pages/publications/105023194597?origin=resultslist
- **Publisher:** Springer Science and Business Media Deutschland GmbH
- **Pages:** 141--156
- **Language:** English
- **Keywords:** Asynchronous Communication; Distributed Architecture; Multi-Agent Systems; Stateless Orchestration

### Abstract

This paper introduces a stateless orchestration architecture and mechanism for managing distributed data pipelines in multi-agent systems. Workflows are decomposed into independent subworkflows by a splitting module. A caching mechanism preserves execution context without relying on local state, supporting true statelessness. Communication is event-driven via Apache Kafka, and a unified data model ensures consistent interaction among components. The architecture is validated on a Kubernetes environment, showing scaling and low-latency features. This approach combines the control of orchestration with the scalability of event-driven systems, offering a robust solution for modular workflow execution. © The Author(s) 2026.

## 04 — Title Screening

**Title:** Multi-Agent Stateless Orchestration for Distributed Data Pipelines Implementation

### Machine Screening

- **Final Score:** 0.75 (threshold: 0.67)
- **Machine Decision:** include
- **Disagreement Type:** strong_disagreement

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.5
- **Final Score:** 0.8333
- **Decision:** include
- **Evidence Excerpt:** Multi-Agent Stateless Orchestration for Distributed Data Pipelines Implementation
- **Rationale:** C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=1.0 C2=1.0 C3=0.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Multi-Agent Stateless Orchestration for Distributed Data Pipelines Implementation
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
