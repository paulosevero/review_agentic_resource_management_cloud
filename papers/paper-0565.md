---
id: paper-0565
title: Multi-agent deep reinforcement learning for collaborative task offloading in mobile edge computing networks
authors:
- Chen, Minxuan
- Guo, Aihuang
- Song, Chunlin
venue: 'Digital Signal Processing: A Review Journal'
venue_type: journal
year: 2023
doi: 10.1016/j.dsp.2023.104127
url: https://www.scopus.com/pages/publications/85163539256?origin=resultslist
publisher: Elsevier Inc.
pages: ''
keywords:
- Collaborative decision-making
- Deep reinforcement learning
- Mobile edge computing
- Multi-agent deep deterministic policy gradient
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

# paper-0565 — Multi-agent deep reinforcement learning for collaborative task offloading in mobile edge computing networks

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> As is widely accepted, mobile edge computing (MEC) is a promising technology to enable wireless devices (WDs) to process computation-intensive tasks. Due to the mutual influence among different WDs, collaborative task offloading is needed in multi-agent environments. In this paper, a multi-agent MEC network with delay-sensitive and non-partitionable tasks is considered, as well as the load on MEC servers. The joint optimization problem of offloading decision and resource allocation is formulated to minimize the average delay. To realize the collaborative decision-making, a multi-agent deep reinforcement learning based algorithm is proposed based on the framework of centralized training and decentralized execution. The centralized deep neural networks (DNN) learn from the past experience and the WDs learn policies from the evaluation of the actions from the centralized DNNs. Based on the learned policies, WDs can make offloading decisions with only local information. Simulation results show that the proposed algorithm achieves near-optimal performance and has the advantage of high stability in varying multi-agent environments. © 2023 Elsevier Inc.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-0565.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
