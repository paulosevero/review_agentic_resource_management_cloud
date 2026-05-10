---
id: paper-0427
title: Multi-agent Computation Offloading in UAV Assisted MEC via Deep Reinforcement Learning
authors:
- He, Hang
- Ren, Tao
- Qiu, Yuan
- Hu, Zheyuan
- Li, Yanqi
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-030-97774-0_38
url: https://www.scopus.com/pages/publications/85127077595?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 416--426
keywords:
- Computation offloading
- Deep reinforcement learning
- Mobile edge computing
- Resource allocation
- Unmanned aerial vehicle
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-0427 — Multi-agent Computation Offloading in UAV Assisted MEC via Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Due to its high maneuverability and flexibility, there have been a growing popularity to adopt Unmanned Aerial Vehicles (UAVs) on Mobile Edge Computing (MEC), serving as edge platforms in infrastructure- unavailable scenarios, e.g., disaster rescue, field operation. Owing to the weak workload, UAVs are typically equipped with limited computing and energy resources. Hence, it is crucial to design efficient edge computation offloading algorithms which could achieve high edge computing performance while keeping low energy consumption. A variety of UAV assisted computation offloading algorithms have been proposed, most of which focus on the scheduling of computation offloading in a centralized way and could become infeasible when the network size increases greatly. To address the issue, we propose a semi-distributed computation offloading framework based on Multi-Agent Twin Delayed (MATD3) deep deterministic policy gradient to minimize the average system cost of the MEC network. We adopt the actor-critic reinforcement learning framework to learn an offloading decision model for each User Equipment (UE), so that each UE could make near-optimal computation offloading decisions by its own and does not suffer from the booming of the network size. Extensive experiments are carried out via numerical simulation and the experimental results verify the effectiveness of the proposed algorithm. © 2022, The Author(s), under exclusive license to Springer Nature Switzerland AG.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0427.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
