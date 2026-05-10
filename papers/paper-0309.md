---
id: paper-0309
title: Distributed Task Migration Optimization in MEC by Extending Multi-Agent Deep Reinforcement Learning Approach
authors:
- Liu, Chubo
- Tang, Fan
- Hu, Yikun
- Tang, Zhuo
- Li, Keqin
venue: IEEE Transactions on Parallel and Distributed Systems
venue_type: journal
year: 2021
doi: 10.1109/TPDS.2020.3046737
url: https://www.scopus.com/pages/publications/85098770653?origin=resultslist
publisher: IEEE Computer Society
pages: 1603--1614
keywords:
- Energy
- mobile edge computing
- mobility
- multi-agent reinforcement learning
- task migration
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

# paper-0309 — Distributed Task Migration Optimization in MEC by Extending Multi-Agent Deep Reinforcement Learning Approach

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Closer to mobile users geographically, mobile edge computing (MEC) can provide some cloud-like capabilities to users more efficiently. This enables it possible for resource-limited mobile users to offload their computation-intensive and latency-sensitive tasks to MEC nodes. For its great benefits, MEC has drawn wide attention and extensive works have been done. However, few of them address task migration problem caused by distributed user mobility, which can't be ignored with quality of service (QoS) consideration. In this article, we study task migration problem and try to minimize the average completion time of tasks under migration energy budget. There are multiple independent users and the movement of each mobile user is memoryless with a sequential decision-making process, thus reinforcement learning algorithm based on Markov chain model is applied with low computation complexity. To further facilitate cooperation among users, we devise a distributed task migration algorithm based on counterfactual multi-agent (COMA) reinforcement learning approach to solve this problem. Extensive experiments are carried out to assess the performance of this distributed task migration algorithm. Compared with no migrating (NM) and single-agent actor-critic (AC) algorithms, the proposed distributed task migration algorithm can achieve up 30-50 percent reduction about average completion time.  © 1990-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0309.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
