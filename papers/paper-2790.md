---
id: paper-2790
title: Task Offloading for Internet of Things in Remote Areas Based on Multi-Agent Reinforcement Learning
authors:
- Sun, Chenxiao
- Liu, Yitong
- Deng, Juan
- Chen, Tianjiao
- Yang, Hongwen
venue: ICCIP 2025 - 2025 The 11th International Conference on Communication and Information Processing
venue_type: conference
year: 2026
doi: 10.1145/3784833.3784927
url: https://www.scopus.com/pages/publications/105030231553?origin=resultslist
publisher: Association for Computing Machinery, Inc
pages: 454--459
keywords:
- LEO
- MARL
- MEC
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
    proposed_justification: C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2790 — Task Offloading for Internet of Things in Remote Areas Based on Multi-Agent Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The emergence of Multi-access Edge Computing (MEC) integrated with low Earth orbit (LEO) satellite technology has revolutionized the processing of Internet of Things (IoT) data in remote areas, addressing the challenges of resource allocation in underserved regions. Thus, a satellite-terrestrial task offloading architecture for remote areas is presented, leveraging multi-agent reinforcement learning (MARL) and the integration of a LEO satellite. The uplink and downlink communication between users, the base station, and the LEO satellite are modeled, incorporating the hybrid automatic repeat request (HARQ) mechanism to enhance reliability. To minimize latency and energy consumption, a differential-based reinforcement learning training method (DRLTM) is introduced. The performance of three MARL algorithms - BiCNet, CommNet, and MADDPG - is evaluated within this architecture. Results demonstrate that DRLTM improves the convergence speed of MADDPG and CommNet by over 50%, while enabling BiCNet to achieve convergence. Additionally, all three MARL algorithms contribute to reducing overall network latency and energy consumption to varying degrees.  © 2025 Copyright held by the owner/author(s).

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Include
- **regex_justification:** "C1=1.0 (agentic/LLM signal in title); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2790.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
