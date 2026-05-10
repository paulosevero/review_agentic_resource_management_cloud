---
id: paper-0965
title: Dynamic optimization of Traffic management using Gen AI
authors:
- Jegadeesan, S.
- Harin Sowmiya, M.
- Ambika, R.
- Thanusha, S.
venue: 2024 International Conference on Smart Technologies for Sustainable Development Goals, ICSTSDG 2024
venue_type: conference
year: 2024
doi: 10.1109/ICSTSDG61998.2024.11026149
url: https://www.scopus.com/pages/publications/105011827076?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Dynamic optimization
- Generative AI
- Image classification
- Image generation
- Movement detection
- Shortest path detection
- Traffic detection
- Transport networks
- Urban planning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)
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
    proposed_decision: Include
    proposed_justification: Talvez tenha algo de LLM e/ou Agentic AI.
    winning_category: llm_agentic_ai_generic
    overrides_applied:
    - ovr_rl_llm_present
    - ovr_cls_llm_present
    my_final_decision: Exclude
    my_justification: Out of scope
    agrees_with_regex: false
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

# paper-0965 — Dynamic optimization of Traffic management using Gen AI

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Dynamic optimization of traffic management using cloud GenAi is a sophisticated technique strengthened for the maximum improvementof urban traffic flow coupled with the relief ofcongestion through the adoption of cutting-edge image processing and deep learning techniques. Basically, the system begins with the process of image taking of vehicles in the dataset. Images of the cars are pre-processed using resizing and grey-scale conversion. This cloud-infrastructure feature provides integration with external data sources like weather and road incidents, thereby sharpening the prediction of traffic flow. The server will compute further based on the Signal Switching Algorithm that has the idea of optimizing flow through switching between multiple alternate stop settings. The process involved in the extraction of key features in an image makes use of statistical measures and LBP. After that, these images are separated into training sets and test sets for the development as well as evaluation of the detection model of a vehicle which would use YOLO. The vehiclecounts per unit length is then calculated in order to obtain the traffic density and then forwarded to the cloud server in order to store it. The accuracy anderror rate quantifies the performance of the system,and the result is reported in the form of comparison graphs and tables. The web application interface also facilitates further accessibility and engagement with the facility of registration, login, uploading images, andretrieving results. © 2024 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0.5 (resource management signal); C3=0 (no infra signal)"
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

- **regex_decision:** Include
- **regex_justification:** "Talvez tenha algo de LLM e/ou Agentic AI."
- **winning_category:** 'llm_agentic_ai_generic'
- **overrides_applied:** ['ovr_rl_llm_present', 'ovr_cls_llm_present']
- **evidence_trail:**
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Gen AI" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "GenAi" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Gen AI" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "GenAi" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_genai, matched_substring: "GenAi" }`
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

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0965.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
