---
id: paper-2599
title: Dynamic resource allocation for multiagent systems via deep reinforcement learning
authors:
- He, Zhisheng
venue: Proceedings of SPIE - The International Society for Optical Engineering
venue_type: conference
year: 2026
doi: 10.1117/12.3105724
url: https://www.scopus.com/pages/publications/105033016970?origin=resultslist
publisher: SPIE
pages: ''
keywords:
- deep reinforcement learning
- dynamic resource allocation
- fairness-efficiency tradeoff
- management objectives
- Multi-agent systems
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

# paper-2599 — Dynamic resource allocation for multiagent systems via deep reinforcement learning

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The rapid development of multi-agent systems (MAS) has introduced significant challenges in dynamic resource allocation (DRA), particularly in scenarios requiring real-time decision-making under uncertainty. Traditional optimization methods often struggle to balance competing objectives such as efficiency, fairness, and priority constraints, especially in large-scale, heterogeneous environments. This study addresses these limitations by proposing a management-oriented deep reinforcement learning (DRL) framework for MAS, which integrates domain-specific objectives into the learning process to achieve adaptive and policy-compliant resource distribution. The research develops a DRL-based solution that dynamically allocates resources while maintaining system efficiency under varying constraints. The methodology employs a multiagent actor-critic architecture, leveraging centralized training with decentralized execution (CTDE) to handle inter-agent coordination. Key algorithmic components include a hybrid reward mechanism combining global efficiency metrics with fairness indices, as well as a scalable state representation for heterogeneous agents. The study further highlights the model's ability to generalize across varying demand patterns, making it suitable for applications like cloud computing task scheduling and smart grid energy distribution. These findings underscore the potential of DRL to bridge technical optimization and managerial decision-making, offering a flexible paradigm for complex resource allocation problems. © COPYRIGHT SPIE. Downloading of the abstract is permitted for personal use only.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2599.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
