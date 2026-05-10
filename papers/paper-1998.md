---
id: paper-1998
title: 'Nexus Search: A Scalable and Distributed Search Engine Powered by Open Source LLMs'
authors:
- Nishith, P.
- Belwal, Meena
venue: 2025 IEEE 4th International Conference for Advancement in Technology, ICONAT 2025
venue_type: conference
year: 2025
doi: 10.1109/ICONAT66879.2025.11362471
url: https://www.scopus.com/pages/publications/105033947956?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- AI Search
- Apache Kafka
- Distributed Systems
- Gemma
- Google Gemini
- knowledge graphs
- Kubernetes
- Large Language Models (LLMs)
- Neo4j
- Node.js
- Ollama
- Puppeteer
- Scalable Search
- Semantic search
- Twilio
- vector search
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-1998 — Nexus Search: A Scalable and Distributed Search Engine Powered by Open Source LLMs

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The proposed work investigates the current state of semantic search, with a specific emphasis on the amalgamation of vector search techniques and knowledge graphs. This study examines pertinent research in the fields of vector indexing and search, graph databases, and the use of Large Language Models (LLMs) such as Google Gemini (and open-source alternatives like Gemma via Ollama) to improve search functionalities. This research endeavors to establish a fundamental basis for the advancement of 'Nexus Search', a scalable, distributed, and AI-powered search engine designed to mimic internal Google Search functionality for organizations, prioritizing data privacy and sovereignty. Nexus Search employs a hybrid methodology that merges vector methods with graph-based representations using Neo4j to augment semantic search functionalities, enabling data retrieval through both keyword matching and semantic similarity. The system architecture incorporates Apache Kafka for distributed task management, Twilio for voice-based search, and Kubernetes for orchestration on Google Cloud Platform. © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1998.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
