---
id: paper-2446
title: Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading
authors:
- Zhang, Xinyi
- Wang, Chunyang
- Zhu, Yanmin
- Cao, Jian
- Liu, Tong
venue: IEEE Transactions on Mobile Computing
venue_type: journal
year: 2025
doi: 10.1109/TMC.2025.3539945
url: https://www.scopus.com/pages/publications/85217484156?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 5839--5856
keywords:
- Computation offloading
- edge computing
- multi-agent reinforcement learning
- task migration
- trajectory prediction
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

# paper-2446 — Multi-Agent Deep Reinforcement Learning With Trajectory Prediction for Task Migration-Assisted Computation Offloading

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Multi-access edge computing has become an effective paradigm to provide offloading services for computation-intensive and delay-sensitive tasks on vehicles. However, high mobility of vehicles usually incurs spatio-temporal load-imbalances among edge servers. Therefore, task migration is employed to maintain dynamic workload balancing by transmitting excessive tasks from overloaded to underloaded servers. Recent studies adopt deep reinforcement learning approaches to generate offloading and migration decisions based on current observations of systems. However, we argue that the migration direction is highly dependent on vehicular movements, and task migration towards the wrong direction could lead to additional delays. Therefore, we emphasize the importance of guiding task migration via exploring prospective trajectories of vehicles. We propose a Mobility-Aware Cooperative Multi-Agent (MCMA) deep reinforcement learning approach to make vehicle-by-vehicle decisions in multi-edge computation offloading scenarios. A two-stage decision framework is designed to solve the joint optimization problem of computation offloading and resource allocation. Additionally, an Informer-based multi-step vehicular trajectory prediction module is incorporated to enhance the capability of forecasting vehicular movements. Extensive experiments and analysis are conducted on synthetic and realistic scenarios, showing that our approach consistently outperforms both heuristic and DRL-based methods. The simulation scenarios and source codes are publicly available here. © 2002-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2446.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
