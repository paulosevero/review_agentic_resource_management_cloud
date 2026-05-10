---
id: paper-1013
title: 'Computing over the Sky: Joint UAV Trajectory and Task Offloading Scheme Based on Optimization-Embedding Multi-Agent Deep Reinforcement Learning'
authors:
- Li, Xuanheng
- Du, Xinyang
- Zhao, Nan
- Wang, Xianbin
venue: IEEE Transactions on Communications
venue_type: journal
year: 2024
doi: 10.1109/TCOMM.2023.3331029
url: https://www.scopus.com/pages/publications/85177063155?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 1355--1369
keywords:
- computation offloading
- mobile edge computing
- reinforcement learning
- trajectory control
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)
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

# paper-1013 — Computing over the Sky: Joint UAV Trajectory and Task Offloading Scheme Based on Optimization-Embedding Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Unmanned aerial vehicle (UAV)-assisted mobile edge computing (MEC) has emerged to support computation-intensive tasks in 6G systems. Since the battery capacity of a UAV is limited, to serve as many users as possible, a joint design on UAV trajectory and offloading strategy with consideration for service fairness is essential to provide energy-efficient computation offloading to the users in UAV-MEC networks. Unfortunately, such a joint decision-making problem is not straightforward due to various task types required from users and various functionalities of different UAVs enabled by different application programs. Considering the above issues, we take energy efficiency and service fairness as the objective, and propose a Multi-Agent Energy-Efficient joint Trajectory and Computation Offloading (MA-ETCO) scheme. To adapt to dynamic demands of users, we develop an optimization-embedding multi-agent deep reinforcement learning (OMADRL) algorithm. Each UAV autonomously learns the trajectory control decision based on MADRL to adapt to dynamic demands. Then, it will obtain the optimal computation offloading decision by solving a mixed-integer nonlinear programming problem. The computation offloading result, in turn, will be used as an indicator to guide UAVs' trajectory design. Compared to relying solely on deep reinforcement learning, such an optimization-embedding way reduces action space dimension and improves convergence efficiency.  © 1972-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0 (no infra signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1013.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
