---
id: paper-0172
title: FIPA-based reference architecture for efficient discovery and selection of appropriate cloud service using cloud ontology
authors:
- Abbas, Ghulam
- Mehmood, Amjad
- Lloret, Jaime
- Raza, Muhammad Summair
- Ibrahim, Muhammad
venue: International Journal of Communication Systems
venue_type: journal
year: 2020
doi: 10.1002/dac.4504
url: https://www.scopus.com/pages/publications/85087758265?origin=resultslist
publisher: John Wiley and Sons Ltd
pages: ''
keywords:
- cloud computing
- cloud discovery and selection
- cloud ontology
- FIPA
- JADE
- multiagent system
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: MAS clássico pré-LLM (FIPA)
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

# paper-0172 — FIPA-based reference architecture for efficient discovery and selection of appropriate cloud service using cloud ontology

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Cloud computing is considered the latest emerging computing paradigm and has brought revolutionary changes in computing technology. With the advancement in this field, the number of cloud users and service providers is increasing continuously with more diversified services. Consequently, the selection of appropriate cloud service has become a difficult task for a new cloud customer. In case of inappropriate selection of a cloud services, a cloud customer may face the vendor locked-in issue and data portability and interoperability problems. These are the major obstacles in the adoption of cloud services. To avoid these complexities, a cloud customer needs to select an appropriate cloud service at the initial stage of the migration to the cloud. Many researches have been proposed to overcome the issues, but problems still exist in intercommunication standards among clouds and vendor locked-in issues. This research proposed an IEEE multiagent Foundation for Intelligent Physical Agent (FIPA) compliance multiagent reference architecture for cloud discovery and selection using cloud ontology. The proposed approach will mitigate the prevailing vendor locked-in issue and also alleviate the portability and interoperability problems in cloud computing. To evaluate the proposed reference architecture and compare it with the state-of-the-art approaches, several experiments have been performed by utilizing the commonly used performance measures. Analysis indicates that the proposed approach enables significant improvements in cloud service discovery and selection in terms of search efficiency, execution, and response time. © 2020 John Wiley & Sons, Ltd.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "MAS clássico pré-LLM (FIPA)"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0172.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
