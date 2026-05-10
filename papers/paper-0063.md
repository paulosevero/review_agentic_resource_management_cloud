---
id: paper-0063
title: Intelligent query processing from biotechnological database using co-operating agents in a secure cloud environment
authors:
- Geetha, R.
- Shunmuganathan, K.L.
venue: ARPN Journal of Engineering and Applied Sciences
venue_type: journal
year: 2018
doi: ''
url: https://www.scopus.com/pages/publications/85045697378?origin=resultslist
publisher: Asian Research Publishing Network
pages: 2511--2518
keywords:
- Cloud computing
- FIPA ACL
- Hadoop
- Multi-agent
- Pattern matching
- Query processing
- Sentinel
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

# paper-0063 — Intelligent query processing from biotechnological database using co-operating agents in a secure cloud environment

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is a scalable and flexible environment that delivers economical computing facilities to clients based on queries. Response to query depends upon the speed of pattern matching, error correction, and resource allocation during query processing. The algorithms for query processing, sequence alignments of data from NCBI, EMBL, DDBJ and storage of recurring complex enquiries, are complicated and time consuming in the HADOOP framework. In order to obtain secure, swift and consistent response to queries, multi-agents have been introduced as a substitute for Job Tracker. They enhance the pace of query handling, allocate tasks to the Task Trackers, boost fault tolerance and increase reliability. Multi-Agents have also been deployed amid user and Agents, in the middle of Agents and between platforms to provide security measures. Agent development is done following the FIPA (Foundation for Intelligent Physical Agents) standards, using FIPA ACL (Agent Communication Language). © 2006-2018 Asian Research Publishing Network (ARPN).

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0063.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
