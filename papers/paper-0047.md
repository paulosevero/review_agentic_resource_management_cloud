---
id: paper-0047
title: Utilising Fog Computing for Developing a Person-Centric Heart Monitoring System
authors:
- Akrivopoulos, Orestis
- Amaxilatis, Dimitrios
- Mavrommati, Irene
- Chatzigiannakis, Ioannis
venue: Proceedings - 2018 International Conference on Intelligent Environments, IE 2018
venue_type: conference
year: 2018
doi: 10.1109/IE.2018.00010
url: https://www.scopus.com/pages/publications/85061531693?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 9--16
keywords:
- Fog computing
- Hear disease
- Heart monitoring
- Person centric
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

# paper-0047 — Utilising Fog Computing for Developing a Person-Centric Heart Monitoring System

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Heart disease and stroke are becoming the leading causes of death worldwide. Electrocardiography monitoring devices (ECG) are the only tool that help physicians diagnose cardiac abnormalities. Although the design of ECGs has followed closely the electronics miniaturization evolution over the years, existing wearable ECGs have limited accuracy and rely on external resources to analyse the signals and evaluate heart activity. In this paper, we work towards empowering the wearable device with processing capabilities to locally analyse the signal and identify abnormal behaviour. The ability to differentiate between normal and abnormal heart activity significantly reduces (a) the need to store the signals, (b) the data transmitted to the cloud, (c) the overall power consumption and (d) the confidentiality of private data. Based on this concept, the HEART system presented in this work, combines wearable embedded devices, mobile edge devices, and cloud services to provide on-the-spot, reliable, accurate, and instant heart monitoring. The wearable device is remotely trained by a physician to learn to accurately identify critical events related to each particular patient. Following this training session, the wearable device becomes capable of interpreting a large number of heart abnormalities without relying on cloud services and edge resources, when the medical doctor is not present. The Fog computing approach extends the cloud computing paradigm by migrating data-processing closer to production site, thus accelerating the system's responsiveness to events. The HEART system's performance concerning the accuracy of detecting abnormal events and the power consumption of the wearable device is evaluated. Results indicate that a very high success rate can be achieved in terms of event detection ratio and the battery is able to sustain operation up to a full week without the need for recharge. © 2018 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0047.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
