---
id: paper-1791
title: Dynamic weight reinforcement learning method considering multiple factors in mobile edge computing system
authors:
- Li, Shihua
- Zhou, Yanjie
- Liu, Xiangqian
- Wang, Ning
- Wang, Junqi
- Zhou, Bing
- Wang, Zongmin
venue: Neurocomputing
venue_type: journal
year: 2025
doi: 10.1016/j.neucom.2024.129194
url: https://www.scopus.com/pages/publications/85213061992?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computation offloading
- Dynamic weight
- Multi-objective deep reinforcement learning
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
    proposed_justification: C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)
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

# paper-1791 — Dynamic weight reinforcement learning method considering multiple factors in mobile edge computing system

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> The accelerated advancement of Mobile Edge Computing (MEC) has facilitated significant progressions in digital medical diagnostic services. However, the multi-region, multi-user, and multi-priority characteristics in medical diagnostic services within MEC systems make the task of offloading problematic. On the one hand, the task offloading problem involves multiple conflicting objectives, such as minimizing delay costs, server load balancing, and user fairness. Some researchers have explored these issues and proposed reinforcement learning-based methods to tackle such problems. However, existing work often characterizes objectives as linear scalarizations of multiple objectives, overlooking their conflicts. On the other hand, the preferences for various objectives in different regions cannot be predicted in advance and may indeed differ, making it challenging to handle in existing research. To address these challenges, we propose a multi-objective, multi-agent reinforcement learning approach. In this approach, the reward at each step is a vector, with each scalar corresponding to an objective. Furthermore, we propose a multi-agent tournament selection method to identify historically significant preferences. This mechanism considers the strategies of other agents while preserving the policies previously learned by the current agent. The objective is to achieve cooperative scheduling, allowing agents to synchronize their decisions based on their historical preferences and those of other agents. Simulation results demonstrate that the proposed algorithm outperforms several baseline algorithms across various performance metrics. © 2024 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0.5 (agentic/LLM signal in title); C2=0 (no resource management signal); C3=1.0 (infra/cloud-edge signal)"
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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-1791.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
