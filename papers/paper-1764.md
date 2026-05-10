---
id: paper-1764
title: Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks
authors:
- Lan, Shizhan
- Guo, Hao
- Wang, Zhenyu
- Yang, Lei
venue: 2025 International Conference on Sensor-Cloud and Edge Computing System, SCECS 2025
venue_type: conference
year: 2025
doi: 10.1109/SCECS65243.2025.11065779
url: https://www.scopus.com/pages/publications/105012240335?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 163--167
keywords:
- caching
- data distribution
- dge computing
- reinforcement learningdge computing
- reinforcement learninge
- vehicular network
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
    my_justification: RL
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

# paper-1764 — Data Dissemination and Caching Based on Deep Reinforcement Learning in the Vehicular Edge Networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The vehicle edge network leverages mobile edge computing (MEC) to provide low-latency data and intelligent services. A key challenge is how to efficiently utilize limited resources to disseminate data and promptly respond to service requests. Existing methods, which cache data at the edge to reduce access delay, only consider single-source data distribution. However, applications like object detection and trajectory prediction involve multiple data copies across edges and vehicles. The destination vehicle can retrieve data from multiple sources, requiring optimal source selection. To tackle these challenges, we formulate a joint optimization problem for data dissemination and caching from multiple sources to multiple destinations, considering data timeliness and request deadlines to maximize request success rates. Specifically, we transform the problem into a minimum Steiner tree problem and propose a multi-agent reinforcement learning algorithm to determine source selection and caching strategies. Extensive experiments demonstrate that our approach significantly improves request success rates compared to benchmarks.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1764.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
