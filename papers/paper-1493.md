---
id: paper-1493
title: 'Optimizing Digital Twin Construction in Smart Factories: A Latency-Minimized MEC Approach'
authors:
- Chou, Shih-Fan
- Pan, Jing-Jhih
venue: Proceedings - 2025 IEEE 26th International Symposium on a World of Wireless, Mobile and Multimedia Networks, WoWMoM 2025
venue_type: conference
year: 2025
doi: 10.1109/WoWMoM65615.2025.00058
url: https://www.scopus.com/pages/publications/105009229354?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 293--298
keywords:
- digital twin
- generative AI
- mobile edge computing (MEC)
- offloading
- smart factory
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-1493 — Optimizing Digital Twin Construction in Smart Factories: A Latency-Minimized MEC Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Digital twin technology plays a pivotal role in smart manufacturing by enabling real-time monitoring, predictive maintenance, and operational optimization. However, traditional digital twins often rely solely on text-based sensor data, resulting in limited system granularity and incomplete process representation. To address this gap, we incorporate image data from mobile devices to enrich digital twin construction with greater detail and accuracy. Given the high computational demands and strict latency requirements of image processing, we propose a Mobile Edge Computing (MEC)-based framework that offloads intensive tasks to nearby edge servers. To minimize system-wide delays, we develop the Min-Max Completion Time (MMCT) algorithm, which strategically prioritizes tasks with the longest processing time to reduce the overall completion time. Simulation results under realistic parameter settings demonstrate that MMCT significantly outperforms baseline approaches - including Pure Local Processing, Pure Offloading, and the Game-Theoretic Offloading Decision Method (GTODM) - especially in scenarios involving high data volume and computational complexity. By improving task responsiveness and reducing latency, our framework ensures timely and comprehensive digital twin updates. We also highlight the potential of integrating generative AI to further enhance task allocation and decision-making in MEC-driven digital twin systems.  © 2025 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1493.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
