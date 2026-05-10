---
id: paper-0720
title: Research on overall energy consumption optimization method for data center based on deep reinforcement learning
authors:
- Simin, Wang
- Lulu, Qin
- Chunmiao, Ma
- Weiguo, Wu
venue: Journal of Intelligent and Fuzzy Systems
venue_type: journal
year: 2023
doi: 10.3233/JIFS-223769
url: https://www.scopus.com/pages/publications/85166388656?origin=resultslist
publisher: IOS Press BV
pages: 7333--7349
keywords:
- cooling system
- data center
- deep reinforcement learning
- Energy consumption
- job scheduling
- multi-agent system
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

# paper-0720 — Research on overall energy consumption optimization method for data center based on deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the rapid development of cloud computing, there are more and more large-scale data centers, which makes the energy management of data centers more complex. In order to achieve better energy-saving effect, it is necessary to solve the problems of concurrent management and interdependence of IT, refrigeration, storage, and network equipment. Reinforcement learning learns by interacting with the environment, which is a good way to realize the independent management of the data center. In this paper, a overall energy consumption method for data center based on deep reinforcement learning is proposed to achieve collaborative energy saving of data center task scheduling and refrigeration equipment. A new multi-agent architecture is proposed to separate the training process from the execution process, simplify the interaction process during system operation and improve the operation effect. In the deep learning stage, a hybrid deep Q network algorithm is proposed to optimize the joint action value function of the data center and obtain the optimal strategy. Experiments show that compared with other reinforcement learning methods, our method can not only reduce the energy consumption of the data center, but also reduce the frequency of hot spots. © 2023 - IOS Press. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0720.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
