---
id: paper-2168
title: 'GPU Programming for AI Workflow Development on AWS SageMaker: An Instructional Approach'
authors:
- Srinivasan, Sriram
- Alabsi, Hamdan
- Obeidat, Rand
- Ponnala, Nithisha
- Zenebe, Azene
venue: Proceedings of 2025 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, SC 2025 Workshops
venue_type: conference
year: 2025
doi: 10.1145/3731599.3767381
url: https://www.scopus.com/pages/publications/105023430223?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 384--392
keywords:
- AI workflow
- AWS SageMaker
- Cloud computing
- Deep learning
- GPU programming
- Instructional design
- Machine learning
- Parallel computing
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-2168 — GPU Programming for AI Workflow Development on AWS SageMaker: An Instructional Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We present the design, implementation, and comprehensive evaluation of a specialized course on GPU architecture, GPU programming, and how these are used for developing AI agents. This course is offered to undergraduate and graduate students during Fall 2024 and Spring 2025. The course began with foundational concepts in GPU/CPU hardware and parallel computing and progressed to develop RAG and optimizing them using GPUs. Students gained experience provisioning and configuring cloud-based GPU instances, implementing parallel algorithms, and deploying scalable AI solutions. We evaluated learning outcomes through assessments, course evaluations, and anonymous surveys. The results reveal that (1) AWS served as an effective and economical platform for practical GPU programming, (2) experiential learning significantly enhanced technical proficiency and engagement, and (3) the course strengthened students’ problem-solving and critical thinking skills through tools such as TensorBoard and HPC profilers, which exposed performance bottlenecks and scaling issues. Our findings underscore the pedagogical value of integrating parallel computing into STEM education. We advocate for broader adoption of similar electives across STEM curricula to prepare students for the demands of modern, compute-intensive fields. © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2168.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
