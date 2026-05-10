---
id: paper-1498
title: 'XaaS Containers: Performance-Portable Representation With Source and IR Containers'
authors:
- Copik, Marcin
- Alnuaimi, Eiman
- Kamatar, Alok
- Hayot-Sasson, Valerie
- Madonna, Alberto
- Gamblin, Todd
- Chard, Kyle
- Foster, Ian
- Hoefler, Torsten
venue: Proceedings of the International Conference for High Performance Computing, Networking, Storage, and Analysis, SC 2025
venue_type: conference
year: 2025
doi: 10.1145/3712285.3759868
url: https://www.scopus.com/pages/publications/105023963994?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 533--555
keywords:
- Containers
- Intermediate Representation
- Performance Portability
language: English
source:
  databases:
  - Scopus
  exports:
  - scopus-2026-04-26.bib
  dedup:
    merged_from: []
    merge_reason: ''
status:
  04-title-screening: exclude
  05-abstract-screening: pending
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Exclude
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
  06-full-text-screening:
    last_iteration: 0
    proposed_decision: null
    proposed_justification: null
    winning_category: null
    overrides_applied: []
    my_final_decision: null
    my_justification: null
    agrees_with_regex: null
    divergence_reason: null
    locked_at_iteration: null
    locked_at: null
taxonomy: {}
---

# paper-1498 — XaaS Containers: Performance-Portable Representation With Source and IR Containers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> High-performance computing (HPC) systems and cloud data centers are converging, and containers are becoming the default method of portable software deployment. Yet, while containers simplify software management, they face significant performance challenges in HPC environments as they must sacrifice hardware-specific optimizations to achieve portability. Although HPC containers can use runtime hooks to access optimized MPI libraries and GPU devices, they are limited by application binary interface (ABI) compatibility and cannot overcome the effects of early-stage compilation decisions. Acceleration as a Service (XaaS) proposes a vision of performance-portable containers, where a containerized application should achieve peak performance across all HPC systems. We present a practical realization of this vision through Source and Intermediate Representation (IR) containers, where we delay performance-critical decisions until the target system specification is known. We analyze specialization mechanisms in HPC software and propose a new LLM-assisted method for automatic discovery of specializations. By examining the compilation pipeline, we develop a methodology to build containers optimized for target architectures at deployment time. Our prototype demonstrates that new XaaS containers combine the convenience of containerization with the performance benefits of system-specialized builds. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0.5 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1498.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
