---
id: paper-2476
title: Heterogeneous multi-agent deep reinforcement learning based low carbon emission task offloading in mobile edge computing
authors:
- Zhou, Xiongjie
- Guan, Xin
- Sun, Di
- Zhang, Xiaoguang
- Zhang, Zhaogong
- Ohtsuki, Tomoaki
venue: Computer Communications
venue_type: journal
year: 2025
doi: 10.1016/j.comcom.2025.108089
url: https://www.scopus.com/pages/publications/85217057189?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Deep reinforcement learning
- Internet of things
- Low carbon emission
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

# paper-2476 — Heterogeneous multi-agent deep reinforcement learning based low carbon emission task offloading in mobile edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile edge computing is an emerging computing paradigm in the Internet of Things. Task offloading is a critical method in mobile edge computing to alleviate computational resource constraints. Nowadays, the rising number of tasks is placing greater demands on computing resources. The increasing consumption of computing resources leads to high carbon emission. Achieving environmentally friendly mobile edge computing while effectively managing low-carbon task offloading poses a significant challenge. Recently, deep reinforcement learning has made certain progress in many research fields. However, there are few deep reinforcement learning methods that consider the carbon emission in task offloading. In this paper, we propose a deep reinforcement learning based low carbon emission task offloading algorithm for minimizing carbon emission in mobile edge computing. Firstly, since different base stations exist in the mobile edge computing environment, we consider the mobile edge computing environment with multiple heterogeneous agents. Secondly, to minimize carbon emission, we consider the carbon intensity of the base station as an optimization factor. We conclude the task offloading strategy to minimize carbon emission, consequently achieving the minimization of carbon emission. Moreover, our proposed algorithm allows user devices to decide their own preference for task offloading. Based on the specific requirements and preferences of user devices, our proposed algorithm can dynamically adjust the weights of delay, energy consumption, and carbon emission, respectively. Experiments indicate that the proposed algorithm can accurately and quickly conclude the task offloading strategy to minimize carbon emission. © 2025 Elsevier B.V.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2476.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
