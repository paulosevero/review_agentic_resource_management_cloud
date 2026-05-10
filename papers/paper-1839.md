---
id: paper-1839
title: Joint Task Partitioning and Resource Allocation in RAV-Enabled Vehicular Edge Computing Based on Deep Reinforcement Learning
authors:
- Liang, Hongbin
- Zhang, Han
- Ale, Laha
- Hong, Xintao
- Wang, Lei
- Jia, Qiong
- Zhao, Dongmei
venue: IEEE Internet of Things Journal
venue_type: journal
year: 2025
doi: 10.1109/JIOT.2025.3527929
url: https://www.scopus.com/pages/publications/85215279174?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15453--15466
keywords:
- Computation offloading
- deep reinforcement learning (DRL)
- remote aerial vehicles (RAVs)
- task partitioning
- vehicle edge computing (VEC)
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

# paper-1839 — Joint Task Partitioning and Resource Allocation in RAV-Enabled Vehicular Edge Computing Based on Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicle edge computing (VEC) leverages compact cloud computing at the mobile network edge to meet the processing and latency needs of vehicles. By bringing computation closer to the vehicles, VEC reduces data transmission, minimizes latency, and boosts performance for compute-intensive applications. However, during peak hours of urban road traffic, the scarce computational resources available at edge servers could pose challenges in fulfilling the processing needs of vehicles. Introducing remote aerial vehicles (RAVs) as supplementary edge computing nodes could significantly mitigate the aforementioned issue. In this article, we propose a flexible edge computing framework in which a fleet of RAVs function as mobile computational service providers, offering computation offloading services to multiple vehicles. We design and optimize a computation offloading model for the RAV-enabled VEC environment. The proposed model tackles the task offloading challenge, aiming to optimize RAV revenue and task processing efficiency while considering the constraints of RAVs’ restricted computational power and energy resources. Toward this end, our model jointly considers two key factors: 1) task partitioning and 2) computational resource allocation. To tackle the challenges posed by the aforementioned nonconvex optimization problem, we construct a Markov decision process (MDP) model for the multi-RAV-enabled mobile edge computing system and introduce an innovative multiagent deep reinforcement learning (MADRL) framework addressing the decision-making challenge represented by MDP model. Comprehensive simulation outcomes illustrate that our devised task offloading technique outperforms other optimization methods. © 2014 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1839.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
