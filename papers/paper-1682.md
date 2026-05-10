---
id: paper-1682
title: 'Diagnosphere: Diagnostic Intelligence and AI-Driven Global Network Optimizing Scans, Patient Health, Evaluation, and Research Ecosystem'
authors:
- Jadhav, Ranjana
- Sivakumar, Aditri
- Bhattacharya, Aditya
- Karad, Aditya
- Anand, Arnav
- Bachute, Orison
venue: EPJ Web of Conferences
venue_type: conference
year: 2025
doi: 10.1051/epjconf/202534101035
url: https://www.scopus.com/pages/publications/105024556353?origin=resultslist
publisher: EDP Sciences
pages: ''
keywords:
- Anomaly Detection
- Artificial Intelligence
- Cloud Computing
- Healthcare Collaboration
- Medical Imaging
- Patient Progress Tracking
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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
    proposed_decision: Exclude
    proposed_justification: Out of scope
    winning_category: out_of_scope
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: true
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

# paper-1682 — Diagnosphere: Diagnostic Intelligence and AI-Driven Global Network Optimizing Scans, Patient Health, Evaluation, and Research Ecosystem

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The contemporary medical system is severely stressed out by the enormous amount of medical imaging data and the need for more accurate patient monitoring. An architecture is introduced in this paper that uses AI for scan evaluation and tracking patient progress that allows real-time, collaborative, and secure AI analysis based on scans. The system utilizes embedding models, large language models (LLMs), and cloud computing to carry out tasks like anomaly detection, treatment evaluation, and recovery prediction [2] automatically. It guarantees the secure authentication of physicians and allows the collaboration initiated by the doctor, thus improving the accuracy and speed of clinical decisions. The suggested framework incorporates e-communication based on WebSocket for the quick sharing of knowledge among healthcare professionals, while better reporting tools, image data fusion, and preliminary image analysis are factors contributing to individualized and promptly provided medical evaluations. The system, developed using the Weaved application and AWS DynamoDB, provides very high data security, dependability, and scalability. In the end, such an AI-led approach is patient outcome–focused and it enhances the whole process of healthcare by utilizing the resources, managing the data, and executing the decisions fast and efficiently within an interlinked, intelligent, medical ecosystem [5]. © The Authors, published by EDP Sciences.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

- **regex_decision:** Exclude
- **regex_justification:** "Out of scope"
- **winning_category:** 'out_of_scope'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: out_of_scope, pattern_id: oos_patient_monitor, matched_substring: "patient monitoring" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "AI-Driven" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "large language models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "LLMs" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "AI-Driven" }`
- **llm_decision:** Exclude
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** True
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1682.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
