---
id: paper-1403
title: 'A-MARL: Agile Multi-Agent Reinforcement Learning for Soft Real-Time Task Scheduling in Edge Computing'
authors:
- Avan, Amin
- Azim, Akramul
- Mahmoud, Qusay H.
venue: Proceedings - 2025 IEEE International Conference on Collaborative Advances in Software and Computing, CASCON 2025
venue_type: conference
year: 2025
doi: 10.1109/CASCON66301.2025.00053
url: https://www.scopus.com/pages/publications/105033227264?origin=resultslist
publisher: Institute of Electrical and Electronics Engineers Inc.
pages: 275--284
keywords:
- Edge Computing
- Multi-Agent Reinforcement Learning
- Real-Time Applications
- Real-Time Systems
- Reinforcement Learning
- Task Scheduling
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

# paper-1403 — A-MARL: Agile Multi-Agent Reinforcement Learning for Soft Real-Time Task Scheduling in Edge Computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Modern soft real-time applications (SRTAs) impose heavy computational demands on embedded devices. While offloading workloads to Edge Computing (EC) resources is attractive, task scheduling remains challenging due to strict timing constraints, a vast search space, multiple conflicting objectives, and highly dynamic environments. Conventional heuristic and meta-heuristic algorithms struggle to adapt to these conditions. Although reinforcement learning (RL) suits dynamic environments, single-agent RL converges slowly on mediumand large-scale problems due to enormous action spaces and excessive exploration. We present Agile Multi-Agent Reinforcement Learning (A-MARL), which enhances Multi-Agent PPO by replacing conventional exploration with entropy-guided rule-based exploration. When policy entropy is high, A-MARL employs Shortest Processing Time (SPT) to guide exploration toward promising action space regions. This adaptive mechanism accelerates convergence and delivers schedules better suited for SRTAs in EC environments. Experiments on representative scenarios show A-MARL consistently outperforms state-of-the-art baselines across all evaluated metrics, demonstrating its effectiveness for SRTA task scheduling in EC. © 2025 IEEE.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1403.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
