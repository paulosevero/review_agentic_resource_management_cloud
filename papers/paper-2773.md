---
id: paper-2773
title: 'Enhanced perception and efficient exploration strategy for dynamic and uncertain UAV-assisted edge computing: AC-SAC'
authors:
- Shi, Shuo
- Li, Chenyu
- Wu, Chenyu
- Xi, Wang
venue: Wireless Networks
venue_type: journal
year: 2026
doi: 10.1007/s11276-025-04040-z
url: https://www.scopus.com/pages/publications/105021434546?origin=resultslist
publisher: Springer
pages: 31--46
keywords:
- Curiosity mechanism
- Multi-head attention mechanism
- Soft actor-critic
- Task offloading
- UAV-assisted edge computing
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: RL
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

# paper-2773 — Enhanced perception and efficient exploration strategy for dynamic and uncertain UAV-assisted edge computing: AC-SAC

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> UAV-assisted Mobile Edge Computing (UAV-MEC) presents significant potential for efficient computing services, yet its dynamic resource management and task offloading face complex challenges, including high-dimensional continuous action spaces, environmental uncertainties, and decision coupling. Traditional Reinforcement Learning (RL) struggles with handling complex multi-entity states effectively, and under dynamic User Equipment (UE) relationships and challenging reward signals, it often exhibits low exploration efficiency and can get trapped in local optima. To address these issues, this paper proposes a novel AC-SAC (Attentive-Curious Soft Actor-Critic) algorithm. The algorithm is built upon the Soft Actor-Critic (SAC) framework. It first integrates a Multi-Head Self-Attention mechanism. This mechanism enables intelligent perception of complex multi-entity states, allowing the agent to adaptively weight state components and profoundly understand dynamic UE relationships. Consequently, it improves environmental evaluation and policy accuracy. Concurrently, the algorithm incorporates a Prediction Error-Based Curiosity Mechanism, which generates intrinsic rewards to effectively supplement external rewards, guiding efficient exploration, overcoming local optima, and significantly enhancing the policy’s exploration efficiency and robustness by deeply learning uncertain environmental dynamics. Experimental results demonstrate that the AC-SAC algorithm effectively tackles dynamic UAV-MEC environments. By jointly optimizing UAV trajectory, UE service selection, and task offloading, it reduces task processing delay, showcasing excellent performance and learning efficiency. © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "RL"
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2773.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
