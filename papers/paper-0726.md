---
id: paper-0726
title: Design and Development of a Log Management System Based on Cloud Native Architecture
authors:
- Sun, Yuchen
- Chen, Yanpiao
- Zhao, Haotian
- Peng, Shan
venue: ICSAI 2023 - 9th International Conference on Systems and Informatics
venue_type: conference
year: 2023
doi: 10.1109/ICSAI61474.2023.10423328
url: https://www.scopus.com/pages/publications/85186118265?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Anomaly Detection
- Cloud Native
- Log System
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

# paper-0726 — Design and Development of a Log Management System Based on Cloud Native Architecture

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapidly development and wide application of cloud computing and service computing, the use of cloud native architecture has become a mainstream trend in software development and deployment. In this booming background, logs have become the key information for each application to record its operation process throughout its life cycle, while existing log management systems are usually designed for specific production environments, which are not able to effectively meet the growing and diversified scenarios. The existing log management systems are usually designed for specific production environments and cannot effectively meet the needs of the growing number of diverse scenarios. Therefore, how to effectively handle log information from multiple sources becomes a key issue. In this paper, we design and develop a log management platform based on cloud-native architecture, which provides log collection, transmission, storage, and system management functions, and at the same time can be oriented to the cloud-native environment and other third-party applications for collection, providing a powerful tool for developers and operation and maintenance personnel. In addition, we designed an anomaly detection system using large language models for log parsing and used this system for anomaly detection in platform logs. Finally, the effectiveness of the system was verified by commonly used log data. The log management platform based on cloud-native architecture passed the test and has been utilized in our real production.  © 2023 IEEE.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0726.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
