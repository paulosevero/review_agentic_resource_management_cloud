---
id: paper-1327
title: Collaborative Task Offloading Optimization for Satellite Mobile Edge Computing Using Multi-Agent Deep Reinforcement Learning
authors:
- Zhang, Hangyu
- Zhao, Hongbo
- Liu, Rongke
- Kaushik, Aryan
- Gao, Xiangqiang
- Xu, Shenzhan
venue: IEEE Transactions on Vehicular Technology
venue_type: journal
year: 2024
doi: 10.1109/TVT.2024.3405642
url: https://www.scopus.com/pages/publications/85198239352?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 15483--15498
keywords:
- computation offloading
- distributed cooperative computing
- multi-agent deep reinforcement learning
- resource allocation
- Satellite mobile edge computing
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

# paper-1327 — Collaborative Task Offloading Optimization for Satellite Mobile Edge Computing Using Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Satellite mobile edge computing (SMEC) achieves efficient processing for space missions by deploying computing servers on low Earth orbit (LEO) satellites, which supplements a strong computing service for future satellite-terrestrial integrated networks. However, considering the spatio-temporal constraints on large-scale LEO networks, inter-satellite cooperative computing is still challenging. In this paper, a multi-agent collaborative task offloading scheme for distributed SMEC is proposed. Facing the time-varying available satellites and service requirements, each autonomous satellite agent dynamically adjusts offloading decisions and resource allocations based on local observations. Furthermore, for evaluating the behavioral contribution of an agent to task completion, we adopt a deep reinforcement learning algorithm based on counterfactual multi-agent policy gradients (COMA) to optimize the strategy, which enables energy-efficient decisions satisfying the time and resource restrictions of SMEC. An actor-critic (AC) framework is effectively exploited to separately implement centralized training and distributed execution (CTDE) of the algorithm. We also redesign the actor structure by introducing an attention-based bidirectional long short-term memory network (Atten-BiLSTM) to explore the temporal characteristics of LEO networks. The simulation results show that the proposed scheme can effectively enable satellite autonomous collaborative computing in the distributed SMEC environment, and outperforms the benchmark algorithms.  © 1967-2012 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1327.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
