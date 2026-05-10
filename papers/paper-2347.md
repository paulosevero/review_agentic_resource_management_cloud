---
id: paper-2347
title: 'Offloading in V2X with road side units: Deep reinforcement learning'
authors:
- Yahya, Widhi
- Lin, Ying-Dar
- Marzuk, Faysal
- Chołda, Piotr
- Lai, Yuan-Cheng
venue: Vehicular Communications
venue_type: journal
year: 2025
doi: 10.1016/j.vehcom.2024.100862
url: https://www.scopus.com/pages/publications/85211235560?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- 5G
- AI
- Mobile edge computing
- Offloading
- Reinforcement learning
- V2X
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-2347 — Offloading in V2X with road side units: Deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Traffic offloading is crucial for reducing computing latency in distributed edge systems such as vehicle-to-everything (V2X) networks, which use roadside units (RSUs) and access network mobile edge computing (AN-MEC) with ML agents. Traffic offloading is part of the control plane problem, which requires fast decision-making in complex V2X systems. This study presents a novel ratio-based offloading strategy using the twin delayed deep deterministic policy gradient (TD3) algorithm to optimize offloading ratios in a two-tier V2X system, enabling computation at both RSUs and the edge. The offloading optimization covers both vertical and horizontal offloading, introducing a continuous search space that needs fast decision-making to accommodate fluctuating traffic in complex V2X systems. We developed a V2X environment to evaluate the performance of the offloading agent, incorporating latency models, state and action definitions, and reward structures. A comparative analysis with metaheuristic simulated annealing (SA) is conducted, and the impact of single versus multiple offloading agents with deployment options at a centralized central office (CO) is examined. Evaluation results indicate that TD3's decision time is five orders of magnitude faster than SA. For 10 and 50 sites, SA takes 602 and 20,421 seconds, respectively, while single-agent TD3 requires 4 to 24 milliseconds and multi-agent TD3 takes 1 to 3 milliseconds. The average latency for SA ranges from 0.18 to 0.32 milliseconds, single-agent TD3 from 0.26 to 0.5 milliseconds, and multi-agent TD3 from 0.22 to 0.45 milliseconds, demonstrating that TD3 approximates SA performance with initial training. © 2024 Elsevier Inc.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2347.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
