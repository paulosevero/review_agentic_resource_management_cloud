---
id: paper-1530
title: Attention-Driven Deep Reinforcement Learning for Efficient Task Offloading in Mobile Edge Computing
authors:
- Dong, He
- Dou, Zheng
- Ji, Yanqi
- Dong, Jian
venue: 2025 10th International Symposium on Advances in Electrical, Electronics and Computer Engineering, ISAEECE 2025
venue_type: conference
year: 2025
doi: 10.1109/ISAEECE66033.2025.11160206
url: https://www.scopus.com/pages/publications/105018736551?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 223--228
keywords:
- Attention mechanism
- Deep reinforcement learning
- Distributed systems
- Mobile edge computing
- Task offloading
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

# paper-1530 — Attention-Driven Deep Reinforcement Learning for Efficient Task Offloading in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Advances in cloud computing and IoT have driven the optimization of distributed systems, enabling near-instantaneous responses. Mobile Edge Computing (MEC) enhances 6 G networks by migrating resource-intensive tasks to edge servers, reducing latency and energy use. This study integrates task offloading and resource allocation to minimize system-wide costs. Although Deep Reinforcement Learning (DRL) is adept at balancing immediate and long-term objectives, resource constraints across mobile devices and servers complicate its application. We propose multi-agent deep reinforcement learning with attention mechanism (AM_MADRL), an attention-based DRL framework, to address these challenges. The algorithm leverages attention mechanisms to extract task features and predict resource demands, enabling MEC servers to make coordinated offloading decisions while respecting system constraints. Simulations confirm AM_MADRL's superiority over existing methods in cost efficiency and scalability, positioning it as a robust solution for dynamic edge networks.  © 2025 IEEE.

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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1530.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
