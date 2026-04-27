---
id: "paper-1498"
title: "XaaS Containers: Performance-Portable Representation With Source and IR Containers"
authors: ["Copik, Marcin", "Alnuaimi, Eiman", "Kamatar, Alok", "Hayot-Sasson, Valerie", "Madonna, Alberto", "Gamblin, Todd", "Chard, Kyle", "Foster, Ian", "Hoefler, Torsten"]
year: 2025
venue: "Proceedings of the International Conference for High Performance Computing, Networking, Storage, and Analysis, SC 2025"
venue_type: "conference"
doi: "10.1145/3712285.3759868"
url: "https://www.scopus.com/pages/publications/105023963994?origin=resultslist"
publisher: "Association for Computing Machinery, Inc"
pages: "533--555"
keywords: ["Containers", "Intermediate Representation", "Performance Portability"]
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
    final_score: 0.4166
    threshold_used: 0.67
    machine_decision: "exclude"
    disagreement_type: "agreement_exclude"
    human_decision: "exclude"
    human_justification: "Sem pistas de uso de LLM e/ou Agentic AI."

---

# paper-1498 — XaaS Containers: Performance-Portable Representation With Source and IR Containers

## Metadata

- **Authors:** Copik, Marcin and Alnuaimi, Eiman and Kamatar, Alok and Hayot-Sasson, Valerie and Madonna, Alberto and Gamblin, Todd and Chard, Kyle and Foster, Ian and Hoefler, Torsten
- **Year:** 2025
- **Venue:** Proceedings of the International Conference for High Performance Computing, Networking, Storage, and Analysis, SC 2025
- **DOI:** 10.1145/3712285.3759868
- **URL:** https://www.scopus.com/pages/publications/105023963994?origin=resultslist
- **Publisher:** Association for Computing Machinery, Inc
- **Pages:** 533--555
- **Language:** English
- **Keywords:** Containers; Intermediate Representation; Performance Portability

### Abstract

High-performance computing (HPC) systems and cloud data centers are converging, and containers are becoming the default method of portable software deployment. Yet, while containers simplify software management, they face significant performance challenges in HPC environments as they must sacrifice hardware-specific optimizations to achieve portability. Although HPC containers can use runtime hooks to access optimized MPI libraries and GPU devices, they are limited by application binary interface (ABI) compatibility and cannot overcome the effects of early-stage compilation decisions. Acceleration as a Service (XaaS) proposes a vision of performance-portable containers, where a containerized application should achieve peak performance across all HPC systems. We present a practical realization of this vision through Source and Intermediate Representation (IR) containers, where we delay performance-critical decisions until the target system specification is known. We analyze specialization mechanisms in HPC software and propose a new LLM-assisted method for automatic discovery of specializations. By examining the compilation pipeline, we develop a methodology to build containers optimized for target architectures at deployment time. Our prototype demonstrates that new XaaS containers combine the convenience of containerization with the performance benefits of system-specialized builds. © 2025 Copyright held by the owner/author(s).

## 04 — Title Screening

**Title:** XaaS Containers: Performance-Portable Representation With Source and IR Containers

### Machine Screening

- **Final Score:** 0.4166 (threshold: 0.67)
- **Machine Decision:** exclude
- **Disagreement Type:** agreement_exclude

### Sub-Agent 1 (Inclusivist)

- **Scores:** C1=0.0 C2=0.5 C3=1.0
- **Final Score:** 0.5
- **Decision:** exclude
- **Evidence Excerpt:** XaaS Containers: Performance-Portable Representation With Source and IR Containers
- **Rationale:** C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)

### Sub-Agent 2 (Exclusivist)

- **Scores:** C1=0.0 C2=0.0 C3=1.0
- **Final Score:** 0.3333
- **Decision:** exclude
- **Evidence Excerpt:** XaaS Containers: Performance-Portable Representation With Source and IR Containers
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
