---
id: paper-2598
title: 'Dual-timeslot optimization and UAV collaboration: A novel task offloading strategy for low-altitude power internet of things'
authors:
- He, Chao
- Wang, Chaofan
- Jiang, Wenhui
- Chen, Tao
- Zhang, Sirui
- Zhang, Yi
venue: Future Generation Computer Systems
venue_type: journal
year: 2026
doi: 10.1016/j.future.2026.108432
url: https://www.scopus.com/pages/publications/105034269483?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Dual-timeslot optimization
- Dynamic environment
- Mobile edge computing
- Power internet of things
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

# paper-2598 — Dual-timeslot optimization and UAV collaboration: A novel task offloading strategy for low-altitude power internet of things

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> AbstractWith the continuous expansion of the Power Internet of Things (PIoT), traditional ground-based nodes face severe challenges in terms of latency, energy consumption, and coverage, especially in low-altitude inspection scenarios. To address these issues, this paper proposes a dual-timeslot cooperative optimization framework, named TSCO-PIoT, which integrates edge servers and unmanned aerial vehicles (UAVs) into an air–ground collaborative system. In the long-timeslot layer, an LSTM-based Deep Deterministic Policy Gradient (LSTM-DDPG) model is employed to optimize service caching and task offloading decisions by exploiting temporal correlations in service requests. In the short-timeslot layer, a multi-agent cooperative genetic algorithm (SMA-GAC) is designed to jointly adjust task offloading decisions, computing resources, and communication bandwidth in response to fast-varying channel and workload dynamics. The two layers are coordinated through a dual-timeslot protocol that aggregates short-timeslot quality-of-experience (QoE) and cache switching costs into long-timeslot rewards. Simulation results show that, compared with representative baseline schemes, TSCO-PIoT reduces average task offloading latency by 24.7%, lowers system energy consumption by 32.8%, increases cache hit rate by 12.5%, and improves edge resource utilization by 15.3%. These results demonstrate that TSCO-PIoT provides adaptive and efficient scheduling for heterogeneous and time-varying PIoT environments. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2598.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
