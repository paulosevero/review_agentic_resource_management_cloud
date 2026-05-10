---
id: paper-1970
title: Leveraging Continuous Integration and Deployment to Operationalize a Fine-Tuned LLaMA Healthcare Chatbot
authors:
- More, Priyanka
- Kothawade, Nishica
- More, Anushka
venue: 2025 2nd International Conference on New Frontiers in Communication, Automation, Management and Security, ICCAMS 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCAMS65118.2025.11233960
url: https://www.scopus.com/pages/publications/105030080259?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- CI/CD Pipeline
- DevOps
- Docker Containerization
- Jenkins Automation
- Kubernetes Orchestration
- Large Language Models (LLMs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Out of scope
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

# paper-1970 — Leveraging Continuous Integration and Deployment to Operationalize a Fine-Tuned LLaMA Healthcare Chatbot

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The study demonstrates the application of Llama 3.1 paradigm and Groq API to build a full CI/CD pipeline that deploys Flask-based applications. A CI/CD orchestration function belongs to Jenkins, while Docker performs containerization and DockerHub registers images and Kubernetes deploys applications, and GitHub manages source code. The fully automated solution allows minimal human involvement, which enables complete automation of machine learning application testing and development, and deployment thus shortening the time to release and reducing errors. This implementation demonstrates the effectiveness of contemporary DevOps practices when delivering big language models. The research examines LLM-based service containerization challenges alongside the advantages of AI application automated deployment before presenting planned enhancements in monitoring frameworks, together with multi-environment deployment methods.  © 2025 IEEE.

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

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1970.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
