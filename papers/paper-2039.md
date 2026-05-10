---
id: paper-2039
title: 'Collaborative fault tolerance for cyber–physical systems: The detection stage'
authors:
- Piardi, Luis
- de Oliveira, André Schneider
- Costa, Pedro
- Leitão, Paulo
venue: Computers in Industry
venue_type: journal
year: 2025
doi: 10.1016/j.compind.2025.104253
url: https://www.scopus.com/pages/publications/85216443398?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Cyber–physical system
- Fault detection
- Fault tolerance
- Multi-agent system
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2039 — Collaborative fault tolerance for cyber–physical systems: The detection stage

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the era of Industry 4.0, fault tolerance is essential for maintaining the robustness and resilience of industrial systems facing unforeseen or undesirable disturbances. Current methodologies for fault tolerance stages namely, detection, diagnosis, and recovery, do not correspond with the accelerated technological evolution pace over the past two decades. Driven by the advent of digital technologies such as Internet of Things, cloud and edge computing, and artificial intelligence, associated with enhanced computational processing and communication capabilities, local or monolithic centralized fault tolerance methodologies are out of sync with contemporary and future systems. Consequently, these methodologies are limited in achieving the maximum benefits enabled by the integration of these technologies, such as accuracy and performance improvements. Accordingly, in this paper, a collaborative fault tolerance methodology for cyber–physical systems, named Collaborative Fault * (CF*), is proposed. The proposed methodology takes advantage of the inherent data analysis and communication capabilities of cyber–physical components. The proposed methodology is based on multi-agent system principles, where key components are self-fault tolerant, and adopts collaborative and distributed intelligence behavior when necessary to improve its fault tolerance capabilities. Experiments were conducted focusing on the fault detection stage for temperature and humidity sensors in warehouse racks. The experimental results confirmed the accuracy and performance improvements under CF* compared with the local methodology and competitiveness when compared with a centralized approach. © 2025 The Authors

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2039.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
