---
id: paper-1572
title: Expert Multi-Agent Conversational System Using Retrieval-Augmented Generation and Dynamic Text-to-SQL for Government Transparency
authors:
- Flores, Nahum
- Ramirez, Carlos
- Mauricio, David
venue: IEEE Access
venue_type: journal
year: 2025
doi: 10.1109/ACCESS.2025.3635530
url: https://www.scopus.com/pages/publications/105022746216?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 198178--198200
keywords:
- artificial intelligence
- data integration
- Large language models (LLM)
- multi-agent systems
- natural language processing (NLP)
- optical character recognition (OCR)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)
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

# paper-1572 — Expert Multi-Agent Conversational System Using Retrieval-Augmented Generation and Dynamic Text-to-SQL for Government Transparency

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Access to structured and actionable public information remains a major challenge for government transparency in Peru, where official data are often fragmented, inconsistently published, and presented in low-quality formats. This study introduces a multi-agent conversational system designed under the Design Science Research paradigm, which is instantiated through three artifacts. First artifact is a data processing system that integrates procurement and legislative records through classification, region detection, and OCR. A second artifact is a set of specialized agents, combining Retrieval-Augmented Generation for attendance and voting with a Text-to-SQL agent for procurement. The third artifact is a multi-agent orchestration system that unifies these components within a microservices architecture. Together, they transform raw governmental records into structured, auditable, and citizen-accessible responses. The pipeline achieved strong results: classifiers reached accuracies up to 0.989, YOLOv11 obtained mAP@50–95 of 0.965 for attendance and 0.886 for voting, and Tesseract delivered a character error rate of 0.031 and word error rate of 0.078. The RAG agents achieved MAP of 0.950 for attendance and 0.926 for voting, confirming robust retrieval even under noisy conditions. For procurement queries, the Text-to-SQL agent outperformed baselines with FLEX of 0.909 and EX of 0.801. End-to-end evaluation confirmed reliability with Faithfulness of 0.942, Answer Relevancy of 0.907, Answer Similarity of 0.984, and Answer Correctness of 0.891, complemented by BERTScore, BLEU, and ROUGE metrics. These results validate the feasibility of large language models and microservice-based architectures to enhance transparency and accountability in low-data-quality environments. © 2013 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1572.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
