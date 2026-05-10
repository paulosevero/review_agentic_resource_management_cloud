---
id: paper-2618
title: Research on UAV–MEC Cooperative Scheduling Algorithms Based on Multi-Agent Deep Reinforcement Learning
authors:
- Huo, Yonghua
- Liu, Ying
- Jiang, Anni
- Yang, Yang
venue: Computers, Materials and Continua
venue_type: journal
year: 2026
doi: 10.32604/cmc.2025.072681
url: https://www.scopus.com/pages/publications/105027967919?origin=resultslist
publisher: Tech Science Press
pages: ''
keywords:
- MATD3
- multi-agent deep reinforcement learning
- task offloading
- UAV-MEC networks
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

# paper-2618 — Research on UAV–MEC Cooperative Scheduling Algorithms Based on Multi-Agent Deep Reinforcement Learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> With the advent of sixth-generation mobile communications (6G), space–air–ground integrated networks have become mainstream. This paper focuses on collaborative scheduling for mobile edge computing (MEC) under a three-tier heterogeneous architecture composed of mobile devices, unmanned aerial vehicles (UAVs), and macro base stations (BSs). This scenario typically faces fast channel fading, dynamic computational loads, and energy constraints, whereas classical queuing-theoretic or convex-optimization approaches struggle to yield robust solutions in highly dynamic settings. To address this issue, we formulate a multi-agent Markov decision process (MDP) for an air–ground-fused MEC system, unify link selection, bandwidth/power allocation, and task offloading into a continuous action space and propose a joint scheduling strategy that is based on an improved MATD3 algorithm. The improvements include Alternating Layer Normalization (ALN) in the actor to suppress gradient variance, Residual Orthogonalization (RO) in the critic to reduce the correlation between the twin Q-value estimates, and a dynamic-temperature reward to enable adaptive trade-offs during training. On a multi-user, dual-link simulation platform, we conduct ablation and baseline comparisons. The results reveal that the proposed method has better convergence and stability. Compared with MADDPG, TD3, and DSAC, our algorithm achieves more robust performance across key metrics. Copyright © 2025 The Authors.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2618.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
