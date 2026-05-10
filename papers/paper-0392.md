---
id: paper-0392
title: Multi-agent DDPG Enpowered UAV Trajectory Optimization for Computation Task Offloading
authors:
- Chen, ZhiJiang
- Lei, Lei
- Song, XiaoQin
venue: International Conference on Communication Technology Proceedings, ICCT
venue_type: conference
year: 2022
doi: 10.1109/ICCT56141.2022.10073166
url: https://www.scopus.com/pages/publications/85152278683?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 608--612
keywords:
- computation offloading policy
- deep deterministic policy gradient
- mobile edge computing
- UAV trajectory optimization
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

# paper-0392 — Multi-agent DDPG Enpowered UAV Trajectory Optimization for Computation Task Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> In order to solve the problems of high cost, poor mobility and difficulty in coping with emergency in large-scale deployment of fixed edge computing nodes in mobile edge computing(MEC), an unmanned aerial vehicle(UAV)-assist task offloading algorithm is proposed to meet the need of computing-intensive and delay-sensitive mobile services. Considering constraints such as the flight range, flight speed of multiple UAVs and system fairness among users, the method aims to minimize the weighted sum of the average computing delay of users and the UAV's energy consumption. This non-convex and NP-hard problem is transformed into a partially observed Markov decision process, and we propose a multi-agent deep deterministic policy gradient algorithm to get optimal offloading decision and UAV flight trajectory. Simulation results show that the proposed algorithm outperforms the baseline algorithm in terms of fairness of mobile service terminals, average system delay and total energy consumption of multiple UAVs. © 2022 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0392.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
