---
id: paper-0118
title: A Proactive Context-Aware Service Replication Scheme for Adhoc IoT Scenarios
authors:
- Choudhury, Bikash
- Choudhury, Subhrabrata
- Dutta, Animesh
venue: IEEE Transactions on Network and Service Management
venue_type: journal
year: 2019
doi: 10.1109/TNSM.2019.2928698
url: https://www.scopus.com/pages/publications/85069898598?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1797--1811
keywords:
- Context-aware
- DCDP
- Internet of things
- proactive sensing
- service replication
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-0118 — A Proactive Context-Aware Service Replication Scheme for Adhoc IoT Scenarios

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> We consider a smart-city IoT scenario where large crowd may gather temporarily rendering the existing infrastructure inadequate for service consumption. This necessitates a service replication framework over quasi-adhoc scenario using the available computing resources carried by the users such as smart-phones. Such framework can offer fog computing solution in addition to enabling consumption of plethora of new services available with the crowd. In this paper, we propose a service replication scheme that achieves improved service availability, service response-time and system-wide resource utilization compared to the existing ones. The scheme uses a dual-threshold-based proactive sensing mechanism to identify the services which are required to be replicated in immediate future and a multi-agent-based optimal task assignment scheme that enables batch-wise decision making. These mechanisms acting together reduces the service drop rate and improves the system-wide resource utilization. The service response time and the overhead involved in making assignment decisions, are markedly reduced by applying a strategy that combines the benefits of both physical and functional contexts together. An integrated model for analyzing the performance of various generic service replication schemes, is also developed in this paper. © 2004-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=0.5 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0118.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
