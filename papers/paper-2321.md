---
id: paper-2321
title: RESOURCE OPTIMIZATION OF INTERNET OF VEHICLES EDGE COMPUTING BASED ON REPUTATION VALUE ALLOCATION
authors:
- Xing, Pengkang
- Liu, Zhongyu
venue: International Journal of Mechatronics and Applied Mechanics
venue_type: journal
year: 2025
doi: 10.17683/ijomam/issue22.v1.4
url: https://www.scopus.com/pages/publications/105025812731?origin=resultslist
publisher: Cefin Publishing House
pages: 40--52
keywords:
- Dynamic allocation
- Edge computing
- Internet of vehicles
- Reputation value
- Resource optimization
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-2321 — RESOURCE OPTIMIZATION OF INTERNET OF VEHICLES EDGE COMPUTING BASED ON REPUTATION VALUE ALLOCATION

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> A resource optimization method for edge computing in the internet of vehicles is proposed, which integrates the deep deterministic policy gradient algorithm with a reputation mechanism. The method dynamically adjusts task offloading strategies and allocates computing resources based on node reputation values, thereby enhancing system security and reliability. To improve convergence speed and stability, a priority experience replay mechanism is introduced. Simulation experiments are conducted under a baseline setting of 50 tasks and total computing resources of 100 GHz. The results show that the average processing delay of the proposed method is 2.25 s, which is 33.6%, 20.5%, and 9.7% lower than that of the double deep Q-network, deep deterministic policy gradient, and multi-agent multi-objective deep reinforcement Learning algorithms, respectively. In terms of resource allocation, nodes with a reputation value of 5.0 are allocated 13.12 GHz of computing resources, while those with a reputation value of 0.5 receive only 4.21 GHz. The proposed method effectively improves the operational efficiency and resource utilization of the internet of vehicles system, reduces energy consumption and operational costs, and provides a new approach for resource optimization in dynamic environments. © 2025 The Author(s). Published by Cefin Publishing House.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2321.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
