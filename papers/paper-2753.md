---
id: paper-2753
title: 'D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers'
authors:
- Ran, Yongyi
- Yin, Hui
- Sun, Tongyao
- Zhou, Xin
- Luo, Jiangtao
- Chen, Shuangwu
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2026
doi: 10.1109/TPDS.2025.3631654
url: https://www.scopus.com/pages/publications/105021539884?origin=resultslist
publisher: IEEE Computer Society
pages: 230--246
keywords:
- Deep reinforcement learning
- geo-distributed data center
- task scheduling
- thermal management
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)
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

# paper-2753 — D3T: Dual-Timescale Optimization of Task Scheduling and Thermal Management for Energy Efficient Geo-Distributed Data Centers

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The surge of artificial intelligence (AI) has intensified compute-intensive tasks, sharply increasing the need for energy-efficient management in geo-distributed data centers. Existing approaches struggle to coordinate task scheduling and cooling control due to mismatched time constants, stochastic Information Technology (IT) workloads, variable renewable energy, and fluctuating electricity prices. To address these challenges, we propose D3T, a dual-timescale deep reinforcement learning (DRL) framework that jointly optimizes task scheduling and thermal management for energy-efficient geo-distributed data centers. At the fast timescale, D3T employs Deep Q-Network (DQN) to schedule tasks, reducing operational expenditure (OPEX) and task sojourn time. At the slow timescale, a QMIX-based multi-agent DRL method regulates cooling across distributed data centers by dynamically adjusting airflow rates, thereby preventing hotspots and reducing energy waste. Extensive experiments were conducted using TRNSYS with real-world traces, and the results demonstrate that, compared to baseline algorithms, D3T reduces OPEX by 13% in IT subsystems and 29% in cooling subsystems, improves power usage effectiveness (PUE) by 7%, and maintains more stable thermal safety across geo-distributed data centers. © 1990-2012 IEEE.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=0.5 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2753.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
