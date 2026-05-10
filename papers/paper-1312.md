---
id: paper-1312
title: Test Case Migration from Monolith to Microservices Using Large Language Models
authors:
- Yeh, Hang-Wei
- Ma, Shang-Pin
- Chen, Yi
venue: Proceedings - 2024 IEEE International Conference on e-Business Engineering, ICEBE 2024
venue_type: conference
year: 2024
doi: 10.1109/ICEBE62490.2024.00014
url: https://www.scopus.com/pages/publications/85215538513?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 29--35
keywords:
- consumer-driven contract testing
- large language model
- Microservice
- test case migration
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

# paper-1312 — Test Case Migration from Monolith to Microservices Using Large Language Models

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to microservices' modularity, high scalability, and good fault tolerance, more and more software systems are transitioning from monolithic architectures to microservice architectures. In this migration process, the migration of test cases is a crucial step to ensure functional consistency and completeness before and after the migration, thereby maintaining the stability and reliability of the microservice system post-migration. However, despite numerous studies on architecture migration, there is still a lack of methods to efficiently convert test cases of monolithic systems into ones for the migrated microservices. Therefore, this study proposes a test migration approach based on Large Language Models (LLM), called LTM3 (LLM-based Test Migration from Monolith to Microservices). During migration, LTM3 identifies the correspondence between existing test cases and monolithic functions, the connections between monolithic functions and migrated microservices, and the dependencies between microservices. Subsequently, by utilizing LLM and appropriate prompting, the integration test cases of the monolithic system are transformed into contract test cases for each microservice. The experimental results showed that LTM3 can effectively migrate most test cases, with only a tiny portion requiring manual adjustment. © 2024 IEEE.

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
- **my_justification:** "Out of scope"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1312.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
