---
id: "paper-050"
title: "Engineering a highly scalable object-aware process management engine using distributed microservices"
authors: ["Andrews, Kevin", "Steinau, Sebastian", "Reichert, Manfred"]
year: 2018
venue: "Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)"
venue_type: "conference"
doi: "10.1007/978-3-030-02671-4_5"
url: "https://www.scopus.com/pages/publications/85055936990?origin=resultslist"
publisher: "Springer Verlag"
pages: "80--97"
keywords: ["Computation theory", "Data encapsulation", "Engines", "Enterprise resource management", "Information systems", "Information use", "Management information systems", "Multi agent systems", "Scalability", "Semantics", "Business process management", "Distributed process", "Object-aware process managements", "Process execution", "Process instances", "Process management systems", "Process-aware information systems", "Prototypical implementation", "Distributed computer systems"]
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
    final_score: 0.3333
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: ""
    human_justification: ""

---

# paper-050 — Engineering a highly scalable object-aware process management engine using distributed microservices

## Metadata

- **Authors:** Andrews, Kevin and Steinau, Sebastian and Reichert, Manfred
- **Year:** 2018
- **Venue:** Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
- **DOI:** 10.1007/978-3-030-02671-4_5
- **URL:** https://www.scopus.com/pages/publications/85055936990?origin=resultslist
- **Publisher:** Springer Verlag
- **Pages:** 80--97
- **Language:** English
- **Keywords:** Computation theory; Data encapsulation; Engines; Enterprise resource management; Information systems; Information use; Management information systems; Multi agent systems; Scalability; Semantics; Business process management; Distributed process; Object-aware process managements; Process execution; Process instances; Process management systems; Process-aware information systems; Prototypical implementation; Distributed computer systems

### Abstract

Scalability of information systems has been a research topic for many years and is as relevant as ever with the dramatic increases in digitization of business processes and data. This also applies to process-aware information systems, most of which are currently incapable of scaling horizontally, i.e., over multiple servers. This paper presents the design science artifact that resulted from engineering a highly scalable process management system relying on the object-aware process management paradigm. The latter allows for distributed process execution by conceptually encapsulating process logic and data into multiple interacting objects that may be processed concurrently. These objects, in turn, are represented by individual microservices at run-time, which can be hosted transparently across entire server clusters. We present measurement data that evaluates the scalability of the artifact on a compute cluster, demonstrating that the current prototypical implementation of the run-time engine can handle very large numbers of users and process instances concurrently in single-case mechanism experiments with large amounts of simulated user input. Finally, the development of scalable process execution engines will further the continued maturation of the data-centric business process management field. © Springer Nature Switzerland AG 2018.

## 04 — Title Screening

**Title:** Engineering a highly scalable object-aware process management engine using distributed microservices

### Machine Screening

- **Final Score:** 0.3333 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Engineering a highly scalable object-aware process management engine using distributed microservices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** Engineering a highly scalable object-aware process management engine using distributed microservices
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)

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
