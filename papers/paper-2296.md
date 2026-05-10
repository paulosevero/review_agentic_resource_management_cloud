---
id: paper-2296
title: Lightweight deep reinforcement learning for dynamic resource allocation in vehicular edge computing
authors:
- Wu, Dapeng
- Wu, Sijun
- Cui, Yaping
- Zhong, Ailing
- Tang, Tong
- Wang, Ruyan
- Lin, Xinqi
venue: Digital Communications and Networks
venue_type: journal
year: 2025
doi: 10.1016/j.dcan.2025.06.005
url: https://www.scopus.com/pages/publications/105018934773?origin=resultslist
publisher: KeAi Communications Co.
pages: 1530--1542
keywords:
- Lightweight
- Reinforcement learning
- Resource allocation
- Vehicular edge computing
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

# paper-2296 — Lightweight deep reinforcement learning for dynamic resource allocation in vehicular edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Vehicular Edge Computing (VEC) enhances the quality of user services by deploying wealth of resources near vehicles. However, due to highly dynamic and complex nature of vehicular networks, centralized decision-making for resource allocation proves inadequate within VECs. Conversely, allocating resources via distributed decision-making consumes vehicular resources. To improve the quality of user service, we formulate a problem of latency minimization, further subdividing this problem into two subproblems to be solved through distributed decision-making. To mitigate the resource consumption caused by distributed decision-making, we propose Reinforcement Learning (RL) algorithm based on sequential alternating multi-agent system mechanism, which effectively reduces the dimensionality of action space without losing the informational content of action, achieving network lightweighting. We discuss the rationality, generalizability, and inherent advantages of proposed mechanism. Simulation results indicate that our proposed mechanism outperforms traditional RL algorithms in terms of stability, generalizability, and adaptability to scenarios with invalid actions, all while achieving network lightweighting. © 2025 Chongqing University of Posts and Telecommunications.

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

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2296.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
