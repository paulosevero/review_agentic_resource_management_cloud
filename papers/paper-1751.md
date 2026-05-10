---
id: paper-1751
title: 'Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS'
authors:
- Kulkarni, Varad
- Reddy, Nikhil
- Simmhan, Yogesh
venue: Proceedings of the IEEE International Conference on High Performance Computing, Data, and Analytics Workshops, HiPCW
venue_type: conference
year: 2025
doi: 10.1109/HiPCW66559.2025.00052
url: https://www.scopus.com/pages/publications/105036053754?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 195--196
keywords:
- ai agents on faas
- ai for education
- pedagogy workflows
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
    my_justification: Não é gerenciamento de recursos em infraestruturas de cloud/edge/fog etc.
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

# paper-1751 — Pedagogy Meets AI & Systems: Towards Orchestrating Tutor Agents in Moodle using FaaS

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Large Language Models (LLMs) are enabling scalable, personalized AI-driven education. We study a real-world setting where teaching for a post-graduate course is handled by a configured AI Tutor Agent based on MS Teams Copilot, with students interacting with it through a chat interface. Tutor-Student conversation transcripts are submitted into the Moodle LMS for analysis. Our workflows assess these interactions via two pipelines: for personalized feedback and class-level insights. These analytics are deployed on public-cloud FaaS platforms, as AWS Step Functions and Azure Durable Functions, to exploit autoscaling and pay-per-use efficiency suited to bursty submission patterns. We benchmark latency, cost and I/O tokens, positioning pedagogy as a novel systems workload and revealing the limits of current FaaS platforms for educational AI.  © 2025 IEEE.

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
- **my_justification:** "Não é gerenciamento de recursos em infraestruturas de cloud/edge/fog etc."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1751.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
