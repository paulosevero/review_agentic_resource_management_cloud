---
id: "paper-046"
title: "Design and Performance Analysis of Load Balancing Strategies for Cloud-Based Business Process Management Systems"
authors: ["Adams, Michael", "Ouyang, Chun", "ter Hofstede, Arthur H. M.", "Yu, Yang"]
year: 2018
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-030-02610-3_22"
url: "https://www.scopus.com/pages/publications/85055787821?origin=resultslist"
publisher: "Springer Verlag"
pages: "390--406"
keywords: ["Business Process Management System", "Load balancing", "Scalability", "Software-as-a-Service", "Workflow engine"]
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

# paper-046 — Design and Performance Analysis of Load Balancing Strategies for Cloud-Based Business Process Management Systems

## Metadata

- **Authors:** Adams, Michael and Ouyang, Chun and ter Hofstede, Arthur H. M. and Yu, Yang
- **Year:** 2018
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-030-02610-3_22
- **URL:** https://www.scopus.com/pages/publications/85055787821?origin=resultslist
- **Publisher:** Springer Verlag
- **Pages:** 390--406
- **Language:** English
- **Keywords:** Business Process Management System; Load balancing; Scalability; Software-as-a-Service; Workflow engine

### Abstract

Business Process Management Systems (BPMS) provide automated support for the execution of business processes in modern organisations. With the advent of cloud computing, the deployment of BPMS is shifting from traditional on-premise models to the Software-as-a-Service (SaaS) paradigm with the aim of delivering Business Process Automation as a Service on the cloud. To cope with the impact of numerous simultaneous requests from multiple tenants, a typical SaaS approach will launch multiple instances of its core applications and distribute workload to these application instances via load balancing strategies that operate under the assumption that tenant requests are stateless. However, since business process executions are stateful and often long-running, strategies that assume statelessness are inadequate for ensuring a uniform distribution of system load. In this paper, we propose several new load balancing strategies that support the deployment of BPMS in the cloud by taking into account (a) the workload imposed by the execution of stateful process instances from multiple tenants and (b) the capacity and availability of BPMS workflow engines at runtime. We have developed a prototypical implementation built upon an open-source BPMS and used it to evaluate the performance of the proposed load balancing strategies within the context of diverse load scenarios with models of varying complexity. © 2018, Springer Nature Switzerland AG.

## 04 — Title Screening

**Title:** Design and Performance Analysis of Load Balancing Strategies for Cloud-Based Business Process Management Systems

### Machine Screening

- **Final Score:** 0.6667 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Design and Performance Analysis of Load Balancing Strategies for Cloud-Based Business Process Management Systems
- **Rationale:** C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=1.0 C3=1.0
- **Final Score:** 0.6667
- **Decision:** exclude
- **Evidence Excerpt:** Design and Performance Analysis of Load Balancing Strategies for Cloud-Based Business Process Management Systems
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
