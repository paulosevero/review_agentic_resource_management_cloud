---
id: paper-0409
title: Multiple Workflows Offloading Based on Deep Reinforcement Learning in Mobile Edge Computing
authors:
- Gao, Yongqiang
- Wang, Yanping
venue: Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)
venue_type: conference
year: 2022
doi: 10.1007/978-3-030-95384-3_30
url: https://www.scopus.com/pages/publications/85126190904?origin=resultslist
publisher: Springer Science and Business Media Deutschland GmbH
pages: 476--493
keywords:
- Multi-agent DDPG
- Multi-objective optimization
- Multiple workflows offloading
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

# paper-0409 — Multiple Workflows Offloading Based on Deep Reinforcement Learning in Mobile Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the maturity of 5G technology and the popularization of smart terminal devices, the applications running on mobile terminals are becoming more and more diversified. Most of them are complex, computationally intensive, and time-sensitive applications such as workflow and machine learning tasks. The traditional cloud computing model is far away from the mobile terminal and thus cannot meet the stringent requirements of these applications on delay and energy consumption. As a new computing model, mobile edge computing can better solve the above problems. Mobile edge computing sinks part of the computing and storage resources in the cloud to the edge of the network close to the mobile device. With computational offloading, complex applications are offloaded to nearby edge servers for execution, which leads to low delay and energy consumption. The existing researches mainly focus on independent task offloading in mobile edge computing, and thus they are not suitable for workflow tasks offloading with dependence on mobile edge computing. This paper proposes a multiple workflows offloading strategy based on deep reinforcement learning in mobile edge computing with the goal of minimizing the overall completion time of multiple workflows and the overall energy consumption of multiple user equipments. We evaluate the performance of the proposed strategy by simulation experiments based on real-world parameters. The results show that the proposed strategy performs better than other alternatives in terms of the overall completion time and the overall energy consumption. © 2022, Springer Nature Switzerland AG.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0409.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
