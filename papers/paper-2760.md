---
id: paper-2760
title: Service migration optimization method for intelligent connected vehicles based on multi-agent deep reinforcement learning; [基于多智能体深度强化学习的智能网联汽车服务迁移优化方法]
authors:
- Rui, Lanlan
- Deng, Shuyu
- Chen, Zixuan
- Gao, Zhipeng
- Qiu, Xuesong
- Guo, Shaoyong
venue: Tongxin Xuebao/Journal on Communications
venue_type: journal
year: 2026
doi: 10.11959/j.issn.1000-436x.2026005
url: https://www.scopus.com/pages/publications/105030938170?origin=resultslist
publisher: Editorial Board of Journal on Communications
pages: 141--155
keywords:
- group relative policy optimization
- intelligent connected vehicles
- mobile edge computing
- multi-agent deep reinforcement learning
- service migration
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

# paper-2760 — Service migration optimization method for intelligent connected vehicles based on multi-agent deep reinforcement learning; [基于多智能体深度强化学习的智能网联汽车服务迁移优化方法]

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> To address the challenges of multi-user resource competition and dynamic changes in edge node availability faced by intelligent connected vehicles during service migration in a highly dynamic Internet of vehicles environment, a service migration method based on multi-agent group relative policy optimization (MAGRPO) was proposed. The service migration problem was formalized as a long-term multi-user joint optimization problem with resource constraints, and a MAGRPO algorithm that did not require an explicit critic network was designed. A policy update signal was constructed based on the relative ranking of discounted returns within the group, thereby effectively mitigating training instability caused by severe penalties (e.g., node overload or failure) and reducing training cost. Simulation results show that the proposed method outperforms existing baseline methods in key metrics such as total service delay, migration energy consumption, and migration success rate. It exhibits stronger robustness and scalability in scenarios where edge node resources are limited and their availability changes dynamically. © 2026, Editorial Board of Journal on Communications. All rights reserved.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2760.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
