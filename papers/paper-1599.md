---
id: paper-1599
title: 'A Hybrid Microservices Architecture for Smart Glasses: Integrating Cloud-Based LLMs, Containerized Services, and On-Device Functionalities'
authors:
- Grumeza, Theodor-Radu
- Lazăr, Thomas-Andrei
- Fortiş, Alexandra-Emilia
venue: Lecture Notes on Data Engineering and Communications Technologies
venue_type: book-chapter
year: 2025
doi: 10.1007/978-3-031-87778-0_42
url: https://www.scopus.com/pages/publications/105002979636?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 429--438
keywords:
- Barcode Scanning
- Cloud Computing
- Containerization
- Expiration Date Detection
- Hybrid Microservices
- IoT
- Large Language Model
- Smart Glasses
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1599 — A Hybrid Microservices Architecture for Smart Glasses: Integrating Cloud-Based LLMs, Containerized Services, and On-Device Functionalities

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In this work, the authors propose a theoretical hybrid microservices architecture with on-device processing and cloud-based computation for real-time assistance in smart visually impaired glasses. The architecture integrates various functionalities, each containerized and deployed either locally or in the cloud, according to their computational requirements. Specifically, the pipeline includes a transformer-based Large Language Model (LLM) service, a barcode-scanning module, an expiration-date detection microservice, and an advanced performance optimization layer. The design references our previous four works, which explored domain-specific LLM architectures in the cloud, LLM integration in barcode scanning, LLM integration in expiration-date scanning, and performance trade-offs for LLMs on different hardware systems. By unifying these components into a hybrid model, our approach aims to deliver low-latency responses for core tasks on the smart glasses and robust, large-scale computations in the cloud. We highlight container orchestration, service-level optimizations, and security concerns, proposing an architecture adaptable to future IoT developments. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1599.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
