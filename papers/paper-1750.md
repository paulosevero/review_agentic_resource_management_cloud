---
id: paper-1750
title: Creating Hybrid Computing Architectures for Data Centers
authors:
- Kuftinova, N.G.
- Ostroukh, A.V.
- Pronin, C.B.
- Podberezkin, A.A.
venue: 2025 Systems of Signals Generating and Processing in the Field of on Board Communications, SOSG 2025 - Conference Proceedings
venue_type: conference
year: 2025
doi: 10.1109/IEEECONF64229.2025.10948062
url: https://www.scopus.com/pages/publications/105003308928?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- a combination of different architectures
- a mathematical model of the concept of hybrid platforms
- data centers
- edge computing
- FLOPS metric
- hybrid computing platforms
- large language models (LLM)
- machine learning (ML)
- performance
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1750 — Creating Hybrid Computing Architectures for Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This is article examines the issue of new conceptual architectures of ultrafast hybrid computing devices based on digital technologies, where the size of an elementary computing device approaches the size of a molecule or even an atom. At this level, the laws of classical physics stop working and quantum laws begin to operate, which for many important dynamic problems have yet to be described theoretically. For such practically significant examples of the use of quantum computers as the training of language models, as well as the analysis of the effectiveness of model training on specified chips and with specified train characteristics (model depth, dataset size, etc.), a new concept for the use of hybrid computing platforms in data centers has emerged. Hybrid computing platforms for data centers represent the integration of various computing resources, including on-premises servers, cloud solutions and virtualized environments. These platforms allow organizations to optimize their computing power, providing flexibility, scalability and costeffectiveness. With the increase in data volumes and the need for cloud services, there is an increase in the creation of data centers. The edge-computing extension, which supports real-time processing at data collection points, matches the potential of quantum computing for revolutionary tasks such as optimization and decision-making. As peripheral systems evolve, the integration of algorithms with quantum technologies can expand their capabilities. This raises pitfalls in evaluating processor performance in hybrid computers, which can vary depending on many factors, including the processor architecture, the types of cores used (for example, high-performance and energy-efficient), as well as the nature of the tasks performed. In this study, a mathematical model of the presented systems is proposed as a combination of combining various concepts that will help to understand and evaluate the performance of hybrid computing, allowing you to optimize the use of resources and improve overall efficiency. Today, there is a growing dependence on hybrid models - mixing local, cloud and peripheral systems, which further emphasizes the need for an infrastructure that accommodates both classical and quantum resources. Quantum computing is increasingly seen as an important part of these hybrid architectures, preparing organizations to meet the new challenges of the advanced computing landscape. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1750.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
