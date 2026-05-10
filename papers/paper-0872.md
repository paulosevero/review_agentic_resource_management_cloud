---
id: paper-0872
title: Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence
authors:
- Choi, Pyeongjun
- Kim, Jeongsoo
- Kwak, Jeongho
venue: NetAISys 2024 - Proceedings of the 2024 2nd International Workshop on Networked AI Systems
venue_type: conference
year: 2024
doi: 10.1145/3662004.3663555
url: https://www.scopus.com/pages/publications/85197303352?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 31--36
keywords:
- DVFS
- Offloaded analytics
- On-device AI
- Thermal and memory aware control
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

# paper-0872 — Impact of Joint Heat and Memory Constraints of Mobile Device in Edge-Assisted On-Device Artificial Intelligence

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Recently, consumer demand for artificial intelligence (AI) applications using deep neural network (DNN) model such as large language model (LLM), miXed Reality (XR), and AI assistants has been steadily increasing. Hitherto, on-device AI and offloaded analytics with the help of mobile edge computing (MEC) have been extensively studied to realize AI services on top of mobile devices. However, both technologies suffer from the limited resources of mobile devices, such as thermal resilience, battery capacity, and memory size. To tackle this problem, we first extensively examine the impact of heat and memory constraints of a mobile device when networking and processing resources and multi-dimensional DNN model sizes are dynamically managed for AI applications via motivating measurement. From the experimental results, we conjecture that the threshold-based approach for joint consideration of heat and memory constraints would increase the performance of AI applications in terms of energy, frames per second (FPS), and inference accuracy. Hence, we propose a threshold-based H&M algorithm that jointly adjusts offloading, Dynamic Voltage and Frequency Scaling (DVFS), and DNN model size, aiming to maximize inference accuracy while keeping target FPS with memory and heat constraints in various environments. Finally, we implement the proposed scheme on a mobile device and an MEC server and evaluate its performance and adaptability via extensive experiments. © 2024 Owner/Author.

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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0872.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
