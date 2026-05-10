---
id: paper-2630
title: 'Evaluating the Practicality of Language Models on Edge Devices for Sensor Data Analysis: A Sensible Approach?'
authors:
- Karthikeyan, Dinesh Kumar
- Shanmugasundaram, Roopesh Kumar
- Paavonen, Anna-Sofia
- Mäkitalo, Niko
venue: Lecture Notes in Networks and Systems
venue_type: conference
year: 2026
doi: 10.1007/978-3-032-03072-6_6
url: https://www.scopus.com/pages/publications/105022156490?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 63--85
keywords:
- Edge Device
- EdgeSense/HealthSense
- Internet of Things (IoT)
- Language Models (LMs)
- Large Language Models (LLMs)
- Prompt Engineering
- Sensors
- Small Langauge Models (SLMs)
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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
    my_justification: LLM as workload
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

# paper-2630 — Evaluating the Practicality of Language Models on Edge Devices for Sensor Data Analysis: A Sensible Approach?

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid growth of IoT and sensor-enabled devices presents challenges in data processing, including high transport costs and resource constraints. Efficient on-device processing is essential to reduce cloud reliance and improve near real-time analysis. Language Models (LMs) offer a new intriguing approach to sensor data analysis, enabling interacting with the data and contextual reasoning. To explore this potential, we propose EdgeSense, a framework for experimenting with LMs on edge devices and mobile phones. As an example case study, we developed the EdgeSense/HealthSense mobile app, which classifies user activities using real-time sensor data and LMs. Our evaluation shows that while EdgeSense achieves over 80% accuracy, response generation remains resource-intensive, utilizing two CPU cores and over 40% of the memory. These results highlight both the potential and limitations of LMs for near real-time sensor data analysis on edge devices, emphasizing the need for further optimization. © The Author(s), under exclusive license to Springer Nature Switzerland AG 2026.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Models" }`
  - `{ category: rl, pattern_id: ovr_rl_llm_present, matched_substring: "Language Models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Language Models" }`
  - `{ category: classical_agents, pattern_id: ovr_cls_llm_present, matched_substring: "Language Models" }`
  - `{ category: llm_agentic_ai_generic, pattern_id: gen_lang_model, matched_substring: "Language Models" }`
- **llm_decision:** Include
- **llm_justification:** "Migrated from legacy v2 — pass-1 (regex) and pass-2 (LLM) collapsed; legacy used dual sub-agents."
- **agrees_with_regex:** False
- **divergence_reason:** None
- **model:** legacy-v2
- **timestamp:** 2026-05-09T00:00:00+00:00

### final

- **my_final_decision:** Exclude
- **my_justification:** "LLM as workload"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2630.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
