---
id: paper-1758
title: 'Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation'
authors:
- Lakshmanan, Murugan
venue: 2025 8th International Conference on Circuit, Power and Computing Technologies, ICCPCT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCPCT65132.2025.11176777
url: https://www.scopus.com/pages/publications/105020171206?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1085--1091
keywords:
- Asynchronous communication
- Dense Passage Retrieval
- large language models
- Retrieval-Augmented Generation
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
    proposed_decision: Exclude
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Include
    my_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    agrees_with_regex: false
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
    my_justification: LLM as workload
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

# paper-1758 — Serverless RAG-Stream: A Cloud Pipeline for Efficient Real-Time Retrieval-Augmented Generation

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Retrieval-Augmented Generation (RAG) enhances large language models (LLMs) by integrating external knowledge through retrieval mechanisms, thereby improving the contextual relevance and accuracy of generated responses. However, conventional RAG systems often encounter challenges related to high latency, limited scalability, and the complexity of managing infrastructure particularly in real-time streaming environments. To overcome these barriers, this work proposes a novel serverless RAG-Stream architecture, designed to deliver low-latency, highly scalable, and cost-effective data processing. The architecture employs AWS Kinesis for real-time data ingestion, Dense Passage Retrieval (DPR) for semantic search, and cloud-based LLMs for dynamic response generation. Workflow orchestration is achieved using serverless functions and asynchronous communication, ensuring optimal resource utilization and simplified management. Experimental evaluations, performed using the WikiText-103 dataset alongside four subsets of the Pile benchmark such as Enron Emails, HackerNews, NIH ExPorter, and YouTube Subtitles, reveal significant performance gains. The serverless RAGStream system achieved an average latency of 150 ms, sustained a throughput of 500 requests per second, and produced highquality outputs, as validated by BLEU, ROUGE, METEOR, and BERTScore metrics. Compared to baseline models, the proposed architecture demonstrates superior scalability, reduced operational complexity, and maintained generation quality, positioning it as a robust solution for real-time, AIpowered applications. © 2025 IEEE.

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
- **agrees_with_regex:** False
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Retrieval-Augmented Generation" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "RAG" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1758.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
