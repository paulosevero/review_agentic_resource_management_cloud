---
id: "paper-091"
title: "Evaluating Multi-tenant Live Migrations Effects on Performance"
authors: ["Rosinosky, Guillaume", "Labba, Chahrazed", "Ferme, Vincenzo", "Youcef, Samir", "Charoy, Fran\u00e7ois", "Pautasso, Cesare"]
year: 2018
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-030-02610-3_4"
url: "https://www.scopus.com/pages/publications/85055817954?origin=resultslist"
publisher: "Springer Verlag"
pages: "61--77"
keywords: ["BPMS", "Live migration", "Multitenancy", "Performance"]
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
    final_score: 0.0833
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-091 — Evaluating Multi-tenant Live Migrations Effects on Performance

## Metadata

- **Authors:** Rosinosky, Guillaume and Labba, Chahrazed and Ferme, Vincenzo and Youcef, Samir and Charoy, François and Pautasso, Cesare
- **Year:** 2018
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-030-02610-3_4
- **URL:** https://www.scopus.com/pages/publications/85055817954?origin=resultslist
- **Publisher:** Springer Verlag
- **Pages:** 61--77
- **Language:** English
- **Keywords:** BPMS; Live migration; Multitenancy; Performance

### Abstract

Multitenancy is an important feature for all Everything as a Service providers like Business Process Management as a Service. It allows to reduce the cost of the infrastructure since multiple tenants share the same service instances. However, tenants have dynamic workloads. The resource they share may not be sufficient at some point in time. It may require Cloud resource (re-)configurations to ensure a given Quality of Service. Tenants should be migrated without stopping the service from a configuration to another to meet their needs while minimizing operational costs on the provider side. Live migrations reveal many challenges: service interruption must be minimized and the impact on co-tenants should be minimal. In this paper, we investigate live tenants migrations duration and its effects on the migrated tenants as well as the co-located ones. To do so, we propose a generic approach to measure these effects for multi-tenant Software as a Service. Further, we propose a testing framework to simulate workloads, and observe the impact of live migrations on Business Process Management Systems. The experimental results highlight the efficiency of our approach and show that migration time depends on the size of data that have to be transferred and that the effects on co-located tenants should not be neglected. © 2018, Springer Nature Switzerland AG.

## 04 — Title Screening

**Title:** Evaluating Multi-tenant Live Migrations Effects on Performance

### Machine Screening

- **Final Score:** 0.0833 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=0.0
- **Final Score:** 0.1667
- **Decision:** exclude
- **Evidence Excerpt:** Evaluating Multi-tenant Live Migrations Effects on Performance
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=0 (no infra signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=0.0
- **Final Score:** 0.0
- **Decision:** exclude
- **Evidence Excerpt:** Evaluating Multi-tenant Live Migrations Effects on Performance
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)

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
