---
id: paper-0224
title: Optimization of task offloading strategy for mobile edge computing based on multi-agent deep reinforcement learning
authors:
- Lu, Haifeng
- Gu, Chunhua
- Luo, Fei
- Ding, Weichao
- Zheng, Shuai
- Shen, Yifan
venue: IEEE Access
venue_type: journal
year: 2020
doi: 10.1109/ACCESS.2020.3036416
url: https://www.scopus.com/pages/publications/85102847429?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 202573--202584
keywords:
- Deep reinforcement learning
- Mobile edge computing
- Multi-agent
- Task offloading
- Wireless power transfer
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

# paper-0224 — Optimization of task offloading strategy for mobile edge computing based on multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Combined with wireless power transfer (WPT) technology, mobile edge computing can provide continuous energy supply and computing resources for mobile devices, and improve their battery life and business application scenarios. This article first designs the mobile edge computing (MEC) model of mobile devices with random mobility and hybrid access point (HAP) with data transmission and energy transmission. On this basis, the selection of target server and the amount of data of floading are taken as the learning objectives, and the task offloading strategy based on multi-agent deep reinforcement learning is constructed. Then combined with MADDPG algorithm and SAC algorithm, the problems of multi-agent environment instability and the difficulty of convergence are solved. The final experimental results show that the improved algorithm based on MADDPG and SAC has good stability and convergence. Compared with other algorithms, it has achieved good results in energy consumption, delay and task failure rate. © 2020 Institute of Electrical and Electronics Engineers Inc.. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0224.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
