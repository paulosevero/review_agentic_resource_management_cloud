---
id: paper-2550
title: 'AI-Driven Microservice Identification for Business Process Digital Transformation: A Multi-Dependency Collaborative Clustering Approach'
authors:
- Daoud, Mohamed
- Assamid, Fatima Ezzahra
- Ennouni, Assia
- Sabri, My Abdelouahed
venue: Statistics, Optimization and Information Computing
venue_type: journal
year: 2026
doi: 10.19139/soic-2310-5070-2523
url: https://www.scopus.com/pages/publications/105029736409?origin=resultslist
publisher: International Academic Press
pages: 2196--2224
keywords:
- Artificial Intelligence
- Business Processes
- Collaborative Clustering
- Digital Transformation
- Microservices
- Process Mining
- Semantic Dependencies
- Smart Modernization
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM).
    winning_category: agent_llm_based
    overrides_applied:
    - ovr_rl_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-2550 — AI-Driven Microservice Identification for Business Process Digital Transformation: A Multi-Dependency Collaborative Clustering Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In the era of digital transformation, enterprises are increasingly seeking to modernize their legacy monolithic systems in favor of more agile and modular architectures. Microservices have emerged as a compelling solution, offering scalability, maintainability, and independent deployment. However, the automated extraction of microservices from legacy systems—particularly when documentation is sparse or outdated—remains a complex and unresolved challenge. This paper introduces an AI-powered, multi-view methodology for microservice identification based on business process (BP) models. Unlike traditional approaches that rely on static code analysis or single-view aggregation, our method simultaneously captures and analyzes three critical types of dependencies within business processes: control flow, data exchange, and semantic similarity. Each dependency is modeled separately and processed through a collaborative clustering framework, where AI agents exchange signals to achieve consensus-based service decomposition. Artificial Intelligence plays a dual role in our system: it is used for semantic enrichment—via Natural Language Processing (NLP) and Sentence-BERT embeddings—and for optimizing the clustering strategy through dependency alignment and explainability metrics. A real-world case study on the Bicing bike-sharing system in Barcelona, composed of over 50 business activities, demonstrates the effectiveness and scalability of our approach. Experimental results show that the AI-enhanced model achieves superior clustering performance in terms of cohesion, coupling, and interpretability compared to baseline methods. By integrating AI-driven analytics with business process understanding, our approach provides a robust pathway toward automated, explainable, and domain-aligned microservice extraction—supporting sustainable digital transformation at scale. Copyright © 2026 International Academic Press

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
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI (Agent+LLM)."
- **winning_category:** 'agent_llm_based'
- **overrides_applied:** ['ovr_rl_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-powered" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI agents" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Natural Language Processing" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "NLP" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2550.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
