---
id: paper-1455
title: Towards An Improved Video RAG Workflow With Orchestration Support in A Visual Data Management System
authors:
- Chatterjee, Sourish
- Verma, Rohit
- Kumar, Abhinav
- Raghunath, Arun
venue: Proceedings of the 9th Workshop on Data Management for End-to-End Machine Learning, DEEM 2025 - In conjunction with the 2025 ACM SIGMOD/PODS Conference
venue_type: conference
year: 2025
doi: 10.1145/3735654.3735945
url: https://www.scopus.com/pages/publications/105011343007?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: ''
keywords:
- Interactive computer graphics
- Management information systems
- Data management system
- Fast video
- Language model
- Parallelizations
- Pre-processing
- Query context
- User query
- Video retrieval
- Visual data
- Work-flows
- Information management
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
  04-title-screening: include
  05-abstract-screening: exclude
  06-full-text-screening: pending
  07-taxonomy-development: pending
  08-analysis: pending
screening:
  04-title-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: true
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
  05-abstract-screening:
    last_iteration: 0
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: RAG para fluxo de vídeo em data lake visual — recuperação de informação multimodal, não decisão de RM (Boundary B).
    agrees_with_regex: false
    divergence_reason: null
    locked_at_iteration: iter-0
    locked_at: '2026-05-09T00:00:00+00:00'
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

# paper-1455 — Towards An Improved Video RAG Workflow With Orchestration Support in A Visual Data Management System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Video Retrieval-Augmented Generation (RAG) Workflows augment user query contexts with stored video contexts to guide a Large Language Model (LLM) in providing more context-relevant answers. The challenge is to design a workflow where the video contexts can be generated with practical latency values. It is also important to ensure that the resources available to run the workflows are not under-utilized whenever possible. In this paper, we propose a video RAG workflow that utilizes the Visual Data Management System (VDMS) interfaced with the Kubernetes (K8s) orchestration framework to design an enhanced video RAG workflow (VRAG) for faster video context generation in the pre-processing phase and a faster response generation with no impact on response accuracy. Our experiments showcase that compared to Conventional RAG(CRAG) workflows, VRAG reduces the pre-processing latency by a minimum of 10%, which decreases manifold with parallelization and the response latency by a minimum of 70% to as high as 97% with further parallelization. © 2025 ACM.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Include
- **my_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval-Augmented Generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Large Language Model" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLM" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "RAG para fluxo de vídeo em data lake visual — recuperação de informação multimodal, não decisão de RM (Boundary B)."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1455.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
