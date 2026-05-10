---
id: paper-2418
title: An intention-driven task offloading strategy based on imitation learning in pervasive edge computing
authors:
- Zhang, Yang
- Zhang, Shukui
- Zhang, Qi
- Fan, Jianxi
venue: Computer Networks
venue_type: journal
year: 2025
doi: 10.1016/j.comnet.2024.110998
url: https://www.scopus.com/pages/publications/85214233220?origin=resultslist
publisher: Elsevier B.V.
pages: ''
keywords:
- Computing-aware
- Imitation learning
- Intention-driven
- Nash equilibrium
- Pervasive edge computing
- Stochastic game
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
    proposed_justification: C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)
    winning_category: null
    overrides_applied: []
    my_final_decision: Exclude
    my_justification: Sem pistas de uso de LLM e/ou Agentic AI.
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

# paper-2418 — An intention-driven task offloading strategy based on imitation learning in pervasive edge computing

## Metadata (from `/03-parse-references-metadata`)

Imported from `legacy/papers/` during v3.2.0 migration. Full machine-readable fields live in the frontmatter.

**Abstract**

> Consider an infrastructure-less wireless network environment (e.g., a land battlefield) in which devices are characterized by varying resource configurations, dynamic mobility, complexity of the generated sensing tasks, and deterministic delay constraints for the processing of these tasks. Solving the associated problem is infeasible on many thin-client mobile or IoT devices. Existing research has not yet addressed the above issues. In this paper, we first analyze the latency problem that arises when offloading tasks to other neighboring devices for processing and model the self-benefit-maximizing task allocation process as a stochastic game. Second, by probing the state information of the available arithmetic resources, we model the problem of minimum Steiner tree (MST)-based task migration as a sequential decision-making process and construct a distribution of activity trajectories formed by the allocation decisions and state changes. Then, based on an expert system demonstration, multiagent imitation learning based on MSTs (MILMST) is proposed. For every task, the MST is used as the decision basis for task offloading based on the agents’ local observations, and the allocation strategy is gradually improved by interacting with the surrounding agents in an online manner. Finally, the superiority of our algorithm is experimentally demonstrated. © 2024 Elsevier B.V.

**Dedup notes**

no duplicates found

---

## 04 — Title Screening

### iter-0 (migrated from legacy)

- **regex_decision:** Exclude
- **regex_justification:** "C1=0 (no agentic/LLM signal); C2=1.0 (resource management signal); C3=1.0 (infra/cloud-edge signal)"
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
- **my_justification:** "Sem pistas de uso de LLM e/ou Agentic AI."
- **locked_at_iteration:** iter-0
- **locked_at:** 2026-05-09T00:00:00+00:00

---

## 05 — Abstract Screening

_(stage 05 not run for this paper — excluded at title screening)_

---

## 06 — Full-Text Screening

_(populated by `/screen --stage full-text`. PDF location: `raw/pdfs/paper-2418.pdf`)_

---

## 07 — Taxonomy

_(populated by `/05-code-taxonomy` after stage 06 lock.)_

---

## 08 — Analysis contributions

_(populated by `/06-analyze` after taxonomy lock.)_
