---
id: paper-0902
title: Adaptive task migration strategy with delay risk control and reinforcement learning for emergency monitoring
authors:
- Fan, Zhiyong
- Lin, Yuanmo
- Ai, Yuxun
- Xu, Hang
venue: Scientific Reports
venue_type: journal
year: 2024
doi: 10.1038/s41598-024-67886-x
url: https://www.scopus.com/pages/publications/85200044958?origin=resultslist
publisher: Nature Research
pages: ''
keywords:
- adult
- algorithm
- article
- awareness
- data processing
- decision making
- human
- interpersonal communication
- learning
- migration
- recycling
- resource allocation
- simulation
- workflow
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

# paper-0902 — Adaptive task migration strategy with delay risk control and reinforcement learning for emergency monitoring

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The timely and reliable handling of post-disaster emergency monitoring tasks is crucial for effective rescue operations. UAV-assisted edge computing plays a pivotal role in the rapid deployment of such systems. However, challenges persist due to communication and computation resource bottlenecks when dealing with delay-sensitive monitoring tasks. In dynamic post-disaster environments, effective task scheduling and resource allocation decisions directly impact the system’s ability to process tasks. Therefore, this paper proposes an adaptive task migration decision-making system for emergency monitoring tasks in UAV-assisted edge computing. Firstly, We decomposed the optimization objectives based on the task processing workflow, then devised a stepwise delay risk control and resource recovery mechanism based on early discarding. Secondly, by integrating multi-agent reinforcement learning (MARL), optimal strategies for task offloading, UAV queue scheduling, and communication resource allocation are learned to enhance the decision system’s environmental awareness and maximize the successful completion of emergency monitoring tasks. Simulation experiments demonstrate that the algorithm significantly improves the success rate of migration tasks and data processing capacity, thereby validating its convergence and effectiveness. © The Author(s) 2024.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0902.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
