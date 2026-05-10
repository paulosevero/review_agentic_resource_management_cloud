---
id: paper-1485
title: 'Towards Dynamic Energy/Carbon Trading and Resource Allocation for MEC: A Two-Timescale Deep Reinforcement Learning Approach'
authors:
- Chen, Xiaojing
- Ding, Yijun
- Ni, Wei
- Wang, Xin
- Sun, Yichuang
- Zhang, Shunqing
venue: 2025 IEEE/CIC International Conference on Communications in China:Shaping the Future of Integrated Connectivity, ICCC 2025
venue_type: conference
year: 2025
doi: 10.1109/ICCC65529.2025.11148917
url: https://www.scopus.com/pages/publications/105017540124?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: ''
keywords:
- Carbon market
- deep reinforcement learning
- mobile edge computing
- smart grid
- two timescales
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

# paper-1485 — Towards Dynamic Energy/Carbon Trading and Resource Allocation for MEC: A Two-Timescale Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Integrating smart grid and carbon market into mobile edge computing (MEC) systems presents significant potential for reducing both operational energy costs and carbon footprints. This paper proposes a joint optimization framework for energy/carbon trading and resource allocation in MEC systems participating in grid-energy and carbon markets, aiming to minimize the long-term time-averaged cost of the energy/carbon tradings and the energy consumption of the system. Built on a twotimescale multi-agent deep reinforcement learning (TTMADRL) optimization framework, the Deep Deterministic Policy Gradient (DDPG) is generalized to make decisions on energy and carbon transactions at the large timescale; while at the small timescale, the task offloading schedules and CPU frequencies are distributively determined at each device by using the Multi-Agent DDPG (MADDPG) algorithm with enhanced scalability. Simulations demonstrate that the proposed TTMADRL achieves a 75.44% reduction in system costs compared to baseline approaches.  © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1485.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
