---
id: paper-2774
title: Robust dependency-aware task offloading for mobile edge computing in low network scenarios using multi-agent deep reinforcement learning
authors:
- Shi, Yanjun
- Wang, Qirui
- Li, Jiajian
- Wang, Xiaocong
- Wei, Chao
venue: Ad Hoc Networks
venue_type: journal
year: 2026
doi: 10.1016/j.adhoc.2026.104179
url: https://www.scopus.com/pages/publications/105034568222?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Dependence-aware
- Low network scenarios
- Mobile edge computing
- Multi-agent deep reinforcement learning
- Proactive offloading
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

# paper-2774 — Robust dependency-aware task offloading for mobile edge computing in low network scenarios using multi-agent deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Mobile Edge Computing (MEC) enhances mission-critical services for heterogeneous autonomous systems (vehicles, e.g., CAVs, USVs, UAVs, and robots), by offloading tasks to edge servers. However, dynamic and efficient offloading for computation-intensive tasks remains challenging in low network scenarios. These scenarios, characterized by unstable communication (e.g., signal fading, backhaul disruptions) due to base station irregularities, dynamic environments, or geography, cause vehicle communication failures, task interruptions, and resource contention. This leads to failed real-time decisions and potential traffic safety hazards, exacerbated by vehicle mobility. To address this challenge, this paper investigates the multi-vehicle task offloading problem for low network scenarios, which is modeled as a decentralized partially observable Markov decision process (Dec-POMDP) problem. Then, a task offloading framework combining a proactive offloading scheme and a dynamic priority allocation strategy is proposed. By incorporating the multi-agent proximal policy optimization (MAPPO) algorithm, the framework enables each vehicle to learn the globally optimal policy and make decisions independently. The method innovatively enables the vehicles to maintain uninterrupted task computation capability even in low network scenarios, while jointly optimizing the energy consumption of the vehicles in low network scenarios. Extensive simulation results demonstrate that, compared with baseline schemes, the proposed framework reduces energy consumption by more than 70% while maintaining a high task success rate. © 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2774.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
