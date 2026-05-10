---
id: paper-1598
title: 'Deploying Large Language Model on Cloud-Edge Architectures: A Case Study for Conversational Historical Characters'
authors:
- Graziano, Mariangela
- Colucci Cante, Luigi
- Di Martino, Beniamino
venue: Lecture Notes on Data Engineering and Communications Technologies
venue_type: book-chapter
year: 2025
doi: 10.1007/978-3-031-87778-0_19
url: https://www.scopus.com/pages/publications/105002995405?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 196--205
keywords:
- Augmented reality
- Cloud computing architecture
- Modeling languages
- Agent based
- Case-studies
- Conversational agents
- EDGE architectures
- Historical characters
- Language model
- Real time performance
- WEB application
- Web applications
- Work analysis
- Chatbots
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
    proposed_decision: Include
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: LLM as workload
    agrees_with_regex: false
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

# paper-1598 — Deploying Large Language Model on Cloud-Edge Architectures: A Case Study for Conversational Historical Characters

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> This work analyzes the deployment of conversational agents based on large language models (LLMs) in cloud-edge architectures, placing emphasis on scalability, efficiency and real-time performance. Through a case study, we present a web application that allows users to interact with an augmented reality avatar that impersonates a historical character. The agent, powered by an LLM delivers immersive and contextually coherent dialogues. We discuss the solutions adopted to manage latency and distribute the computational load between the cloud, which takes care of language processing, and the edge nodes, ensuring a smooth user experience. The results obtained demonstrate how accurate design can optimize the use of LLMs in distributed environments, offering advanced and high-performance interactions even in applications with high reactivity and customization requirements.  © The Author(s), under exclusive license to Springer Nature Switzerland AG 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
- **winning_category:** None
- **overrides_applied:** []
- **evidence_trail:**
  - _(not preserved from legacy)_
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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1598.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
