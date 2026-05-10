---
id: paper-1956
title: 'Smart AI Applications: Integrating Raspberry Pi 3 with NLP for Edge Computing'
authors:
- Mittal, Ayushi
- Kedawat, Khushal
- Gupta, Eshita
- Gupta, Vinay
venue: 7th International Conference on Energy, Power and Environment, ICEPE 2025
venue_type: conference
year: 2025
doi: 10.1109/ICEPE65965.2025.11139558
url: https://www.scopus.com/pages/publications/105016859470?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- large language models
- Natural language processing
- Raspberry Pi 3
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1956 — Smart AI Applications: Integrating Raspberry Pi 3 with NLP for Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Artificial intelligence (AI) is used in many ways by the modern world. It can be used to effectively manage complex issues in a wide range of industries, including banking, education, entertainment, and healthcare. The efficiency and convenience of daily lives are being enhanced by AI. Artificial intelligence's natural language processing (NLP) branch enables machines to understand, generate, and respond to human language. The integration of Raspberry Pi 3 and advanced natural language processing models represents a significant advance in the development of intelligent systems. The feasibility of interfacing Raspberry Pi 3 with an LLM such as Google's Gemini is explored by this research. The aim of this study is to provide an efficient and compact solution for AI-based applications. In this study, system architecture, methodology, performance evaluation under different workloads and challenges are discussed. The results are shown to indicate that LLMs cannot be locally hosted by the Raspberry Pi 3, and it is effectively served as a client for cloud-based models. The average achieving response times are reported to be under 1.5 seconds for typical queries. The potential of combining edge computing with cloud-hosted LLMs for applications in IoT, education, and robotics is highlighted by this work, while the need for future advancements in model optimization and hardware capabilities is underscored. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1956.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
